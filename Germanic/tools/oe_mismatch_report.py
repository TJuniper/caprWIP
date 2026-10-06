#!/usr/bin/env python3
"""Unified OE mismatch report with mechanistic sub-buckets.

Each bucket targets ONE hypothesis / ONE mechanism so that future debugging
is safe and focused.  See inline comments for the rationale behind each split.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple
from oe_pipeline import evaluation_input, load_rows as load_contextual_rows

# Note: Hyphen (-) is NOT stripped because compounds use it (e.g., *regnă-bugô)
PROTO_STRIP_RE = re.compile(r"[{}*\s/()]")

# =============================================================================
# DIAGNOSTIC NOTES: Initial impressions for each bucket type
# These help prioritize fixes and understand root causes.
# =============================================================================
BUCKET_DIAGNOSTICS: Dict[str, Dict[str, str]] = {
    # CORE BUCKETS
    "i_umlaut_missing_true": {
        "issue": "I-umlaut trigger not applied",
        "likely_cause": "Diphthong (*ai) not being parsed as umlaut trigger, or rule ordering",
        "action": "Check i-umlaut rule handles diphthongs with *i component",
    },
    "fronting_missing__afb": {
        "issue": "A-fronting before nasals/consonants not applied",
        "likely_cause": "Often TSV issue — proto is one form class (verb), target is another (noun)",
        "action": "Check paradigm cell alignment; may need different proto form",
    },
    "breaking_missing__expected_ea": {
        "issue": "Breaking to ēa not applied",
        "likely_cause": "Breaking context not recognized (before r/l/h + consonant)",
        "action": "Check breaking rule environments",
    },
    "breaking_missing__expected_ea_got_a": {
        "issue": "Expected ēa but got short a/æ",
        "likely_cause": "Breaking not applying; may also involve length issues",
        "action": "Check breaking before dental fricatives (þ/ð)",
    },
    "breaking_missing__expected_eo": {
        "issue": "Breaking to ēo not applied",
        "likely_cause": "Breaking context (before r/l/h + C) not triggering for *e/i",
        "action": "Check breaking rule for front vowels before velars",
    },
    "breaking_missing__expected_eo_got_e": {
        "issue": "Expected ēo but got e/ē",
        "likely_cause": "Breaking rule missing this context or ordered wrong",
        "action": "Check *e before r/l/h in breaking environments",
    },
    "long_vowel_missing": {
        "issue": "Long vowel expected but short produced",
        "likely_cause": "Compensatory lengthening, contraction, or TSV proto issue",
        "action": "Check if proto should have long vowel; check lengthening rules",
    },
    "no_output": {
        "issue": "FST produces no output (grammar rejection)",
        "likely_cause": "Compound separator (-), unusual cluster, or grammar gap",
        "action": "Check if proto contains unsupported sequences; may need grammar extension",
    },
    "palatalization_missing": {
        "issue": "Palatal ġ/ċ expected but velar g/c produced",
        "likely_cause": "Palatalization rule not applying in this context",
        "action": "Check palatalization environments; may be suffix-related",
    },
    # OTHER BUCKETS
    "palatal_marker_variant": {
        "issue": "Orthographic difference: sċ vs sc, ċ vs c",
        "likely_cause": "TSV uses one spelling convention, FST uses another",
        "action": "Normalize TSV to consistent palatal marking convention",
    },
    "gemination_extra": {
        "issue": "FST geminated where target has single consonant",
        "likely_cause": "West Germanic gemination applied incorrectly, or TSV target is unusual",
        "action": "Research actual OE form; may be borrowing or irregular",
    },
    "a_restoration_needed": {
        "issue": "Fronted æ where target has restored a (before back vowel)",
        "likely_cause": "A-restoration rule not applying or incomplete",
        "action": "Check a-restoration scope — may miss some contexts (e.g., nafola)",
    },
    "back_expected_front_out__other": {
        "issue": "FST produced front vowel, target has back vowel",
        "likely_cause": "Dialectal/analogical form, or vowel coloring not modeled",
        "action": "Research if target is regular or a variant; may need u-coloring rule",
    },
    "final_n_missing__expected_en": {
        "issue": "Target ends in -en but FST dropped the n",
        "likely_cause": "TSV target may be oblique form (dat.pl), not nominative",
        "action": "Check TSV proto/target paradigm cell alignment",
    },
    "final_n_missing__expected_an": {
        "issue": "Target ends in -an but FST has bare stem",
        "likely_cause": "TSV paradigm cell mismatch or n-stem morphology",
        "action": "Verify proto form matches expected OE form class",
    },
    "syncopation_missing": {
        "issue": "FST kept medial vowel that target syncopates",
        "likely_cause": "High vowel syncope rule not applying (meoloc→meolc)",
        "action": "Check syncope rule for unstressed high vowels",
    },
    "breaking_extra__eo_for_high": {
        "issue": "FST broke to eo where target has high vowel (ū/ī)",
        "likely_cause": "Breaking applied where it shouldn't; may be TSV proto issue",
        "action": "Check if proto vowel is correct (*eu vs *ū)",
    },
    "breaking_extra__wrong_form": {
        "issue": "Breaking difference plus consonant skeleton mismatch",
        "likely_cause": "TSV proto/target are different lexemes or form classes",
        "action": "Verify TSV alignment; likely needs different proto",
    },
    "vowel_quality__stressed_vowel": {
        "issue": "Root vowel differs (e.g., e vs i, a vs o)",
        "likely_cause": "Dialectal variation, analogical leveling, or proto vowel wrong",
        "action": "Research the specific vowel history; may be TSV issue",
    },
    "vowel_quality__ie_vs_eo": {
        "issue": "FST has ie where target has eo (or vice versa)",
        "likely_cause": "i-umlaut applied where back mutation expected, or vice versa",
        "action": "Check umlaut/mutation chronology; ie < eo (i-umlaut) vs eo (breaking/back mutation)",
    },
    "vowel_quality__ie_vs_ea": {
        "issue": "FST has ie where target has ea (or vice versa)",
        "likely_cause": "Breaking diphthong confusion; ie < i + breaking vs ea < æ + breaking",
        "action": "Check breaking input vowel; may be proto vowel issue",
    },
    "vowel_quality__a_vs_o": {
        "issue": "FST has a where target has o (or vice versa)",
        "likely_cause": "Pre-nasal rounding (*a > o before nasal), or dialectal",
        "action": "Check nasal context; if not pre-nasal, may be dialectal or TSV issue",
    },
    "vowel_quality__i_vs_e": {
        "issue": "FST has i where target has e (or vice versa)",
        "likely_cause": "Raising/lowering; may involve unstressed reduction or breaking input",
        "action": "Check stress and surrounding consonants; e before r,l,h often raises",
    },
    "vowel_quality__u_lowering_exception": {
        "issue": "FST lowered u→o but target keeps u (wulf, bucc, etc.)",
        "likely_cause": "Known lexical exceptions to u-lowering (Luick §78)",
        "action": "Add exception list to u-lowering rule or accept as documented",
    },
    "final_vowel_extra": {
        "issue": "FST has final vowel, target is vowelless",
        "likely_cause": "Apocope not applied, or TSV target is reduced form",
        "action": "Check apocope rules; may be morphology mismatch",
    },
    "final_vowel_missing__weak_noun_like": {
        "issue": "Target ends in -e/-a (weak noun), FST has bare stem",
        "likely_cause": "Proto is strong form, target is weak; or apocope over-applied",
        "action": "Check morphological class alignment in TSV",
    },
    "cons_mismatch__f_vs_b__intervocalic": {
        "issue": "FST has f where target has b (intervocalic)",
        "likely_cause": "Missing or misapplied *b→*β→f vs geminate *bb→bb",
        "action": "Check if this is gemination context (habban has *bb)",
    },
}

# Treat these as vowels in the proto stream when looking for an i/j trigger.
PROTO_VOWELS = set("aeiouyāēīōūǣȳ")
PROTO_TRIGGERS = set("ijī")
PROTO_DIPHTHONGS = ("ai", "au", "eu", "iu")

FRONT_VOWELS = set("æǣeiīyȳ")
BACK_VOWELS = set("aāoōuū")
LONG_VOWELS = set("āēīōūǣȳ")
HIGH_FRONT_VOWELS = set("iīyȳ")
OE_DIPHTHONGS = ("īe", "ie", "ēo", "eo", "ēa", "ea")
PALATAL_MARKERS = ("ċ", "ġ", "sc", "cg")
BREAKING_DIPHTHONGS = ("ēa", "ēo", "īe", "ea", "eo", "ie")
# Characters that are definitely consonants in OE orthography.
OE_CONSONANTS = set("bcdfgġhklmnprstwxþðċ")


def normalize_proto(raw: str) -> str:
    normalized = PROTO_STRIP_RE.sub("", raw or "")
    # Proto inventory uses θ; normalize þ to avoid false no_output buckets.
    return normalized.replace("þ", "θ")


def load_rows(tsv_path: Path) -> List[Dict[str, str]]:
    return load_contextual_rows(tsv_path)


def load_known_problems(ledger_path: Path) -> Dict[str, Dict[str, str]]:
    """Load `oe_known_problems.tsv` as a dict keyed by normalized proto.

    Each entry has the original ledger fields (proto, status, category,
    reason, refs, added). Used by the intervention summary to count
    "Documented exceptions" properly: any mismatch whose proto appears
    in this ledger is documented and won't be counted as open phonology
    work, regardless of its mechanistic sub-bucket.
    """
    out: Dict[str, Dict[str, str]] = {}
    if not ledger_path.exists():
        return out
    with ledger_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            proto = (row.get("proto") or "").strip()
            if not proto:
                continue
            out[normalize_proto(proto)] = {
                "proto": proto,
                "status": (row.get("status") or "").strip(),
                "category": (row.get("category") or "").strip(),
                "reason": (row.get("reason") or "").strip(),
                "refs": (row.get("refs") or "").strip(),
                "added": (row.get("added") or "").strip(),
            }
    return out


def apply_down(bin_path: Path, form: str) -> List[str]:
    proc = subprocess.run(
        ["flookup", "-i", str(bin_path)],
        input=(form + "\n").encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    outputs: List[str] = []
    for raw in proc.stdout.decode("utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        parts = raw.split("\t", 1)
        out = parts[1] if len(parts) == 2 else ""
        if out and out != "+?":
            outputs.append(out)
    # Deduplicate while preserving order.
    seen = set()
    deduped: List[str] = []
    for item in outputs:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


def has_front(s: str) -> bool:
    return any(ch in s for ch in FRONT_VOWELS) or any(d in s for d in ("ie", "īe", "eo", "ēo", "ea", "ēa"))


def has_back(s: str) -> bool:
    return any(ch in s for ch in BACK_VOWELS)


def has_long(s: str) -> bool:
    return any(ch in s for ch in LONG_VOWELS) or any(d in s for d in ("ēa", "ēo", "īe"))


def has_breaking_diph(s: str) -> bool:
    return any(d in s for d in BREAKING_DIPHTHONGS)


def consonant_skeleton(s: str) -> str:
    """Strip vowels/diphthongs to compare consonant material."""
    for diph in BREAKING_DIPHTHONGS:
        s = s.replace(diph, "")
    for ch in LONG_VOWELS | FRONT_VOWELS | BACK_VOWELS:
        s = s.replace(ch, "")
    return s


def has_palatal_marker(s: str) -> bool:
    return any(marker in s for marker in PALATAL_MARKERS)


def has_high_front(s: str) -> bool:
    return any(ch in s for ch in HIGH_FRONT_VOWELS) or any(d in s for d in ("ie", "īe"))


def oe_first_vowel_unit(s: str) -> str:
    for i in range(len(s)):
        for diph in OE_DIPHTHONGS:
            if s.startswith(diph, i):
                return diph
        ch = s[i]
        if ch in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS):
            return ch
    return ""


def oe_first_is_front(s: str) -> bool:
    unit = oe_first_vowel_unit(s)
    return unit in FRONT_VOWELS or unit in {"ie", "īe", "eo", "ēo", "ea", "ēa"}


def oe_first_is_back(s: str) -> bool:
    unit = oe_first_vowel_unit(s)
    return unit in BACK_VOWELS


def oe_first_is_high_front(s: str) -> bool:
    unit = oe_first_vowel_unit(s)
    return unit in HIGH_FRONT_VOWELS or unit in {"ie", "īe"}


def vowel_sequence(s: str) -> List[str]:
    """Return vowel/diphthong units in order for quick mismatch heuristics."""
    seq: List[str] = []
    i = 0
    while i < len(s):
        pair = s[i : i + 2]
        if pair in BREAKING_DIPHTHONGS:
            seq.append(pair)
            i += 2
            continue
        if s[i] in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS):
            seq.append(s[i])
        i += 1
    return seq


def consonant_sequence(s: str) -> str:
    """Strip vowels/diphthongs to compare consonant order (keeps gemination)."""
    for diph in BREAKING_DIPHTHONGS:
        s = s.replace(diph, "")
    return "".join(ch for ch in s if ch not in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS))


def has_palatal_variant_mismatch(out: str, expected: str) -> bool:
    """Detect sc/cg vs ċ/ġ representation mismatches."""
    exp_fine = ("ċ" in expected) or ("ġ" in expected)
    exp_sc = ("sc" in expected) or ("cg" in expected)
    out_fine = ("ċ" in out) or ("ġ" in out)
    out_sc = ("sc" in out) or ("cg" in out)
    return (exp_fine and out_sc and not out_fine) or (exp_sc and out_fine and not out_sc)


def has_consonant_gemination(s: str) -> bool:
    vowels = FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] and s[i] not in vowels:
            return True
    return False


def has_final_devoicing_issue(out: str, expected: str) -> bool:
    """Detect voiced stop in output that should be devoiced in expected.
    
    Handles both word-final (d#→t#) and pre-consonantal (dm→tm) contexts.
    """
    if not out or not expected:
        return False
    out_cons = consonant_sequence(out)
    exp_cons = consonant_sequence(expected)
    if not out_cons or not exp_cons or len(out_cons) != len(exp_cons):
        return False
    # Check for d→t, g→c/k, b→p in final or pre-consonantal position
    # Compare last few consonants
    pairs = [("d", "t"), ("g", "c"), ("g", "k"), ("b", "p")]
    for i in range(min(3, len(out_cons))):  # Check last 3 consonants
        idx = -(i+1)
        for voiced, voiceless in pairs:
            if out_cons[idx] == voiced and exp_cons[idx] == voiceless:
                # Rest of consonants should match
                if out_cons[:idx] == exp_cons[:idx] and (idx == -1 or out_cons[idx+1:] == exp_cons[idx+1:]):
                    return True
    return False


def has_intervocalic_voicing_issue(out: str, expected: str) -> bool:
    """Detect intervocalic b/d/g that should be f/þ/ġ (fricatives)."""
    if not out or not expected:
        return False
    # Check for patterns like VbV→VfV, VdV→VþV (medial stops should be fricatives)
    vowels = FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS
    # Simple heuristic: look for b in out where expected has f/v, same for d/þ, g/ġ
    for i in range(1, len(out) - 1):
        if out[i] in "bdg":
            if (i > 0 and out[i-1] in vowels) and (i < len(out)-1 and out[i+1] in vowels):
                # Intervocalic position
                if out[i] == "b" and ("f" in expected or "v" in expected):
                    return True
                if out[i] == "d" and "þ" in expected:
                    return True
                if out[i] == "g" and "ġ" in expected:
                    return True
    return False


def trigger_in_next_syllable(proto_norm: str) -> bool:
    """Heuristic: an i/ī/j appears before any other vowel after the first vowel."""
    first_vowel_idx = None
    for idx, ch in enumerate(proto_norm):
        if ch in PROTO_VOWELS:
            first_vowel_idx = idx
            break
    if first_vowel_idx is None:
        return False
    for ch in proto_norm[first_vowel_idx + 1 :]:
        if ch in PROTO_TRIGGERS:
            return True
        if ch in PROTO_VOWELS:
            return False
    return False


def proto_first_vowel_unit(proto_norm: str) -> str:
    for i in range(len(proto_norm)):
        for diph in PROTO_DIPHTHONGS:
            if proto_norm.startswith(diph, i):
                return diph
        ch = proto_norm[i]
        if ch in PROTO_VOWELS:
            return ch
    return ""


def is_a_fronting_context(proto_norm: str) -> bool:
    first = proto_first_vowel_unit(proto_norm)
    return first in {"a", "ā"}


def ends_with_vowel(s: str) -> bool:
    if not s:
        return False
    return s[-1] in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS)


def proto_mismatch_suspect(proto_norm: str, out: str, expected: str) -> bool:
    """Heuristic: expected shows high-front raising but proto lacks trigger and starts front."""
    if trigger_in_next_syllable(proto_norm):
        return False
    if not oe_first_is_high_front(expected):
        return False
    if oe_first_is_high_front(out):
        return False
    if not oe_first_is_back(out):
        return False
    first = proto_first_vowel_unit(proto_norm)
    if first in {"e", "ē", "i", "ī", "æ", "ǣ", "y", "ȳ", "eu", "iu"}:
        return True
    return False


def base_bucket(proto_norm: str, out: str, expected: str) -> str:
    if proto_mismatch_suspect(proto_norm, out, expected):
        return "proto_mismatch_suspect"
    if has_breaking_diph(expected) and not has_breaking_diph(out):
        return _breaking_subtype(out, expected)
    if has_long(expected) and not has_long(out):
        expected_cons = consonant_skeleton(expected)
        out_cons = consonant_skeleton(out)
        if expected_cons and expected_cons != out_cons and expected_cons in out_cons:
            return "other"
        return "long_vowel_missing"
    if oe_first_is_front(expected) and oe_first_is_back(out):
        if trigger_in_next_syllable(proto_norm):
            return "i_umlaut_missing_true"
        if is_a_fronting_context(proto_norm):
            # Check if the mismatch also involves a form-class difference
            # (e.g., verb infinitive in proto but noun expected, or vice versa)
            out_cons = consonant_sequence(out)
            exp_cons = consonant_sequence(expected)
            if out_cons != exp_cons:
                return "fronting_missing__also_wrong_form"
            return "fronting_missing__afb"
        return "other"
    if has_palatal_marker(expected) and not has_palatal_marker(out):
        return "palatalization_missing"
    return "other"


def _find_first_cons_mismatch(out: str, expected: str) -> str:
    """Find the first consonant pair that differs between out and expected.

    Returns a string like 'þ_vs_d' or '' if consonants are identical / not alignable.
    """
    out_c = consonant_sequence(out)
    exp_c = consonant_sequence(expected)
    if out_c == exp_c:
        return ""
    for i in range(min(len(out_c), len(exp_c))):
        if out_c[i] != exp_c[i]:
            return f"{out_c[i]}_vs_{exp_c[i]}"
    if len(out_c) != len(exp_c):
        return "length_diff"
    return ""


def _cons_mismatch_position(out: str, expected: str) -> str:
    """Classify the position of the first consonant mismatch."""
    vowels = FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS
    out_c = consonant_sequence(out)
    exp_c = consonant_sequence(expected)
    mismatch_idx = -1
    for i in range(min(len(out_c), len(exp_c))):
        if out_c[i] != exp_c[i]:
            mismatch_idx = i
            break
    if mismatch_idx < 0:
        return ""
    # Find the mismatched consonant in the original string and check context
    mismatched_char = out_c[mismatch_idx]
    cons_count = 0
    for i, ch in enumerate(out):
        if ch in OE_CONSONANTS:
            if cons_count == mismatch_idx:
                # Check context
                before = out[i - 1] if i > 0 else ""
                after = out[i + 1] if i < len(out) - 1 else ""
                if i == len(out) - 1 or (after not in vowels and before not in vowels):
                    return "word_final"
                if before in vowels and after in vowels:
                    return "intervocalic"
                return "cluster"
            cons_count += 1
    return ""


def _breaking_subtype(out: str, expected: str) -> str:
    """Classify breaking mismatch by expected diphthong and produced monophthong."""
    for diph in BREAKING_DIPHTHONGS:
        if diph in expected and diph not in out:
            mono = oe_first_vowel_unit(out) if not has_breaking_diph(out) else ""
            if diph in ("ea", "ēa"):
                if mono in ("a", "ā", "æ", "ǣ"):
                    return "breaking_missing__expected_ea_got_a"
                return "breaking_missing__expected_ea"
            if diph in ("eo", "ēo"):
                if mono in ("e", "ē"):
                    return "breaking_missing__expected_eo_got_e"
                return "breaking_missing__expected_eo"
            if diph in ("ie", "īe"):
                if mono in ("i", "ī"):
                    return "breaking_missing__expected_ie_got_i"
                return "breaking_missing__expected_ie"
    return "breaking_missing"


def _breaking_extra_subtype(out: str, expected: str, proto_norm: str) -> str:
    """Classify cases where output has a breaking diphthong but expected doesn't."""
    out_cons = consonant_sequence(out)
    exp_cons = consonant_sequence(expected)

    # If consonant skeletons differ substantially, this is likely a wrong-form/lexeme
    # issue rather than a genuine extra-breaking phonology problem.
    if out_cons != exp_cons and len(out_cons) != len(exp_cons):
        return "breaking_extra__wrong_form"

    # Identify which diphthong is extra in the output
    for diph in BREAKING_DIPHTHONGS:
        if diph in out and diph not in expected:
            exp_vowel = oe_first_vowel_unit(expected)
            if diph in ("ea", "ēa"):
                if exp_vowel in ("a", "ā", "æ", "ǣ"):
                    return "breaking_extra__ea_for_a"
                return "breaking_extra__ea_other"
            if diph in ("eo", "ēo"):
                if exp_vowel in ("e", "ē"):
                    return "breaking_extra__eo_for_e"
                if exp_vowel in ("i", "ī", "u", "ū"):
                    return "breaking_extra__eo_for_high"
                return "breaking_extra__eo_other"
            if diph in ("ie", "īe"):
                if exp_vowel in ("i", "ī"):
                    return "breaking_extra__ie_for_i"
                if exp_vowel in ("ē",):
                    return "breaking_extra__ie_for_e"
                return "breaking_extra__ie_other"
    return "breaking_extra__other"


def _palatal_extra_subtype(out: str, expected: str, proto_norm: str) -> str:
    """Classify palatal-extra mismatch by the mechanism that caused it."""
    # Check if this is purely an orthographic normalization difference:
    # expected has plain c/g where output has ċ/ġ, but underlying phonology identical.
    out_depal = out.replace("ċ", "c").replace("ġ", "g")
    exp_depal = expected.replace("ċ", "c").replace("ġ", "g")
    if out_depal == exp_depal:
        return "palatal_extra__orth_normalization"

    # Check if palatalization was triggered by a *j in the proto-form
    has_j = "j" in proto_norm
    if has_j:
        # Check if the palatal marker is adjacent to the j-related vowel
        return "palatal_extra__j_triggered"

    # Check if velar was palatalized before a front vowel
    # Pattern: we produced ċ/ġ, expected has c/g — velar before front vowel in our output
    for i, ch in enumerate(out):
        if ch in ("ċ", "ġ") and i < len(out) - 1:
            next_ch = out[i + 1]
            if next_ch in FRONT_VOWELS:
                # Check if expected has the non-palatal version in roughly the same position
                plain = "c" if ch == "ċ" else "g"
                if plain in expected:
                    return "palatal_extra__velar_before_front"
    # Broader check: is there any front vowel adjacent to a palatal in the output?
    for i, ch in enumerate(out):
        if ch in ("ċ", "ġ"):
            before = out[i - 1] if i > 0 else ""
            after = out[i + 1] if i < len(out) - 1 else ""
            if before in FRONT_VOWELS or after in FRONT_VOWELS:
                return "palatal_extra__velar_before_front"

    return "palatal_extra__other"


def _back_front_subtype(out: str, expected: str, proto_norm: str) -> str:
    """Classify back_expected_front_out: output has front vowel, expected has back."""
    # Check if the mismatch is primarily in suffix/tail material
    common_prefix = 0
    for i in range(min(len(out), len(expected))):
        if out[i] == expected[i]:
            common_prefix += 1
        else:
            break
    if common_prefix >= 2 and common_prefix >= len(expected) - 2:
        return "a_restoration_needed__morph_tail"

    # Is this an AFB-like context? Proto *a was fronted but expected has back vowel.
    # This means a-restoration should have undone the fronting, or the TSV target
    # uses an a-restored form that we're not producing.
    if is_a_fronting_context(proto_norm):
        out_cons = consonant_sequence(out)
        exp_cons = consonant_sequence(expected)
        if out_cons != exp_cons:
            return "a_restoration_needed__also_wrong_form"
        return "a_restoration_needed"

    # Non-*a context: expected has back vowel where we produce front
    first_exp = oe_first_vowel_unit(expected)
    first_out = oe_first_vowel_unit(out)
    if first_exp in ("a", "ā") and first_out in ("æ", "ǣ", "e", "ē"):
        return "a_restoration_needed"

    return "back_expected_front_out__other"


# Known u-lowering exception roots (Luick §78, R/T §2.3.1).
# Output has o where expected has u (or vice versa) near labials/velars.
_U_LOWERING_ROOTS = {"wulf", "wolf", "full", "foll", "bucc", "bocc", "fugol", "fogol",
                     "wull", "woll", "rust", "rost", "lufu", "lofu"}


def _vowel_quality_subtype(out: str, expected: str, proto_norm: str) -> str:
    """Split vowel_quality_other into mechanistic sub-buckets."""
    out_vowels = vowel_sequence(out)
    exp_vowels = vowel_sequence(expected)

    # 1. u/o alternation (u-lowering exceptions)
    for i in range(min(len(out_vowels), len(exp_vowels))):
        if (out_vowels[i] == "o" and exp_vowels[i] == "u") or \
           (out_vowels[i] == "u" and exp_vowels[i] == "o"):
            # Check if this is a known u-lowering exception context
            if any(root in out or root in expected for root in _U_LOWERING_ROOTS):
                return "vowel_quality__u_lowering_exception"
            return "vowel_quality__u_o_alternation"

    # 2. æ/e quality (AFB-related or fronting quality)
    for i in range(min(len(out_vowels), len(exp_vowels))):
        if {out_vowels[i], exp_vowels[i]} == {"æ", "e"} or \
           {out_vowels[i], exp_vowels[i]} == {"ǣ", "ē"}:
            return "vowel_quality__ae_e_alternation"

    # 3. Stressed vowel: first vowel differs, rest are the same
    if len(out_vowels) == len(exp_vowels) and len(out_vowels) >= 1:
        if out_vowels[0] != exp_vowels[0] and out_vowels[1:] == exp_vowels[1:]:
            pair = frozenset({out_vowels[0], exp_vowels[0]})
            # ie vs eo: diphthong confusion (i-umlaut vs back mutation)
            if pair == frozenset({"ie", "eo"}) or pair == frozenset({"īe", "ēo"}):
                return "vowel_quality__ie_vs_eo"
            # ie vs ea: breaking variant confusion
            if pair == frozenset({"ie", "ea"}) or pair == frozenset({"īe", "ēa"}):
                return "vowel_quality__ie_vs_ea"
            # a vs o: pre-nasal rounding or other
            if pair == frozenset({"a", "o"}) or pair == frozenset({"ā", "ō"}):
                return "vowel_quality__a_vs_o"
            # i vs e: raising/lowering
            if pair == frozenset({"i", "e"}) or pair == frozenset({"ī", "ē"}):
                return "vowel_quality__i_vs_e"
            return "vowel_quality__stressed_vowel"

    # 4. Unstressed vowel: first vowel matches, later vowel(s) differ
    if len(out_vowels) == len(exp_vowels) and len(out_vowels) >= 2:
        if out_vowels[0] == exp_vowels[0] and out_vowels[1:] != exp_vowels[1:]:
            # Sub-classify by the nature of the unstressed difference
            for i in range(1, len(out_vowels)):
                if out_vowels[i] != exp_vowels[i]:
                    pair = (out_vowels[i], exp_vowels[i])
                    # e→o or o→e in unstressed syllable (common OE reduction)
                    if set(pair) == {"e", "o"}:
                        return "vowel_quality__unstressed_e_o"
                    # o→a or a→o in unstressed syllable
                    if set(pair) == {"o", "a"} or set(pair) == {"ō", "a"}:
                        return "vowel_quality__unstressed_o_a"
                    break
            return "vowel_quality__unstressed_vowel"

    return "vowel_quality__other"


def _final_vowel_missing_subtype(out: str, expected: str, proto_norm: str) -> str:
    """Classify final_vowel_missing by mechanism."""
    out_cons = consonant_sequence(out)
    exp_cons = consonant_sequence(expected)

    # Check for weak-noun-like patterns: output ends in -o/-a/-on/-an
    # but expected ends in -e/-a (weak noun nominative).
    if expected[-1:] in ("e", "a") and out_cons == exp_cons:
        return "final_vowel_missing__weak_noun_like"

    # Apocope candidate: expected has final vowel, output doesn't, and the
    # consonant skeletons match (pure final-vowel difference).
    if exp_cons == out_cons:
        return "final_vowel_missing__apocope_candidate"

    # Proto form suspect: different consonant structures.
    if len(out_cons) != len(exp_cons):
        # Detect verb-infinitive producing an inflected form where expected is a noun:
        # proto ends in -ăną (strong verb inf) or -ōjăną/-ēją (weak verb inf)
        # and expected is a much shorter noun/adjective.
        is_verb_proto = proto_norm.endswith("ană") or proto_norm.endswith("anăn") or \
                        "ōjăną" in proto_norm or "ējăną" in proto_norm or \
                        proto_norm.endswith("ēną") or proto_norm.endswith("ōną")
        if is_verb_proto and len(expected) <= len(out) - 2:
            return "final_vowel_missing__verb_vs_noun"

        # Detect weak-noun oblique (proto ends in -ōn/-ăn) where expected is
        # a different form (nominative or stem).
        is_weak_noun = proto_norm.endswith("ōn") or proto_norm.endswith("ăn") or \
                       proto_norm.endswith("ōną") or proto_norm.endswith("ōn")
        if is_weak_noun and expected[-1:] in ("e", "a"):
            return "final_vowel_missing__weak_noun_form"

        return "final_vowel_missing__morph_form_mismatch"

    return "final_vowel_missing__other"


def _inflectional_suffix_extra_subtype(out: str, expected: str, proto_norm: str = "") -> str:
    """Subdivide inflectional_suffix_extra by the kind of suffix."""
    # Detect verb-infinitive vs noun/adj mismatch: proto has verbal *-ăną
    # (ă=U+0103, n, ą=U+0105) but expected is a bare stem.
    if out.endswith("an") and proto_norm.endswith("\u0103n\u0105"):
        exp_cons = consonant_sequence(expected)
        out_stem = out[:-2]
        if consonant_sequence(out_stem) == exp_cons or exp_cons in consonant_sequence(out_stem):
            return "infl_suffix_extra__verb_vs_noun"

    # Detect noun n-stem suffix: proto ends in ăn (ă=U+0103, n) but NOT verb inf.
    # TSV has n-stem oblique, expected is nominative/bare.
    if out.endswith("an") and proto_norm.endswith("\u0103n") and not proto_norm.endswith("\u0103n\u0105"):
        exp_cons = consonant_sequence(expected)
        out_stem = out[:-2]
        if consonant_sequence(out_stem) == exp_cons or exp_cons in consonant_sequence(out_stem):
            return "infl_suffix_extra__nstem_vs_bare"

    for suffix in ("on", "an", "en", "ian"):
        if out.endswith(suffix):
            exp_cons = consonant_sequence(expected)
            out_stem = out[: -len(suffix)]
            if consonant_sequence(out_stem) == exp_cons or exp_cons in consonant_sequence(out_stem):
                return f"infl_suffix_extra__{suffix}"
    for suffix in ("as", "es", "os"):
        if out.endswith(suffix):
            return f"infl_suffix_extra__{suffix}"
    return "infl_suffix_extra__other"


def _final_n_missing_subtype(out: str, expected: str) -> str:
    """Subdivide final_n_missing by context."""
    # Check if expected ends with -an (infinitive/weak noun)
    if expected.endswith("an"):
        return "final_n_missing__expected_an"
    if expected.endswith("on"):
        return "final_n_missing__expected_on"
    if expected.endswith("en"):
        return "final_n_missing__expected_en"
    # Bare -n
    return "final_n_missing__bare_n"


def other_subtype(out: str, expected: str, proto_norm: str = "") -> str:
    if expected.endswith("n") and not out.endswith("n"):
        return _final_n_missing_subtype(out, expected)
    if ends_with_vowel(expected) and not ends_with_vowel(out):
        return _final_vowel_missing_subtype(out, expected, proto_norm)
    if ends_with_vowel(out) and not ends_with_vowel(expected):
        # Distinguish wrong-lexeme from genuine extra vowel
        out_cons = consonant_sequence(out)
        exp_cons = consonant_sequence(expected)
        if out_cons and exp_cons and out_cons[0] != exp_cons[0]:
            return "final_vowel_extra__wrong_lexeme"
        return "final_vowel_extra"
    if has_breaking_diph(out) and not has_breaking_diph(expected):
        return _breaking_extra_subtype(out, expected, proto_norm)
    if has_palatal_marker(out) and not has_palatal_marker(expected):
        return _palatal_extra_subtype(out, expected, proto_norm)
    if has_palatal_variant_mismatch(out, expected):
        return "palatal_marker_variant"
    if has_long(out) and not has_long(expected):
        return "length_extra_other"
    if oe_first_is_front(expected) and oe_first_is_back(out):
        return "front_expected_back_out"
    if oe_first_is_back(expected) and oe_first_is_front(out):
        return _back_front_subtype(out, expected, proto_norm)
    out_cons = consonant_sequence(out)
    expected_cons = consonant_sequence(expected)
    if out_cons == expected_cons:
        out_vowels = vowel_sequence(out)
        expected_vowels = vowel_sequence(expected)
        if len(expected_vowels) > len(out_vowels):
            return "epenthetic_vowel_missing"
        if len(expected_vowels) == len(out_vowels) and expected_vowels != out_vowels:
            return _vowel_quality_subtype(out, expected, proto_norm)
    if has_consonant_gemination(out) and not has_consonant_gemination(expected):
        return "gemination_extra"
    # Check specific consonant phenomena before falling back to catch-all
    if out_cons != expected_cons:
        exp_cons_only = consonant_sequence(expected)
        # 0. Inflectional suffix present in output but not expected
        if len(out) > len(expected) + 1:
            for suffix in ("an", "en", "on", "um", "as", "es", "os", "ian"):
                if out.endswith(suffix):
                    out_stem = out[: -len(suffix)]
                    if consonant_sequence(out_stem) == exp_cons_only:
                        return _inflectional_suffix_extra_subtype(out, expected, proto_norm)
                    if exp_cons_only and len(out_cons) > len(exp_cons_only):
                        if out_cons.endswith(exp_cons_only[-1:]) and exp_cons_only in out_cons:
                            return _inflectional_suffix_extra_subtype(out, expected, proto_norm)
        # 1. Final devoicing
        if has_final_devoicing_issue(out, expected):
            return "final_devoicing_missing"
        # 2. Intervocalic voicing
        if has_intervocalic_voicing_issue(out, expected):
            return "intervocalic_voicing_missing"
        # 3. Prefix morphology
        if len(expected) >= len(out) + 2:
            if exp_cons_only and out_cons in exp_cons_only[1:]:
                return "prefix_morphology_issue"
        # 4. þ/ð allography (same phoneme, different grapheme)
        out_norm_th = out.replace("ð", "þ")
        exp_norm_th = expected.replace("ð", "þ")
        if out_norm_th == exp_norm_th:
            return "orth__thorn_eth_allography"
        # 5. Consonant-pair sub-buckets
        pair = _find_first_cons_mismatch(out, expected)
        pos = _cons_mismatch_position(out, expected)
        if pair and pos:
            return f"cons_mismatch__{pair}__{pos}"
        if pair:
            return f"cons_mismatch__{pair}"
        return "consonant_mismatch_other"
    # Check for r-metathesis (VrC ↔ rVC)
    if _is_metathesis(out, expected):
        return "r_metathesis"
    # Check for suffix form mismatch (-eian vs -ian, etc.)
    if out.endswith("eian") and expected.endswith("ian"):
        return "suffix_form__eian_vs_ian"
    if out.endswith("eon") and expected.endswith("on") and len(out) == len(expected) + 1:
        return "suffix_form__eon_vs_on"
    # Syncopation: output has extra medial vowel compared to expected
    if len(out) > len(expected) and consonant_sequence(out) == consonant_sequence(expected):
        return "syncopation_missing"
    return "uncategorized"


def _is_metathesis(out: str, expected: str) -> bool:
    """Detect if the difference is likely r-metathesis (VrC ↔ rVC)."""
    # Check for common OE r-metathesis patterns
    out_s = sorted(out)
    exp_s = sorted(expected)
    if out_s != exp_s:
        return False
    # Same characters but different order → likely metathesis
    if "r" in out and "r" in expected:
        return True
    return False


def build_report(
    rows: Iterable[Dict[str, str]], bin_path: Path
) -> Tuple[Dict[str, List[Tuple[str, str, str]]], Dict[str, List[Tuple[str, str, str]]]]:
    buckets: Dict[str, List[Tuple[str, str, str]]] = defaultdict(list)
    other_subs: Dict[str, List[Tuple[str, str, str]]] = defaultdict(list)
    for row in rows:
        outputs = apply_down(bin_path, evaluation_input(row))
        expected = row["counterpart"]
        if not outputs:
            buckets["no_output"].append((row["proto"], "+?", expected))
            continue
        if expected in outputs:
            continue
        out = outputs[0]
        bucket = base_bucket(row["proto_norm"], out, expected)
        buckets[bucket].append((row["proto"], out, expected))
        if bucket == "other":
            other_subs[other_subtype(out, expected, row["proto_norm"])].append((row["proto"], out, expected))
    return buckets, other_subs


def write_report(
    buckets: Dict[str, List[Tuple[str, str, str]]],
    other_subs: Dict[str, List[Tuple[str, str, str]]],
    output_path: Path,
    max_examples: int,
    known_problems: Dict[str, Dict[str, str]] = None,
) -> None:
    if known_problems is None:
        known_problems = {}
    # Core buckets (from base_bucket) — include breaking sub-buckets
    core_keys = [
        "i_umlaut_missing_true",
        "proto_mismatch_suspect",
        "fronting_missing__afb",
        "fronting_missing__also_wrong_form",
        "long_vowel_missing",
        "no_output",
        "palatalization_missing",
    ]
    # Add any breaking_missing sub-bucket keys that actually exist
    breaking_keys = sorted(k for k in buckets if k.startswith("breaking_missing"))
    core_keys = core_keys[:4] + breaking_keys + core_keys[4:]

    # Other-bucket sub-categories — fixed order for stable ones, then dynamic
    fixed_other_keys = [
        "final_vowel_extra",
        "final_vowel_extra__wrong_lexeme",
        "length_extra_other",
        "front_expected_back_out",
        "palatal_marker_variant",
        "orth__thorn_eth_allography",
        "epenthetic_vowel_missing",
        "syncopation_missing",
        "gemination_extra",
        "final_devoicing_missing",
        "intervocalic_voicing_missing",
        "prefix_morphology_issue",
        "r_metathesis",
    ]
    # Collect all dynamic sub-bucket keys not in the fixed list
    dynamic_keys = sorted(k for k in other_subs if k not in fixed_other_keys)
    # Group dynamic keys by prefix for readability
    breaking_extra_keys = [k for k in dynamic_keys if k.startswith("breaking_extra__")]
    palatal_keys = [k for k in dynamic_keys if k.startswith("palatal_extra__")]
    a_restoration_keys = [k for k in dynamic_keys if k.startswith("a_restoration_needed")]
    back_front_keys = [k for k in dynamic_keys if k.startswith("back_expected_front_out__")]
    vowel_quality_keys = [k for k in dynamic_keys if k.startswith("vowel_quality__")]
    final_vowel_keys = [k for k in dynamic_keys if k.startswith("final_vowel_missing__")]
    final_n_keys = [k for k in dynamic_keys if k.startswith("final_n_missing__")]
    infl_suffix_keys = [k for k in dynamic_keys if k.startswith("infl_suffix_extra__")]
    cons_mismatch_keys = [k for k in dynamic_keys if k.startswith("cons_mismatch__")]
    suffix_form_keys = [k for k in dynamic_keys if k.startswith("suffix_form__")]
    other_dynamic = [
        k for k in dynamic_keys
        if not any(k.startswith(p) for p in (
            "breaking_extra__", "palatal_extra__", "a_restoration_needed",
            "back_expected_front_out__",
            "vowel_quality__", "final_vowel_missing__", "final_n_missing__",
            "infl_suffix_extra__", "cons_mismatch__", "suffix_form__",
        ))
        and k not in ("consonant_mismatch_other", "uncategorized")
    ]

    other_order = (
        fixed_other_keys
        + ["--- breaking_extra sub-buckets ---"] + breaking_extra_keys
        + ["--- palatal_extra sub-buckets ---"] + palatal_keys
        + ["--- a_restoration sub-buckets ---"] + a_restoration_keys
        + ["--- back_expected_front_out sub-buckets ---"] + back_front_keys
        + ["--- vowel_quality sub-buckets ---"] + vowel_quality_keys
        + ["--- final_vowel_missing sub-buckets ---"] + final_vowel_keys
        + ["--- final_n_missing sub-buckets ---"] + final_n_keys
        + ["--- inflectional_suffix_extra sub-buckets ---"] + infl_suffix_keys
        + ["--- consonant_mismatch sub-buckets ---"] + cons_mismatch_keys
        + ["--- suffix_form sub-buckets ---"] + suffix_form_keys
        + other_dynamic
        + ["consonant_mismatch_other", "uncategorized"]
    )

    mismatch_total = sum(len(v) for v in buckets.values())
    lines: List[str] = []
    lines.append(f"Total mismatches: {mismatch_total}")
    lines.append("")

    # Categorize buckets by intervention type
    tsv_fixable_keys = {
        "fronting_missing__also_wrong_form", "breaking_extra__wrong_form",
        "infl_suffix_extra__verb_vs_noun", "infl_suffix_extra__nstem_vs_bare",
        "infl_suffix_extra__on",
        "final_vowel_missing__verb_vs_noun", "final_vowel_missing__weak_noun_form",
        "final_vowel_missing__morph_form_mismatch",
        "final_vowel_extra__wrong_lexeme",
        "final_n_missing__expected_an", "final_n_missing__expected_en",
        "final_n_missing__bare_n",
        "a_restoration_needed__also_wrong_form",
        "prefix_morphology_issue",
        "cons_mismatch__length_diff",
        "orth__thorn_eth_allography",
        "palatal_extra__orth_normalization",
    }
    documented_keys = {
        "vowel_quality__u_lowering_exception",
    }
    phonology_keys_core = set(core_keys)
    all_other_keys_with_counts = {k: len(v) for k, v in other_subs.items() if v}

    # Helper: count items in a bucket that are NOT in the known-problems ledger.
    def _open(items: List[Tuple[str, str, str]]) -> int:
        return sum(1 for proto, _, _ in items if normalize_proto(proto) not in known_problems)

    # Ledger-aware documented count: every mismatch whose PROTO is in the
    # known-problems ledger counts as documented, regardless of bucket.
    # Plus the historical bucket-key fallback for clusters explicitly tagged.
    documented_protos_seen = set()
    for items in buckets.values():
        for proto, _, _ in items:
            if normalize_proto(proto) in known_problems:
                documented_protos_seen.add(normalize_proto(proto))
    for items in other_subs.values():
        for proto, _, _ in items:
            if normalize_proto(proto) in known_problems:
                documented_protos_seen.add(normalize_proto(proto))

    tsv_count = sum(_open(other_subs.get(k, [])) for k in tsv_fixable_keys)
    # Documented = every mismatch whose PROTO is in the known-problems ledger,
    # regardless of mechanistic bucket. Plus any items remaining in
    # `documented_keys` buckets whose proto is NOT in the ledger (rare).
    documented_count = len(documented_protos_seen) + sum(
        _open(other_subs.get(k, [])) for k in documented_keys
    )
    phonology_core = sum(
        _open(buckets.get(k, [])) for k in core_keys
    )
    phonology_other = sum(
        _open(other_subs.get(k, []))
        for k in all_other_keys_with_counts
        if k not in tsv_fixable_keys and k not in documented_keys
    )

    lines.append("=== INTERVENTION SUMMARY ===")
    lines.append(f"  TSV/data fixes needed:      {tsv_count}")
    lines.append(f"  Documented exceptions:       {documented_count}")
    lines.append(f"  Phonology (core buckets):    {phonology_core}")
    lines.append(f"  Phonology (other buckets):   {phonology_other}")
    lines.append("")

    # Ledger summary: list every documented-exception mismatch so the user
    # can see at a glance what's known-issue vs open.
    if documented_protos_seen:
        lines.append("=== DOCUMENTED EXCEPTIONS (oe_known_problems.tsv) ===")
        # Collect (proto, out, expected, ledger_status, ledger_category) tuples
        seen: List[Tuple[str, str, str, str, str]] = []
        for items in list(buckets.values()) + list(other_subs.values()):
            for proto, out, expected in items:
                norm = normalize_proto(proto)
                if norm in known_problems:
                    entry = known_problems[norm]
                    seen.append((proto, out, expected, entry["status"], entry["category"]))
        # Deduplicate by proto+out+expected (a single proto might appear once)
        seen_keys = set()
        for proto, out, expected, status, category in seen:
            k = (proto, out, expected)
            if k in seen_keys:
                continue
            seen_keys.add(k)
            lines.append(f"  {proto} -> {out} (expected {expected})  [{status}: {category}]")
        lines.append("")

    # Summary counts
    lines.append("=== CORE BUCKETS ===")
    for key in core_keys:
        count = len(buckets.get(key, []))
        if count > 0:
            lines.append(f"  {key}: {count}")
    lines.append("")
    lines.append("=== OTHER SUB-BUCKETS ===")
    for key in other_order:
        if key.startswith("---"):
            lines.append(key)
            continue
        count = len(other_subs.get(key, []))
        if count > 0:
            lines.append(f"  {key}: {count}")
    lines.append("")

    # Detailed examples
    lines.append("=== DETAILED EXAMPLES ===")
    lines.append("")
    for key in core_keys:
        items = buckets.get(key, [])
        if not items:
            continue
        lines.append(f"{key} ({len(items)}):")
        for proto, out, expected in items[:max_examples]:
            lines.append(f"  {proto} -> {out} (expected {expected})")
        # Add diagnostic note for singleton buckets
        if len(items) <= 2 and key in BUCKET_DIAGNOSTICS:
            diag = BUCKET_DIAGNOSTICS[key]
            lines.append(f"  >> ISSUE: {diag['issue']}")
            lines.append(f"  >> LIKELY: {diag['likely_cause']}")
            lines.append(f"  >> ACTION: {diag['action']}")
        lines.append("")

    for key in other_order:
        if key.startswith("---"):
            continue
        items = other_subs.get(key, [])
        if not items:
            continue
        lines.append(f"{key} ({len(items)}):")
        for proto, out, expected in items[:max_examples]:
            lines.append(f"  {proto} -> {out} (expected {expected})")
        # Add diagnostic note for singleton/small buckets
        if len(items) <= 2 and key in BUCKET_DIAGNOSTICS:
            diag = BUCKET_DIAGNOSTICS[key]
            lines.append(f"  >> ISSUE: {diag['issue']}")
            lines.append(f"  >> LIKELY: {diag['likely_cause']}")
            lines.append(f"  >> ACTION: {diag['action']}")
        lines.append("")

    lines.append("=== A-FRONTING AUDIT ===")
    lines.append("--- fronting_missing__afb ---")
    for proto, out, expected in buckets.get("fronting_missing__afb", []):
        lines.append(f"{proto} -> {out} (expected {expected})")
    lines.append("")
    lines.append("--- fronting_missing__also_wrong_form ---")
    for proto, out, expected in buckets.get("fronting_missing__also_wrong_form", []):
        lines.append(f"{proto} -> {out} (expected {expected})")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    # Default paths: resolved through the shared runtime layout
    # (host: bins in <repo>/backend; container: /usr/app).
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from capr_runtime import layout
    rt = layout()
    germanic_dir = rt.germanic_dir
    parser.add_argument(
        "--tsv",
        default=str(rt.corpus_tsv),
        help="Aligned TSV with Old English rows (default: %(default)s)",
    )
    parser.add_argument(
        "--bin",
        default=str(rt.bin_dir / "old_english.bin"),
        help="Generator FST for apply-down (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default=str(germanic_dir / "docs" / "debug_snapshots" / "oe_mismatch_report.txt"),
        help="Report output path (default: %(default)s)",
    )
    parser.add_argument(
        "--known-problems",
        default=str(germanic_dir / "data" / "oe_known_problems.tsv"),
        help="Known-problems ledger TSV (default: %(default)s)",
    )
    parser.add_argument(
        "--examples",
        type=int,
        default=5,
        help="Max examples per bucket (default: %(default)s)",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = load_rows(tsv_path)
    known_problems = load_known_problems(Path(args.known_problems).expanduser().resolve())
    buckets, other_subs = build_report(rows, bin_path)
    write_report(buckets, other_subs, output_path, args.examples, known_problems=known_problems)
    print(f"Wrote {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
