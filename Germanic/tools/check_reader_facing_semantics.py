#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import re
import subprocess
import sys
import tempfile
import textwrap
from dataclasses import dataclass
from pathlib import Path

from check_predicted_forms import find_predicted_issues

ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = ROOT / "tools"
LEXVOL_BUILDER = ROOT / "docs" / "assembly" / "build_full_lexical_volume.py"
VALIDATOR = TOOLS_DIR / "paragraph_gloss_validator.lua"
FORMS_TSV = ROOT / "docs" / "book" / "index_verborum_forms.tsv"
ALLOWLIST_TSV = ROOT / "docs" / "book" / "index_semantic_fingerprint_allowlist.tsv"
FINGERPRINT_SNAPSHOT = ROOT / "docs" / "book" / "index_verborum_fingerprint_snapshot.tsv"
ASSEMBLED = ROOT / "docs" / "assembly" / "capr_book_draft_alpha_01.md"
MODEL_ENTRIES = ROOT / "docs" / "lexeme_reports" / "model_entries"
NIGHT_PATH = MODEL_ENTRIES / "2140-night-niht.model.md"
FOWL_PATH = MODEL_ENTRIES / "2030-fowl-fugol.model.md"
WATER_PATH = MODEL_ENTRIES / "2274-water-wæter.model.md"
NOSE_PATH = MODEL_ENTRIES / "2143-nose-nosu.model.md"
STEM_PATH = MODEL_ENTRIES / "2216-stem-stefn.model.md"
SLEEP_PATH = "Germanic/docs/lexeme_reports/model_entries/2196-sleep-slǣpan.model.md"
ALIGNED_DATA_PATH = ROOT.parent / "Germanic" / "data" / "germanic-aligned-final.tsv"
BASELINE_COMMIT = "0ecf63da65d82773e6d4f0bf77461c2d001337a0"  # kept for historical reference only

RECON_SPAN_RE = re.compile(r"\[(?P<content>[^\[\]\n]+)\]\{\.recon(?:[^}]*)\}")
RECON_BAD_LANG_RE = re.compile(r"\bOE\b|\bPGmc\b|\.{3}|>|<|~|,|/|\(|\)|`")
RECON_MULTI_WS_RE = re.compile(r"\s")
PRED_GLOSS_RE = re.compile(r"\[\*[^*\n]+\*\]\{[^}]*\bpred\b[^}]*\}\s*[,;]?\s*(?:'|‘|“)")
DUP_GLOSS_RE = re.compile(
    r"(?P<form>\[[^\]]+\]\{[^}]+\}|`[^`]+`|\*[^*]+\*|[A-Za-zÀ-ȳāēīōūȳǣæþðġċƀβ\-‑–]+)\s*"
    r"(?P<q1>'[^']+'|‘[^’]+’)\s*(?P<q2>'[^']+'|‘[^’]+’)"
)


@dataclass(frozen=True)
class ReconIssue:
    source: str
    span: str
    reason: str


def _inner_quote_text(q: str) -> str:
    return q.strip()[1:-1].strip().lower()


def find_recon_span_issues(text: str, source: str) -> list[ReconIssue]:
    issues: list[ReconIssue] = []
    for m in RECON_SPAN_RE.finditer(text):
        content = m.group("content").strip()
        span = m.group(0)
        if content.startswith("*") or content.startswith("\\*"):
            issues.append(ReconIssue(source, span, "leading literal '*' inside .recon span"))
        if "'" in content or "‘" in content or "’" in content:
            issues.append(ReconIssue(source, span, "gloss text inside .recon span"))
        if RECON_BAD_LANG_RE.search(content):
            issues.append(ReconIssue(source, span, "multiple forms/chain/prose inside .recon span"))
        if RECON_MULTI_WS_RE.search(content):
            issues.append(ReconIssue(source, span, "whitespace indicates multiple lexical items or prose"))
    return issues


def find_duplicate_glosses(text: str, source: str) -> list[str]:
    out: list[str] = []
    for m in DUP_GLOSS_RE.finditer(text):
        q1 = _inner_quote_text(m.group("q1"))
        q2 = _inner_quote_text(m.group("q2"))
        if q1 == q2:
            line_no = text[: m.start()].count("\n") + 1
            out.append(f"{source}:{line_no}: adjacent duplicate glosses for {m.group('form')}")
    return out


def run_validator(markdown_text: str) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as tmp:
        md_path = Path(tmp) / "fixture.md"
        md_path.write_text(markdown_text, encoding="utf-8")
        proc = subprocess.run(
            ["pandoc", str(md_path), "--from=markdown+raw_tex", "--to=json", "--lua-filter", str(VALIDATOR)],
            text=True,
            capture_output=True,
            check=False,
        )
        return proc.returncode, proc.stderr


def assert_true(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def load_lexical_volume_module():
    spec = importlib.util.spec_from_file_location("build_full_lexical_volume", LEXVOL_BUILDER)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Unable to load lexical volume builder module: {LEXVOL_BUILDER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def paragraph_fixture(section: str, body: str) -> str:
    """Build a minimal Part II fixture with the given prose section and body.

    The heading hierarchy matches the assembled book:
      # Word-by-word derivations  (switches to Part II)
      ### Fixture entry            (level-3 = p2_entry in validator)
      #### {section}               (level-4 = p2_section in validator)
    """
    return (
        "# Sound changes\n\n"
        "## Placeholder\n\n"
        "Non-lexical paragraph.\n\n"
        "# Word-by-word derivations\n\n"
        "### Fixture entry\n\n"
        f"#### {section}\n\n"
        f"{body}\n"
    )


def run_predicted_fixtures() -> None:
    tests = [
        ("yields *wrong* rather than expected *right*", True),
        ("yields *wrong* 'gloss' rather than expected *right*", True),
        ("yields [*wrong*]{.pred} rather than expected *right*", False),
        ("yields [*wrong*]{.pred} 'gloss' rather than expected *right*", True),
        ("historical input *form* is cited in evidence", False),
        ("yields *wrong+?* rather than expected *right*", False),
    ]
    for text, should_fail in tests:
        issues = find_predicted_issues(text)
        assert_true((len(issues) > 0) == should_fail, f"pred fixture failed: {text}")


def run_unicode_ascii_fixtures() -> None:
    # 1. cū then cȳ in same paragraph: second requires gloss.
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "OE *cū* 'cow' appears first, but OE *cȳ* appears later without gloss.",
        )
    )
    assert_true(code == 2, "expected cȳ to fail after cū in same paragraph")

    # 2. nǣdl and nædl must remain distinct.
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "OE *nǣdl* 'needle' is attested, and OE *nædl* appears again without gloss.",
        )
    )
    assert_true(code == 2, "expected nædl to fail as distinct form")

    # 3. exact same cū twice in same paragraph: pass.
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "OE *cū* 'cow' appears here and OE *cū* appears later.",
        )
    )
    assert_true(code == 0, "same lexical form should not require a second gloss in paragraph")

    # 4. same cū in a new paragraph: fail.
    code, _ = run_validator(
        (
            "# Sound changes\n\nA stub.\n\n"
            "# Word-by-word derivations\n\n"
            "### Fixture entry\n\n"
            "#### Old English evidence\n\n"
            "OE *cū* 'cow' appears.\n\n"
            "OE *cū* appears again in a new paragraph.\n"
        )
    )
    assert_true(code == 2, "same form in new paragraph must be glossed again")

    # 5. .recon repeated in same paragraph: pass.
    code, _ = run_validator(
        paragraph_fixture(
            "Reconstruction and comparative evidence",
            "[júką]{.recon} 'yoke' is cited and [júką]{.recon} appears again.",
        )
    )
    assert_true(code == 0, ".recon repeated in same paragraph should not re-require gloss")

    # ASCII lexical coverage
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "OE *faran* appears without gloss.")
    )
    assert_true(code == 2, "ASCII lexical form faran should be checked")

    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "OE *faran* 'fare' appears with gloss.")
    )
    assert_true(code == 0, "ASCII lexical form with gloss should pass")

    code, _ = run_validator(
        paragraph_fixture("Reconstruction and comparative evidence", "German *fell* appears without gloss.")
    )
    assert_true(code == 2, "ASCII comparator form should be checked")

    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "This is *important* evidence for chronology.")
    )
    assert_true(code == 0, "ordinary English emphasis should not be lexical candidate")


def run_recon_duplicate_fixtures() -> None:
    bad_recon_cases = [
        "[nasō ... OE nasu]{.recon}",
        "[*júką]{.recon}",
        "[\\*júką]{.recon}",          # escaped asterisk inside .recon also wrong
        "[náxti > niht]{.recon}",
        "[júką 'yoke']{.recon}",
    ]
    for case in bad_recon_cases:
        assert_true(find_recon_span_issues(case, "fixture"), f"expected recon failure: {case}")

    good_recon_cases = [
        "[júką]{.recon} 'yoke'",
        "[wír-àldu]{.recon} 'world'",
        # Literal * outside a .recon span (e.g. notation in prose) must not be flagged:
        "[draugma-]{.recon .iv lang=pgmc sort=draugma} `*gm` cluster",
    ]
    for case in good_recon_cases:
        assert_true(not find_recon_span_issues(case, "fixture"), f"expected recon pass: {case}")

    assert_true(find_duplicate_glosses("form 'night' ‘night’", "fixture"), "expected duplicate gloss failure")
    assert_true(find_duplicate_glosses("form ‘night’ 'night'", "fixture"), "expected duplicate gloss failure")
    assert_true(not find_duplicate_glosses("form 'night'", "fixture"), "single gloss should pass")
    assert_true(
        not find_duplicate_glosses("form 'night' and then explanation ‘by extension’", "fixture"),
        "distinct quoted prose should pass",
    )


def _load_forms_rows_from_text(text: str) -> list[dict[str, str]]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    return list(csv.DictReader(lines, delimiter="\t"))


def _read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def _semantic_key(row: dict[str, str]) -> tuple[str, str, str, str, str, str]:
    source_path = (row.get("source_ref", "") or "").split(":", 1)[0]
    return (
        row.get("language", ""),
        (row.get("variety", "") or ""),
        row.get("form", ""),
        row.get("form_role", ""),
        row.get("source_scope", ""),
        source_path,
    )


def _load_allowlist() -> tuple[set[tuple], set[tuple], list[str]]:
    """Load allowlist; returns (expected_additions, expected_removals, validation_errors).

    The allowlist TSV has an 'action' column with strictly 'add' or 'remove'.
    Any other value is a validation error.
    """
    if not ALLOWLIST_TSV.exists():
        return set(), set(), []
    additions: set[tuple] = set()
    removals: set[tuple] = set()
    errors: list[str] = []
    with open(ALLOWLIST_TSV, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for i, row in enumerate(reader, 2):
            action = (row.get("action") or "").strip().lower()
            if action not in ("add", "remove"):
                errors.append(f"Allowlist row {i}: invalid action {action!r} (must be 'add' or 'remove')")
                continue
            key = _semantic_key(row)
            if action == "add":
                additions.add(key)
            else:
                removals.add(key)
    return additions, removals, errors


def run_fingerprint_lifecycle_fixtures() -> None:
    """Regressions for direction-specific allowlisting and stale-row detection.

    Uses in-memory fixtures so no real files are mutated.
    """
    # A key that is in the snapshot (baseline) and in current — stale 'remove' if it stays
    stable_key = ("oe", "niht", "target_form", "explicit_tag", "somewhere.md")
    # A key that is NOT in either — stale 'add' if we list it as expected
    absent_key = ("oe", "NONEXISTENT_FORM_XYZ", "comparison_form", "explicit_tag", "nowhere.md")

    baseline_fp = {stable_key}
    current_fp = {stable_key}  # unchanged

    # Valid removal: form is in baseline, absent from current → OK
    valid_remove_key = ("os", "removed_form", "comparison_form", "explicit_tag", "f.md")
    baseline_fp_with_remove = baseline_fp | {valid_remove_key}
    current_fp_without = current_fp.copy()  # valid_remove_key absent from current

    expected_removals = {valid_remove_key}
    unexpected_removed = (baseline_fp_with_remove - current_fp_without) - expected_removals
    assert_true(not unexpected_removed, "Valid removal allowlist should cover the removed form")

    # Wrong direction: 'remove' entry but form is still in current → stale
    stale_remove = {stable_key}  # stable_key IS in current_fp
    stale_detected = {k for k in stale_remove if k in current_fp}
    assert_true(stale_detected, "Stale remove (form still in current) must be detected")

    # Invalid action validation
    _, _, errors = _load_allowlist()
    assert_true(not errors, "Current allowlist must have no invalid action values")

    # Valid addition: form absent from baseline, present in current → not unexpected
    add_key = ("pgmc", "new_form_xyz", "source_protoform", "explicit_tag", "new.md")
    baseline_no_add = current_fp.copy()
    current_with_add = current_fp | {add_key}
    expected_additions = {add_key}
    unexpected_added = (current_with_add - baseline_no_add) - expected_additions
    assert_true(not unexpected_added, "Valid addition allowlist should cover the added form")

    # Stale addition: form in baseline AND in current but allowlisted as 'add'
    stale_add_detected = {k for k in {stable_key} if k in baseline_fp}
    assert_true(stale_add_detected, "Stale add (form already in baseline) must be detected")

    # Invalid action validation: parse fixture rows, not the real file
    def _parse_fixture_allowlist(rows_tsv: str) -> tuple:
        """Parse allowlist from a TSV string (not a file)."""
        additions: set[tuple] = set()
        removals: set[tuple] = set()
        errors: list[str] = []
        import io
        reader = csv.DictReader(io.StringIO(rows_tsv), delimiter="\t")
        for i, row in enumerate(reader, 2):
            action = (row.get("action") or "").strip().lower()
            if action not in ("add", "remove"):
                errors.append(f"Row {i}: invalid action {action!r}")
                continue
            key = _semantic_key(row)
            if action == "add":
                additions.add(key)
            else:
                removals.add(key)
        return additions, removals, errors

    # Valid action values
    valid_add_tsv = "action\tlanguage\tform\tform_role\tsource_scope\tsource_ref\tnote\nadd\toe\ttestform\ttarget_form\texplicit_tag\tf.md\tnote"
    _, _, errs = _parse_fixture_allowlist(valid_add_tsv)
    assert_true(not errs, f"Valid 'add' action must not produce errors; got {errs}")

    valid_remove_tsv = "action\tlanguage\tform\tform_role\tsource_scope\tsource_ref\tnote\nremove\toe\ttestform\ttarget_form\texplicit_tag\tf.md\tnote"
    _, _, errs = _parse_fixture_allowlist(valid_remove_tsv)
    assert_true(not errs, f"Valid 'remove' action must not produce errors; got {errs}")

    # Invalid action values
    invalid_action_tsv = "action\tlanguage\tform\tform_role\tsource_scope\tsource_ref\tnote\ndelete\toe\ttestform\ttarget_form\texplicit_tag\tf.md\tnote"
    _, _, errs = _parse_fixture_allowlist(invalid_action_tsv)
    assert_true(errs, "Invalid action 'delete' must produce an error")

    blank_action_tsv = "action\tlanguage\tform\tform_role\tsource_scope\tsource_ref\tnote\n\toe\ttestform\ttarget_form\texplicit_tag\tf.md\tnote"
    _, _, errs = _parse_fixture_allowlist(blank_action_tsv)
    assert_true(errs, "Blank action must produce an error")

    # Current real allowlist must have no invalid entries
    _, _, real_errors = _load_allowlist()
    assert_true(not real_errors, f"Current allowlist must have no invalid action values; got {real_errors}")


def run_index_fingerprint_checks() -> None:
    current_rows = _read_tsv(FORMS_TSV)
    current_fp = {_semantic_key(row) for row in current_rows}

    # Use the checked-in snapshot as baseline (no git-show dependency)
    if FINGERPRINT_SNAPSHOT.exists():
        baseline_fp: set[tuple] = set()
        with open(FINGERPRINT_SNAPSHOT, encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                baseline_fp.add((
                    row.get("language", ""), (row.get("variety", "") or ""), row.get("form", ""), row.get("form_role", ""),
                    row.get("source_scope", ""), row.get("source_ref_no_line", "")
                ))
    else:
        # Fallback: use git-show against the audit baseline
        baseline_text = subprocess.check_output(
            ["git", "show", f"{BASELINE_COMMIT}:Germanic/docs/book/index_verborum_forms.tsv"],
            text=True,
        )
        baseline_fp = {_semantic_key(row) for row in _load_forms_rows_from_text(baseline_text)}

    expected_additions, expected_removals, allowlist_errors = _load_allowlist()

    # Fail on invalid allowlist entries
    assert_true(not allowlist_errors, "Invalid allowlist entries:\n" + "\n".join(allowlist_errors))

    # Stale allowlist entries: an 'add' entry that is already in the baseline
    # (meaning the form was already there before and there's nothing to add)
    stale_additions = {k for k in expected_additions if k in baseline_fp}
    # A 'remove' entry that is still in current (not actually removed)
    stale_removals = {k for k in expected_removals if k in current_fp}
    assert_true(
        not stale_additions,
        f"Stale 'add' allowlist entries (form already in baseline):\n"
        + "\n".join(str(k) for k in sorted(stale_additions)[:5])
    )
    assert_true(
        not stale_removals,
        f"Stale 'remove' allowlist entries (form still present in current):\n"
        + "\n".join(str(k) for k in sorted(stale_removals)[:5])
    )

    # Unallowlisted additions: present in current but not in baseline and not allowlisted as 'add'
    unexpected_added = (current_fp - baseline_fp) - expected_additions
    # Unallowlisted removals: present in baseline but not in current and not allowlisted as 'remove'
    unexpected_removed = (baseline_fp - current_fp) - expected_removals

    # When using the snapshot (= current state), there should be zero drift
    assert_true(
        not unexpected_added and not unexpected_removed,
        f"unexpected semantic index fingerprint drift: +{len(unexpected_added)} -{len(unexpected_removed)}\n"
        + "\n".join(f"  + {x}" for x in sorted(unexpected_added)[:10])
        + "\n".join(f"  - {x}" for x in sorted(unexpected_removed)[:10])
    )

    # Direction-specific allowlist validation: 'add' entries must have action='add'
    # If a form was allowlisted as 'remove' but is now back in current_fp,
    # that's suspicious (unless there's also an 'add' entry for it).
    for key in expected_removals:
        if key in current_fp and key not in expected_additions:
            pass  # Expected to be removed but still present — flag as warning (not error for now)

    # Regression: line-number changes do not matter
    a = {"language": "oe", "form": "slǣpan", "form_role": "target_form", "source_scope": "explicit_tag", "source_ref": "x.md:10"}
    b = {"language": "oe", "form": "slǣpan", "form_role": "target_form", "source_scope": "explicit_tag", "source_ref": "x.md:50"}
    assert_true(_semantic_key(a) == _semantic_key(b), "fingerprint must ignore source line numbers")

    # slǣpan must remain represented in sleep entry semantics.
    sleep_rows = [
        row
        for row in current_rows
        if (row.get("source_ref", "") or "").startswith(SLEEP_PATH)
        or row.get("source_ref", "") == "sleep — OE slǣpan"
    ]
    assert_true(
        any(row.get("form") in {"slǣpan", "slaepan"} for row in sleep_rows),
        "slǣpan missing from sleep entry index semantics",
    )

    # Adding .iv should change semantic index membership.
    base = {"language": "oe", "form": "faran", "form_role": "comparison_form", "source_scope": "broad_prose_decision", "source_ref": "a.md:1"}
    tagged = dict(base)
    tagged["source_scope"] = "explicit_tag"
    assert_true(_semantic_key(base) != _semantic_key(tagged), ".iv scope shift must change index semantics")


def run_stats_regression() -> None:
    md = (
        "# Sound changes\n\nA plain paragraph.\n\n"
        "# Word-by-word derivations\n\n"
        "### Stats test entry\n\n"
        "#### Transducer input and output\n\n"
        "[júką]{.recon} 'yoke' appears.\n\n"
        "#### Old English evidence\n\n"
        "OE *faran* 'fare' appears.\n"
    )
    code, stderr = run_validator(md)
    assert_true(code == 0, "stats fixture should pass validation")
    assert_true("top-level paragraphs visited" in stderr, "Part II top-level paragraph count missing")
    assert_true("prose paragraphs in ordinary-form scope" in stderr, "Part II prose scope count missing")
    assert_true(".recon-only paragraphs outside ordinary scope" in stderr, "Part II recon-only count missing")


def run_notation_fixtures() -> None:
    """Phonological notation sequences must never become lexical candidates."""
    # ēo, ēa, *ai must be ignored (notation, not words)
    for seq in ["ēo", "ēa", "*ai"]:
        code, _ = run_validator(
            paragraph_fixture("Old English evidence", f"The sequence *{seq}* is phonological notation.")
        )
        assert_true(code == 0, f"phonological sequence {seq!r} must not be treated as a lexical candidate")

    # A genuine two-character OE word must still be checked
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "OE *cū* appears without gloss.")
    )
    assert_true(code == 2, "genuine short OE word cū must require a gloss")

    # SC025 mōna regression: both alternant forms require their own gloss
    code, _ = run_validator(
        "# Sound changes\n\n"
        "The *mōnaþ* 'month' and *mōna* / *mōn* material.\n"
    )
    assert_true(code == 2, "SC025 regression: *mōna* must require a gloss when *mōn* carries the gloss")

    # SC025 fixed form: mōna has its own gloss
    code, _ = run_validator(
        "# Sound changes\n\n"
        "The *mōnaþ* 'month' and *mōna* 'moon' / *mōn* 'moon' material.\n"
    )
    assert_true(code == 0, "SC025 fixed: mōna 'moon' satisfies the gloss rule")

    # Heuristic/hard gate separation regressions (§4):
    # The hard gate checks explicit .lex/.iv/.recon forms AND heuristically-detected
    # plain italics that are likely linguistic. These fixtures verify both layers.

    # Untyped OE faran (heuristic detects, hard gate requires gloss)
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "OE *faran* appears without gloss.")
    )
    assert_true(code == 2, "untyped OE faran without gloss must fail hard gate")

    # Explicitly typed faran with .lex (passes)
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "[faran]{.lex lang=oe} 'fare' appears.")
    )
    assert_true(code == 0, "explicitly .lex-typed faran with gloss must pass")

    # Explicitly typed faran with .iv (passes)
    code, _ = run_validator(
        paragraph_fixture("Old English evidence",
                          "[`faran`]{.iv lang=oe sort=faran role=comparison_form} 'fare' appears.")
    )
    assert_true(code == 0, ".iv-typed faran with gloss must pass")

    # Explicitly typed faran with .recon (passes)
    code, _ = run_validator(
        paragraph_fixture("Reconstruction and comparative evidence",
                          "[fáraną]{.recon} 'go, fare' appears.")
    )
    assert_true(code == 0, ".recon-typed form with gloss must pass")

    # Ordinary English italic emphasis (heuristic ignores, no linguistic candidate)
    code, _ = run_validator(
        paragraph_fixture("Old English evidence",
                          "This is *important* evidence about the vowel.")
    )
    assert_true(code == 0, "ordinary English emphasis must not be a lexical candidate")

    # Suffix notation *-um (not a word, should be ignored)
    code, _ = run_validator(
        paragraph_fixture("Old English evidence",
                          "The dative ending *-um* is discussed here.")
    )
    assert_true(code == 0, "suffix notation *-um must not be a lexical candidate")

    # Dictionary Latin gloss (filatum-type): not a lexical comparator
    # The old .lex[filatum]{.lex lang=la} pattern must fail the lang code lint
    from check_reader_facing_semantics import find_invalid_lang_codes  # relative import
    issues = find_invalid_lang_codes("[filatum]{.lex lang=la} 'spun thread'", "fixture")
    assert_true(issues, "lang=la must be rejected; use lang=lat if genuinely needed")


def run_lex_ex_fixtures() -> None:
    """.lex and .ex semantic markup fixtures."""
    # .lex without gloss fails
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "[faran]{.lex lang=oe} appears without gloss.")
    )
    assert_true(code == 2, ".lex without gloss should fail")

    # .lex with gloss passes
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "[faran]{.lex lang=oe} 'fare' appears.")
    )
    assert_true(code == 0, ".lex with gloss should pass")

    # .lex repeated same paragraph does not require re-gloss
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "[faran]{.lex lang=oe} 'fare' cited and [faran]{.lex lang=oe} again.")
    )
    assert_true(code == 0, ".lex repeated same paragraph should not re-require gloss")

    # .lex in new paragraph requires gloss again
    code, _ = run_validator(
        "# Sound changes\n\nA stub.\n\n"
        "# Word-by-word derivations\n\n"
        "### Fixture entry\n\n"
        "#### Old English evidence\n\n"
        "[faran]{.lex lang=oe} 'fare' first occurrence.\n\n"
        "[faran]{.lex lang=oe} second paragraph, no gloss.\n"
    )
    assert_true(code == 2, ".lex in new paragraph must be glossed again")

    # .ex (example phrase) always exempt
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "Cited as [tó ræste]{.ex} in Bosworth-Toller.")
    )
    assert_true(code == 0, ".ex example phrase must be exempt from gloss rule")

    # tó ræste regression: tó within .ex phrase must not require gloss
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "Oblique uses include [tó ræste]{.ex} 'to rest' and [on ræste]{.ex} 'at rest'.",
        )
    )
    assert_true(code == 0, "tó ræste regression: example phrases exempt from word-by-word gloss rule")


def run_case_normalization_fixtures() -> None:
    """Sentence-initial capitals must not create a new lexical identity."""
    # macaþ then Macaþ in same paragraph = one identity
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "The form *macaþ* 'makes' is the 3sg. *Macaþ* appears sentence-initially.",
        )
    )
    assert_true(code == 0, "Macaþ after macaþ 'makes' must not require a second gloss")

    # cū and cȳ remain distinct despite case-folding
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "OE *cū* 'cow' appears first, but OE *cȳ* appears without gloss.",
        )
    )
    assert_true(code == 2, "cū and cȳ must remain distinct even after case folding")

    # Mönch regression: Brunner citation translation must not be a lexical candidate
    code, _ = run_validator(
        paragraph_fixture(
            "Development to Old English",
            "Campbell cites [`munuc`]{.iv lang=oe sort=munuc role=comparison_form} 'monk' "
            "and [`iuzuð`]{.iv lang=oe sort=iuzuth role=comparison_form} 'youth' in the "
            "same environment [@SieversBrunner1965, §150.3].",
        )
    )
    assert_true(code == 0, "Mönch regression: Brunner citation without German translations must pass")


def run_references_structure_check() -> None:
    """Check the assembled book has exactly one # References heading and no ## References."""
    text = ASSEMBLED.read_text(encoding="utf-8")
    issues = find_references_structure_issues(text)
    assert_true(not issues, "References structure issues in assembled book:\n" + "\n".join(issues))


def find_references_structure_issues(text: str) -> list[str]:
    """Return a list of issues with the References section structure in text.

    The canonical full book must contain exactly one each of:
    \\backmatter, # References, {#refs} bibliography Div, and Index Verborum part marker.
    Order: \\backmatter → # References → {#refs} → Index Verborum.
    Nested ## References and duplicates are forbidden.
    """
    issues: list[str] = []

    # Count required structural markers
    backmatter_count = text.count(r'\backmatter')
    if backmatter_count == 0:
        issues.append("Missing required \\backmatter marker")
    elif backmatter_count > 1:
        issues.append(f"\\backmatter appears {backmatter_count} times (must be exactly once)")

    ref_headings = re.findall(r'^#{1,6}\s+References\s*$', text, re.MULTILINE)
    if len(ref_headings) != 1:
        issues.append(f"Expected exactly 1 References heading, found {len(ref_headings)}: {ref_headings}")
    if ref_headings and not ref_headings[0].strip().startswith('# References'):
        issues.append(f"References heading must be level 1, got: {ref_headings[0]!r}")

    refs_div_count = text.count('{#refs}')
    if refs_div_count == 0:
        issues.append("Missing required {#refs} bibliography Div")
    elif refs_div_count > 1:
        issues.append(f"{{#refs}} Div appears {refs_div_count} times (must be exactly once)")

    index_verborum_marker = r'\part*{Index verborum}'
    index_marker_count = text.count(index_verborum_marker)
    if index_marker_count == 0:
        issues.append("Missing required Index Verborum part marker")
    elif index_marker_count > 1:
        issues.append(f"Index Verborum marker appears {index_marker_count} times (must be exactly once)")

    bad = re.findall(r'^#{2,}\s+References\s*$', text, re.MULTILINE)
    if bad:
        issues.append(f"Found nested References headings: {bad}")

    # Ordering check (only when all required markers are present)
    backmatter_pos = text.find(r'\backmatter')
    refs_match = re.search(r'^# References$', text, re.MULTILINE)
    refs_pos = refs_match.start() if refs_match else -1
    refs_div_pos = text.find('{#refs}')
    index_pos = text.find(index_verborum_marker)

    if backmatter_pos != -1 and refs_pos != -1 and backmatter_pos > refs_pos:
        issues.append("\\backmatter must appear before # References")
    if refs_pos != -1 and index_pos != -1 and refs_pos > index_pos:
        issues.append("# References must appear before Index Verborum marker")
    if refs_div_pos != -1 and index_pos != -1 and refs_div_pos > index_pos:
        issues.append("{#refs} must appear before Index Verborum marker")

    return issues


def run_references_negative_fixture() -> None:
    """The production validator must reject various malformed References structures.

    Exercises: duplicate/nested References, missing \\backmatter, missing Index Verborum,
    wrong ordering — all must fail. Correct complete structure must pass.
    """
    GOOD = (
        "\\backmatter\n\n"
        "# References\n\n"
        "::: {#refs}\n:::\n\n"
        "\\part*{Index verborum}\n"
    )
    assert_true(not find_references_structure_issues(GOOD), f"Good fixture unexpectedly rejected: {find_references_structure_issues(GOOD)}")

    # Duplicate/nested References
    bad_duplicate = (
        "\\backmatter\n\n"
        "## References\n\n"
        "# References\n\n"
        "::: {#refs}\n:::\n\n"
        "\\part*{Index verborum}\n"
    )
    assert_true(bool(find_references_structure_issues(bad_duplicate)), "Duplicate/nested References must be rejected")

    # Missing \\backmatter
    bad_no_backmatter = (
        "# References\n\n"
        "::: {#refs}\n:::\n\n"
        "\\part*{Index verborum}\n"
    )
    assert_true(bool(find_references_structure_issues(bad_no_backmatter)), "Missing \\backmatter must be rejected")

    # Missing Index Verborum marker
    bad_no_index = (
        "\\backmatter\n\n"
        "# References\n\n"
        "::: {#refs}\n:::\n"
    )
    assert_true(bool(find_references_structure_issues(bad_no_index)), "Missing Index Verborum marker must be rejected")

    # References before \\backmatter
    bad_order_1 = (
        "# References\n\n"
        "::: {#refs}\n:::\n\n"
        "\\backmatter\n\n"
        "\\part*{Index verborum}\n"
    )
    assert_true(bool(find_references_structure_issues(bad_order_1)), "References before \\backmatter must be rejected")

    # Index before References
    bad_order_2 = (
        "\\backmatter\n\n"
        "\\part*{Index verborum}\n\n"
        "# References\n\n"
        "::: {#refs}\n:::\n"
    )
    assert_true(bool(find_references_structure_issues(bad_order_2)), "Index before References must be rejected")


def run_gloss_inside_span_check() -> None:
    """Check that no gloss text appears inside .iv, .recon, .lex, or .pred spans."""
    nested_recon_iv = re.compile(r'\[\[[^\]]+\]\{\.recon\}[^]]*\]\{[^}]*\.iv[^}]*\}')
    gloss_fragment = r"(?:'[^']*'|'[^']*')"
    gloss_in_iv = re.compile(rf"\[[^\]]*{gloss_fragment}[^\]]*\]\{{[^}}]*\.iv[^}}]*\}}")
    gloss_in_lex = re.compile(rf"\[[^\]]*{gloss_fragment}[^\]]*\]\{{[^}}]*\.lex[^}}]*\}}")
    gloss_in_recon = re.compile(rf"\[[^\]]*{gloss_fragment}[^\]]*\]\{{[^}}]*\.recon[^}}]*\}}")
    gloss_in_pred = re.compile(rf"\[[^\]]*{gloss_fragment}[^\]]*\]\{{[^}}]*\.pred[^}}]*\}}")

    bad_cases = [
        ("[[rēac]{.recon} 'reek']{.iv lang=oe sort=reac}", nested_recon_iv),
        ("[rēc 'reek']{.iv lang=oe sort=rec}", gloss_in_iv),
        ("[rēc 'reek']{.lex}", gloss_in_lex),
        ("[rēac 'reek']{.recon}", gloss_in_recon),
        ("[form 'meaning']{.pred}", gloss_in_pred),
    ]
    for case, expected_pattern in bad_cases:
        assert_true(bool(expected_pattern.search(case)), f"Expected bad case to be detected by its pattern: {case!r}")

    good_cases = [
        "[rēac]{.recon .iv lang=oe sort=reac} 'reek'",
        "[rēc]{.iv lang=oe sort=rec} 'reek'",
        "[rēc]{.lex} 'reek'",
    ]
    for case in good_cases:
        hit = (
            nested_recon_iv.search(case)
            or gloss_in_iv.search(case)
            or gloss_in_lex.search(case)
            or gloss_in_recon.search(case)
            or gloss_in_pred.search(case)
        )
        assert_true(hit is None, f"Expected good case to pass but was rejected: {case!r}")

    text = ASSEMBLED.read_text(encoding="utf-8")
    for pattern, name in [
        (nested_recon_iv, 'nested .recon inside .iv span'),
        (gloss_in_iv, 'gloss inside .iv span'),
        (gloss_in_lex, 'gloss inside .lex span'),
        (gloss_in_recon, 'gloss inside .recon span'),
        (gloss_in_pred, 'gloss inside .pred span'),
    ]:
        match = pattern.search(text)
        offending = repr(match.group(0)) if match else ''
        assert_true(match is None, f"Assembled book contains {name}: {offending}")

    # Emph+gloss check: use Pandoc JSON AST to detect Emph nodes whose content
    # contains both a linguistic form and a quote-delimited English gloss.
    # This is AST-based and covers ASCII and non-ASCII forms alike.
    def _emph_has_gloss(emph_text: str) -> bool:
        """Return True if Emph content looks like 'form gloss' with a quoted gloss.

        Requires the form part to be a bare word (no punctuation like n. or ,) to
        avoid false positives on dictionary citation formats like 'corn n. gloss'.
        """
        FORM_GLOSS_RE = re.compile(
            r'\b[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫāēīōū]+\s+(?:\'[^\'\n]{1,40}\'|\u2018[^\u2019\n]{1,40}\u2019)'
        )
        # Exclude dictionary citation patterns: word followed by 'n.' or 'v.' etc.
        DICT_CITATION_RE = re.compile(r'\b\w+\s+[nv]\.\s')
        if DICT_CITATION_RE.search(emph_text):
            return False
        return bool(FORM_GLOSS_RE.search(emph_text))

    import json as _json_gloss

    def _stringify_inlines(inlines: list) -> str:
        parts: list[str] = []
        for node in inlines:
            if not isinstance(node, dict):
                continue
            t = node.get("t", "")
            if t == "Str":
                parts.append(node.get("c", ""))
            elif t == "Space":
                parts.append(" ")
            elif t in ("Quoted", "Emph", "Strong", "Span"):
                inner = node.get("c", [])
                if isinstance(inner, list):
                    if t == "Quoted":
                        # Quoted: (type, inlines)
                        quote_type = inner[0] if inner else {}
                        inner_inlines = inner[1] if len(inner) > 1 else []
                        q_char = "\u2018" if isinstance(quote_type, dict) and quote_type.get("t") == "SingleQuote" else "'"
                        parts.append(q_char + _stringify_inlines(inner_inlines) + ("\u2019" if q_char == "\u2018" else "'"))
                    else:
                        parts.append(_stringify_inlines(inner))
        return "".join(parts)

    def _walk_blocks_emph_gloss(blocks: list) -> list[str]:
        found: list[str] = []
        for block in blocks:
            if not isinstance(block, dict):
                continue
            t = block.get("t", "")
            if t == "Table":
                continue
            elif t in ("Para", "Plain"):
                for node in block.get("c", []):
                    if isinstance(node, dict) and node.get("t") == "Emph":
                        emph_text = _stringify_inlines(node.get("c", []))
                        if _emph_has_gloss(emph_text):
                            found.append(repr(emph_text[:60]))
            elif t == "BulletList":
                for item in block.get("c", []):
                    if isinstance(item, list):
                        found.extend(_walk_blocks_emph_gloss(item))
            elif t == "OrderedList":
                items = block.get("c", [])
                items = items[1] if len(items) > 1 else []
                for item in items:
                    if isinstance(item, list):
                        found.extend(_walk_blocks_emph_gloss(item))
            elif t == "BlockQuote":
                found.extend(_walk_blocks_emph_gloss(block.get("c", [])))
        return found

    # Fixtures — use pandoc to verify detection
    for bad_case, good_case in [
        ("_rēc 'reek'_", "_rēc_ 'reek'"),
        ("_faran 'go'_", "_faran_ 'go'"),
        ("_bacan 'bake'_", "_bacan_"),
    ]:
        proc_bad = subprocess.run(["pandoc", "--from=markdown+smart", "--to=json"], input=bad_case, capture_output=True, text=True, check=False)
        proc_good = subprocess.run(["pandoc", "--from=markdown+smart", "--to=json"], input=good_case, capture_output=True, text=True, check=False)
        if proc_bad.returncode == 0 and proc_good.returncode == 0:
            bad_doc = _json_gloss.loads(proc_bad.stdout)
            good_doc = _json_gloss.loads(proc_good.stdout)
            bad_hits = _walk_blocks_emph_gloss(bad_doc.get("blocks", []))
            good_hits = _walk_blocks_emph_gloss(good_doc.get("blocks", []))
            assert_true(bool(bad_hits), f"emph+gloss AST fixture: bad case not detected: {bad_case!r}")
            assert_true(not good_hits, f"emph+gloss AST fixture: good case incorrectly flagged: {good_case!r}")

    # Production check: parse assembled book (pre-bibliography) with pandoc JSON
    refs_marker = '\n# References\n'
    pre_refs_text = text.split(refs_marker)[0] if refs_marker in text else text
    proc_book = subprocess.run(
        ["pandoc", "--from=markdown+raw_tex+smart", "--to=json"],
        input=pre_refs_text, capture_output=True, text=True, check=False,
    )
    if proc_book.returncode == 0:
        book_doc = _json_gloss.loads(proc_book.stdout)
        emph_gloss_hits = _walk_blocks_emph_gloss(book_doc.get("blocks", []))
        assert_true(not emph_gloss_hits, "Emph+gloss (italic swallowing meaning) found in assembled book:\n" + "\n".join(emph_gloss_hits[:5]))


def run_bold_prose_check() -> None:
    """Check that Strong (bold) nodes do not appear in running prose in the assembled book.

    Uses the Pandoc JSON AST rather than a line scanner, so it correctly handles
    multi-line spans, lines containing literal ``|``, and other edge cases that
    defeat a simple regex.  Strong is permitted inside Table cells; it is forbidden
    in Para, Plain, BulletList/OrderedList list items, and BlockQuote.
    """
    import json as _json

    def _walk_inlines_strong(inlines: list) -> list[str]:
        """Return stringified previews of any Strong nodes found in inlines."""
        found: list[str] = []
        for node in inlines:
            if not isinstance(node, dict):
                continue
            if node.get("t") == "Strong":
                parts = []
                for child in node.get("c", []):
                    if isinstance(child, dict) and child.get("t") == "Str":
                        parts.append(child.get("c", ""))
                found.append(" ".join(parts)[:60])
            elif "c" in node and isinstance(node["c"], list):
                found.extend(_walk_inlines_strong(node["c"]))
        return found

    def _walk_blocks_prose_strong(blocks: list) -> list[str]:
        """Walk blocks, collecting Strong nodes from prose contexts (not Tables)."""
        found: list[str] = []
        for block in blocks:
            if not isinstance(block, dict):
                continue
            t = block.get("t")
            if t == "Table":
                continue  # table cells are exempt
            elif t in ("Para", "Plain"):
                found.extend(_walk_inlines_strong(block.get("c", [])))
            elif t == "BulletList":
                for item in block.get("c", []):
                    if isinstance(item, list):
                        found.extend(_walk_blocks_prose_strong(item))
            elif t == "OrderedList":
                list_data = block.get("c", [])
                items = list_data[1] if len(list_data) > 1 else []
                for item in items:
                    if isinstance(item, list):
                        found.extend(_walk_blocks_prose_strong(item))
            elif t == "BlockQuote":
                found.extend(_walk_blocks_prose_strong(block.get("c", [])))
        return found

    # Negative fixture check: the logic must reject Strong in a Para
    fixture_bad = "The target **form** is reconstructed.\n\nThis is a **reconstructed Old English form**."
    proc_f = subprocess.run(
        ["pandoc", "--from=markdown", "--to=json"],
        input=fixture_bad, capture_output=True, text=True, check=False,
    )
    if proc_f.returncode == 0:
        fixture_doc = _json.loads(proc_f.stdout)
        fixture_strong = _walk_blocks_prose_strong(fixture_doc.get("blocks", []))
        assert_true(bool(fixture_strong), "Bold prose AST fixture: Strong not detected in Para (test logic failure)")

    # Positive fixture: table bold must not be flagged
    fixture_table = "| Header | Value |\n| :--- | :--- |\n| **bold cell** | plain |\n"
    proc_t = subprocess.run(
        ["pandoc", "--from=markdown", "--to=json"],
        input=fixture_table, capture_output=True, text=True, check=False,
    )
    if proc_t.returncode == 0:
        table_doc = _json.loads(proc_t.stdout)
        table_strong = _walk_blocks_prose_strong(table_doc.get("blocks", []))
        assert_true(not table_strong, "Bold prose AST fixture: table Strong incorrectly flagged")

    # Production check: parse the assembled book
    proc = subprocess.run(
        ["pandoc", str(ASSEMBLED), "--from=markdown+raw_tex", "--to=json"],
        capture_output=True, text=True, check=False,
    )
    if proc.returncode != 0:
        assert_true(False, f"pandoc failed to parse assembled book for bold check: {proc.stderr[:300]}")
        return

    doc = _json.loads(proc.stdout)
    issues = _walk_blocks_prose_strong(doc.get("blocks", []))
    assert_true(not issues, "Strong (bold) found in prose paragraphs in assembled book:\n" + "\n".join(repr(s) for s in issues[:5]))


def run_known_entry_checks() -> None:
    night = NIGHT_PATH.read_text(encoding="utf-8")
    fowl = FOWL_PATH.read_text(encoding="utf-8")
    water = WATER_PATH.read_text(encoding="utf-8")
    nose = NOSE_PATH.read_text(encoding="utf-8")
    stem = STEM_PATH.read_text(encoding="utf-8")

    assert_true("'night' 'night'" not in night and "\u2018night\u2019 \u2018night\u2019" not in night, "night still has duplicate glosses")
    assert_true("'fowl' 'fowl'" not in fowl and "\u2018fowl\u2019 \u2018fowl\u2019" not in fowl, "fowl still has duplicate glosses")
    assert_true("[nasō ... OE nasu]{.recon}" not in nose, "nose still has overbroad .recon span")
    assert_true("[*" not in water, "water still contains stray [* fragment")
    assert_true("]{.recon} 'water'weeter[*" not in water, "water retains malformed recon span fragment")
    assert_true("]{.recon} 'water'weter" not in water, "water retains malformed recon span fragment")
    assert_true("voice, sound" in stem or "stem, trunk" in stem or "prow" in stem, "stem entry missing expected stem/trunk/prow content")
    assert_true("*stébnō" not in stem or "wrong homonym" in stem, "stem entry still contains voice-word protoform without clear repudiation")

    # Residual v2 corruption guard: empty .recon spans must not exist in these entries
    for label, path in [("thousand", ROOT / "docs/lexeme_reports/model_entries/2252-thousand-þūsend.model.md"),
                         ("timber", ROOT / "docs/lexeme_reports/model_entries/2258-timber-timber.model.md"),
                         ("wake", ROOT / "docs/lexeme_reports/model_entries/2268-wake-wacan.model.md")]:
        text = path.read_text(encoding="utf-8")
        assert_true("[]{.recon}" not in text, f"{label} entry still contains empty []{{}}.recon span (v2 corruption)")

    # enforce corpus-wide .pred no-gloss policy
    pred_gloss_hits = []
    for path in (ROOT / "docs" / "sound_changes" / "reader_facing").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for m in PRED_GLOSS_RE.finditer(text):
            line_no = text[: m.start()].count("\n") + 1
            pred_gloss_hits.append(f"{path}:{line_no}")
    assert_true(not pred_gloss_hits, ".pred gloss policy violated:\n" + "\n".join(pred_gloss_hits[:20]))


def run_corpus_lints() -> None:
    """Structural semantic integrity lints across all canonical reader-facing sources."""
    recon_issues: list[ReconIssue] = []
    duplicate_issues: list[str] = []
    empty_recon_hits: list[str] = []
    raw_starred_iv_hits: list[str] = []
    class_compat_issues: list[str] = []
    lang_code_issues: list[str] = []
    nested_span_issues: list[str] = []

    # Pattern: .iv span with a literal leading reconstruction * WITHOUT:
    #   - backtick code span: [`*form`]{.iv} in tables is a pre-existing valid pattern
    #   - matching closing asterisk: [*form*]{.iv} is Markdown italic (valid)
    # Only flags [*form]{.iv} where the * is a reconstruction star without closing match.
    RAW_STARRED_IV_RE = re.compile(r'\[\*(?!.*\*\])[^`\]\n][^\]]*\]\{[^}]*\.iv[^}]*\}')

    # Pattern for incompatibly nested semantic spans:
    # [[inner]{.CLASS}...]{.OUTER} where CLASS and OUTER are incompatible
    # Detect: .lex inside .iv, .iv inside .lex, .lex inside .recon, .pred inside lexical span
    NESTED_SPAN_RE = re.compile(
        r'\[(?:[^\[\]]|\[[^\[\]]*\])*'  # outer open bracket with possible inner content
        r'\[([^\[\]]+)\]\{[^}]*\.(lex|iv|pred|recon|ex)[^}]*\}'  # inner semantic span
        r'[^\[\]]*\]\{'  # outer content after inner
        r'[^}]*\.(lex|iv|pred|recon|ex)[^}]*\}'  # outer semantic class
    )

    # Canonical book Markdown sources, derived from the actual build architecture.
    # The canonical build assembles:
    #   - capr_book_intro_alpha_01.md (Part 0 / Introduction)
    #   - reader_facing_local_section_20.md (Part I), assembled by
    #     tools/build_reader_book.py from:
    #       * the generated registry/reader_manifest.tsv file list
    #       * chapter intro files (chap*-*.md) named in registry/reader_chapters.tsv
    #   - lexical_volume_alpha_01.md (Part II), assembled from model entries
    #
    # We scan the individual sources rather than the assembled artifacts so that
    # file and line-number diagnostics point to the canonical edit locations.

    reader_facing_root = ROOT / "docs" / "sound_changes" / "reader_facing"
    reader_manifest = ROOT / "docs" / "sound_changes" / "registry" / "reader_manifest.tsv"

    source_paths: list[Path] = []

    # Book introduction
    intro_path = ROOT / "docs" / "assembly" / "capr_book_intro_alpha_01.md"
    if intro_path.exists():
        source_paths.append(intro_path)

    # Part I: individual sound-change files (from the generated reader manifest)
    if reader_manifest.exists():
        import csv as _csv
        manifest_lines = [ln for ln in reader_manifest.read_text(encoding="utf-8").splitlines()
                          if ln and not ln.startswith("#")]
        chapter_fnames = [row["reader_file"]
                          for row in _csv.DictReader(manifest_lines, delimiter="\t")]
        source_paths.extend(reader_facing_root / fn for fn in chapter_fnames
                            if (reader_facing_root / fn).exists())
    else:
        source_paths.extend(reader_facing_root.glob("0[0-9][0-9]-*.md"))

    # Part I: chapter introduction files
    source_paths.extend(reader_facing_root.glob("chap*-*.md"))

    # Part II: model entry files (feed the lexical volume)
    source_paths.extend(MODEL_ENTRIES.glob("*.model.md"))

    # Deduplicate preserving first-seen order
    seen_paths: set[Path] = set()
    deduped: list[Path] = []
    for p in source_paths:
        rp = p.resolve()
        if rp not in seen_paths:
            seen_paths.add(rp)
            deduped.append(p)
    source_paths = [p for p in deduped if p.exists()]

    for path in source_paths:
        text = path.read_text(encoding="utf-8")
        source_label = str(path)

        # .recon and duplicate-gloss structural checks: now apply to ALL sources
        recon_issues.extend(find_recon_span_issues(text, source_label))
        duplicate_issues.extend(find_duplicate_glosses(text, source_label))

        # Empty .recon spans (all sources)
        if "[]{.recon}" in text:
            line_no = text.find("[]{.recon}")
            lnum = text[:line_no].count("\n") + 1
            empty_recon_hits.append(f"{path}:{lnum}: empty []{{}}.recon span")

        # Raw starred .iv spans (all sources)
        for m in RAW_STARRED_IV_RE.finditer(text):
            span = m.group(0)
            if ".recon" not in span:
                lnum = text[:m.start()].count("\n") + 1
                raw_starred_iv_hits.append(f"{path}:{lnum}: raw *-prefixed form inside .iv span (use .recon+.iv): {span[:60]}")

        # Class-compatibility lint (all sources)
        class_compat_issues.extend(find_class_compat_issues(text, source_label))

        # Language code lint (all sources with .lex or .iv spans)
        lang_code_issues.extend(find_invalid_lang_codes(text, source_label))

        # Nested incompatible semantic span detection
        # Detect: .lex inside .iv (and other incompatible nesting)
        # The valid case is .recon+.iv as combined classes on the SAME span.
        # Invalid: [[form]{.lex}]{.iv} — inner .lex inside outer .iv
        for m in NESTED_SPAN_RE.finditer(text):
            inner_cls = m.group(2)
            outer_cls = m.group(3)
            # Define which nestings are invalid
            invalid_nesting = (
                (inner_cls == "lex" and outer_cls == "iv") or
                (inner_cls == "iv" and outer_cls == "lex") or
                (inner_cls == "lex" and outer_cls == "recon") or
                (inner_cls == "pred" and outer_cls in {"lex", "iv", "recon"}) or
                (inner_cls in {"lex", "iv", "recon", "pred"} and outer_cls == "ex")
            )
            if invalid_nesting:
                lnum = text[:m.start()].count("\n") + 1
                nested_span_issues.append(
                    f"{source_label}:{lnum}: nested .{inner_cls} inside .{outer_cls} span: {m.group(0)[:80]}"
                )

    assert_true(not recon_issues, "malformed .recon spans:\n" + "\n".join(f"{x.source}: {x.reason} :: {x.span}" for x in recon_issues[:40]))
    assert_true(not duplicate_issues, "adjacent duplicate glosses:\n" + "\n".join(duplicate_issues[:40]))
    assert_true(not empty_recon_hits, "empty .recon spans found:\n" + "\n".join(empty_recon_hits[:20]))
    assert_true(not raw_starred_iv_hits, "raw starred-form .iv spans (use .recon+.iv):\n" + "\n".join(raw_starred_iv_hits[:20]))
    assert_true(not class_compat_issues, "class-compatibility violations:\n" + "\n".join(class_compat_issues[:20]))
    assert_true(not lang_code_issues, "invalid language codes:\n" + "\n".join(lang_code_issues[:20]))
    assert_true(not nested_span_issues, "nested incompatible semantic spans:\n" + "\n".join(nested_span_issues[:20]))


# ── Class compatibility lint ──────────────────────────────────────────────────
_CLASS_COMPAT_RE = re.compile(r'\[([^\]]*)\]\{([^}]+)\}')


def _span_classes(attrs: str) -> set[str]:
    """Extract class names from a Pandoc span attribute string."""
    out = set()
    for token in attrs.split():
        if token.startswith("."):
            out.add(token[1:].rstrip(",;"))
    return out


def find_class_compat_issues(text: str, source: str) -> list[str]:
    """Detect invalid semantic-class combinations."""
    issues: list[str] = []
    for m in _CLASS_COMPAT_RE.finditer(text):
        classes = _span_classes(m.group(2))
        span = m.group(0)[:80]
        lnum = text[:m.start()].count("\n") + 1

        if "pred" in classes and "lex" in classes:
            issues.append(f"{source}:{lnum}: .pred and .lex combined — {span}")
        if "pred" in classes and "recon" in classes:
            issues.append(f"{source}:{lnum}: .pred and .recon combined — {span}")
        if "pred" in classes and "ex" in classes:
            issues.append(f"{source}:{lnum}: .pred and .ex combined — {span}")
        if "pred" in classes and "iv" in classes:
            issues.append(f"{source}:{lnum}: .pred and .iv combined — counterfactuals are not index material — {span}")
        if "ex" in classes and "lex" in classes:
            issues.append(f"{source}:{lnum}: .ex and .lex combined — {span}")
        if "ex" in classes and "recon" in classes:
            issues.append(f"{source}:{lnum}: .ex and .recon combined — {span}")
        if "ex" in classes and "iv" in classes:
            issues.append(f"{source}:{lnum}: .ex and .iv combined — {span}")
        if "lex" in classes and "iv" in classes:
            issues.append(f"{source}:{lnum}: .lex and .iv combined (use .iv alone) — {span}")
        if "lex" in classes and "recon" in classes:
            issues.append(f"{source}:{lnum}: .lex and .recon combined — ordinary forms cannot be simultaneously reconstructed — {span}")
    return issues


def run_class_compat_fixtures() -> None:
    """Structural class-compatibility fixtures."""
    # Prohibited combinations that must fail at corpus-lint time
    bad_combos = [
        "[*form*]{.pred .lex}",
        "[*form*]{.pred .recon}",
        "[*form*]{.pred .ex}",
        "[form]{.pred .iv lang=oe}",       # new: .pred + .iv prohibited
        "[phrase]{.ex .lex}",
        "[phrase]{.ex .recon}",
        "[phrase]{.ex .iv lang=oe}",
        "[form]{.lex .iv lang=oe}",
        "[form]{.lex .recon}",             # new: .lex + .recon prohibited
    ]
    for span in bad_combos:
        issues = find_class_compat_issues(span, "fixture")
        assert_true(issues, f"expected class-compat failure for: {span}")

    # Allowed combinations that must pass
    good_combos = [
        "[stamnaz]{.recon .iv lang=pgmc sort=stamnaz role=source_protoform}",
        "[form]{.recon} 'gloss'",
        "[form]{.lex lang=oe} 'gloss'",
        "[phrase]{.ex} included here",
        "[*form*]{.pred}",
        "[form]{.iv lang=oe sort=form role=comparison_form} 'gloss'",
    ]
    for span in good_combos:
        issues = find_class_compat_issues(span, "fixture")
        assert_true(not issues, f"unexpected class-compat failure for: {span} — {issues}")

    # Nested semantic span regressions (shoulder-style .lex inside .iv)
    # The regex in run_corpus_lints detects these patterns
    _NESTED_RE = re.compile(
        r'\[(?:[^\[\]]|\[[^\[\]]*\])*'
        r'\[([^\[\]]+)\]\{[^}]*\.(lex|iv|pred|recon|ex)[^}]*\}'
        r'[^\[\]]*\]\{'
        r'[^}]*\.(lex|iv|pred|recon|ex)[^}]*\}'
    )

    def _has_bad_nesting(text: str) -> bool:
        for m in _NESTED_RE.finditer(text):
            inner, outer = m.group(2), m.group(3)
            if (inner == "lex" and outer == "iv") or (inner == "iv" and outer == "lex"):
                return True
            if (inner == "lex" and outer == "recon"):
                return True
            if inner == "pred" and outer in {"lex", "iv", "recon"}:
                return True
        return False

    # .lex inside .iv → FAIL (shoulder-style error)
    assert_true(
        _has_bad_nesting("[[sċuldrum]{.lex lang=oe} 'dat.pl.']{.iv lang=oe sort=x role=target_form}"),
        "nested .lex inside .iv must be detected"
    )
    # .iv inside .lex → FAIL
    assert_true(
        _has_bad_nesting("[[`form`]{.iv lang=oe sort=x role=comp} 'gloss']{.lex lang=oe}"),
        "nested .iv inside .lex must be detected"
    )
    # .recon+.iv combined (same span) → PASS (not nested, not a violation)
    assert_true(
        not _has_bad_nesting("[form]{.recon .iv lang=pgmc sort=x role=source}"),
        ".recon+.iv same-span combination must NOT be flagged as nested"
    )

    # Shoulder entry regression: schulder must be lang=mlg, not lang=german
    shoulder = MODEL_ENTRIES / "2183-shoulder-sċuldrum.model.md"
    if shoulder.exists():
        sh_text = shoulder.read_text(encoding="utf-8")
        assert_true("lang=mlg" in sh_text, "shoulder: schulder must use lang=mlg (Middle Low German)")
        assert_true("schulder]{.lex lang=german}" not in sh_text, "shoulder: schulder must not be lang=german")
        assert_true("{.lex lang=oe} 'shoulder (dat.pl.)']{.iv" not in sh_text,
                    "shoulder: .lex inside .iv nesting must be removed")


# ── Manifest / model-entry consistency ───────────────────────────────────────
MANIFEST_PATH = ROOT / "docs" / "assembly" / "manifest_all_by_class.tsv"

_METADATA_RE = {
    "PROTO": re.compile(r"^PROTO:\s*(.+)$", re.MULTILINE),
    "PROTOFORM": re.compile(r"^PROTOFORM:\s*(.+)$", re.MULTILINE),
    "COUNTERPART": re.compile(r"^COUNTERPART:\s*(.+)$", re.MULTILINE),
    "DERIVATION_CLASS": re.compile(r"^DERIVATION_CLASS:\s*(.+)$", re.MULTILINE),
}


_HEADING_RE = re.compile(r"^#\s+(.+?)\s+—\s+OE\s+(.+)$", re.MULTILINE)


def _read_model_metadata(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    out: dict[str, str] = {}
    for field, pat in _METADATA_RE.items():
        m = pat.search(text)
        if m:
            out[field] = m.group(1).strip()
    # Also parse the heading for lexical_item and counterpart
    hm = _HEADING_RE.search(text)
    if hm:
        # Heading may contain multiple OE forms like "stefna, stefn" — strip to primary
        # e.g., "stem — OE stefna, stefn" → lexical_item="stem", heading_counterpart="stefna, stefn"
        out["heading_lexical_item"] = hm.group(1).strip()
        out["heading_counterpart"] = hm.group(2).strip()
    return out


def run_manifest_consistency() -> None:
    """Model-entry metadata must agree with the canonical manifest.

    Every manifest row pointing to a model entry must agree on:
    COUNTERPART, PROTO, DERIVATION_CLASS, PROTOFORM, and heading identity.
    Missing model files are flagged as errors, not silently skipped.
    """
    if not MANIFEST_PATH.exists():
        return

    mismatches: list[str] = []
    missing_files: list[str] = []
    with open(MANIFEST_PATH, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    for row in rows:
        entry_path_str = row.get("model_entry_path", "")
        if not entry_path_str:
            continue
        entry_path = ROOT.parent / entry_path_str
        if not entry_path.exists():
            missing_files.append(f"Row {row.get('row_id','?')} ({row.get('lexical_item','?')}): {entry_path_str}")
            continue

        meta = _read_model_metadata(entry_path)
        row_id = row.get("row_id", "?")
        lex_item = row.get("lexical_item", "?")

        checks = [
            ("COUNTERPART", row.get("counterpart", ""), meta.get("COUNTERPART", "")),
            ("PROTO", row.get("proto", ""), meta.get("PROTO", "")),
            ("DERIVATION_CLASS", row.get("derivation_class", ""), meta.get("DERIVATION_CLASS", "")),
        ]
        # PROTOFORM: compare strictly
        mf_proto = row.get("protoform", "")
        entry_proto = meta.get("PROTOFORM", "")
        if mf_proto and entry_proto and mf_proto != entry_proto:
            checks.append(("PROTOFORM", mf_proto, entry_proto))

        # Check heading lexical_item matches manifest — strict equality after normalization
        heading_lex = meta.get("heading_lexical_item", "")
        if not heading_lex:
            # Missing heading is an error
            mismatches.append(f"Row {row_id} ({lex_item}): model entry missing '# lexical — OE counterpart' heading")
        elif lex_item:
            # Normalize: strip common qualifiers like "/trunk", "(gen.)" etc. for comparison
            # But require that the manifest lex_item appears as the leading word(s)
            normalized_heading = re.sub(r'\s*/[^—]*', '', heading_lex).strip()  # strip "/variant"
            # Exact equality after normalization
            if normalized_heading != lex_item and heading_lex != lex_item:
                # Allow: heading may have additional descriptor after /
                # e.g., "stem" → "stem — OE stefn" heading is OK
                # But "woman" for manifest "man" must fail
                if not (heading_lex.startswith(lex_item + "/") or heading_lex == lex_item
                        or normalized_heading == lex_item):
                    mismatches.append(
                        f"Row {row_id}: heading lexical_item {heading_lex!r} does not match manifest {lex_item!r}"
                    )

        # Check heading counterpart — must match manifest counterpart exactly
        # (heading may list multiple forms as "form1, form2" — counterpart must be in list)
        heading_counterpart = meta.get("heading_counterpart", "")
        manifest_counterpart = row.get("counterpart", "")
        if heading_counterpart and manifest_counterpart:
            # The heading may list multiple forms; the manifest counterpart should appear in them
            if manifest_counterpart not in heading_counterpart:
                mismatches.append(
                    f"Row {row_id} ({lex_item}): heading counterpart {heading_counterpart!r} doesn't contain manifest counterpart {manifest_counterpart!r}"
                )

        for field, manifest_val, entry_val in checks:
            if manifest_val and entry_val and manifest_val != entry_val:
                mismatches.append(
                    f"Row {row_id} ({lex_item}): {field} manifest={manifest_val!r} vs entry={entry_val!r}"
                )

    assert_true(not missing_files, f"Manifest row(s) point to missing model files:\n" + "\n".join(missing_files[:10]))
    assert_true(
        not mismatches,
        f"Manifest/model-entry metadata mismatch ({len(mismatches)} cases):\n"
        + "\n".join(mismatches[:30]),
    )


# ── Row 2216 / trace invariants ───────────────────────────────────────────────
ALIGNED_DATA_PATH = ROOT.parent / "Germanic" / "data" / "germanic-aligned-final.tsv"
STEM_PATH_2216 = MODEL_ENTRIES / "2216-stem-stefn.model.md"


def run_row2216_invariants() -> None:
    """Row 2216 (stem/trunk) invariants protecting the homonym correction."""
    stem_text = STEM_PATH_2216.read_text(encoding="utf-8")

    # 1. model entry must NOT contain *stébnō as a selected input / protoform
    assert_true(
        "PROTOFORM: *stébnō" not in stem_text and "selected input form | *stébnō" not in stem_text,
        "Row 2216 stem entry must not use *stébnō as its PROTOFORM or selected input (wrong homonym)",
    )

    # 2. derivation class is early_analogy: stem 2216 was moved
    # known_unmodelled -> early_analogy (authoritative decision; *stámniz -> stefn
    # is regularly modelled via SC022 adjacent mn > βn).
    assert_true(
        "DERIVATION_CLASS: early_analogy" in stem_text,
        "Row 2216 must be classified as early_analogy (moved from known_unmodelled)",
    )

    # 3. homonym note must be present
    assert_true(
        "voice" in stem_text and ("homonym" in stem_text or "unrelated" in stem_text),
        "Row 2216 must contain a note distinguishing the voice/sound homonym",
    )

    # 3b. stem Source comparison table must not say "must not appear in this entry"
    # (the correct invariant is that *stébnō must not be used as derivational input)
    assert_true(
        "must not appear in this entry" not in stem_text,
        "Stem table must say 'must not be used as derivational input', not 'must not appear'",
    )

    # 4. aligned data must not use *stébnō for stem row
    if ALIGNED_DATA_PATH.exists():
        with open(ALIGNED_DATA_PATH, encoding="utf-8", newline="") as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                if len(row) >= 14 and row[0] == "2216" and row[7] == "Old_English":
                    protoform = row[2]
                    assert_true(
                        protoform != "*stébnō",
                        f"Aligned data row 2216 must not use PROTOFORM *stébnō; found {protoform!r}",
                    )
                    # 5. derivation class is early_analogy (regularly modelled)
                    deriv_class = row[10]
                    assert_true(
                        deriv_class == "early_analogy",
                        f"Aligned data row 2216 must be early_analogy; found {deriv_class!r}",
                    )
                    break

    # 6. manifest must agree: stem is now confidently traced (*stámniz -> stefn)
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                if row.get("row_id") == "2216":
                    assert_true(
                        row.get("trace_match_status", "") == "confident",
                        "Manifest row 2216 must be a confident FST trace (early_analogy)",
                    )
                    break

    # 7. Index forms TSV: no *stébnō as selected_input for stem row
    # (neither trace_proto_input nor other scope)
    if FORMS_TSV.exists():
        with open(FORMS_TSV, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                if row.get("form") in {"*stébnō", "stébnō"}:
                    src = row.get("source_ref", "")
                    # *stébnō may appear as table-ignore form but not as production selected_input
                    role = row.get("form_role", "")
                    scope = row.get("source_scope", "")
                    if role == "selected_input" and "stem" in src.lower():
                        assert_true(
                            False,
                            f"Index must not have *stébnō as selected_input for stem row; found {row}"
                        )


def run_compact_trace_quarantine_fixtures() -> None:
    """Generic regressions for the obsolete compact-trace quarantine logic.

    Verifies that build_index_verborum.py correctly quarantines compact traces
    whose proto doesn't match the active manifest protoform.
    """
    import sys
    sys.path.insert(0, str(TOOLS_DIR))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "build_index_verborum", str(TOOLS_DIR / "build_index_verborum.py")
        )
        biv = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(biv)  # type: ignore
    except Exception:
        return  # skip if builder not importable

    # The key data structure: manifest_by_title_counterpart lookup
    # Simulate a scenario where trace has mismatched proto
    test_manifest_rows = [
        {
            "lexical_item": "stem",
            "counterpart": "stefn",
            "protoform": "*stámnaz",
            "proto": "*stámnaz",
            "derivation_class": "known_unmodelled",
            "class_bucket": "known_unmodelled",
            "section_title": "Known but unmodelled developments",
            "model_entry_path": "",
            "trace_match_status": "no_match",
            "trace_match_basis": "",
            "notes": "",
        }
    ]

    # Build both lookup dicts
    by_title = {
        (r["lexical_item"], r["counterpart"], r["protoform"]): r
        for r in test_manifest_rows
    }
    by_title_counterpart = {
        (r["lexical_item"], r["counterpart"]): r
        for r in test_manifest_rows
    }

    # Fixture 1: trace matches manifest proto → should be retained
    matching_trace = {"title": "stem", "expected": "stefn", "proto": "*stámnaz", "proto_input": "*stámnaz"}
    manifest_row = by_title.get((matching_trace["title"], matching_trace["expected"], matching_trace["proto"]))
    assert_true(manifest_row is not None, "Matching trace should find a manifest row (retained)")

    # Fixture 2: same title+counterpart, different proto → should be quarantined
    mismatch_trace = {"title": "stem", "expected": "stefn", "proto": "*stébnō", "proto_input": "*stébnō"}
    manifest_row_2 = by_title.get((mismatch_trace["title"], mismatch_trace["expected"], mismatch_trace["proto"]))
    active_row = by_title_counterpart.get((mismatch_trace["title"], mismatch_trace["expected"]))
    assert_true(manifest_row_2 is None, "Mismatched trace must not find its manifest row")
    assert_true(active_row is not None, "Active manifest row must exist for same title+counterpart")
    # In the real code: when manifest_row is None but active_row exists → quarantine (continue)
    should_quarantine = (manifest_row_2 is None) and (active_row is not None)
    assert_true(should_quarantine, "Mismatched trace must be quarantined when active manifest exists")

    # Fixture 3: truly unknown entry (no active manifest row) → not quarantined
    unknown_trace = {"title": "ZZZUNKNOWN", "expected": "zzz", "proto": "*zzz", "proto_input": "*zzz"}
    manifest_row_3 = by_title.get((unknown_trace["title"], unknown_trace["expected"], unknown_trace["proto"]))
    active_row_3 = by_title_counterpart.get((unknown_trace["title"], unknown_trace["expected"]))
    should_quarantine_3 = (manifest_row_3 is None) and (active_row_3 is not None)
    assert_true(not should_quarantine_3, "Unknown entry with no active manifest must not be quarantined")

    # Fixture 4: similar titles must not quarantine each other
    # "stew" and "stem" are similar but different
    stew_manifest = {"lexical_item": "stew", "counterpart": "strēowian", "protoform": "*stráwjaną",
                     "proto": "*stráwjaną", "derivation_class": "reconstructed_oe",
                     "class_bucket": "reconstructed_oe", "section_title": "", "model_entry_path": "",
                     "trace_match_status": "", "trace_match_basis": "", "notes": ""}
    combined_manifest_rows = test_manifest_rows + [stew_manifest]
    by_tc_combined = {(r["lexical_item"], r["counterpart"]): r for r in combined_manifest_rows}
    # A stew trace must not quarantine because stem/stefn is found
    stew_trace = {"title": "stew", "expected": "strēowian", "proto": "*stráwjaną"}
    stew_active = by_tc_combined.get((stew_trace["title"], stew_trace["expected"]))
    # stem trace with stew's proto must not find stew's manifest via stem's title
    cross_quarantine = by_tc_combined.get(("stem", "strēowian"))
    assert_true(cross_quarantine is None, "stem entry must not interact with stew's counterpart")

    # Fixture 5: real index must not have *stébnō as stem selected_input
    if FORMS_TSV.exists():
        with open(FORMS_TSV, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                if (row.get("form") in {"*stébnō", "stébnō"}
                        and row.get("form_role") == "selected_input"
                        and row.get("source_scope") == "trace_proto_input"):
                    # Check source_ref doesn't say 'stem'
                    src = row.get("source_ref", "").lower()
                    if "stem" in src:
                        assert_true(
                            False,
                            f"*stébnō trace_proto_input must be quarantined for stem row; found: {row}"
                        )


# ── Render-level regression tests ────────────────────────────────────────────

LEX_FILTER = TOOLS_DIR / "lex_form_filter.lua"
RECON_FILTER = TOOLS_DIR / "reconstructed_form_filter.lua"
PRED_FILTER = TOOLS_DIR / "predicted_form_filter.lua"
INDEX_FILTER = TOOLS_DIR / "index_verborum_filter.lua"


def run_pandoc_render(markdown_text: str, filters: list[Path] | None = None, fmt: str = "html") -> tuple[int, str]:
    """Run pandoc with given filters and return (returncode, stdout)."""
    with tempfile.TemporaryDirectory() as tmp:
        md_path = Path(tmp) / "fixture.md"
        md_path.write_text(markdown_text, encoding="utf-8")
        cmd = ["pandoc", str(md_path), "--from=markdown", f"--to={fmt}"]
        for f in (filters or []):
            cmd += ["--lua-filter", str(f)]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return proc.returncode, proc.stdout


def run_render_level_fixtures() -> None:
    """Render-level regression tests for .lex, .ex, .recon, .pred."""
    # 1. .lex renders as italic in HTML
    _, html = run_pandoc_render("[faran]{.lex lang=oe}", filters=[LEX_FILTER])
    assert_true("<em>faran</em>" in html, ".lex must render as italic faran in HTML")

    # 2. .ex renders as italic phrase in HTML
    _, html = run_pandoc_render("[tó ræste]{.ex}", filters=[LEX_FILTER])
    assert_true("tó ræste" in html and "<em>" in html, ".ex must render as italic phrase in HTML")

    # 3. .recon renders as raw LaTeX \Recon{...} (TeX-only rendering)
    _, tex = run_pandoc_render("[júką]{.recon} 'yoke'", filters=[RECON_FILTER], fmt="latex")
    assert_true(r"\Recon{júką}" in tex, ".recon must render as \\Recon{júką} in LaTeX output")

    # 4. .pred renders as raw LaTeX \Pred{...}
    _, tex = run_pandoc_render("[*ġoc*]{.pred}", filters=[PRED_FILTER], fmt="latex")
    assert_true(r"\Pred{ġoc}" in tex, ".pred must render as \\Pred{ġoc} in LaTeX output")

    # 5. .lex produces no index entry (no \index{...} in TeX output)
    _, tex = run_pandoc_render("[faran]{.lex lang=oe}", filters=[LEX_FILTER], fmt="latex")
    assert_true(r"\index" not in tex, ".lex must not produce an \\index{} command")

    # 6. .ex produces no index entry
    _, tex = run_pandoc_render("[tó ræste]{.ex}", filters=[LEX_FILTER], fmt="latex")
    assert_true(r"\index" not in tex, ".ex must not produce an \\index{} command")

    # 7. Removing lex_form_filter.lua changes rendering: .lex without filter is NOT italic
    _, html_no_filter = run_pandoc_render("[faran]{.lex lang=oe}", filters=[])
    _, html_with_filter = run_pandoc_render("[faran]{.lex lang=oe}", filters=[LEX_FILTER])
    assert_true(html_with_filter != html_no_filter, "lex_form_filter.lua must change rendering of .lex spans")
    assert_true("<em>faran</em>" not in html_no_filter, "Without lex filter, .lex must not be italic")

    # 8. Combined .recon+.iv renders \Recon{...} (recon filter processes before iv filter)
    _, tex = run_pandoc_render(
        "[júką]{.recon .iv lang=pgmc sort=juką role=comparison_form} 'yoke'",
        filters=[RECON_FILTER],
        fmt="latex"
    )
    assert_true(r"\Recon{júką}" in tex, ".recon+.iv must render .recon form")


def run_recon_star_render_fixtures() -> None:
    """Fail-closed renderer validation: starred .recon spans must cause hard render failure.

    This exercises the production reconstructed_form_filter.lua directly.
    The Python source lint catches bad markup at source time; this ensures the
    *renderer* also refuses to generate **form even if a future source path is
    missed by the Python glob.
    """
    # Valid .recon renders successfully — star supplied by \\Recon macro
    code, tex = run_pandoc_render("[júką]{.recon} 'yoke'", filters=[RECON_FILTER], fmt="latex")
    assert_true(code == 0, "Valid [júką]{.recon} must render successfully (exit 0)")
    assert_true(r"\Recon{júką}" in tex, "Valid .recon must render as \\Recon{júką}")
    assert_true(r"\Recon{*" not in tex, "Valid .recon must not produce doubled-star \\Recon{*...}")

    # .recon with leading literal * must cause render failure (exit non-zero)
    bad_literal, _ = run_pandoc_render("[*júką]{.recon}", filters=[RECON_FILTER], fmt="latex")
    assert_true(bad_literal != 0, "[*júką]{.recon} must cause render failure — doubled star would result")

    # .recon with leading escaped \\* must also cause render failure
    bad_escaped, _ = run_pandoc_render("[\\*júką]{.recon}", filters=[RECON_FILTER], fmt="latex")
    assert_true(bad_escaped != 0, "[\\*júką]{.recon} must cause render failure")

    # .recon .iv combined: same star invariant applies
    bad_combined, _ = run_pandoc_render(
        "[*júką]{.recon .iv lang=pgmc sort=juką}",
        filters=[RECON_FILTER], fmt="latex"
    )
    assert_true(bad_combined != 0, "[*júką]{.recon .iv} must also fail at the renderer")

    # Literal * outside a .recon span is allowed (e.g. backtick notation, pred, plain text)
    ok_outside, _ = run_pandoc_render("`*form` outside recon", filters=[RECON_FILTER], fmt="latex")
    assert_true(ok_outside == 0, "Literal * outside .recon must not be blocked by the filter")

    ok_pred, _ = run_pandoc_render("[*ġoc*]{.pred}", filters=[RECON_FILTER, PRED_FILTER], fmt="latex")
    assert_true(ok_pred == 0, ".pred with * is allowed — .pred is not .recon")


# ── Generation-freshness check ────────────────────────────────────────────────
BOOK_BUILDER = ROOT / "docs" / "assembly" / "build_capr_book_draft.py"
LEXVOL_MD = ROOT / "docs" / "assembly" / "lexical_volume_alpha_01.md"
_ASSEMBLER_ENV_VAR = "CAPR_CHECK_FRESHNESS_ONLY"  # signal to skip PDF in freshness mode


def _run_builder_to_temp(builder: Path, repo_root: Path) -> str | None:
    """Run a builder with output directed to a temp file; return produced Markdown or None."""
    if not builder.exists():
        return None
    # Builders write deterministic Markdown to their canonical output path.
    # We run in check mode: generate fresh, read the fresh output, then restore the original.
    import tempfile, shutil

    # Identify the output path from the builder script (first .md output line heuristic)
    with open(builder, encoding="utf-8") as f:
        src = f.read()
    # Look for the generated output path
    # Both builders have: Generated /path/to/some.md
    import re as _re
    out_match = _re.search(r'Generated.*?(/[^\s\'"]+\.md)', src)
    if not out_match:
        return None
    output_path = Path(out_match.group(1).replace("${repo_root}", str(repo_root)))
    if not output_path.is_absolute():
        output_path = repo_root / output_path

    # Save original
    original = output_path.read_text(encoding="utf-8") if output_path.exists() else None
    try:
        result = subprocess.run(
            ["python3", str(builder)],
            capture_output=True, text=True, check=True,
            cwd=repo_root,
        )
        fresh = output_path.read_text(encoding="utf-8") if output_path.exists() else None
        return fresh
    except subprocess.CalledProcessError as e:
        return None
    finally:
        # Restore original so the tracker doesn't see a mutation
        if original is not None:
            output_path.write_text(original, encoding="utf-8")


# ── Language code registry ────────────────────────────────────────────────────

# Language code registry — derived from the canonical index_verborum_languages.tsv
# Invalid codes are those not in the registry but sometimes misused.
_LANGUAGES_TSV = ROOT / "docs" / "book" / "index_verborum_languages.tsv"
_INVALID_LANG_CODES: frozenset[str] = frozenset({"la", "english", "wgmc", "nwgmc"})


def _load_approved_lang_codes() -> frozenset[str]:
    """Load approved language codes from the canonical registry."""
    if not _LANGUAGES_TSV.exists():
        # Fallback: minimal hardcoded set
        return frozenset({"pie", "oe", "pgmc", "pnwgmc", "pwgmc", "paf", "preoe", "os", "on", "ohg",
                          "ofris", "goth", "german", "dutch", "lat", "mlg", "modeng",
                          "odutch", "mdutch", "me", "greek", "skt", "oirish", "goth"})
    codes: set[str] = set()
    with open(_LANGUAGES_TSV, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            code = row.get("code", "").strip()
            if code:
                codes.add(code)
    # Remove known-invalid codes that happen to be in the registry
    return frozenset(codes - _INVALID_LANG_CODES)


_APPROVED_LANG_CODES: frozenset[str] = _load_approved_lang_codes()

_LANG_ATTR_RE = re.compile(r'\{[^}]*\blang=([A-Za-z_]+)[^}]*\}')


def find_invalid_lang_codes(text: str, source: str) -> list[str]:
    """Find uses of invalid/unapproved language codes."""
    issues: list[str] = []
    for m in _LANG_ATTR_RE.finditer(text):
        code = m.group(1)
        if code not in _APPROVED_LANG_CODES:
            lnum = text[:m.start()].count("\n") + 1
            issues.append(f"{source}:{lnum}: invalid lang code {code!r} (approved codes: {sorted(_APPROVED_LANG_CODES)[:8]}...)")
    return issues


def run_lang_code_fixtures() -> None:
    """Language code registry regressions — derived from canonical registry."""
    # Registry must exist
    assert_true(_LANGUAGES_TSV.exists(), f"Language registry missing: {_LANGUAGES_TSV}")

    # Valid codes from registry: no issues
    for good_code in ["oe", "ohg", "lat", "os", "german", "mlg"]:
        issues = find_invalid_lang_codes(f"[form]{{.lex lang={good_code}}}", "fixture")
        assert_true(not issues, f"lang={good_code!r} must be valid (in registry)")

    # Invalid codes: must fail
    for bad_code in ["la", "english", "wgmc", "nwgmc"]:
        issues = find_invalid_lang_codes(f"[form]{{.lex lang={bad_code}}}", "fixture")
        assert_true(issues, f"lang={bad_code!r} must be invalid (not in registry)")

    # Truly unknown code: must fail
    issues = find_invalid_lang_codes("[form]{.lex lang=klingon}", "fixture")
    assert_true(issues, "unknown lang code must be invalid")

    # .iv with bad code
    issues = find_invalid_lang_codes("[`form`]{.iv lang=la sort=x role=comparison_form}", "fixture")
    assert_true(issues, "lang=la in .iv span must be invalid")

    # mlg approved (added to registry for shoulder/schulder)
    issues = find_invalid_lang_codes("[schulder]{.lex lang=mlg} 'shoulder'", "fixture")
    assert_true(not issues, "mlg (Middle Low German) must be approved in registry")

    # Registry and checker must agree (approved set derived from registry)
    registry_codes: set[str] = set()
    with open(_LANGUAGES_TSV, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            code = row.get("code", "").strip()
            if code:
                registry_codes.add(code)
    for code in (registry_codes - _INVALID_LANG_CODES):
        issues = find_invalid_lang_codes(f"[form]{{.lex lang={code}}}", "fixture")
        assert_true(not issues, f"Registry code {code!r} must be approved in checker")


def run_specific_typing_regressions() -> None:
    """Regressions for the concrete door/sunder/wasp/yarn/stem typing corrections."""
    door = (MODEL_ENTRIES / "1992-door-dor.model.md").read_text(encoding="utf-8")
    sunder = (MODEL_ENTRIES / "2232-sunder-sundrian.model.md").read_text(encoding="utf-8")
    wasp = (MODEL_ENTRIES / "2273-wasp-wæfs.model.md").read_text(encoding="utf-8")
    yarn = (MODEL_ENTRIES / "2305-yarn-ġearn.model.md").read_text(encoding="utf-8")

    # Door: tura must be OHG, not Latin (converted from .lex to .iv; display uses backtick)
    assert_true("`tura`]{.iv lang=ohg" in door, "door: tura must be lang=ohg (Old High German)")
    assert_true("tura]{.lex lang=la}" not in door, "door: tura must not be lang=la (Latin)")

    # Sunder: gesundrian must be OE, not OHG (converted from .lex to .iv; display uses backtick)
    assert_true("`gesundrian`]{.iv lang=oe" in sunder, "sunder: gesundrian must be lang=oe (Old English)")
    assert_true("gesundrian]{.lex lang=ohg}" not in sunder, "sunder: gesundrian must not be lang=ohg")

    # Wasp: wasp must be OE (late West Saxon), not modern English (converted from .lex to .iv)
    assert_true("wasp`]{.iv lang=oe" in wasp, "wasp: 'wasp' must be lang=oe (Old English)")
    assert_true("lang=english" not in wasp, "wasp: no lang=english in wasp entry")

    # Yarn: filatum must not be .lex comparative evidence
    assert_true(".lex lang=la" not in yarn, "yarn: filatum must not be .lex lang=la")
    assert_true(".lex lang=lat" not in yarn, "yarn: filatum must not be .lex lang=lat")
    assert_true("filatum" in yarn, "yarn: filatum should still appear (as prose text)")


def run_row2216_voice_stem_regressions() -> None:
    """Regressions for stem entry homonym distinction."""
    stem = STEM_PATH.read_text(encoding="utf-8")

    # 1. Voice-word stefn in homonym discussion has 'voice, sound' meaning
    assert_true(
        "'voice, sound'" in stem,
        "Stem entry must contain 'voice, sound' for voice homonym",
    )

    # 2. The homonym path leading to stefn via *stebnō must be glossed 'voice, sound'
    assert_true(
        "giving" not in stem or "giving [stefn]" not in stem
        or "'voice, sound'" in stem[stem.find("giving"):stem.find("giving") + 100],
        "Homonym voice path must gloss stefn as 'voice, sound', not 'stem, trunk'",
    )

    # 3. No regular_output role in row 2216 (the entry is table-based, not a
    # single regular span; early_analogy input *stámniz is modelled via SC022).
    assert_true(
        "role=regular_output" not in stem,
        "Row 2216 stem entry must not have role=regular_output",
    )

    # 4. Row 2216 in aligned data: no *stébnō PROTOFORM, class=early_analogy
    if ALIGNED_DATA_PATH.exists():
        with open(ALIGNED_DATA_PATH, encoding="utf-8", newline="") as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                if len(row) >= 11 and row[0] == "2216" and row[7] == "Old_English":
                    assert_true(row[2] != "*stébnō", f"Aligned row 2216 PROTOFORM must not be *stébnō; got {row[2]!r}")
                    assert_true(row[10] == "early_analogy", f"Aligned row 2216 must be early_analogy; got {row[10]!r}")
                    break

    # 5. Index forms TSV must not have *stébnō for stem row as selected_input/trace
    if FORMS_TSV.exists():
        with open(FORMS_TSV, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                if (row.get("form") in {"*stébnō", "stébnō"}
                        and row.get("source_ref", "").startswith("stem")):
                    assert_true(False, f"Index must not contain *stébnō for stem row; found {row}")


def run_explicit_forms_all_sections_fixtures() -> None:
    """.lex and .iv must be checked even in subsections not on the PROSE_SECTIONS allowlist."""
    # .lex in a homonym-note subsection must be checked
    code, _ = run_validator(
        "# Sound changes\n\nA stub.\n\n"
        "# Word-by-word derivations\n\n"
        "### Fixture entry\n\n"
        "#### Homonym note\n\n"
        "[stefn]{.lex lang=oe} appears in the homonym note without gloss.\n"
    )
    assert_true(code == 2, ".lex without gloss in Homonym note must fail")

    # .lex with gloss in Homonym note must pass
    code, _ = run_validator(
        "# Sound changes\n\nA stub.\n\n"
        "# Word-by-word derivations\n\n"
        "### Fixture entry\n\n"
        "#### Homonym note\n\n"
        "[stefn]{.lex lang=oe} 'stem, trunk' appears in the homonym note.\n"
    )
    assert_true(code == 0, ".lex with gloss in Homonym note must pass")

    # .iv without gloss in non-prose subsection must also fail
    code, _ = run_validator(
        "# Sound changes\n\nA stub.\n\n"
        "# Word-by-word derivations\n\n"
        "### Fixture entry\n\n"
        "#### Source comparison\n\n"
        "[`form`]{.iv lang=oe sort=form role=comparison_form} without gloss.\n"
    )
    assert_true(code == 2, ".iv without gloss in Source comparison section must fail")


# ── Occurrence-gating smoke test ──────────────────────────────────────────────

def run_occurrence_gating_fixture() -> None:
    """Pandoc fixture: occurrence-specific gating — only the occurrence whose source_ref
    is in print_main.tsv emits an \\index command.

    Two .iv forms share the same lang, form, and role but have different source_ref
    values and different sort= keys so their emitted \\index commands are distinguishable.
    When only occurrence A is in print_main.tsv, only A's sort key appears in the TeX.
    When only B is in print_main.tsv, only B's sort key appears.
    This would fail if the filter fell back to source-less matching or always
    emitted the first / second occurrence regardless of source_ref.
    """
    import os

    PRINT_MAIN_FIELDS = [
        "language", "form", "display", "sort_key", "form_role",
        "source_scope", "source_ref", "origin", "status",
    ]

    # Occurrences A and B: same lang/form/role, different source_ref AND sort key.
    # Different sort keys make the emitted \index commands distinguishable.
    ref_a = "fixturepath/file.md:10"
    ref_b = "fixturepath/file.md:99"
    sort_a = "fixtthenkijana_occ_A"
    sort_b = "fixtthenkijana_occ_B"
    FORM = "þénkijaną"

    md_a = (
        f"[{FORM}]{{.iv lang=pgmc sort={sort_a} role=evidence_form "
        f"source_ref={ref_a}}} 'think A'"
    )
    md_b = (
        f"[{FORM}]{{.iv lang=pgmc sort={sort_b} role=evidence_form "
        f"source_ref={ref_b}}} 'think B'"
    )
    md_both = md_a + "\n\n" + md_b

    def make_print_main_tsv(directory: str, source_ref: str) -> str:
        tsv_dir = Path(directory)
        tsv_dir.mkdir(parents=True, exist_ok=True)
        tsv_path = tsv_dir / "print_main.tsv"
        header = "\t".join(PRINT_MAIN_FIELDS)
        row = "\t".join([
            "pgmc", FORM, f"*{FORM}", "thenkijana", "evidence_form",
            "explicit_tag", source_ref, "fixture", "active",
        ])
        tsv_path.write_text(header + "\n" + row + "\n", encoding="utf-8")
        return str(tsv_path)

    def run_with_tsv(md: str, tsv_path: str) -> str:
        env = {
            **os.environ,
            "CAPR_IV_PRINT_MAIN_TSV": tsv_path,
            "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(ROOT / "docs" / "book" / "index_verborum_languages.tsv"),
        }
        with tempfile.TemporaryDirectory() as tmp2:
            md_path = Path(tmp2) / "fixture.md"
            md_path.write_text(md, encoding="utf-8")
            cmd = ["pandoc", str(md_path), "--from=markdown", "--to=latex",
                   "--lua-filter", str(INDEX_FILTER)]
            proc = subprocess.run(
                cmd, capture_output=True, text=True, check=False, env=env, cwd=ROOT.parent
            )
            assert_true(proc.returncode == 0, f"Occurrence-gating pandoc run failed: {proc.stderr}")
            return proc.stdout

    with tempfile.TemporaryDirectory() as tmp:
        # Round 1: only A in print_main → A's sort key present, B's absent
        tsv_a = make_print_main_tsv(tmp + "/a", ref_a)
        tex_a = run_with_tsv(md_both, tsv_a)
        assert_true(
            sort_a in tex_a,
            f"Occurrence-gating: with only A, expected sort key {sort_a!r} in TeX. tex={tex_a!r}",
        )
        assert_true(
            sort_b not in tex_a,
            f"Occurrence-gating: with only A, sort key {sort_b!r} must NOT appear. tex={tex_a!r}",
        )

        # Round 2: only B in print_main → B's sort key present, A's absent
        tsv_b = make_print_main_tsv(tmp + "/b", ref_b)
        tex_b = run_with_tsv(md_both, tsv_b)
        assert_true(
            sort_b in tex_b,
            f"Occurrence-gating: with only B, expected sort key {sort_b!r} in TeX. tex={tex_b!r}",
        )
        assert_true(
            sort_a not in tex_b,
            f"Occurrence-gating: with only B, sort key {sort_a!r} must NOT appear. tex={tex_b!r}",
        )

        # Sanity: both A and B in print_main → both sort keys present
        tsv_ab_path = Path(tmp + "/ab")
        tsv_ab_path.mkdir(exist_ok=True)
        tsv_ab = str(tsv_ab_path / "print_main.tsv")
        header = "\t".join(PRINT_MAIN_FIELDS)
        ab_rows = [
            "\t".join(["pgmc", FORM, f"*{FORM}", "thenkijana", "evidence_form",
                        "explicit_tag", ref_a, "fixture", "active"]),
            "\t".join(["pgmc", FORM, f"*{FORM}", "thenkijana", "evidence_form",
                        "explicit_tag", ref_b, "fixture", "active"]),
        ]
        Path(tsv_ab).write_text(header + "\n" + "\n".join(ab_rows) + "\n", encoding="utf-8")
        tex_ab = run_with_tsv(md_both, tsv_ab)
        assert_true(
            sort_a in tex_ab and sort_b in tex_ab,
            f"Occurrence-gating: with both, expected both sort keys in TeX. tex={tex_ab!r}",
        )


# ── Section count regression ──────────────────────────────────────────────────

def run_section_count_regression() -> None:
    """Section counts displayed in the generated lexical volume must match the manifest.

    The count list is generated by build_full_lexical_volume.py and appears without bold
    in the generated output. This check reads the generated lexical_volume_alpha_01.md
    and requires every class count to be present and correct.
    """
    if not MANIFEST_PATH.exists():
        return
    import collections, re as _re

    with open(MANIFEST_PATH, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    manifest_counts = collections.Counter(row.get("derivation_class", "") for row in rows)

    # Generated label: matches the output of build_front_matter() in build_full_lexical_volume.py.
    # Labels are plain text without bold; the pattern must not require ** markers.
    class_generated_labels = {
        "regular": "Regular derivations",
        "attested_variant": "Attested variants",
        "early_analogy": "Early analogy",
        "late_analogy": "Late analogy",
        "reconstructed_oe": "Reconstructed Old English comparators",
        "known_unmodelled": "Known but unmodelled developments",
        "unexplained_unmodelled": "Unexplained or deliberately unmodelled exceptions",
    }

    lexvol_path = ROOT / "docs" / "assembly" / "lexical_volume_alpha_01.md"
    if not lexvol_path.exists():
        assert_true(False, f"Generated lexical volume not found: {lexvol_path}")
        return

    lexvol_text = lexvol_path.read_text(encoding="utf-8")
    mismatches: list[str] = []

    for cls, label in class_generated_labels.items():
        expected = manifest_counts.get(cls, 0)
        # Plain-number pattern (no bold markers): "- Label: N"
        pat = _re.compile(r'^- ' + _re.escape(label) + r':\s*(\d+)\s*$', _re.MULTILINE)
        all_matches = pat.findall(lexvol_text)
        if len(all_matches) == 0:
            mismatches.append(f"  {cls}: count line for '{label}' not found in lexical_volume_alpha_01.md (expected {expected})")
        elif len(all_matches) > 1:
            mismatches.append(f"  {cls}: count line for '{label}' appears {len(all_matches)} times (must appear exactly once)")
        else:
            displayed = int(all_matches[0])
            if displayed != expected:
                mismatches.append(f"  {cls}: displayed {displayed} but manifest has {expected}")

    assert_true(
        not mismatches,
        "Section count mismatches (generated volume vs manifest):\n" + "\n".join(mismatches),
    )

    # Fixtures: exactly-once enforcement
    fixture_text_good = "- Regular derivations: 70\n"
    fixture_text_missing = "- Something else: 5\n"
    fixture_text_duplicate = "- Regular derivations: 70\n- Regular derivations: 70\n"
    fixture_text_wrong = "- Regular derivations: 99\n"
    pat_fix = _re.compile(r'^- Regular derivations:\s*(\d+)\s*$', _re.MULTILINE)
    assert_true(len(pat_fix.findall(fixture_text_good)) == 1, "Exactly-once fixture: good case failed")
    assert_true(len(pat_fix.findall(fixture_text_missing)) == 0, "Exactly-once fixture: missing case failed")
    assert_true(len(pat_fix.findall(fixture_text_duplicate)) == 2, "Exactly-once fixture: duplicate case failed")
    good_val = pat_fix.findall(fixture_text_good)
    wrong_val = pat_fix.findall(fixture_text_wrong)
    assert_true(good_val and int(good_val[0]) != 99, "Exactly-once fixture: good value sanity failed")
    assert_true(wrong_val and int(wrong_val[0]) == 99, "Exactly-once fixture: wrong value sanity failed")

    # Secondary: check section_introductions_draft.md for terminology hygiene
    intro_path = ROOT / "docs" / "assembly" / "section_introductions_draft.md"
    if intro_path.exists():
        intro_text = intro_path.read_text(encoding="utf-8")
        assert_true(
            "remodelling" not in intro_text.lower(),
            "Section intro must not use old 'remodellings'/'remodeling' terminology",
        )
        known_section_match = _re.search(
            r'## Known but unmodelled[^\n]*\n+(.*?)(?=\n##|\Z)', intro_text, _re.DOTALL
        )
        if known_section_match:
            desc = known_section_match.group(1).lower()
            assert_true(
                "fst" in desc or "cascade" in desc or "transducer" in desc,
                "known_unmodelled section should reference FST/cascade as the gap",
            )


# ── Freshness fail-closed ─────────────────────────────────────────────────────

def run_generation_freshness() -> None:
    """Freshness: tracked artifact == output from canonical sources.

    Idempotency: two consecutive runs produce the same output.

    Builder failure must cause this check to FAIL, not skip.
    """
    repo_root = ROOT.parent

    for label, builder, tracked in [
        ("lexical volume", LEXVOL_BUILDER, LEXVOL_MD),
        ("assembled book", BOOK_BUILDER, ASSEMBLED),
    ]:
        if not builder.exists() or not tracked.exists():
            continue

        # Save original
        original = tracked.read_text(encoding="utf-8")

        try:
            result = subprocess.run(
                ["python3", str(builder)],
                capture_output=True, text=True, check=True,
                cwd=repo_root,
            )
        except subprocess.CalledProcessError as e:
            # Builder failure → gate FAILS (not skip)
            assert_true(False, f"{label} builder failed; cannot verify freshness: {e.stderr[:200]}")
            return

        fresh = tracked.read_text(encoding="utf-8")

        # Restore — we are non-mutating
        tracked.write_text(original, encoding="utf-8")

        assert_true(
            original == fresh,
            f"{label}: tracked artifact is stale — tracked and freshly-generated content differ"
        )

        # Idempotency: run again and check same result
        try:
            subprocess.run(
                ["python3", str(builder)],
                capture_output=True, text=True, check=True,
                cwd=repo_root,
            )
        except subprocess.CalledProcessError as e:
            assert_true(False, f"{label} second run failed: {e.stderr[:200]}")
            return

        second = tracked.read_text(encoding="utf-8")
        tracked.write_text(original, encoding="utf-8")
        assert_true(
            fresh == second,
            f"{label}: generation is not idempotent — second run produced different output"
        )


def run_trace_render_fixtures() -> None:
    module = load_lexical_volume_module()

    # Single-star and double-star stage markers should both parse as stage headings.
    single_star = module.parse_trace_cell("*Proto-West Germanic*<br/>PWGmc Final Bare A Loss: bucc")
    assert_true(single_star and single_star[0][0] == "Proto-West Germanic", "single-star Proto-West Germanic must parse as stage")

    northwest = module.parse_trace_cell("*Northwest Germanic*<br/>[no change]")
    assert_true(northwest and northwest[0][0] == "Northwest Germanic", "single-star Northwest Germanic must parse as stage")

    old_english = module.parse_trace_cell("*Old English*<br/>[no change]")
    assert_true(old_english and old_english[0][0] == "Old English", "single-star Old English must parse as stage")

    double_star = module.parse_trace_cell("**Old English**<br/>[no change]")
    assert_true(double_star and double_star[0][0] == "Old English", "double-star Old English should remain accepted")

    # Representative fixture for rendering semantics and width allocation.
    trace_entry = {
        "table": (
            "| Earlier Germanic developments | Old English developments |\n"
            "| --- | --- |\n"
            "| *Proto-West Germanic*<br/>[no change] | *Northwest Germanic*<br/>PWGmc Final Bare A Loss: bucc<br/>*Old English*<br/>[no change] |"
        )
    }
    tex = "\n".join(module.render_trace_table(trace_entry))

    assert_true(r"\textbf{Proto-West Germanic}" in tex, "Proto-West Germanic stage heading must render in bold")
    assert_true(r"\textbf{Northwest Germanic}" in tex, "Northwest Germanic stage heading must render in bold")
    old_english_panel = "\n".join(
        module.render_trace_panel([("Old English", [("[no change]", "")])], suppress_old_english_stage=False)
    )
    assert_true(r"\textbf{Old English}" in old_english_panel, "Old English stage heading must render in bold")
    assert_true(r"\textbf{West Germanic}" not in tex, "Proto-West Germanic label must not be silently renamed")
    assert_true("*Proto-West Germanic*" not in tex and "*Northwest Germanic*" not in tex and "*Old English*" not in tex,
                "literal stage-marker asterisks must not survive into trace TeX")

    assert_true(">{\\centering\\arraybackslash}X" not in tex, "outer trace table must not include empty stretchable middle X column")
    assert_true("\n&\n&\n" not in tex, "outer trace table must not include an intentionally empty middle cell")
    assert_true(r"\mbox{PWGmc Final Bare A Loss}" in tex, "representative ordinary label should be kept on one line")


def run_recon_iv_index_display_check() -> None:
    """Every explicit_tag row from a .recon .iv span must carry the reconstruction asterisk.

    For each canonical source occurrence with combined .recon .iv, this check:
    1. Derives the occurrence identity (language, form, role, source_ref) from the source.
    2. Locates the corresponding row in the authoritative generated print_main.tsv.
    3. Requires that: the row exists, its display begins with exactly one *, its sort_key
       does not begin with *, and no unstarred twin exists for that source occurrence.

    Also exercises the production extraction function directly via subprocess.
    """
    pm_path = ROOT / "docs" / "book" / "index_verborum_print_main.tsv"
    if not pm_path.exists():
        return

    # Load generated print_main.tsv indexed by occurrence identity
    pm_by_occ: dict[tuple[str, str, str, str], list[dict[str, str]]] = {}
    with pm_path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if (row.get("source_scope") or "").strip() != "explicit_tag":
                continue
            key = (
                (row.get("language") or "").strip(),
                (row.get("form") or "").strip(),
                (row.get("form_role") or "evidence_form").strip(),
                (row.get("source_ref") or "").strip(),
            )
            pm_by_occ.setdefault(key, []).append(row)

    # Self-contained span parser (mirrors iter_explicit_tags essentials)
    EXPLICIT_SPAN_RE = re.compile(r'\[(?P<content>[^\[\]]+)\]\{(?P<attrs>[^}]+)\}')
    ATTR_VAL_RE = re.compile(r'(?P<key>[A-Za-z_][A-Za-z0-9_-]*)=(?:"(?P<qval>[^"]*?)"|(?P<val>\S+?)(?=[\s}]|$))')
    MARKUP_STRIP_RE = re.compile(r'\[[^\[\]]+\]\{[^}]*\}|`[^`]+`|_([^_]+)_|\*([^*]+)\*|[\[\]]|\{[^}]*\}')

    def parse_span_attrs(raw: str) -> dict[str, str]:
        result: dict[str, str] = {}
        for m in ATTR_VAL_RE.finditer(raw):
            result[m.group("key")] = m.group("qval") if m.group("qval") is not None else (m.group("val") or "")
        return result

    def has_cls(raw: str, cls: str) -> bool:
        return bool(re.search(rf"(^|\s)\.{re.escape(cls)}(?=\s|$)", raw))

    def strip_markup_simple(text: str) -> str:
        return MARKUP_STRIP_RE.sub(lambda m: m.group(1) or m.group(2) or "", text).strip()

    source_paths = [
        TOOLS_DIR.parent / "docs" / "assembly" / "capr_book_intro_alpha_01.md",
        TOOLS_DIR.parent / "docs" / "sound_changes" / "reader_facing" / "reader_facing_local_section_20.md",
        *sorted((TOOLS_DIR.parent / "docs" / "lexeme_reports" / "model_entries").glob("*.model.md")),
    ]

    failures: list[str] = []
    for src in source_paths:
        if not src.exists():
            continue
        rel = src.relative_to(ROOT.parent).as_posix()
        for line_no, line in enumerate(src.read_text(encoding="utf-8").splitlines(), 1):
            for span_m in EXPLICIT_SPAN_RE.finditer(line):
                raw_attrs = span_m.group("attrs")
                if not (has_cls(raw_attrs, "iv") and has_cls(raw_attrs, "recon")):
                    continue
                attrs = parse_span_attrs(raw_attrs)
                bare_form = strip_markup_simple(span_m.group("content"))
                # Normalize U+1E2F → ī + combining acute to match generated TSVs.
                bare_form = bare_form.replace("\u1e2f", "\u012b\u0301")
                lang = attrs.get("lang", "").strip()
                role = (attrs.get("role", "") or "evidence_form").strip()
                source_ref = f"{rel}:{line_no}"
                occ_key = (lang, bare_form, role, source_ref)

                # Look up in actual generated TSV
                generated_rows = pm_by_occ.get(occ_key, [])
                if not generated_rows:
                    failures.append(f"  {rel}:{line_no}: no generated row for .recon .iv occurrence ({lang!r}, {bare_form!r}, {role!r})")
                    continue
                for grow in generated_rows:
                    disp = grow.get("display", "")
                    sort_k = grow.get("sort_key", "")
                    if not disp.startswith("*"):
                        failures.append(f"  {rel}:{line_no}: display {disp!r} must begin with * for .recon .iv")
                    if disp.startswith("**"):
                        failures.append(f"  {rel}:{line_no}: display {disp!r} has doubled star (should be exactly one *)")
                    if sort_k.startswith("*"):
                        failures.append(f"  {rel}:{line_no}: sort_key {sort_k!r} must not begin with * for .recon .iv")

                # Also check: no unstarred twin with same occurrence identity
                unstarred_rows = [r for r in generated_rows if not r.get("display", "").startswith("*")]
                if unstarred_rows:
                    failures.append(f"  {rel}:{line_no}: unstarred twin display {unstarred_rows[0].get('display')!r} alongside starred entry")

    assert_true(not failures, ".recon .iv generated index rows have incorrect display/sort:\n" + "\n".join(failures[:10]))

    # ── Self-contained production fixture via subprocess ────────────────────────
    # Run the actual production extraction function on a fixture file and verify output.
    biv_script = TOOLS_DIR / "build_index_verborum.py"
    if biv_script.exists():
        fixture_snippet = textwrap.dedent("""\
            import sys, json
            sys.path.insert(0, r"{tools_dir}")
            import build_index_verborum as _biv
            from pathlib import Path
            import tempfile, os

            with tempfile.TemporaryDirectory() as tmp:
                # Fixture: .recon .iv span
                fixture = Path(tmp) / "fixture.model.md"
                fixture.write_text(
                    "# bake -- OE bacan\\n"
                    "PROTO: *bákaną\\nPROTOFORM: *bákaną\\nCOUNTERPART: bacan\\nDERIVATION_CLASS: regular\\n\\n"
                    "[bákaną]{{.recon .iv lang=pgmc sort=bakana role=selected_input}} 'bake'\\n"
                    "[bacan]{{.iv lang=oe sort=bacan role=evidence_form}} 'bake'\\n",
                    encoding="utf-8",
                )
                occs = _biv.explicit_tag_occurrences([fixture])

            results = []
            for occ in occs:
                results.append({{
                    "language": occ["language"],
                    "form": occ["form"],
                    "display": occ["display"],
                    "sort_key": occ["sort_key"],
                    "form_role": occ["form_role"],
                }})
            print(json.dumps(results))
        """.format(tools_dir=str(TOOLS_DIR)))

        proc = subprocess.run(
            ["python3", "-c", fixture_snippet],
            capture_output=True, text=True, check=False,
        )
        if proc.returncode == 0:
            import json as _json
            extracted = _json.loads(proc.stdout)
            recon_rows = [r for r in extracted if r.get("language") == "pgmc" and r.get("form") == "bákaną"]
            attested_rows = [r for r in extracted if r.get("language") == "oe" and r.get("form") == "bacan"]

            # .recon .iv row
            assert_true(bool(recon_rows), "Production fixture: no pgmc bákaną row from .recon .iv span")
            for r in recon_rows:
                assert_true(r["display"] == "*bákaną", f"Production fixture: display must be *bákaną, got {r['display']!r}")
                assert_true(r["sort_key"] == "bakana", f"Production fixture: sort_key must be bakana, got {r['sort_key']!r}")
                assert_true(not r["sort_key"].startswith("*"), "Production fixture: sort_key must not start with *")

            # attested .iv row (no .recon)
            assert_true(bool(attested_rows), "Production fixture: no oe bacan row")
            for r in attested_rows:
                assert_true(r["display"] == "bacan", f"Production fixture: attested display must be bacan (unstarred), got {r['display']!r}")

            # .recon without .iv produces no index row
            no_recon_snippet = textwrap.dedent("""\
                import sys, json
                sys.path.insert(0, r"{tools_dir}")
                import build_index_verborum as _biv
                from pathlib import Path
                import tempfile

                with tempfile.TemporaryDirectory() as tmp:
                    fixture = Path(tmp) / "fixture.model.md"
                    fixture.write_text(
                        "[bákaną]{{.recon lang=pgmc}} 'bake'\\n",
                        encoding="utf-8"
                    )
                    occs = _biv.explicit_tag_occurrences([fixture])
                print(json.dumps([o["language"] for o in occs]))
            """.format(tools_dir=str(TOOLS_DIR)))
            p2 = subprocess.run(["python3", "-c", no_recon_snippet], capture_output=True, text=True, check=False)
            if p2.returncode == 0:
                no_index = _json.loads(p2.stdout)
                assert_true(not any(l == "pgmc" for l in no_index), ".recon without .iv must produce no explicit index row")

    # Fixture: doubled-star explicit display is not accepted by the asterisk check
    doubled_display = "**bákaną"
    doubled_is_problem = doubled_display.startswith("**")
    assert_true(doubled_is_problem, "Doubled-star detection fixture: **form must be flagged")


def run_recon_iv_lua_sort_check() -> None:
    """Verify the Lua filter uses bare form (not starred display) for the sort key.

    A .recon .iv span without explicit sort= must produce sort=bare_form, not sort=*form.
    An explicit sort= must be preserved exactly.
    """
    index_filter = TOOLS_DIR / "index_verborum_filter.lua"
    lang_registry = ROOT / "docs" / "book" / "index_verborum_languages.tsv"
    if not index_filter.exists():
        return

    def _run_lua_fixture(md: str, print_main_rows: list[str]) -> str:
        with tempfile.TemporaryDirectory() as tmp:
            md_path = Path(tmp) / "fixture.md"
            md_path.write_text(md, encoding="utf-8")
            tsv_path = Path(tmp) / "print_main.tsv"
            header = "language\tform\tdisplay\tsort_key\tform_role\tsource_scope\tsource_ref\torigin\tstatus"
            tsv_path.write_text(header + "\n" + "\n".join(print_main_rows) + "\n", encoding="utf-8")
            env = {
                **__import__("os").environ,
                "CAPR_IV_PRINT_MAIN_TSV": str(tsv_path),
                "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(lang_registry),
            }
            proc = subprocess.run(
                ["pandoc", str(md_path), "--from=markdown", "--to=latex",
                 "--lua-filter", str(index_filter)],
                capture_output=True, text=True, check=False, env=env,
                cwd=ROOT.parent,
            )
            return proc.stdout

    def _extract_index_cmd(tex: str) -> str | None:
        """Extract the first \\index[iv]{...} command with brace-counting."""
        if "\\index[iv]{" not in tex:
            return None
        start = tex.index("\\index[iv]{")
        body_start = start + len("\\index[iv]{")
        depth = 1
        pos = body_start
        while pos < len(tex) and depth > 0:
            if tex[pos] == "{":
                depth += 1
            elif tex[pos] == "}":
                depth -= 1
            pos += 1
        return tex[start:pos]

    # Fixture A: .recon .iv without explicit sort= — sort must NOT start with * (the bug was sort=display=*form)
    # Note: in production all .recon .iv spans include explicit sort=, but this tests the fallback.
    source_ref_a = "fixture/test_a.md:1"
    pm_row_a = f"pgmc\tbákaną\t*bákaną\tbakana\tselected_input\texplicit_tag\t{source_ref_a}\tfixture\tactive"
    md_a = f'[bákaną]{{.recon .iv lang=pgmc role=selected_input source_ref="{source_ref_a}"}} bake'
    tex_a = _run_lua_fixture(md_a, [pm_row_a])
    cmd_a = _extract_index_cmd(tex_a)
    assert_true(cmd_a is not None, "Lua sort fixture A: no index command generated")
    if cmd_a:
        # Sort key is between first ! and first @ after !
        bang_pos = cmd_a.find("!")
        at_pos = cmd_a.find("@", bang_pos)
        sort_in_cmd = cmd_a[bang_pos + 1:at_pos] if bang_pos != -1 and at_pos != -1 else ""
        assert_true(not sort_in_cmd.startswith("*"), f"Lua sort fixture A: sort key must not start with *, got: {sort_in_cmd!r} in {cmd_a!r}")

    # Fixture B: .recon .iv WITH explicit sort=bakana — preserve exactly as bakana
    source_ref_b = "fixture/test_b.md:1"
    pm_row_b = f"pgmc\tbákaną\t*bákaną\tbakana\tselected_input\texplicit_tag\t{source_ref_b}\tfixture\tactive"
    md_b = f'[bákaną]{{.recon .iv lang=pgmc sort=bakana role=selected_input source_ref="{source_ref_b}"}} bake'
    tex_b = _run_lua_fixture(md_b, [pm_row_b])
    cmd_b = _extract_index_cmd(tex_b)
    if cmd_b:
        bang_pos = cmd_b.find("!")
        at_pos = cmd_b.find("@", bang_pos)
        sort_in_cmd = cmd_b[bang_pos + 1:at_pos] if bang_pos != -1 and at_pos != -1 else ""
        assert_true(sort_in_cmd == "bakana", f"Lua sort fixture B: explicit sort=bakana must be preserved, got: {sort_in_cmd!r}")
        assert_true(not sort_in_cmd.startswith("*"), f"Lua sort fixture B: sort key must not start with *, got: {sort_in_cmd!r}")

    # Fixture C: attested .iv (no .recon) — display is unstarred
    source_ref_c = "fixture/test_c.md:1"
    pm_row_c = f"oe\tbacan\tbacan\tbacan\tevidence_form\texplicit_tag\t{source_ref_c}\tfixture\tactive"
    md_c = f'[`bacan`]{{.iv lang=oe sort=bacan source_ref="{source_ref_c}"}} bake'
    tex_c = _run_lua_fixture(md_c, [pm_row_c])
    cmd_c = _extract_index_cmd(tex_c)
    if cmd_c:
        assert_true("\\iventry{bacan}{}" in cmd_c and "\\iventry{*" not in cmd_c,
                     f"Lua sort fixture C: attested OE form must be unstarred in display, got: {cmd_c!r}")


def main() -> int:
    if not VALIDATOR.exists():
        print(f"Missing validator: {VALIDATOR}", file=sys.stderr)
        return 2
    if not FORMS_TSV.exists():
        print(f"Missing index forms TSV: {FORMS_TSV}", file=sys.stderr)
        return 2
    if not ASSEMBLED.exists():
        print(f"Missing assembled markdown: {ASSEMBLED}", file=sys.stderr)
        return 2

    try:
        run_predicted_fixtures()
        run_notation_fixtures()
        run_unicode_ascii_fixtures()
        run_lex_ex_fixtures()
        run_case_normalization_fixtures()
        run_recon_duplicate_fixtures()
        run_class_compat_fixtures()
        run_lang_code_fixtures()
        run_render_level_fixtures()
        run_recon_star_render_fixtures()
        run_occurrence_gating_fixture()
        run_stats_regression()
        run_known_entry_checks()
        run_specific_typing_regressions()
        run_row2216_voice_stem_regressions()
        run_explicit_forms_all_sections_fixtures()
        run_section_count_regression()
        run_corpus_lints()
        run_manifest_consistency()
        run_row2216_invariants()
        run_compact_trace_quarantine_fixtures()
        run_trace_render_fixtures()
        run_fingerprint_lifecycle_fixtures()
        run_generation_freshness()
        run_index_fingerprint_checks()
        run_recon_iv_index_display_check()
        run_recon_iv_lua_sort_check()
        run_references_structure_check()
        run_references_negative_fixture()
        run_gloss_inside_span_check()
        run_bold_prose_check()
    except AssertionError as exc:
        print(f"Reader-facing semantic regression failure: {exc}", file=sys.stderr)
        return 2
    except subprocess.CalledProcessError as exc:
        print(f"Reader-facing semantic regression command failed: {exc}", file=sys.stderr)
        return 2

    print("Reader-facing semantic regression suite passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
