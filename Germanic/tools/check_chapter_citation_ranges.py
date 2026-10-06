#!/usr/bin/env python3
"""Validate page citations to chapters of edited volumes against their ranges.

CAPR cites one edited volume heavily: the Cambridge History of the English
Language, vol. I (1992), which Richard Hogg edited but did not write. Its
chapters have different authors, so a page citation carries an authorship
claim. For most of the project's life that volume shared a single citation key
with Hogg's own sole-authored Grammar of Old English, and page citations to it
were silently attributed to the wrong scholar: the rhotacism statement on p. 39
is Bammesberger's, the account of deverbal feminines in the 350s is
Kastovsky's, and the traditional ordering of the prehistoric changes on p. 446
is Toon's.

This check makes that class of error impossible to reintroduce quietly. It
tests two things:

  * a numeric page locator on a chapter key must fall inside that chapter's
    declared page range;
  * a page-specific citation to the container key of an edited volume should
    normally name the chapter author instead.

The chapter ranges are NOT typed here. They are read from the `pages` field of
the chapter entries in docs/refs.bib, so the bibliography stays the single
authority and the check cannot drift away from it.

The check is deliberately conservative. Section locators, folio and note
references, and other non-numeric locators are left alone, as is a bare
whole-volume citation, which is a legitimate way to refer to a collection.

Usage:
    python3 Germanic/tools/check_chapter_citation_ranges.py [--all]

By default only active, human-authored material is scanned. Frozen archives
and generated audit inventories record what the citations used to be and are
not rewritten to a precision the original harvest never had; --all reports
them too, for information.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BIB = REPO_ROOT / "docs/refs.bib"

# Container keys for edited volumes: citing a single page of one of these
# means citing some particular contributor's chapter.
CONTAINER_KEYS = {"HoggCHEL1992"}

SCANNED_SUFFIXES = {".md", ".tsv", ".py", ".tex", ".txt", ".json", ".yml", ".yaml"}

# Paths that record history rather than assert it. A citation frozen in an
# audit inventory or a dev-note slice is evidence about an earlier state of
# the project, and correcting it in place would manufacture a precision the
# original never had.
ARCHIVE_MARKERS = (
    "docs/archive/",
    "debug_snapshots/",
    "dev_notes_slices/",
    "citation_locator_",
    "/references/",
    "cascade_baseline/",
    # Generated views. index_verborum_audit quotes surrounding prose clipped to
    # a column width, so a locator can be truncated mid-number there; the
    # authority is the reader source it quotes, which is scanned.
    "index_verborum",
)

CITE = re.compile(
    r"@(?P<key>[A-Za-z][A-Za-z0-9]*)"
    r"\s*[,:]\s*"
    r"(?P<loc>(?:pp?\.\s*)?(?P<first>\d{1,4})(?:\s*(?:--|-|,\s*)\d{1,4})*)"
    r"(?![\d.]*\s*[A-Za-z])"
)


def _field(body: str, name: str) -> str | None:
    found = re.search(r"^\s*%s\s*=\s*\{(.*?)\}\s*,?\s*$" % name,
                      body, re.MULTILINE | re.DOTALL)
    return " ".join(found.group(1).split()) if found else None


def read_bibliography(bib_text: str):
    """Read chapter page ranges and volume membership out of refs.bib.

    A chapter entry is one with a `booktitle` (it sits inside a larger work)
    and a numeric `pages` span; that is exactly the set for which a page
    locator is checkable. Each key is also tagged with the volume it belongs
    to, so a page can only ever be reassigned to a sibling chapter of the
    same book.
    """
    ranges: dict[str, tuple[int, int]] = {}
    volume: dict[str, str] = {}
    for entry in re.finditer(r"@\w+\{([^,]+),(.*?)\n\}", bib_text, re.DOTALL):
        key, body = entry.group(1).strip(), entry.group(2)
        booktitle = _field(body, "booktitle")
        if booktitle is None:
            # A container is identified by its own title matching the
            # booktitle its chapters declare.
            title = _field(body, "title")
            if title:
                volume.setdefault(key, title)
            continue
        volume[key] = booktitle
        pages = re.search(r"^\s*pages\s*=\s*\{(\d+)\s*--\s*(\d+)\}",
                          body, re.MULTILINE)
        if pages:
            ranges[key] = (int(pages.group(1)), int(pages.group(2)))
    return ranges, volume


def chapter_owner(ranges, volume, key: str, page: int) -> str | None:
    """Which sibling chapter of the SAME volume owns this page.

    Scoped to one container: two unrelated works can both have a chapter
    running to p. 60, and suggesting one for the other would be nonsense.
    """
    for other, (lo, hi) in ranges.items():
        if other != key and volume.get(other) == volume.get(key) \
                and lo <= page <= hi:
            return other
    return None


# This check's own regression tests cite impossible pages deliberately, to
# prove the check still catches them. They are fixtures, not claims, and the
# only file excluded on those grounds is the one that tests this module.
SELF_TEST = "Germanic/tests/test_chapter_citation_ranges.py"


def is_archive(path: Path) -> bool:
    text = path.as_posix()
    if text.endswith(SELF_TEST):
        return True
    return any(marker in text for marker in ARCHIVE_MARKERS)


def scan(paths, ranges, volume):
    findings = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for match in CITE.finditer(text):
            key = match.group("key")
            page = int(match.group("first"))
            line = text.count("\n", 0, match.start()) + 1
            where = f"{path.relative_to(REPO_ROOT)}:{line}"
            if key in ranges:
                lo, hi = ranges[key]
                if not lo <= page <= hi:
                    owner = chapter_owner(ranges, volume, key, page)
                    hint = (f"p. {page} lies in {owner}" if owner
                            else f"p. {page} lies outside the volume")
                    findings.append(
                        (where, f"{key} is pp. {lo}--{hi}, but is cited at "
                                f"p. {page}; {hint}"))
            elif key in CONTAINER_KEYS:
                owner = chapter_owner(ranges, volume, key, page)
                hint = (f"use {owner} instead" if owner
                        else "name the contributor whose chapter this is")
                findings.append(
                    (where, f"{key} is an edited volume, so a page citation "
                            f"attributes p. {page} to no author; {hint}"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true",
                        help="also report frozen archives and audit inventories")
    args = parser.parse_args()

    ranges, volume = read_bibliography(BIB.read_text(encoding="utf-8"))
    if not ranges:
        print("no chapter entries with declared page ranges found in refs.bib",
              file=sys.stderr)
        return 2

    candidates = [p for p in REPO_ROOT.rglob("*")
                  if p.is_file() and p.suffix in SCANNED_SUFFIXES
                  and ".git/" not in p.as_posix() and p != BIB]
    active = [p for p in candidates if not is_archive(p)]
    findings = scan(active, ranges, volume)
    archived = (scan([p for p in candidates if is_archive(p)], ranges, volume)
                if args.all else [])

    print(f"chapter keys with declared ranges: {len(ranges)}")
    for key, (lo, hi) in sorted(ranges.items(), key=lambda kv: kv[1]):
        print(f"  {key:<24} pp. {lo}--{hi}")
    print(f"active files scanned: {len(active)}")

    if archived:
        print(f"\nfrozen/archival sites (reported, not failed): {len(archived)}")
        for where, why in archived[:20]:
            print(f"  {where}: {why}")
        if len(archived) > 20:
            print(f"  ... ({len(archived) - 20} more)")

    if findings:
        print(f"\nIMPOSSIBLE CHAPTER/PAGE COMBINATIONS: {len(findings)}")
        for where, why in findings:
            print(f"  {where}: {why}")
        print("\nA page citation to an edited volume is an authorship claim. "
              "Cite the author of the chapter the page falls in.")
        return 1

    print("\nOK: every page citation to a chapter falls inside that chapter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
