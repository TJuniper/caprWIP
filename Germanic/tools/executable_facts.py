#!/usr/bin/env python3
"""Executable facts derived from the ONE executable authority.

AUTHORITY
    Germanic/fsts/germanic.txt

Every mechanically derivable fact about a Foma rule -- its exact definition
text, where it is written, and which line it currently occupies -- is computed
here, from the file that actually defines it. None of it may be copied by hand
into a TSV, because a hand-copied mirror is a second authority that silently
goes stale the moment the rule is edited or a comment line is inserted above
it.

In particular a LINE NUMBER is not data. It is a rendering of the current
state of a file. It is computed on demand for display and is never persisted
in a human-edited source.

Public API
    define_facts()          name -> DefineFact for every define in germanic.txt
    definition_raw(name)     the canonical one-line rendering of a definition
    source_anchor(name)      'define Name (line N)' for display only
    STABLE_ANCHOR_RE         matches an anchor that carries no line number

Usage:
    python3 Germanic/tools/executable_facts.py            # list every define
    python3 Germanic/tools/executable_facts.py NAME ...   # show named defines
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FST = REPO_ROOT / "Germanic/fsts/germanic.txt"
FST_REL = "Germanic/fsts/germanic.txt"

# A '#' that is not part of the .#. word-boundary symbol starts a comment.
_COMMENT_RE = re.compile(r"(?<!\.)#(?!\.)")
_DEFINE_RE = re.compile(r"\bdefine\s+([A-Za-z][A-Za-z0-9_]*)")

# A source anchor with no line number in it: the stable form that may be
# stored. Anything matching _LINE_REF is display-only.
STABLE_ANCHOR_RE = re.compile(r"^define\s+[A-Za-z][A-Za-z0-9_]*$")
LINE_REF_RE = re.compile(r"\(\s*line\s+\d+\s*\)|\blines?\s+\d+", re.I)


@dataclass(frozen=True)
class DefineFact:
    """Everything mechanically knowable about one Foma definition."""

    name: str
    line: int
    body: str

    @property
    def stable_anchor(self) -> str:
        """The anchor that survives inserting lines above the definition."""
        return f"define {self.name}"

    @property
    def display_anchor(self) -> str:
        """Anchor plus the CURRENT line, for reports only. Never persisted."""
        return f"define {self.name} (line {self.line})"

    @property
    def definition_raw(self) -> str:
        """The definition rendered on one line, whitespace collapsed."""
        return f"define {self.name} {' '.join(self.body.split())};"


def _blank_comments(text: str) -> str:
    """Replace comment characters with spaces, preserving every offset.

    Offsets must be preserved so that line numbers and bracket depths computed
    on this copy still refer to the real file. Blanking rather than deleting
    also means a ';' inside a comment cannot terminate a definition -- the
    failure mode that a naive non-greedy 'up to the first semicolon' regex has.
    """
    out = []
    for line in text.split("\n"):
        m = _COMMENT_RE.search(line)
        out.append(line[:m.start()] + " " * (len(line) - m.start()) if m else line)
    return "\n".join(out)


def parse_defines(text: str) -> dict[str, DefineFact]:
    """Map define name -> DefineFact, scanning at bracket depth 0."""
    scan = _blank_comments(text)
    facts: dict[str, DefineFact] = {}
    for m in _DEFINE_RE.finditer(scan):
        name = m.group(1)
        depth = 0
        for i in range(m.end(), len(scan)):
            ch = scan[i]
            if ch in "([":
                depth += 1
            elif ch in ")]":
                depth -= 1
            elif ch == ";" and depth == 0:
                body = scan[m.end():i].strip()
                line = scan.count("\n", 0, m.start()) + 1
                if name in facts:
                    raise ValueError(f"duplicate define {name}")
                facts[name] = DefineFact(name=name, line=line, body=body)
                break
        else:
            raise ValueError(f"unterminated define {name}")
    return facts


def define_facts(fst_path: Path | None = None) -> dict[str, DefineFact]:
    path = fst_path or FST
    return parse_defines(path.read_text(encoding="utf-8"))


def definition_raw(name: str, facts: dict[str, DefineFact] | None = None) -> str:
    facts = facts if facts is not None else define_facts()
    return facts[name].definition_raw


def source_anchor(name: str, facts: dict[str, DefineFact] | None = None) -> str:
    facts = facts if facts is not None else define_facts()
    return facts[name].display_anchor


def main() -> int:
    facts = define_facts()
    names = sys.argv[1:] or sorted(facts)
    missing = [n for n in names if n not in facts]
    for n in missing:
        print(f"no such define: {n}", file=sys.stderr)
    for n in names:
        if n in facts:
            print(f"{facts[n].display_anchor}\n    {facts[n].definition_raw}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
