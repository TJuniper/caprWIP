import csv
import io
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "backend"))
from oe_input_context import (
    CITATION_CONTEXT, FIELDS, InputContext, context_for_row, display_form,
    load_context_metadata, validate_context_rows,
    lexical_fst,
    board_context, lexical_apply_down,
)


class InputContextTests(unittest.TestCase):
    def test_independent_contexts_keep_segmental_reconstruction(self):
        form = "ízwiz"
        self.assertEqual(CITATION_CONTEXT.encode(form), form)
        self.assertEqual(InputContext("unstressed", "final").encode(form), "ᵘízwiz")
        self.assertEqual(InputContext("unstressed", "nonfinal").encode(form), "ᶜízwiz")
        self.assertEqual(display_form("*ᵘ*í*w*w*i"), "*í*w*w*i")
        self.assertEqual(display_form("*u*m*b*i*ᶜ"), "*u*m*b*i")
        self.assertEqual(display_form("ᶜízwiz"), form)

    def test_unknown_contexts_and_already_encoded_inputs_fail(self):
        for args in (("unknown", "final"), ("stressed", "unknown"),
                     ("stressed", "nonfinal")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                InputContext(*args)
        for form in ("", "ᵘízwiz", "ízwizᶜ"):
            with self.subTest(form=form), self.assertRaises(ValueError):
                CITATION_CONTEXT.encode(form)

    def test_selected_metadata_validates_identity_and_input(self):
        entries = load_context_metadata(ROOT / "Germanic/data/entry_context_metadata.tsv")
        self.assertEqual(set(entries), {"2326"})
        self.assertEqual(context_for_row("2326", "*ízwiz", entries),
                         InputContext("unstressed", "final"))
        self.assertEqual(context_for_row("2040", "*gíftiz", entries), CITATION_CONTEXT)
        with self.assertRaisesRegex(ValueError, "disagrees"):
            context_for_row("2326", "*other", entries)
        with self.assertRaisesRegex(ValueError, "absent"):
            validate_context_rows(entries, {"2040"})
        validate_context_rows(entries, {"2040", "2326"})

    def test_malformed_sidecar_is_not_silently_defaulted(self):
        valid = ["2326", "*ízwiz", "unstressed", "final", "SC098",
                 "RingeTaylor2014", "41-42,57-58", "Selected weak context"]
        variants = []
        for position, value in ((2, "unknown"), (4, "SC055"), (6, "section 3"),
                                (1, "*ᵘ*ízwiz"), (7, "")):
            invalid = valid.copy()
            invalid[position] = value
            variants.append([invalid])
        variants.append([valid, valid])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contexts.tsv"
            for rows in variants:
                data = io.StringIO()
                writer = csv.writer(data, delimiter="\t")
                writer.writerow(FIELDS)
                writer.writerows(rows)
                path.write_text(data.getvalue(), encoding="utf-8")
                with self.subTest(rows=rows), self.assertRaises(ValueError):
                    load_context_metadata(path)

    def test_canonical_selected_input_is_separate_from_lexical_identity(self):
        sys.path.insert(0, str(ROOT / "Germanic/tools"))
        from oe_pipeline import evaluation_input, load_rows, normalize_proto
        rows = load_rows(ROOT / "Germanic/data/germanic-aligned-final.tsv")
        self.assertEqual(len(rows), 387)
        marked = [row for row in rows if evaluation_input(row) != row["proto_norm"]]
        self.assertEqual([row["row_id"] for row in marked], ["2326"])
        self.assertEqual((marked[0]["proto"], marked[0]["proto_norm"], marked[0]["fst_input"]),
                         ("*ízwiz", "ízwiz", "ᵘízwiz"))
        self.assertEqual(normalize_proto("*ízwiz"), "ízwiz")
        with self.assertRaisesRegex(ValueError, "assembled"):
            evaluation_input({"proto_norm": "ízwiz", "word_stress": "unstressed"})

    def test_board_projection_only_wraps_context_capable_oe_networks(self):
        native = Mock()
        native.alphabet.return_value = {"ᵘ", "ᶜ", "i", "x"}
        constructor = Mock()
        with patch.dict(sys.modules, {"foma": SimpleNamespace(FST=constructor)}):
            projected = lexical_fst(native, "Old_English")
            lexical_apply_down(projected, "i")
        constructor.assert_called_once_with("[[0] [[? - [{ᵘ}|{ᶜ}]]*]]")
        constructor.return_value.compose.assert_called_once_with(native)
        constructor.return_value.compose.return_value.apply_down.assert_called_once_with("i")
        self.assertIs(lexical_fst(native, "Old_Burmese"), native)
        native.alphabet.return_value = {"i", "x"}
        self.assertIs(lexical_fst(native, "Old_English"), native)

    def test_board_context_defaults_explicitly_and_rejects_invalid_metadata(self):
        self.assertEqual(board_context(None), CITATION_CONTEXT)
        self.assertEqual(board_context({
            "checkpoint": "SC098", "wordStress": "unstressed",
            "phonologicalFinality": "final",
        }), InputContext("unstressed", "final"))
        for metadata in ({}, {"checkpoint": "SC055", "wordStress": "unstressed",
                              "phonologicalFinality": "final"},
                         {"checkpoint": "SC098", "wordStress": "unknown",
                          "phonologicalFinality": "final"}):
            with self.subTest(metadata=metadata), self.assertRaises(ValueError):
                board_context(metadata)


if __name__ == "__main__":
    unittest.main()
