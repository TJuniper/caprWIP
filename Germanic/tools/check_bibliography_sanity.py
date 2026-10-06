#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BIB_PATH = REPO_ROOT / "docs/refs.bib"
DEFAULT_INTRO_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_intro_alpha_01.md"
OPTIONAL_RENDERED_PATHS = [
    REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.tex",
    REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_20.tex",
]

FORBIDDEN_GLOBAL_STRINGS = [
    "Sims-Williams, David",
    "Sims-Williams, U.",
    "Historical Phonology: Why Mechanise Sound Change? Uncovering Cognates and Relative Chronology",
    "Forward Application of Sound Changes: Uncover New Cognates, Sharpen Relative Chronology",
    "Etymologisches wörterbuch Der Deutschen Sprache",
    "Historische Grammatik Der Englischen Sprache",
    "Vergleichendes Und Etymologisches wörterbuch Der Germanischen Starken Verben",
    "Morphologische Untersuchungen Auf Dem Gebiete Der Indogermanischen Sprachen",
]

REQUIRED_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("Sims-Williams, Patrick", re.compile(r"Sims-Williams,\s+Patrick")),
    ("Mechanising Historical Phonology", re.compile(r"Mechanising Historical Phonology")),
    ("10.1111/1467-968X.12138", re.compile(r"10\.1111/1467-968X\.12138")),
    (
        "Morphologische Untersuchungen auf dem Gebiete der indogermanischen Sprachen",
        re.compile(r"Morphologische Untersuchungen auf dem Gebiete der indogermanischen Sprachen"),
    ),
    ("Brunner, Karl", re.compile(r"Brunner,\s+Karl")),
    (
        "Altenglische Grammatik nach der angelsächsischen Grammatik von Eduard Sievers",
        re.compile(r"Altenglische Grammatik nach der angels(?:ä|\{\\\"a\})chsischen Grammatik von Eduard Sievers"),
    ),
    ("Hulden, Mans", re.compile(r"Hulden,\s+Mans")),
    (
        "Proceedings of the Demonstrations Session at EACL 2009",
        re.compile(r"Proceedings of the Demonstrations Session at EACL 2009"),
    ),
]


@dataclass(frozen=True)
class BibEntry:
    key: str
    body: str


def parse_entries(bib_text: str) -> list[BibEntry]:
    chunks = [chunk for chunk in re.split(r"(?m)(?=^@)", bib_text) if chunk.strip()]
    entries: list[BibEntry] = []
    for chunk in chunks:
        key_match = re.match(r"@\w+\{([^,]+),", chunk.strip())
        if not key_match:
            continue
        entries.append(BibEntry(key=key_match.group(1).strip(), body=chunk))
    return entries


def require_entry(entries: list[BibEntry], key: str) -> BibEntry:
    for entry in entries:
        if entry.key == key:
            return entry
    raise AssertionError(f"Missing bibliography entry: {key}")


def assert_forbidden_strings(text: str, label: str) -> None:
    for bad in FORBIDDEN_GLOBAL_STRINGS:
        if bad in text:
            raise AssertionError(f"Forbidden bibliography string found in {label}: {bad}")


def assert_required_patterns(text: str, label: str) -> None:
    for description, pattern in REQUIRED_PATTERNS:
        if not pattern.search(text):
            raise AssertionError(f"Required bibliography string missing from {label}: {description}")


def assert_osthoff_entry(entry: BibEntry) -> None:
    if not re.search(r"year\s*=\s*\{1878(?:--|–)1910\}", entry.body):
        raise AssertionError("Osthoff/Brugmann entry must use 1878–1910.")
    if not re.search(r"volumes?\s*=\s*\{6\}", entry.body):
        raise AssertionError("Osthoff/Brugmann entry must list 6 volumes.")
    if "Morphologische Untersuchungen auf dem Gebiete der indogermanischen Sprachen" not in entry.body:
        raise AssertionError("Osthoff/Brugmann title must use corrected capitalization.")


def assert_sims_entries(entries: list[BibEntry]) -> None:
    sims_entries = [entry for entry in entries if "Sims-Williams" in entry.body]
    if not sims_entries:
        raise AssertionError("No Sims-Williams entry found in bibliography.")
    if len(sims_entries) != 1:
        raise AssertionError(f"Expected exactly one Sims-Williams entry; found {len(sims_entries)}.")
    sims_body = sims_entries[0].body
    if "10.1111/1467-968X.12113" in sims_body:
        raise AssertionError("Invalid Sims-Williams DOI 10.1111/1467-968X.12113 found.")
    if "10.1111/1467-968X.12123" in sims_body:
        raise AssertionError("Invalid Sims-Williams DOI 10.1111/1467-968X.12123 found.")
    if "Sims-Williams, Patrick" not in sims_body:
        raise AssertionError("Sims-Williams entry must be attributed to Patrick Sims-Williams.")
    if "Mechanising Historical Phonology" not in sims_body:
        raise AssertionError("Sims-Williams entry must cite Mechanising Historical Phonology.")
    if "10.1111/1467-968X.12138" not in sims_body:
        raise AssertionError("Sims-Williams entry must use DOI 10.1111/1467-968X.12138.")


def assert_intro_citations(intro_text: str) -> None:
    if "@SimsWilliams2018a" in intro_text or "@SimsWilliams2018b" in intro_text:
        raise AssertionError("Intro still cites deprecated SimsWilliams2018a/2018b keys.")
    if "D. Sims-Williams" in intro_text or "U. Sims-Williams" in intro_text:
        raise AssertionError("Intro still contains bogus Sims-Williams initials.")
    if "@SimsWilliams2018" not in intro_text:
        raise AssertionError("Intro must cite @SimsWilliams2018.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bib-path", type=Path, default=DEFAULT_BIB_PATH)
    parser.add_argument("--intro-path", type=Path, default=DEFAULT_INTRO_PATH)
    args = parser.parse_args()

    bib_path = args.bib_path.expanduser().resolve()
    intro_path = args.intro_path.expanduser().resolve()
    if not bib_path.exists():
        raise AssertionError(f"Bibliography file not found: {bib_path}")
    if not intro_path.exists():
        raise AssertionError(f"Intro file not found: {intro_path}")

    bib_text = bib_path.read_text(encoding="utf-8")
    entries = parse_entries(bib_text)
    if not entries:
        raise AssertionError(f"No entries parsed from bibliography: {bib_path}")

    assert_forbidden_strings(bib_text, str(bib_path))
    assert_required_patterns(bib_text, str(bib_path))
    assert_sims_entries(entries)

    osthoff = require_entry(entries, "OsthoffBrugmann1881")
    assert_osthoff_entry(osthoff)

    brunner = require_entry(entries, "SieversBrunner1965")
    if "Brunner, Karl" not in brunner.body:
        raise AssertionError("SieversBrunner1965 entry must list Brunner as author.")
    if not re.search(
        r"Altenglische Grammatik nach der angels(?:ä|\{\\\"a\})chsischen Grammatik von Eduard Sievers",
        brunner.body,
    ):
        raise AssertionError("SieversBrunner1965 entry title is not corrected.")

    hulden = require_entry(entries, "Hulden2009")
    if "Proceedings of the Demonstrations Session at EACL 2009" not in hulden.body:
        raise AssertionError("Hulden2009 entry must use Demonstrations Session at EACL 2009 wording.")

    intro_text = intro_path.read_text(encoding="utf-8")
    assert_intro_citations(intro_text)

    scanned_paths = [str(bib_path), str(intro_path)]
    for rendered_path in OPTIONAL_RENDERED_PATHS:
        if not rendered_path.exists():
            continue
        rendered_text = rendered_path.read_text(encoding="utf-8")
        assert_forbidden_strings(rendered_text, str(rendered_path))
        scanned_paths.append(str(rendered_path))

    print(f"bibliography sanity checks passed ({len(scanned_paths)} files)")


if __name__ == "__main__":
    main()
