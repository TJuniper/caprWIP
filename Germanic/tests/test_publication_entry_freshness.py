import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic/tools"))
import artifact_graph as graph

ENTRY_POINTS = (
    "Germanic/docs/assembly/build_capr_book_draft_docker.sh",
    "Germanic/docs/assembly/build_full_lexical_volume_docker.sh",
    "Germanic/docs/assembly/build_full_lexical_volume.sh",
    "Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_20_docker.sh",
)


class PublicationEntryTests(unittest.TestCase):
    def run_entry(self, entry, refresh_status):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ENTRY_POINTS:
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(REPO_ROOT / name, target)
            bin_dir = root / "bin"
            bin_dir.mkdir()
            log = root / "calls.log"
            commands = {
                "python3": ('printf "python3 %s\\n" "$*" >> "$CALL_LOG"\n'
                            'if [ "$*" = "Germanic/tools/adjudicate.py --refresh" ]; then\n'
                            '  exit "$REFRESH_STATUS"\nfi\nexit 0\n'),
                "docker": ('printf "docker %s\\n" "$*" >> "$CALL_LOG"\n'
                           'if [ "$1" = "info" ]; then exit 0; fi\nexit 77\n'),
                "pandoc": 'printf "pandoc\\n" >> "$CALL_LOG"\nexit 77\n',
            }
            for name, body in commands.items():
                command = bin_dir / name
                command.write_text("#!/bin/sh\n" + body, encoding="utf-8")
                command.chmod(0o755)
            env = dict(os.environ, PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
                       CALL_LOG=str(log), REFRESH_STATUS=str(refresh_status))
            result = subprocess.run(["bash", str(root / entry)], cwd=root,
                                    env=env, capture_output=True, text=True)
            return result, log.read_text(encoding="utf-8").splitlines()

    def test_every_entry_refreshes_before_checks_builders_or_rendering(self):
        for entry in ENTRY_POINTS:
            with self.subTest(entry=entry):
                result, calls = self.run_entry(entry, 0)
                self.assertEqual(result.returncode, 77, result.stderr)
                first_python = next(c for c in calls if c.startswith("python3 "))
                self.assertEqual(first_python,
                                 "python3 Germanic/tools/adjudicate.py --refresh")

    def test_failed_refresh_stops_every_entry_before_publication(self):
        for entry in ENTRY_POINTS:
            with self.subTest(entry=entry):
                result, calls = self.run_entry(entry, 19)
                self.assertEqual(result.returncode, 19, result.stderr)
                self.assertEqual([c for c in calls if c.startswith("python3 ")],
                                 ["python3 Germanic/tools/adjudicate.py --refresh"])
                self.assertFalse(any(c.startswith(("docker run ", "pandoc"))
                                     for c in calls), calls)


class LexicalFreshnessTests(unittest.TestCase):
    def test_input_or_output_drift_is_rejected_and_no_op_preserves_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "lexical.md"
            output.write_text("current lexical history\n", encoding="utf-8")
            provenance = root / "provenance.json"
            inputs = {"model.md": "model-hash", "corpus.tsv": "corpus-hash"}
            provenance.write_text(json.dumps({
                "inputs": inputs,
                "outputs": {"lexical.md": hashlib.sha256(output.read_bytes()).hexdigest()},
            }), encoding="utf-8")
            original = (output.read_bytes(), provenance.read_bytes())
            with patch.object(graph, "LEXICAL_PROVENANCE", provenance), \
                    patch.object(graph, "_lexical_outputs", return_value=[output]), \
                    patch.object(graph, "_rel", side_effect=lambda p: p.name), \
                    patch.object(graph, "_lexical_input_hashes", return_value=inputs):
                self.assertEqual(graph._lexical_verify(), [])
                self.assertEqual((output.read_bytes(), provenance.read_bytes()), original)
                for source in ("model.md", "corpus.tsv"):
                    with patch.object(graph, "_lexical_input_hashes",
                                      return_value={**inputs, source: "changed"}):
                        self.assertTrue(graph._lexical_verify())
                output.write_text("stale lexical history\n", encoding="utf-8")
                self.assertTrue(graph._lexical_verify())


if __name__ == "__main__":
    unittest.main()
