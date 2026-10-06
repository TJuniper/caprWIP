#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "docs" / "assembly"))
import index_verborum_render as ivr
from index_verborum_emission import make_non_explicit_occurrence_id, write_emission_views

# Import the print normalization function from the lexical volume builder so
# that index form/display fields use the same encoding as assembled prose.
# This ensures U+1E2F (ḯ) → ī + combining acute, matching Pandoc's output.
try:
    from build_full_lexical_volume import normalize_print_text as _normalize_iv_form
except ImportError:
    def _normalize_iv_form(text: str) -> str:  # type: ignore[misc]
        return text.replace("\u1e2f", "\u012b\u0301")
BOOK_DIR = REPO_ROOT / "Germanic/docs/book"
ASSEMBLY_DIR = REPO_ROOT / "Germanic/docs/assembly"
INTRO_PATH = ASSEMBLY_DIR / "capr_book_intro_alpha_01.md"
README_PATH = BOOK_DIR / "index_verborum_README.md"
MANIFEST_PATH = ASSEMBLY_DIR / "manifest_all_by_class.tsv"
COMPACT_PATH = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"
CHRONOLOGY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_20.md"
MODEL_ENTRIES_DIR = REPO_ROOT / "Germanic/docs/lexeme_reports/model_entries"
FORMS_PATH = BOOK_DIR / "index_verborum_forms.tsv"
PRINT_MAIN_PATH = BOOK_DIR / "index_verborum_print_main.tsv"
EXPLICIT_ALLOW_SORTKEY_PATH = BOOK_DIR / "index_verborum_explicit_allow_sortkey.tsv"
PRINT_EXCLUDED_PATH = BOOK_DIR / "index_verborum_print_excluded.tsv"
PREOE_REVIEW_PATH = BOOK_DIR / "index_verborum_preoe_review.tsv"
PRINT_DECISIONS_PATH = BOOK_DIR / "index_verborum_print_decisions.tsv"
READER_FACING_EXAMPLES_PATH = BOOK_DIR / "reader_facing_example_forms.tsv"
PRINT_AUDIT_PATH = BOOK_DIR / "index_verborum_print_audit.md"
PRINT_UNIQUE_PATH = BOOK_DIR / "index_verborum_print_unique.tsv"
PRINT_ANOMALIES_PATH = BOOK_DIR / "index_verborum_print_anomalies.tsv"
OVERRIDES_PATH = BOOK_DIR / "index_verborum_overrides.tsv"
AUDIT_PATH = BOOK_DIR / "index_verborum_audit.md"
TABLE_SUGGESTIONS_PATH = BOOK_DIR / "index_verborum_table_suggestions.tsv"
BROAD_PROSE_SUGGESTIONS_PATH = BOOK_DIR / "index_verborum_broad_prose_suggestions.tsv"
TABLE_DECISIONS_PATH = BOOK_DIR / "index_verborum_table_decisions.tsv"
BROAD_PROSE_DECISIONS_PATH = BOOK_DIR / "index_verborum_broad_prose_decisions.tsv"
UNRESOLVED_BASELINE_PATH = BOOK_DIR / "index_verborum_unresolved_baseline.tsv"
LANGUAGE_REGISTRY_PATH = BOOK_DIR / "index_verborum_languages.tsv"
INDEX_HEADER_PATH = ASSEMBLY_DIR / "book_draft_index_registry.tex"

PRODUCTION_FIELDS = [
    "language",
    "variety",
    "form",
    "display",
    "sort_key",
    "form_role",
    "source_scope",
    "source_ref",
    "occurrence_id",
    "origin",
    "status",
]
OVERRIDE_FIELDS = [
    "action",
    "language",
    "variety",
    "form",
    "display",
    "sort_key",
    "source_scope",
    "source_ref",
    "note",
]
TABLE_SUGGESTION_FIELDS = [
    "source_ref",
    "nearest_heading",
    "row_label",
    "form",
    "display",
    "suggested_language",
    "suggested_role",
    "confidence",
    "reason",
    "context",
]
BROAD_PROSE_SUGGESTION_FIELDS = [
    "source_ref",
    "nearest_heading",
    "form",
    "suggested_language",
    "suggested_role",
    "confidence",
    "reason",
    "context",
]
TABLE_DECISION_FIELDS = [
    "action",
    "source_ref",
    "form",
    "language",
    "variety",
    "form_role",
    "note",
]
BROAD_PROSE_DECISION_FIELDS = [
    "action",
    "source_ref",
    "form",
    "language",
    "variety",
    "form_role",
    "note",
]
PRINT_DECISION_FIELDS = [
    "action",
    "language",
    "variety",
    "form",
    "source_ref",
    "form_role",
    "note",
]
PRINT_EXCLUDED_FIELDS = PRODUCTION_FIELDS + ["exclusion_reason", "decision_action", "decision_note"]
PRINT_UNIQUE_FIELDS = [
    "language",
    "display",
    "sort_key",
    "printed_variety",
    "source_varieties",
    "occurrence_count",
    "roles",
    "source_scopes",
    "sample_sources",
]
PRINT_ANOMALY_FIELDS = [
    "language",
    "variety",
    "form",
    "display",
    "sort_key",
    "form_role",
    "source_scope",
    "source_ref",
    "anomaly_flags",
    "hard_error",
    "note",
]
PREOE_REVIEW_FIELDS = [
    "form",
    "source_ref",
    "source_scope",
    "form_role",
    "reason_for_current_inclusion",
    "proposed_print_status",
    "note",
]
READER_FACING_EXAMPLE_FIELDS = [
    "source_ref",
    "nearest_heading",
    "form",
    "inferred_language",
    "example_role",
    "main_index_overlap",
    "include_in_example_index",
    "reason",
    "context",
]
TABLE_SEMANTIC_SOURCE_SCOPE = "table_semantic_auto"
TABLE_SEMANTIC_ORIGIN = "table_semantic_rule"
TABLE_SEMANTIC_DECISION_SOURCE_SCOPE = "table_semantic_decision"
TABLE_SEMANTIC_DECISION_ORIGIN = "table_semantic_decision"
TABLE_DECISION_ACTIONS = {"accept", "defer", "ignore"}
BROAD_PROSE_DECISION_SOURCE_SCOPE = "broad_prose_decision"
BROAD_PROSE_DECISION_ORIGIN = "broad_prose_curated"
BROAD_PROSE_DECISION_ACTIONS = {"accept", "defer", "ignore"}
PRINT_DECISION_ACTIONS = {"include_main", "exclude_main", "defer_print"}


def load_language_registry() -> tuple[list[dict[str, str]], list[str], dict[str, str], dict[str, str]]:
    with LANGUAGE_REGISTRY_PATH.open(encoding="utf-8") as handle:
        rows = [
            {key: (value or "").strip() for key, value in row.items()}
            for row in csv.DictReader(handle, delimiter="\t")
        ]
    order = [row["code"] for row in rows]
    titles = {row["code"]: row["title"] for row in rows}
    columns = {row["code"]: row["columns"] for row in rows}
    return rows, order, titles, columns


LANGUAGE_REGISTRY, LANGUAGE_ORDER, LANGUAGE_TITLES, LANGUAGE_COLUMNS = load_language_registry()
KNOWN_LANGUAGE_CODES = {row["code"] for row in LANGUAGE_REGISTRY}
LANG_META = ivr.load_language_registry()
VARIETY_REGISTRY = ivr.load_variety_registry()
ALLOWED_FORM_ROLES = {
    "evidence_form",
    "source_protoform",
    "selected_input",
    "target_form",
    "comparison_form",
    "regular_output",
}

# Reconstructed historical stages, ordered oldest -> youngest. A reconstruction
# asterisk marks a form as *reconstructed*, not as Proto-Germanic: the historical
# stage is a separate axis that must be declared explicitly by the canonical
# source (model-entry PROTO_STAGE / PROTOFORM_STAGE, propagated via the manifest).
# `nsgmc` (northern West Germanic / North Sea Germanic) is a genuine domain
# distinct from `pnwgmc` (Proto-Northwest Germanic); do not conflate them.
RECONSTRUCTED_STAGE_CODES = ("pie", "pgmc", "pnwgmc", "pwgmc", "nsgmc", "paf", "preoe")


def require_reconstructed_stage(stage: str, *, form: str, scope: str, source_ref: str) -> str:
    """Fail-closed resolution of a reconstructed form's historical stage.

    Computational convenience must not silently become historical metadata: an
    absent or unrecognised stage is never coerced to ``pgmc``. It raises so the
    gap is fixed at the data layer instead of mislabelling the printed index.
    """
    stage = (stage or "").strip()
    if not stage:
        raise ValueError(
            f"Missing historical stage for reconstructed form {form!r} "
            f"({scope} @ {source_ref}); declare PROTO_STAGE/PROTOFORM_STAGE. "
            "Reconstructed forms are not silently labelled pgmc."
        )
    if stage not in RECONSTRUCTED_STAGE_CODES:
        raise ValueError(
            f"Unknown reconstructed stage {stage!r} for form {form!r} "
            f"({scope} @ {source_ref}); valid stages: {list(RECONSTRUCTED_STAGE_CODES)}"
        )
    return stage

FORM_RE = re.compile(r"[*A-Za-zÀ-ɏḀ-ỿͰ-Ͽἀ-῿þðæǣœȳċġǭǫáéíóúāēīōūḗḯ'().-]+")
MARKUP_FORM_RE = re.compile(r"\\emph\{([^}]+)\}|`([^`]+)`")
RECON_SPAN_RE = re.compile(r"\[([^\]]+)\]\{\.recon(?:[^}]*)?\}")
NESTED_RECON_IV_RE = re.compile(r"\[\[(?P<form>[^\]]+)\]\{\.recon\}(?P<tail>.*?)\]\{(?P<attrs>[^}]*)\}")
EXPLICIT_TAG_RE = re.compile(r"\[(?P<content>[^\]]+)\]\{(?P<attrs>[^}]*)\}")
ATTR_RE = re.compile(r"(?P<key>[A-Za-z_][A-Za-z0-9_-]*)=(?P<value>\"[^\"]*\"|[^\s}]+)")
STAGE_FORM_RE = re.compile(
    r"(?P<label>(?:PGmc|Proto-Germanic|PWGmc|Proto-West Germanic|Proto-West-Germanic|"
    r"NWGmc|Proto-Northwest Germanic|Proto-Northwest-Germanic|EAF|Early Anglo-Frisian|"
    r"OE|Old English|"
    r"West Saxon|WS|Anglo Frisian|Anglian)[^:\n<]{0,80}):\s*(?P<form>\*?[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ'./()-]+)"
)
FAILURE_FORM_TOKEN_RE = (
    r"(?:\[(?:[^\]]+)\]\{(?:\.[^}]+)\}|\\emph\{[^}]+\}|\*[^*\n]+\*|`[^`\n]+`|_[^_\n]+_|"
    r"\*?[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ'./()-]+)"
)
_GLOSS_OPT = r"""(?:\s*[\u2018\u2019'"\u201c\u201d][^\u2019'"\u201d\n]{1,40}[\u2019'"\u201d])?"""
FAILURE_EXAMPLE_RE = re.compile(
    r"(?P<label>PGmc|PWGmc|NWGmc|OE|Old English)\s+"
    r"(?P<input>" + FAILURE_FORM_TOKEN_RE + r")" + _GLOSS_OPT + r"\s+"
    r"yields\s+"
    r"(?P<yield>" + FAILURE_FORM_TOKEN_RE + r")" + _GLOSS_OPT + r"\s+"
    r"(?:rather than expected(?:\s+OE)?|instead of(?:\s+expected(?:\s+OE)?)?)\s+"
    r"(?P<expected>" + FAILURE_FORM_TOKEN_RE + r")"
)
NOISE_LINE_PREFIXES = (
    "#",
    "PROTO:",
    "PROTOFORM:",
    "COUNTERPART:",
    "DERIVATION_CLASS:",
    "### Transducer input and output",
    "|",
    r"\begingroup",
    r"\endgroup",
)
TABLE_AUDIT_HEADING_KEYWORDS = ("comparison", "status")
TABLE_AUDIT_HEADER_KEYWORDS = ("form", "input", "outcome", "comparison", "branch")
TABLE_AUDIT_HEADER_EXCLUDE = ("result", "status", "relevance")
TABLE_STOPWORDS = {
    "attested",
    "expected",
    "regular",
    "output",
    "type",
    "same",
    "broader",
    "computed",
    "documented",
    "selected",
    "inherited",
    "ritual",
    "oe",
    "on",
    "ohg",
    "os",
    "ofri",
    "goth",
    "pgmc",
    "pwgmc",
    "pnwgmc",
    "pre-oe",
}
TABLE_SELECTED_PHRASES = (
    "selected input",
    "selected pre-oe input",
    "selected dative",
    "selected genitive",
    "selected oblique",
    "selected weak noun",
    "selected strong",
    "selected i-stem",
    "selected a-stem",
    "selected oe-facing input",
    "oe-facing input",
    "selected j-present branch",
    "selected derived formation",
    "derived oe-facing formation",
    "modeled input",
    "form followed here",
    "selected transponent",
    "selected weak feminine",
    "selected class-i",
    "selected class-ii",
    "selected class-vi",
    "selected strong verner-grade input",
    "selected pre-syncope input",
    "selected imperative singular",
    "selected present third singular",
    "selected 3sg present",
    "selected derived oe-facing formation",
    "selected weak masculine noun",
    "selected e-grade nominative",
    "selected archaic finite cell",
    "selected oe-oriented transponent",
)
TABLE_OUTPUT_PHRASES = (
    "regular output",
    "trace output",
    "compact-trace output",
    "documented output",
    "computed output",
    "exact match",
)
TABLE_SOURCE_PHRASES = (
    "citation",
    "citation reconstruction",
    "comparative headword",
    "broader family label",
    "lexeme-level headword",
    "lexeme-level infinitive",
    "ordinary lexeme line",
    "source label",
    "comparative label",
    "citation nominative singular",
    "citation infinitive",
    "citation in-stem headword",
    "base noun",
    "generalized comparative label",
    "competing citation reconstruction",
    "earlier etymological headword",
    "later g-bearing comparative label",
    "comparative citation",
    "comparative n-stem line",
    "comparative i-stem line",
    "comparative family label",
    "broader comparative headword",
)
TABLE_COMPARISON_PHRASES = (
    "attested variant",
    "dictionary headword",
    "control form",
    "later analogical",
    "non-selected",
    "competing branch",
    "rejected path",
    "broader paradigm",
    "related formation",
    "variant cluster",
    "same noun family",
    "family background",
    "later oblique tradition",
    "later reduced",
    "related finite form",
    "genuine oe doublet",
    "companion",
    "dialectal",
    "variant line",
    "background variant",
    "broader oe variant cluster",
    "plural control",
)
TABLE_NEGATIVE_PHRASES = (
    "wrong vowel",
    "wrong ending",
    "non-match",
    "does not reach the target",
    "retained too long",
    "negative control",
    "poorer comparison",
    "does not account cleanly",
    "not the selected target",
    "but not the target",
    "not the direct source",
    "excluded by",
    "later hardening stage",
    "intermediate pre-oe stage",
    "same derivation",
    "not the proto-germanic form followed here",
)
TABLE_TARGET_PHRASES = (
    "selected target",
    "attested target",
    "old english target",
    "selected attested cell",
)
PROSE_SELECTED_PHRASES = (
    "selected input",
    "selected form",
    "selected cell",
    "selected branch",
    "selected infinitive",
    "selected nominative",
    "selected dative",
    "selected genitive",
    "selected oblique",
    "selected comparison form",
    "selected input here is",
    "selected input is",
    "selected form isolates",
    "form followed here",
    "relevant comparison form",
)
PROSE_SOURCE_CUES = (
    "kroonen gives",
    "kroonen cites",
    "kroonen treats",
    "kroonen reconstructs",
    "orel cites",
    "orel gives",
    "bright notes",
    "bright lists",
    "bosworth-toller records",
    "clark hall gives",
    "clark hall records",
    "ringe and taylor give",
    "ringe and taylor treat",
    "campbell gives",
    "campbell lists",
    "campbell states",
    "fulk presents",
    "fulk cites",
    "cross-references",
    "dictionary headword",
    "citation form",
    "headword tradition",
)
PROSE_COMPARISON_CUES = (
    "comparison form",
    "competing",
    "doublet",
    "variant",
    "plural",
    "preterite",
    "oblique",
    "genitive",
    "dative",
    "cross-references",
    "headword",
    "dictionary",
    "reflexes",
    "attested",
    "records",
    "notes",
    "gives",
    "lists",
    "cites",
)
PROSE_NORMALIZATION_CUES = (
    "normalized",
    "spelling used here",
    "source spelling",
    "source spellings",
    "written here as",
    "capitalized",
)
DEVELOPMENT_CHAIN_CUES = (
    "gives",
    "yields",
    "produces",
    "producing",
    "then",
    "stage",
    "whence",
    "via",
    "surfaces as",
    "leaves",
    "yielding",
    "later",
)
PROSE_GLOSS_FORMS = {
    "among",
    "cell",
    "line",
    "material",
    "noun",
    "ofris",
    "paradigm-cell",
    "regular",
    "row",
    "sea",
    "shoulder",
    "side",
    "spellings",
    "tail",
    "target",
    "umlaut",
    "weak",
    "weak-tail",
}
TABLE_METADATA_LABELS = {
    "oe",
    "on",
    "ohg",
    "os",
    "ofri",
    "goth",
    "pgmc",
    "pwgmc",
    "pnwgmc",
    "pre-oe",
}
BARE_TABLE_CELL_RE = re.compile(r"^\s*\*?[A-Za-zÀ-ɏḀ-ỿͰ-Ͽἀ-῿þðæǣœȳċġǭǫáéíóúāēīōūḗḯ.-]+\s*(?:/\s*\*?[A-Za-zÀ-ɏḀ-ỿͰ-Ͽἀ-῿þðæǣœȳċġǭǫáéíóúāēīōūḗḯ.-]+\s*)*$")
TRANSLIT_MAP = {
    "þ": "th",
    "ð": "d",
    "æ": "ae",
    "ǣ": "ae",
    "œ": "oe",
    "ċ": "c",
    "ġ": "g",
    "ȳ": "y",
    "ǭ": "o",
    "ǫ": "o",
    "ā": "a",
    "ē": "e",
    "ī": "i",
    "ō": "o",
    "ū": "u",
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    "ḗ": "e",
    "ḯ": "i",
    "ṛ": "r",
    "ṝ": "r",
    "ḷ": "l",
    "ḹ": "l",
    "ṃ": "m",
    "ṁ": "m",
    "ḥ": "h",
    "ś": "s",
    "ṣ": "s",
    "ñ": "n",
    "ṇ": "n",
    "ṭ": "t",
    "ḍ": "d",
    "α": "a",
    "β": "b",
    "γ": "g",
    "δ": "d",
    "ε": "e",
    "ζ": "z",
    "η": "e",
    "θ": "th",
    "ι": "i",
    "κ": "k",
    "λ": "l",
    "μ": "m",
    "ν": "n",
    "ξ": "x",
    "ο": "o",
    "π": "p",
    "ρ": "r",
    "σ": "s",
    "ς": "s",
    "τ": "t",
    "υ": "u",
    "φ": "ph",
    "χ": "ch",
    "ψ": "ps",
    "ω": "o",
}


def write_index_registry_header(production_rows: list[ProductionOccurrence]) -> None:
    """Write the book_draft_index_registry.tex with a single unified index declaration.

    All languages are indexed under the single 'iv' index stream using two-level
    MakeIndex entries (language-group@title!form-sort@form-display). This produces
    one continuous three-column index where language names are group headings within
    the flow rather than independently balanced per-language column sets.
    """
    lines = [
        r"\providecommand{\ivlangheader}[2]{\textbf{#1}\if\relax\detokenize{#2}\relax\else\ \textit{(#2)}\fi}",
        r"\providecommand{\iventry}[2]{\emph{#1}\if\relax\detokenize{#2}\relax\else\nobreakspace\textnormal{(#2)}\fi}",
        r"\makeindex[name=iv,title={},columns=3]",
    ]
    INDEX_HEADER_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


README_LANG_BEGIN = "<!-- BEGIN AUTO-LANGUAGE-LIST -->"
README_LANG_END = "<!-- END AUTO-LANGUAGE-LIST -->"


def rewrite_readme_language_block() -> None:
    if not README_PATH.exists():
        return
    text = README_PATH.read_text(encoding="utf-8")
    if README_LANG_BEGIN not in text or README_LANG_END not in text:
        return
    body_lines = []
    for row in LANGUAGE_REGISTRY:
        if row.get("active") != "1":
            continue
        body_lines.append(f"- `{row['code']}` — {row['title']}")
    replacement = README_LANG_BEGIN + "\n" + "\n".join(body_lines) + "\n" + README_LANG_END
    text = re.sub(
        re.escape(README_LANG_BEGIN) + r".*?" + re.escape(README_LANG_END),
        replacement,
        text,
        flags=re.S,
    )
    README_PATH.write_text(text, encoding="utf-8")


@dataclass
class ProductionOccurrence:
    language: str
    form: str
    display: str
    sort_key: str
    form_role: str
    source_scope: str
    source_ref: str
    origins: set[str] = field(default_factory=set)
    status: str = "auto"
    variety: str = ""
    # Deterministic source-locator occurrence identity.
    # explicit_tag rows use canonical source_ref:ordinal IDs.
    # non-explicit rows use scope-aware deterministic IDs.
    occurrence_id: str = ""

    @property
    def key(self) -> tuple[str, str, str, str, str, str, str]:
        identity = self.occurrence_id
        return (self.language, self.variety, self.form, self.display, self.form_role, self.source_scope, identity)


@dataclass(frozen=True)
class CandidateOccurrence:
    form: str
    source_ref: str
    source_path: str
    line_no: int
    heading: str
    line_text: str
    candidate_origin: str = "broad_prose_candidate"


@dataclass(frozen=True)
class TableFormMention:
    form: str
    source_ref: str
    source_path: str
    line_no: int
    heading: str
    line_text: str
    row_label: str
    row_text: str
    cell_header: str
    cell_kind: str
    cell_text: str
    candidate_origin: str = "table_candidate"


def transliterate_sort_key(text: str) -> str:
    text = text.lstrip("*").casefold()
    normalized = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    replaced = "".join(TRANSLIT_MAP.get(ch, ch) for ch in stripped)
    return re.sub(r"[^a-z0-9]+", "", replaced)


def run_sort_key_assertions() -> None:
    assert transliterate_sort_key("þanc") == "thanc", transliterate_sort_key("þanc")
    assert transliterate_sort_key("bæþ") == "baeth", transliterate_sort_key("bæþ")
    assert transliterate_sort_key("bǣr") == "baer", transliterate_sort_key("bǣr")
    assert transliterate_sort_key("ġiefan") == "giefan", transliterate_sort_key("ġiefan")
    assert transliterate_sort_key("sċuldrum") == "sculdrum", transliterate_sort_key("sċuldrum")


def strip_markup(text: str) -> str:
    value = text.strip()
    for prefix, suffix in ((r"\emph{", "}"), ("`", "`"), ("*", "*"), ("_", "_")):
        if value.startswith(prefix) and value.endswith(suffix):
            value = value[len(prefix) : len(value) - len(suffix)]
            break
    # Do not strip () — parentheses are part of forms like cū(e).
    return value.strip("`.,;:!?[]{}""\"' ")


def normalize_semantic_text(text: str) -> str:
    text = NESTED_RECON_IV_RE.sub(lambda match: f"{strip_markup(match.group('form'))} {strip_markup(match.group('tail'))}".strip(), text)
    text = EXPLICIT_TAG_RE.sub(lambda match: strip_markup(match.group("content")), text)
    text = MARKUP_FORM_RE.sub(lambda match: strip_markup(next(group for group in match.groups() if group)), text)
    text = re.sub(r"\s+", " ", text)
    return text.casefold().strip()


def oe_target_display(counterpart: str, derivation_class: str) -> str:
    return f"*{counterpart}" if derivation_class == "reconstructed_oe" else counterpart


def heading_ref(lexical_item: str, counterpart: str, derivation_class: str = "") -> str:
    return f"{lexical_item} — OE {oe_target_display(counterpart, derivation_class)}"


def looks_formlike(text: str) -> bool:
    if not text:
        return False
    if "/" in text and not text.startswith("*"):
        return False
    if ".md" in text or ".pdf" in text or ".tsv" in text or "\\" in text or "<" in text or ">" in text:
        return False
    if sum(1 for ch in text.lstrip("*") if unicodedata.category(ch).startswith("L")) < 2:
        return False
    return True


def normalize_form(text: str) -> str:
    cleaned = strip_markup(text)
    return cleaned if looks_formlike(cleaned) else ""


def normalize_decision_form(text: str) -> str:
    value = text.strip()
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    return value.strip("`.,;:!?()[]{}“”\"' ")


def relative_source_path(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def stage_to_language(label: str, form: str) -> str:
    compact = label.strip()
    if compact.startswith(("PGmc", "Proto-Germanic")):
        return "pgmc"
    if compact.startswith(("PWGmc", "Proto-West Germanic", "Proto-West-Germanic")):
        return "pwgmc"
    if compact.startswith(("PNWGmc", "NWGmc", "Proto-Northwest Germanic", "Proto-Northwest-Germanic")):
        return "pnwgmc"
    if compact.startswith(("EAF", "Early Anglo-Frisian")):
        return "preoe"
    if compact.startswith(("Old Norse", "ON")):
        return "on"
    if compact.startswith(("Old Saxon", "OS")):
        return "os"
    if compact.startswith(("Old High German", "OHG")):
        return "ohg"
    if compact.startswith(("Old Frisian", "OFri")):
        return "ofris"
    if compact.startswith(("Gothic", "Goth")):
        return "goth"
    if compact.startswith(("Old Dutch",)):
        return "odutch"
    if compact.startswith(("Middle Dutch",)):
        return "mdutch"
    if compact.startswith(("Dutch",)):
        return "dutch"
    if compact.startswith(("German",)):
        return "german"
    if compact.startswith(("Latin", "Lat.")):
        return "lat"
    if compact.startswith(("Greek", "Gk.")):
        return "greek"
    if compact.startswith(("Sanskrit", "Skt.")):
        return "skt"
    if compact.startswith(("Middle English",)):
        return "me"
    if compact.startswith(("Modern English",)):
        return "modeng"
    if compact.startswith(("Old Irish",)):
        return "oirish"
    return "preoe" if form.startswith("*") else "oe"


# The compact derivation report labels the selected input with the name of the
# Foma input-filter network, which has been renamed over time (ProtoInput ->
# EnglishProtoInput). Matching only one spelling silently drops every selected
# input from the index, so accept both and fail closed if neither is found.
PROTO_INPUT_RE = re.compile(r"^(?:English )?Proto Input:\s*(.+)$", re.M)


def add_production(
    store: dict[tuple[str, str, str, str, str, str, str], ProductionOccurrence],
    *,
    language: str,
    form: str,
    form_role: str,
    source_scope: str,
    source_ref: str,
    origin: str,
    display: str | None = None,
    sort_key: str | None = None,
    status: str = "auto",
    variety: str = "",
    occurrence_id: str = "",
) -> None:
    cleaned = normalize_form(form)
    if not cleaned or not language:
        return
    if language not in KNOWN_LANGUAGE_CODES:
        raise ValueError(f"Unknown index verborum language code: {language}")
    if form_role not in ALLOWED_FORM_ROLES:
        raise ValueError(f"Unknown index verborum form role: {form_role}")
    variety = (variety or "").strip()
    VARIETY_REGISTRY.validate_occurrence(language, variety)
    visible = display or cleaned
    if source_scope == "explicit_tag" and not occurrence_id:
        occurrence_id = f"{source_ref}:1"
    if source_scope != "explicit_tag" and not occurrence_id:
        occurrence_id = make_non_explicit_occurrence_id(
            {
                "source_scope": source_scope,
                "source_ref": source_ref,
                "language": language,
                "variety": variety,
                "form": cleaned,
                "display": visible,
                "form_role": form_role,
                "sort_key": sort_key or transliterate_sort_key(visible),
            }
        )
    identity = occurrence_id
    key = (language, variety, cleaned, visible, form_role, source_scope, identity)
    if key not in store:
        new_occ = ProductionOccurrence(
            language=language,
            form=cleaned,
            display=visible,
            sort_key=sort_key or transliterate_sort_key(visible),
            form_role=form_role,
            source_scope=source_scope,
            source_ref=source_ref,
            status=status,
            variety=variety,
            occurrence_id=occurrence_id,
        )
        store[key] = new_occ
    store[key].origins.add(origin)
    if status == "override":
        store[key].status = "override"


def parse_manifest_rows() -> list[dict[str, str]]:
    with MANIFEST_PATH.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def parse_compact_entries() -> list[dict[str, object]]:
    text = COMPACT_PATH.read_text(encoding="utf-8")
    chunks: list[list[str]] = []
    current: list[str] = []
    for line in text.splitlines():
        if line.startswith("# "):
            if current:
                chunks.append(current)
            current = [line]
        elif current:
            current.append(line)
    if current:
        chunks.append(current)

    entries: list[dict[str, object]] = []
    for chunk in chunks:
        block = "\n".join(chunk)
        title = chunk[0][2:].strip()
        proto_match = re.search(r"^PROTO:\s*(.+)$", block, re.M)
        expected_match = re.search(r"^EXPECTED:\s*(.+)$", block, re.M)
        outputs_match = re.search(r"^OUTPUTS:\s*(.+)$", block, re.M)
        proto_input_match = PROTO_INPUT_RE.search(block)
        table_lines: list[str] = []
        in_table = False
        for line in chunk:
            if line.startswith("| Earlier Germanic developments | Old English developments |"):
                in_table = True
            if in_table and line.startswith("|"):
                table_lines.append(line)
                continue
            if in_table and not line.startswith("|"):
                break
        stages: list[tuple[str, str]] = []
        table_text = "\n".join(table_lines).replace("<br>", "\n")
        for stage_match in STAGE_FORM_RE.finditer(table_text):
            label = stage_match.group("label").strip()
            if ";" in label:
                continue
            form = normalize_form(stage_match.group("form"))
            if not form:
                continue
            stages.append((label, form))
        entries.append(
            {
                "title": title,
                "proto": proto_match.group(1).strip() if proto_match else "",
                "expected": expected_match.group(1).strip() if expected_match else "",
                "outputs": [item.strip() for item in outputs_match.group(1).split(",")] if outputs_match else [],
                "proto_input": proto_input_match.group(1).strip() if proto_input_match else "",
                "stages": stages,
            }
        )
    if entries and not any(entry["proto_input"] for entry in entries):
        raise ValueError(
            "compact derivation report yielded no selected inputs; the "
            "'Proto Input:' label has probably changed again (see PROTO_INPUT_RE)"
        )
    return entries


def parse_attr_string(raw: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for match in ATTR_RE.finditer(raw):
        value = match.group("value").strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        attrs[match.group("key")] = value
    return attrs


def has_tag_class(raw_attrs: str, cls: str) -> bool:
    return re.search(rf"(^|\s)\.{re.escape(cls)}(?=\s|$)", raw_attrs) is not None


def strip_explicit_markup(text: str) -> str:
    text = NESTED_RECON_IV_RE.sub("", text)
    return EXPLICIT_TAG_RE.sub("", text)


def iter_explicit_tags(path: Path) -> list[dict[str, str]]:
    tags: list[dict[str, str]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        nested_spans = [(m.start(), m.end()) for m in NESTED_RECON_IV_RE.finditer(line)]
        for match in NESTED_RECON_IV_RE.finditer(line):
            attrs = parse_attr_string(match.group("attrs"))
            tags.append(
                {
                    "content": match.group("form"),
                    "line_no": str(line_no),
                    "lang": attrs.get("lang", "").strip(),
                    "sort": attrs.get("sort", "").strip(),
                    "display": attrs.get("display", "").strip() or f"*{strip_markup(match.group('form'))}",
                    "role": attrs.get("role", "").strip(),
                    "variety": attrs.get("variety", "").strip(),
                }
            )
        scrubbed = list(line)
        for start, end in nested_spans:
            for idx in range(start, end):
                scrubbed[idx] = " "
        scrubbed_line = "".join(scrubbed)
        for match in EXPLICIT_TAG_RE.finditer(scrubbed_line):
            raw_attrs = match.group("attrs")
            if not (has_tag_class(raw_attrs, "iv") or has_tag_class(raw_attrs, "pred")):
                continue
            attrs = parse_attr_string(raw_attrs)
            explicit_display = attrs.get("display", "").strip()
            # A combined .recon .iv span carries reconstruction semantics; derive
            # the starred display automatically when no explicit display= is provided.
            if has_tag_class(raw_attrs, "recon") and not explicit_display:
                explicit_display = f"*{strip_markup(match.group('content'))}"
            tags.append(
                {
                    "content": match.group("content"),
                    "line_no": str(line_no),
                    "lang": attrs.get("lang", "").strip(),
                    "sort": attrs.get("sort", "").strip(),
                    "display": explicit_display,
                    "role": attrs.get("role", "").strip(),
                    "variety": attrs.get("variety", "").strip(),
                }
            )
    return tags


def source_files_for_tags() -> list[Path]:
    return [INTRO_PATH, CHRONOLOGY_PATH, *sorted(MODEL_ENTRIES_DIR.glob("*.model.md"))]


def source_files_for_audit() -> list[Path]:
    return [INTRO_PATH, CHRONOLOGY_PATH, *sorted(MODEL_ENTRIES_DIR.glob("*.model.md"))]


def explicit_tag_occurrences(paths: list[Path] | None = None) -> list[dict[str, str]]:
    occurrences: list[dict[str, str]] = []
    for path in paths or source_files_for_tags():
        rel = relative_source_path(path)
        # Track ordinals: count ALL occurrences at each source_ref.
        # This gives globally unique occurrence_ids for same-line spans.
        from collections import Counter as _Counter
        ref_counter: "_Counter[str]" = _Counter()
        for tag in iter_explicit_tags(path):
            source_ref = f"{rel}:{tag['line_no']}"
            ref_counter[source_ref] += 1
            ordinal = ref_counter[source_ref]
            occurrence_id = f"{source_ref}:{ordinal}"
            occurrences.append(
                {
                    "language": tag["lang"],
                    "form": strip_markup(tag["content"]),
                    "display": tag["display"] or strip_markup(tag["content"]),
                    "sort_key": tag["sort"] or transliterate_sort_key(strip_markup(tag["content"])),
                    "form_role": tag["role"] or "evidence_form",
                    "source_scope": "explicit_tag",
                    "source_ref": source_ref,
                    "occurrence_id": occurrence_id,
                    "origin": rel,
                    "variety": tag.get("variety", ""),
                }
            )
    return occurrences


def normalize_failure_form(text: str) -> str:
    token = text.strip()
    # Handle .recon spans (reconstructed lexical forms): strip to bare form with * prefix.
    m_recon = RECON_SPAN_RE.match(token)
    if m_recon:
        token = "*" + m_recon.group(1)
    # If the token is an explicit tagged span like [*bearda*]{.pred} or {.iv},
    # extract the inner content first.
    m = EXPLICIT_TAG_RE.match(token)
    if m:
        token = m.group('content').strip()
    # Markdown italic wrappers like *bearda* represent reconstructed forms in
    # reader-facing failure prose; keep the leading reconstruction marker.
    if token.startswith("*") and token.endswith("*") and len(token) > 2:
        token = "*" + token[1:-1]
    cleaned = strip_markup(token)
    return cleaned if looks_formlike(cleaned) else ""


def iter_failure_example_matches(line: str) -> list[dict[str, str]]:
    matches: list[dict[str, str]] = []
    for match in FAILURE_EXAMPLE_RE.finditer(line):
        input_form = normalize_failure_form(match.group("input"))
        yielded = normalize_failure_form(match.group("yield"))
        expected = normalize_failure_form(match.group("expected"))
        if not (input_form and yielded and expected):
            continue
        matches.append(
            {
                "label": match.group("label"),
                "input": input_form,
                "yield": yielded,
                "expected": expected,
            }
        )
    return matches


def reader_facing_failure_occurrences() -> list[dict[str, str]]:
    occurrences: list[dict[str, str]] = []
    rel = CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix()
    for line_no, line in enumerate(CHRONOLOGY_PATH.read_text(encoding="utf-8").splitlines(), start=1):
        for match in iter_failure_example_matches(line):
            input_form = match["input"]
            yielded = match["yield"]
            expected = match["expected"]
            occurrences.append(
                {
                    "language": stage_to_language(match["label"], input_form),
                    "form": input_form,
                    "display": input_form,
                    "sort_key": transliterate_sort_key(input_form),
                    "form_role": "selected_input",
                    "source_scope": "reader_failure_input",
                    "source_ref": f"{rel}:{line_no}",
                    "origin": rel,
                }
            )
            for form, scope in ((yielded, "reader_failure_output"), (expected, "reader_failure_expected")):
                occurrences.append(
                    {
                        "language": "preoe" if form.startswith("*") else "oe",
                        "form": form,
                        "display": form,
                        "sort_key": transliterate_sort_key(form),
                        "form_role": "regular_output" if scope == "reader_failure_output" else "comparison_form",
                        "source_scope": scope,
                        "source_ref": f"{rel}:{line_no}",
                        "origin": rel,
                    }
                )
    return occurrences


def split_markdown_table_row(line: str) -> list[str]:
    raw = line.strip()
    if raw.startswith("|"):
        raw = raw[1:]
    if raw.endswith("|"):
        raw = raw[:-1]
    return [cell.strip() for cell in raw.split("|")]


def is_markdown_table_delimiter(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def heading_supports_table_audit(heading: str) -> bool:
    lowered = heading.casefold()
    return any(keyword in lowered for keyword in TABLE_AUDIT_HEADING_KEYWORDS)


def header_supports_table_audit(header: str) -> bool:
    lowered = re.sub(r"\s+", " ", header.casefold())
    if any(keyword in lowered for keyword in TABLE_AUDIT_HEADER_EXCLUDE):
        return False
    if lowered in {"item", "value"}:
        return False
    return any(keyword in lowered for keyword in TABLE_AUDIT_HEADER_KEYWORDS)


def table_header_kind(header: str) -> str:
    lowered = normalize_semantic_text(header)
    if "candidate input" in lowered or "input or form" in lowered:
        return "input"
    if "oe comparison form" in lowered:
        return "comparison"
    if "outcome" in lowered or "oe output" in lowered or "oe relation" in lowered:
        return "output"
    if any(token in lowered for token in ("form", "branch", "label", "notation", "stage")):
        return "form"
    return ""


def notation_or_metadata_reason(form: str) -> str:
    lowered = form.casefold()
    if lowered in TABLE_METADATA_LABELS:
        return "table metadata label"
    if (
        "~" in form
        or "..." in form
        or form.endswith("-")
        or form.startswith("-")
        or "*-" in form
        or "-*" in form
        or " " in form
        or "(" in form
        or ")" in form
    ):
        return "notation or compound expression"
    return ""


def extract_forms_from_markup(text: str) -> list[str]:
    forms: list[str] = []
    seen: set[str] = set()
    nested_text = text
    for match in NESTED_RECON_IV_RE.finditer(text):
        form = normalize_form(match.group("form"))
        if form and form not in seen:
            forms.append(form)
            seen.add(form)
    nested_text = NESTED_RECON_IV_RE.sub("", nested_text)
    for match in EXPLICIT_TAG_RE.finditer(nested_text):
        form = normalize_form(match.group("content"))
        if form and form not in seen:
            forms.append(form)
            seen.add(form)
    scrubbed = EXPLICIT_TAG_RE.sub(" ", nested_text)
    for match in MARKUP_FORM_RE.finditer(scrubbed):
        raw = next(group for group in match.groups() if group)
        form = normalize_form(raw.replace("<br>", " "))
        if form and form.casefold() not in TABLE_STOPWORDS and form not in seen:
            forms.append(form)
            seen.add(form)
    bare = scrubbed.strip()
    if BARE_TABLE_CELL_RE.fullmatch(bare):
        for chunk in re.split(r"\s*/\s*", bare):
            form = normalize_form(chunk.strip())
            if form and form.casefold() not in TABLE_STOPWORDS and form not in seen:
                forms.append(form)
                seen.add(form)
    return forms


def table_form_mentions_from_path(path: Path, *, allow_non_model_entry: bool = False) -> list[TableFormMention]:
    if not allow_non_model_entry and path.parent != MODEL_ENTRIES_DIR:
        return []
    rel = relative_source_path(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    mentions: list[TableFormMention] = []
    current_heading = ""
    idx = 0
    while idx < len(lines):
        stripped = lines[idx].strip()
        if stripped.startswith("#"):
            current_heading = stripped
        if (
            not heading_supports_table_audit(current_heading)
            or not stripped.startswith("|")
            or idx + 1 >= len(lines)
        ):
            idx += 1
            continue
        header_cells = split_markdown_table_row(lines[idx])
        delimiter_cells = split_markdown_table_row(lines[idx + 1].strip())
        if len(header_cells) != len(delimiter_cells) or not is_markdown_table_delimiter(delimiter_cells):
            idx += 1
            continue
        header_kinds = [table_header_kind(header) for header in header_cells]
        idx += 2
        while idx < len(lines) and lines[idx].strip().startswith("|"):
            row_line = lines[idx].strip()
            row_cells = split_markdown_table_row(lines[idx])
            row_label = row_cells[0].strip() if row_cells else ""
            row_text = " | ".join(row_cells)
            for col_idx, cell_text in enumerate(row_cells):
                if col_idx >= len(header_kinds):
                    continue
                cell_kind = header_kinds[col_idx]
                if not cell_kind:
                    continue
                cell_header = header_cells[col_idx]
                for form in extract_forms_from_markup(cell_text):
                    mentions.append(
                        TableFormMention(
                            form=form,
                            source_ref=f"{rel}:{idx + 1}",
                            source_path=rel,
                            line_no=idx + 1,
                            heading=current_heading,
                            line_text=row_line,
                            row_label=row_label,
                            row_text=row_text,
                            cell_header=cell_header,
                            cell_kind=cell_kind,
                            cell_text=cell_text,
                        )
                    )
            idx += 1
    return mentions


def collect_table_semantic_results(
    production_rows: list[ProductionOccurrence],
) -> dict[str, list[dict[str, str]]]:
    production_pairs = {(row.form, row.source_ref) for row in production_rows}
    manifest_map = manifest_rows_by_model_entry_path()
    auto_rows: list[dict[str, str]] = []
    suggestions: list[dict[str, str]] = []
    ignored: list[dict[str, str]] = []
    notation: list[dict[str, str]] = []
    mentions_by_pair: dict[tuple[str, str], TableFormMention] = {}
    seen_auto: set[tuple[str, str, str, str]] = set()
    seen_suggest: set[tuple[str, str, str, str]] = set()
    seen_ignored: set[tuple[str, str]] = set()
    seen_notation: set[tuple[str, str]] = set()

    for path in sorted(MODEL_ENTRIES_DIR.glob("*.model.md")):
        source_path = relative_source_path(path)
        entry_row = manifest_map.get(source_path)
        target_forms = entry_target_forms(entry_row)
        for mention in table_form_mentions_from_path(path):
            pair = (mention.form, mention.source_ref)
            mentions_by_pair.setdefault(pair, mention)
            if pair in production_pairs:
                continue
            notation_reason = notation_or_metadata_reason(mention.form)
            if notation_reason:
                if pair not in seen_notation:
                    seen_notation.add(pair)
                    notation.append(
                        {
                            "source_ref": mention.source_ref,
                            "nearest_heading": mention.heading,
                            "row_label": mention.row_label,
                            "form": mention.form,
                            "display": mention.form,
                            "suggested_language": "",
                            "suggested_role": "",
                            "confidence": "ignore",
                            "reason": notation_reason,
                            "context": mention.line_text,
                        }
                    )
                continue
            if mention.form.casefold() in TABLE_STOPWORDS or candidate_category(mention.form) != "needs_review":
                if pair not in seen_ignored:
                    seen_ignored.add(pair)
                    ignored.append(
                        {
                            "source_ref": mention.source_ref,
                            "nearest_heading": mention.heading,
                            "row_label": mention.row_label,
                            "form": mention.form,
                            "display": mention.form,
                            "suggested_language": "",
                            "suggested_role": "",
                            "confidence": "ignore",
                            "reason": "table stopword or fragment",
                            "context": mention.line_text,
                        }
                    )
                continue

            semantic_text = normalize_semantic_text(
                " | ".join([mention.heading, mention.row_label, mention.row_text, mention.cell_header, mention.cell_text])
            )
            is_selected = contains_phrase(semantic_text, TABLE_SELECTED_PHRASES)
            is_source = contains_phrase(semantic_text, TABLE_SOURCE_PHRASES)
            is_output = contains_phrase(semantic_text, TABLE_OUTPUT_PHRASES)
            is_comparison = contains_phrase(semantic_text, TABLE_COMPARISON_PHRASES)
            is_negative = contains_phrase(semantic_text, TABLE_NEGATIVE_PHRASES)
            is_target = contains_phrase(semantic_text, TABLE_TARGET_PHRASES)
            caution_intermediate = contains_phrase(semantic_text, TABLE_NEGATIVE_PHRASES)

            role_candidates: list[tuple[str, str, str]] = []
            if mention.cell_kind == "input":
                if is_selected and not is_negative:
                    role_candidates.append(("selected_input", "auto", "selected-input row"))
                elif is_source:
                    role_candidates.append(("source_protoform", "auto", "source-protoform row"))
                elif is_comparison or is_negative:
                    role_candidates.append(("comparison_form", "suggest", "comparison/negative row"))
            elif mention.cell_kind == "output":
                if is_output:
                    role_candidates.append(("regular_output", "auto", "output row"))
                    if mention.form in target_forms or is_target:
                        role_candidates.append(("target_form", "auto", "output matches target"))
                elif mention.form in target_forms and is_target:
                    role_candidates.append(("target_form", "auto", "explicit target row"))
                elif is_comparison or is_source or is_negative:
                    role_candidates.append(("comparison_form", "suggest", "output used as comparison"))
            elif mention.cell_kind == "comparison":
                if mention.form in target_forms and (is_target or is_output or is_selected):
                    role_candidates.append(("target_form", "auto", "comparison cell matches target"))
                elif is_comparison or is_source or is_negative or is_output:
                    role_candidates.append(("comparison_form", "auto", "comparison cell"))
            elif mention.cell_kind == "form":
                if mention.form in target_forms and (is_target or is_selected or is_output):
                    role_candidates.append(("target_form", "auto", "form row target"))
                    if is_output:
                        role_candidates.append(("regular_output", "auto", "form row regular output"))
                elif mention.form.startswith("*") and is_selected and not is_negative:
                    role_candidates.append(("selected_input", "auto", "selected form row"))
                elif mention.form.startswith("*") and is_source:
                    role_candidates.append(("source_protoform", "auto", "source form row"))
                elif is_comparison or is_negative or is_source:
                    role_candidates.append(("comparison_form", "auto", "comparison form row"))

            for role, confidence, reason in role_candidates:
                language, confident_language = infer_table_semantic_language(mention, role, target_forms)
                if not language:
                    if role == "comparison_form" and mention.form.startswith("*"):
                        # No explicit stage hint: fail closed. Do not silently
                        # default to pgmc OR preoe. A negative/caution phrase is
                        # not positive evidence for any stage; leave unresolved
                        # so the mention is queued for manual review.
                        language = ""
                    else:
                        key = (mention.form, mention.source_ref, role, "suggest")
                        if key not in seen_suggest:
                            seen_suggest.add(key)
                            suggestions.append(
                                {
                                    "source_ref": mention.source_ref,
                                    "nearest_heading": mention.heading,
                                    "row_label": mention.row_label,
                                    "form": mention.form,
                                    "display": mention.form,
                                    "suggested_language": "",
                                    "suggested_role": role,
                                    "confidence": "suggest",
                                    "reason": f"{reason}; language unclear",
                                    "context": mention.line_text,
                                }
                            )
                        continue
                if confidence == "auto" and role == "comparison_form" and mention.cell_kind == "form" and not confident_language:
                    confidence = "suggest"
                if confidence == "auto" and role == "comparison_form" and is_negative:
                    confidence = "suggest"
                if confidence == "auto" and mention.form.startswith("*") and role == "comparison_form" and not confident_language:
                    confidence = "suggest"
                if confidence == "auto" and mention.form.startswith("*") and caution_intermediate:
                    confidence = "suggest"
                if confidence == "auto":
                    key = (language, mention.form, role, mention.source_ref)
                    if key not in seen_auto:
                        seen_auto.add(key)
                        auto_rows.append(
                            {
                                "language": language,
                                "form": mention.form,
                                "display": mention.form,
                                "sort_key": transliterate_sort_key(mention.form),
                                "form_role": role,
                                "source_scope": TABLE_SEMANTIC_SOURCE_SCOPE,
                                "source_ref": mention.source_ref,
                                "origin": TABLE_SEMANTIC_ORIGIN,
                                "status": "auto",
                            }
                        )
                else:
                    key = (mention.form, mention.source_ref, role, "suggest")
                    auto_key = (language, mention.form, role, mention.source_ref)
                    if auto_key not in seen_auto and key not in seen_suggest:
                        seen_suggest.add(key)
                        suggestions.append(
                            {
                                "source_ref": mention.source_ref,
                                "nearest_heading": mention.heading,
                                "row_label": mention.row_label,
                                "form": mention.form,
                                "display": mention.form,
                                "suggested_language": language,
                                "suggested_role": role,
                                "confidence": "suggest",
                                "reason": reason,
                                "context": mention.line_text,
                            }
                        )

    auto_keys = {(row["language"], row["form"], row["form_role"], row["source_ref"]) for row in auto_rows}
    suggestions = [
        row
        for row in suggestions
        if (row["suggested_language"], row["form"], row["suggested_role"], row["source_ref"]) not in auto_keys
    ]
    return apply_table_decisions({
        "auto_rows": auto_rows,
        "suggestions": suggestions,
        "ignored": ignored,
        "notation": notation,
        "suggest_pairs": [{"form": row["form"], "source_ref": row["source_ref"]} for row in suggestions],
        "ignore_pairs": [{"form": row["form"], "source_ref": row["source_ref"]} for row in ignored],
    }, mentions_by_pair)


def write_table_suggestions(path: Path, suggestions: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=TABLE_SUGGESTION_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in sorted(suggestions, key=lambda item: (item["source_ref"], item["form"], item["suggested_role"])):
            writer.writerow(row)


def write_broad_prose_suggestions(path: Path, suggestions: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=BROAD_PROSE_SUGGESTION_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in sorted(suggestions, key=lambda item: (item["source_ref"], item["form"], item["suggested_role"])):
            writer.writerow({field: row.get(field, "") for field in BROAD_PROSE_SUGGESTION_FIELDS})


def load_broad_prose_decisions() -> list[dict[str, str]]:
    if not BROAD_PROSE_DECISIONS_PATH.exists():
        return []
    with BROAD_PROSE_DECISIONS_PATH.open(encoding="utf-8") as handle:
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in csv.DictReader(handle, delimiter="\t")]
    for row in rows:
        action = row.get("action", "")
        if action not in BROAD_PROSE_DECISION_ACTIONS:
            raise ValueError(f"Unknown broad prose decision action: {action or '<blank>'}")
        if row.get("form"):
            row["form"] = normalize_form(row["form"])
        if action in {"accept", "defer"}:
            if not row.get("language"):
                raise ValueError(f"Broad prose decision {action} requires language: {row}")
            if row["language"] not in KNOWN_LANGUAGE_CODES:
                raise ValueError(f"Broad prose decision has unknown language code: {row}")
            if row.get("form_role") not in ALLOWED_FORM_ROLES:
                raise ValueError(f"Broad prose decision {action} requires a valid form_role: {row}")
    return rows


def load_print_decisions() -> list[dict[str, str]]:
    if not PRINT_DECISIONS_PATH.exists():
        return []
    with PRINT_DECISIONS_PATH.open(encoding="utf-8") as handle:
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in csv.DictReader(handle, delimiter="\t")]
    for row in rows:
        action = row.get("action", "")
        if action not in PRINT_DECISION_ACTIONS:
            raise ValueError(f"Unknown print decision action: {action or '<blank>'}")
        if row.get("form"):
            row["form"] = normalize_decision_form(row["form"])
        if action in {"include_main", "exclude_main"} and not row.get("source_ref") and not row.get("form"):
            raise ValueError(f"Print decision {action} requires at least form or source_ref: {row}")
        role = row.get("form_role", "")
        if role and role not in ALLOWED_FORM_ROLES:
            raise ValueError(f"Print decision has invalid form_role: {row}")
        language = row.get("language", "")
        if language and language not in KNOWN_LANGUAGE_CODES:
            raise ValueError(f"Print decision has unknown language code: {row}")
    return rows


def print_decision_matches_row(decision: dict[str, str], row: ProductionOccurrence) -> bool:
    if decision.get("language") and decision["language"] != row.language:
        return False
    if decision.get("form") and decision["form"] != row.form:
        return False
    # Strip line number from row source_ref before comparing
    if decision.get("source_ref"):
        row_source_no_line = re.sub(r':\d+$', '', row.source_ref)
        if decision["source_ref"] != row_source_no_line:
            return False
    if decision.get("form_role") and decision["form_role"] != row.form_role:
        return False
    # Variety is matched exactly and fail-closed (blank matches only blank).
    if (decision.get("variety", "") or "").strip() != (row.variety or "").strip():
        return False
    return True


def apply_broad_prose_decisions(
    buckets: dict[str, list[dict[str, str]]],
) -> tuple[dict[str, list[dict[str, str]]], list[dict[str, str]]]:
    decisions = load_broad_prose_decisions()
    if not decisions:
        return buckets, []

    updated = {key: list(value) for key, value in buckets.items()}
    suggestion_entries = updated.get("broad_prose_suggestion", [])
    unresolved_entries = updated.get("needs_review", [])
    decision_rows: list[dict[str, str]] = []
    deferred_entries: list[dict[str, str]] = []
    ignored_entries: list[dict[str, str]] = []
    seen_decision_rows: set[tuple[str, str, str, str]] = set()
    consume_suggestions: set[int] = set()
    consume_unresolved: set[int] = set()

    for decision in decisions:
        match_suggestion_index = next(
            (
                idx
                for idx, row in enumerate(suggestion_entries)
                if row.get("form") == decision.get("form") and row.get("source_ref") == decision.get("source_ref")
            ),
            None,
        )
        match_unresolved_index = next(
            (
                idx
                for idx, row in enumerate(unresolved_entries)
                if row.get("form") == decision.get("form") and row.get("source_ref") == decision.get("source_ref")
            ),
            None,
        )
        suggestion_row = suggestion_entries[match_suggestion_index] if match_suggestion_index is not None else None
        unresolved_row = unresolved_entries[match_unresolved_index] if match_unresolved_index is not None else None
        if suggestion_row is None and unresolved_row is None and decision["action"] != "accept":
            continue
        if suggestion_row is None and unresolved_row is None and decision["action"] == "accept":
            continue

        note = decision.get("note", "")
        language = decision.get("language") or (suggestion_row or {}).get("suggested_language", "")
        role = decision.get("form_role") or (suggestion_row or {}).get("suggested_role", "")
        base_entry = suggestion_row or unresolved_row or {}

        if decision["action"] == "accept":
            variety = (decision.get("variety") or "").strip()
            key = (language, variety, decision["form"], role, decision["source_ref"])
            if key not in seen_decision_rows:
                seen_decision_rows.add(key)
                decision_rows.append(
                    {
                        "language": language,
                        "variety": variety,
                        "form": decision["form"],
                        "display": decision["form"],
                        "sort_key": transliterate_sort_key(decision["form"]),
                        "form_role": role,
                        "source_scope": BROAD_PROSE_DECISION_SOURCE_SCOPE,
                        "source_ref": decision["source_ref"],
                        "origin": BROAD_PROSE_DECISION_ORIGIN,
                        "status": "override",
                    }
                )
        elif decision["action"] == "defer":
            deferred_entries.append(
                {
                    "form": decision["form"],
                    "source_ref": decision["source_ref"],
                    "suggested_language": language,
                    "suggested_role": role,
                    "reason": note or base_entry.get("reason", "curated defer"),
                }
            )
        else:
            ignored_entries.append(
                {
                    "form": decision["form"],
                    "source_ref": decision["source_ref"],
                    "reason": note or base_entry.get("reason", "curated ignore"),
                }
            )

        if match_suggestion_index is not None:
            consume_suggestions.add(match_suggestion_index)
        if match_unresolved_index is not None:
            consume_unresolved.add(match_unresolved_index)

    if consume_suggestions:
        updated["broad_prose_suggestion"] = [
            row for idx, row in enumerate(suggestion_entries) if idx not in consume_suggestions
        ]
    if consume_unresolved:
        updated["needs_review"] = [
            row for idx, row in enumerate(unresolved_entries) if idx not in consume_unresolved
        ]
    if deferred_entries:
        updated["broad_prose_deferred"] = sorted(
            deferred_entries,
            key=lambda item: (item["source_ref"], item["form"], item["suggested_role"]),
        )
    if ignored_entries:
        updated["broad_prose_curated_ignored"] = sorted(
            ignored_entries,
            key=lambda item: (item["source_ref"], item["form"]),
        )
    return updated, decision_rows


def load_table_decisions() -> list[dict[str, str]]:
    if not TABLE_DECISIONS_PATH.exists():
        return []
    with TABLE_DECISIONS_PATH.open(encoding="utf-8") as handle:
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in csv.DictReader(handle, delimiter="\t")]
    for row in rows:
        action = row.get("action", "")
        if action not in TABLE_DECISION_ACTIONS:
            raise ValueError(f"Unknown table decision action: {action or '<blank>'}")
        if row.get("form"):
            row["form"] = normalize_form(row["form"])
        if action in {"accept", "defer"}:
            if not row.get("language"):
                raise ValueError(f"Table decision {action} requires language: {row}")
            if row["language"] not in KNOWN_LANGUAGE_CODES:
                raise ValueError(f"Table decision has unknown language code: {row}")
            if row.get("form_role") not in ALLOWED_FORM_ROLES:
                raise ValueError(f"Table decision {action} requires a valid form_role: {row}")
    return rows


def table_semantic_suggestion_row(
    mention: TableFormMention,
    *,
    language: str,
    role: str,
    reason: str,
) -> dict[str, str]:
    return {
        "source_ref": mention.source_ref,
        "nearest_heading": mention.heading,
        "row_label": mention.row_label,
        "form": mention.form,
        "display": mention.form,
        "suggested_language": language,
        "suggested_role": role,
        "confidence": "suggest",
        "reason": reason,
        "context": mention.line_text,
    }


def table_semantic_ignored_row(
    mention: TableFormMention,
    *,
    reason: str,
) -> dict[str, str]:
    return {
        "source_ref": mention.source_ref,
        "nearest_heading": mention.heading,
        "row_label": mention.row_label,
        "form": mention.form,
        "display": mention.form,
        "suggested_language": "",
        "suggested_role": "",
        "confidence": "ignore",
        "reason": reason,
        "context": mention.line_text,
    }


def table_decision_matches_result(
    decision: dict[str, str],
    row: dict[str, str],
    *,
    language_field: str,
    role_field: str,
) -> bool:
    if decision.get("form") != row.get("form") or decision.get("source_ref") != row.get("source_ref"):
        return False
    if decision.get("language") and decision["language"] != row.get(language_field, ""):
        return False
    if decision.get("form_role") and decision["form_role"] != row.get(role_field, ""):
        return False
    return True


def apply_table_decisions(
    raw_results: dict[str, list[dict[str, str]]],
    mentions_by_pair: dict[tuple[str, str], TableFormMention],
) -> dict[str, list[dict[str, str]]]:
    decisions = load_table_decisions()
    if not decisions:
        return {
            **raw_results,
            "decision_rows": [],
        }

    consumed_suggestions: set[int] = set()
    consumed_ignored: set[int] = set()
    decision_rows: list[dict[str, str]] = []
    extra_suggestions: list[dict[str, str]] = []
    extra_ignored: list[dict[str, str]] = []
    seen_decision_rows: set[tuple[str, str, str, str]] = set()
    seen_suggestions: set[tuple[str, str, str]] = set()
    seen_ignored: set[tuple[str, str]] = set()

    suggestions = raw_results["suggestions"]
    ignored = raw_results["ignored"]

    for decision in decisions:
        pair = (decision["form"], decision["source_ref"])
        mention = mentions_by_pair.get(pair)
        matching_suggestion_indexes = [
            idx
            for idx, row in enumerate(suggestions)
            if table_decision_matches_result(decision, row, language_field="suggested_language", role_field="suggested_role")
        ]
        matching_ignored_indexes = [
            idx
            for idx, row in enumerate(ignored)
            if decision.get("form") == row.get("form") and decision.get("source_ref") == row.get("source_ref")
        ]
        suggestion_row = suggestions[matching_suggestion_indexes[0]] if matching_suggestion_indexes else None
        ignored_row = ignored[matching_ignored_indexes[0]] if matching_ignored_indexes else None
        note = decision.get("note", "")

        if decision["action"] == "accept":
            if not mention:
                raise ValueError(f"Table decision accept could not find table mention: {decision}")
            language = decision.get("language") or (suggestion_row or {}).get("suggested_language", "")
            role = decision.get("form_role") or (suggestion_row or {}).get("suggested_role", "")
            if not language or not role:
                raise ValueError(f"Table decision accept requires language and form_role: {decision}")
            variety = (decision.get("variety") or "").strip()
            key = (language, variety, mention.form, role, mention.source_ref)
            if key not in seen_decision_rows:
                seen_decision_rows.add(key)
                decision_rows.append(
                    {
                        "language": language,
                        "variety": variety,
                        "form": mention.form,
                        "display": mention.form,
                        "sort_key": transliterate_sort_key(mention.form),
                        "form_role": role,
                        "source_scope": TABLE_SEMANTIC_DECISION_SOURCE_SCOPE,
                        "source_ref": mention.source_ref,
                        "origin": TABLE_SEMANTIC_DECISION_ORIGIN,
                        "status": "override",
                    }
                )
            consumed_suggestions.update(matching_suggestion_indexes)
            consumed_ignored.update(matching_ignored_indexes)
            continue

        if decision["action"] == "defer":
            if matching_suggestion_indexes:
                continue
            if not mention:
                raise ValueError(f"Table decision defer could not find table mention: {decision}")
            language = decision.get("language") or (suggestion_row or {}).get("suggested_language", "")
            role = decision.get("form_role") or (suggestion_row or {}).get("suggested_role", "")
            if not language or not role:
                raise ValueError(f"Table decision defer requires language and form_role: {decision}")
            reason = note or (ignored_row or {}).get("reason") or "curated defer"
            key = (mention.form, mention.source_ref, role)
            if key not in seen_suggestions:
                seen_suggestions.add(key)
                extra_suggestions.append(
                    table_semantic_suggestion_row(mention, language=language, role=role, reason=reason)
                )
            consumed_ignored.update(matching_ignored_indexes)
            continue

        if not mention:
            raise ValueError(f"Table decision ignore could not find table mention: {decision}")
        reason = note or (suggestion_row or ignored_row or {}).get("reason") or "curated ignore"
        if pair not in seen_ignored:
            seen_ignored.add(pair)
            extra_ignored.append(table_semantic_ignored_row(mention, reason=reason))
        consumed_suggestions.update(matching_suggestion_indexes)
        consumed_ignored.update(matching_ignored_indexes)

    final_suggestions = [
        row for idx, row in enumerate(suggestions)
        if idx not in consumed_suggestions
    ] + extra_suggestions
    final_ignored = [
        row for idx, row in enumerate(ignored)
        if idx not in consumed_ignored
    ] + extra_ignored

    final_suggestions.sort(key=lambda item: (item["source_ref"], item["form"], item["suggested_role"]))
    final_ignored.sort(key=lambda item: (item["source_ref"], item["form"]))
    return {
        **raw_results,
        "suggestions": final_suggestions,
        "ignored": final_ignored,
        "suggest_pairs": [{"form": row["form"], "source_ref": row["source_ref"]} for row in final_suggestions],
        "ignore_pairs": [{"form": row["form"], "source_ref": row["source_ref"]} for row in final_ignored],
        "decision_rows": decision_rows,
    }


def table_candidates_from_path(path: Path, *, allow_non_model_entry: bool = False) -> list[CandidateOccurrence]:
    return [
        CandidateOccurrence(
            form=mention.form,
            source_ref=mention.source_ref,
            source_path=mention.source_path,
            line_no=mention.line_no,
            heading=mention.heading,
            line_text=mention.line_text,
            candidate_origin=mention.candidate_origin,
        )
        for mention in table_form_mentions_from_path(path, allow_non_model_entry=allow_non_model_entry)
    ]


def excluded_intermediate_trace_forms() -> list[dict[str, str]]:
    manifest_rows = parse_manifest_rows()
    manifest_by_title = {
        (row["lexical_item"], row["counterpart"], row["protoform"]): row
        for row in manifest_rows
    }
    entries: list[dict[str, str]] = []
    for entry in parse_compact_entries():
        manifest_row = manifest_by_title.get((entry["title"], entry["expected"], entry["proto"]))
        if manifest_row is not None:
            ref = heading_ref(manifest_row["lexical_item"], manifest_row["counterpart"], manifest_row["derivation_class"])
        else:
            ref = heading_ref(str(entry["title"]), str(entry["expected"]))
        for label, form in entry["stages"]:
            entries.append(
                {
                    "form": form,
                    "source_ref": ref,
                    "source_path": COMPACT_PATH.relative_to(REPO_ROOT).as_posix(),
                    "heading": label,
                    "category": "intermediate_trace_form",
                    "context": label,
                    "sort_key": transliterate_sort_key(form),
                }
            )
    entries.sort(key=lambda row: (row.get("sort_key", ""), row["form"], row["source_ref"]))
    return entries


def broad_candidates_from_path(path: Path) -> list[CandidateOccurrence]:
    rel = relative_source_path(path)
    candidates: list[CandidateOccurrence] = []
    in_fence = False
    current_heading = ""
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("#"):
            current_heading = stripped
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or stripped.startswith(NOISE_LINE_PREFIXES) or stripped.startswith("\\"):
            continue
        if stripped.startswith("|") or stripped.startswith("define "):
            continue
        scan_line = NESTED_RECON_IV_RE.sub("", line)
        scrubbed = strip_explicit_markup(scan_line)
        # .recon spans represent reconstructed lexical forms; extract with asterisk prefix.
        for match in RECON_SPAN_RE.finditer(scan_line):
            form = strip_markup("*" + match.group(1))
            if form:
                candidates.append(
                    CandidateOccurrence(
                        form=form,
                        source_ref=f"{rel}:{line_no}",
                        source_path=rel,
                        line_no=line_no,
                        heading=current_heading,
                        line_text=stripped,
                        candidate_origin="broad_prose_candidate",
                    )
                )
        for match in MARKUP_FORM_RE.finditer(scrubbed):
            raw = next(group for group in match.groups() if group)
            form = strip_markup(raw)
            if form:
                candidates.append(
                    CandidateOccurrence(
                        form=form,
                        source_ref=f"{rel}:{line_no}",
                        source_path=rel,
                        line_no=line_no,
                        heading=current_heading,
                        line_text=stripped,
                        candidate_origin="broad_prose_candidate",
                    )
                )
        for match in re.finditer(r"\b(?:PGmc|PWGmc|NWGmc|OE|ON|OHG|OFri|Goth)\s+(\*?[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ'./()\-]+)", scrubbed):
            form = strip_markup(match.group(1))
            if form:
                candidates.append(
                    CandidateOccurrence(
                        form=form,
                        source_ref=f"{rel}:{line_no}",
                        source_path=rel,
                        line_no=line_no,
                        heading=current_heading,
                        line_text=stripped,
                        candidate_origin="broad_prose_candidate",
                    )
                )
    return candidates


def headings_for_source_path(source_path: str) -> list[tuple[int, str]]:
    path = Path(source_path)
    if not path.is_absolute():
        path = REPO_ROOT / source_path
    if not path.exists():
        return []
    headings: list[tuple[int, str]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("#"):
            headings.append((line_no, stripped))
    return headings


def nearest_heading_for_source_line(source_path: str, line_no: int) -> str:
    current = ""
    for heading_line, heading in headings_for_source_path(source_path):
        if heading_line > line_no:
            break
        current = heading
    return current


def production_line_occurrences(
    production_rows: list[ProductionOccurrence],
) -> dict[str, list[tuple[str, int, str]]]:
    by_source: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    for row in production_rows:
        ref = row.source_ref
        if ".md:" not in ref:
            continue
        path_part, line_part = ref.rsplit(":", 1)
        if not line_part.isdigit():
            continue
        line_no = int(line_part)
        by_source[path_part].append((row.form, line_no, nearest_heading_for_source_line(path_part, line_no)))
    return by_source


def orthographic_normalization_key(text: str) -> str:
    value = text.lstrip("*").casefold()
    normalized = unicodedata.normalize("NFKD", value)
    stripped = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    parts: list[str] = []
    for ch in stripped:
        if ch in {"þ", "ð"}:
            parts.append("th")
        elif ch in {"æ", "ǣ"}:
            parts.append("ae")
        elif ch == "œ":
            parts.append("oe")
        elif ch in {"ċ", "ġ"}:
            parts.append(ch.replace("ċ", "c").replace("ġ", "g"))
        elif ch == "ȳ":
            parts.append("y")
        else:
            parts.append(ch)
    loose = "".join(parts).replace("ae", "ea")
    return re.sub(r"[^a-z0-9]+", "", loose)


def model_entry_heading_map() -> dict[str, str]:
    return {
        heading_ref(row["lexical_item"], row["counterpart"], row["derivation_class"]): row["model_entry_path"]
        for row in parse_manifest_rows()
        if row.get("model_entry_path")
    }


def build_entry_coverage_index(
    production_rows: list[ProductionOccurrence],
) -> dict[str, dict[str, set[str]]]:
    manifest_map = manifest_rows_by_model_entry_path()
    heading_map = model_entry_heading_map()
    coverage_index: dict[str, dict[str, set[str]]] = defaultdict(
        lambda: {
            "forms": set(),
            "displays": set(),
            "casefold_forms": set(),
            "casefold_displays": set(),
            "orth_keys": set(),
        }
    )
    for row in production_rows:
        entry_path = ""
        if row.source_ref in heading_map:
            entry_path = heading_map[row.source_ref]
        elif ".model.md:" in row.source_ref:
            path_part = row.source_ref.rsplit(":", 1)[0]
            if path_part in manifest_map:
                entry_path = path_part
        if not entry_path:
            continue
        coverage = coverage_index[entry_path]
        coverage["forms"].add(row.form)
        coverage["displays"].add(row.display)
        coverage["casefold_forms"].add(row.form.casefold())
        coverage["casefold_displays"].add(row.display.casefold())
        coverage["orth_keys"].add(orthographic_normalization_key(row.form))
        coverage["orth_keys"].add(orthographic_normalization_key(row.display))
    return coverage_index


def same_entry_coverage_reason(
    candidate: CandidateOccurrence,
    coverage_index: dict[str, dict[str, set[str]]],
) -> str:
    coverage = coverage_index.get(candidate.source_path)
    if not coverage:
        return ""
    if candidate.form in coverage["forms"] or candidate.form in coverage["displays"]:
        return "same form already indexed in this entry"
    return ""


def orthographic_variant_reason(
    candidate: CandidateOccurrence,
    coverage_index: dict[str, dict[str, set[str]]],
) -> str:
    coverage = coverage_index.get(candidate.source_path)
    if not coverage:
        return ""
    if candidate.form in coverage["forms"] or candidate.form in coverage["displays"]:
        return ""
    casefold = candidate.form.casefold()
    loose_key = orthographic_normalization_key(candidate.form)
    text = normalize_semantic_text(candidate.line_text)
    if casefold in coverage["casefold_forms"] or casefold in coverage["casefold_displays"]:
        return "capitalization variant of indexed form"
    if candidate.form[:1].isupper() and loose_key in coverage["orth_keys"]:
        return "capitalization variant of indexed form"
    if loose_key in coverage["orth_keys"] and contains_phrase(text, PROSE_NORMALIZATION_CUES):
        return "orthographic/normalization variant of indexed form"
    return ""


def first_starred_form_after_from(candidate: CandidateOccurrence) -> str:
    from_match = re.search(r"\bfrom\b", candidate.line_text, flags=re.IGNORECASE)
    if not from_match:
        return ""
    tail = candidate.line_text[from_match.end() :]
    for match in NESTED_RECON_IV_RE.finditer(tail):
        form = strip_markup(match.group("form"))
        if form:
            return "*" + form
    for match in RECON_SPAN_RE.finditer(tail):
        form = strip_markup(match.group(1))
        if form:
            return "*" + form
    for form in extract_forms_from_markup(tail):
        if form.startswith("*"):
            return form
    return ""


def has_development_chain_cues(semantic_text: str) -> bool:
    return any(token in semantic_text for token in DEVELOPMENT_CHAIN_CUES)


def broad_prose_notation_reason(candidate: CandidateOccurrence) -> str:
    reason = notation_or_metadata_reason(candidate.form)
    if reason:
        return reason
    if re.fullmatch(r"[A-Za-z][A-Z]", candidate.form):
        return "phonological environment notation"
    if any(token in candidate.form for token in (",", "/", ">")):
        return "notation or compound expression"
    semantic_text = normalize_semantic_text(candidate.line_text)
    source_form_after_from = first_starred_form_after_from(candidate)
    chain_like_development = (
        candidate.form.startswith("*")
        and candidate.heading.startswith("### Development")
        and has_development_chain_cues(semantic_text)
    )
    line_forms = extract_forms_from_markup(candidate.line_text)
    starred_line_forms = [form for form in line_forms if form.startswith("*")]
    if chain_like_development and source_form_after_from and candidate.form != source_form_after_from:
        return "intermediate or model-stage form in development chain"
    if chain_like_development and candidate.form in starred_line_forms:
        starred_form_index = starred_line_forms.index(candidate.form)
        if starred_form_index > 0:
            return "intermediate or model-stage form in development chain"
    if (
        chain_like_development
        and not source_form_after_from
        and not re.search(rf"\bfrom\b[^.]*{re.escape(candidate.form.casefold())}\b", semantic_text)
    ):
        return "intermediate or model-stage form in development chain"
    if (
        candidate.form.startswith("*")
        and candidate.heading.startswith("### Development")
        and "stage" in semantic_text
        and (not source_form_after_from or candidate.form != source_form_after_from)
    ):
        return "intermediate or model-stage form in development chain"
    return ""


def ordinary_prose_gloss_reason(candidate: CandidateOccurrence) -> str:
    lowered = candidate.form.casefold()
    semantic_text = normalize_semantic_text(candidate.line_text)
    if candidate.form.startswith("OE") and re.search(r"[A-Z]", candidate.form[2:]):
        return "formal rule label"
    if lowered == "help" and "separate noun" in semantic_text:
        return "ordinary prose/gloss word"
    if lowered in PROSE_GLOSS_FORMS or lowered in FALSE_POSITIVE_FORMS:
        return "ordinary prose/gloss word"
    return ""


def likely_category_language(category: str) -> str:
    return {
        "likely_oe": "oe",
        "likely_pgmc": "pgmc",
        "likely_pwgmc": "pwgmc",
        "likely_nwgmc": "pnwgmc",
        "likely_pnwgmc": "pnwgmc",
        "likely_preoe": "preoe",
        "likely_on": "on",
        "likely_os": "os",
        "likely_ohg": "ohg",
        "likely_ofris": "ofris",
        "likely_goth": "goth",
        "likely_odutch": "odutch",
        "likely_mdutch": "mdutch",
        "likely_dutch": "dutch",
        "likely_german": "german",
        "likely_lat": "lat",
        "likely_greek": "greek",
        "likely_skt": "skt",
        "likely_me": "me",
        "likely_modeng": "modeng",
        "likely_oirish": "oirish",
    }.get(category, "")


def inline_labeled_language(candidate: CandidateOccurrence) -> str:
    text = normalize_semantic_text(candidate.line_text)
    form = re.escape(candidate.form.casefold())
    for pattern, code in (
        (rf"\b(?:oe|old english)\s+{form}\b", "oe"),
        (rf"\b(?:pgmc|proto-germanic)\s+{form}\b", "pgmc"),
        (rf"\b(?:pwgmc|proto-west germanic)\s+{form}\b", "pwgmc"),
        (rf"\b(?:pnwgmc|nwgmc|proto-northwest germanic)\s+{form}\b", "pnwgmc"),
        (rf"\b(?:paf|proto-anglo-frisian)\s+{form}\b", "paf"),
        (rf"\b(?:pie|proto-indo-european)\s+{form}\b", "pie"),
        (rf"\b(?:on|old norse)\s+{form}\b", "on"),
        (rf"\b(?:os|old saxon)\s+{form}\b", "os"),
        (rf"\b(?:ohg|old high german)\s+{form}\b", "ohg"),
        (rf"\b(?:ofri|ofris|old frisian)\s+{form}\b", "ofris"),
        (rf"\b(?:goth|gothic)\s+{form}\b", "goth"),
        (rf"\b(?:german)\s+{form}\b", "german"),
        (rf"\b(?:dutch)\s+{form}\b", "dutch"),
        (rf"\b(?:latin|lat\.)\s+{form}\b", "lat"),
        (rf"\b(?:greek|gk\.)\s+{form}\b", "greek"),
        (rf"\b(?:sanskrit|skt\.)\s+{form}\b", "skt"),
    ):
        if re.search(pattern, text):
            return code
    return ""


def same_entry_old_english_hint(candidate: CandidateOccurrence) -> bool:
    if not candidate.source_path.endswith(".model.md"):
        return False
    path = REPO_ROOT / candidate.source_path
    if not path.exists():
        return False
    current_heading = ""
    needle = candidate.form.casefold()
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            current_heading = stripped
        normalized = normalize_semantic_text(line)
        if needle not in normalized:
            continue
        if current_heading.startswith("### Old English evidence"):
            return True
        if re.search(rf"\b(?:old english|oe)\s+{re.escape(needle)}\b", normalized):
            return True
    return False


def infer_broad_prose_language(candidate: CandidateOccurrence) -> str:
    text = " ".join([candidate.heading, candidate.line_text])
    inline_code = inline_labeled_language(candidate)
    if inline_code:
        return inline_code
    if not candidate.form.startswith("*") and same_entry_old_english_hint(candidate):
        return "oe"
    hints = explicit_language_hints(text)
    non_oe_hints = hints - {"oe"}
    if candidate.form.startswith("*"):
        for code in ("preoe", "paf", "nsgmc", "pwgmc", "pnwgmc", "pgmc", "pie"):
            if code in hints:
                return code
        if len(non_oe_hints) == 1:
            return next(iter(non_oe_hints))
        # No explicit stage hint: fail closed. Do not silently default to pgmc.
        # The mention will be queued for manual review in suggestions.
        return ""
    if len(non_oe_hints) == 1:
        return next(iter(non_oe_hints))
    if candidate.heading.startswith("### Old English evidence"):
        return "oe"
    guessed = likely_category_language(guess_unresolved_category(candidate))
    return guessed or "oe"


def broad_prose_suggestion_row(
    candidate: CandidateOccurrence,
    *,
    language: str,
    role: str,
    reason: str,
    confidence: str = "suggest",
) -> dict[str, str]:
    return {
        "source_ref": candidate.source_ref,
        "nearest_heading": candidate.heading,
        "form": candidate.form,
        "suggested_language": language,
        "suggested_role": role,
        "confidence": confidence,
        "reason": reason,
        "context": re.sub(r"\s+", " ", candidate.line_text).strip()[:160],
    }


def infer_broad_prose_suggestion(candidate: CandidateOccurrence) -> dict[str, str] | None:
    if candidate.candidate_origin != "broad_prose_candidate":
        return None
    if candidate.source_path == CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix():
        return None
    intro_path = INTRO_PATH.relative_to(REPO_ROOT).as_posix()
    if not candidate.source_path.endswith(".model.md") and candidate.source_path != intro_path:
        return None
    semantic_text = normalize_semantic_text(" ".join([candidate.heading, candidate.line_text]))
    if candidate.form == "help" and "separate noun" in semantic_text:
        return None
    if candidate.source_path == intro_path:
        language = "" if candidate.form.startswith("*") else "oe"
        if not language:
            # Introductory illustrative example with no stage hint: fail closed.
            # Return None to skip this entry instead of generating a suggestion.
            return None
        return broad_prose_suggestion_row(
            candidate,
            language=language,
            role="comparison_form" if not candidate.form.startswith("*") else "source_protoform",
            reason="introductory illustrative example",
        )
    language = infer_broad_prose_language(candidate)
    if candidate.form.startswith("*"):
        source_form_after_from = first_starred_form_after_from(candidate)
        if (
            candidate.heading.startswith("### Development")
            and source_form_after_from
            and candidate.form != source_form_after_from
            and has_development_chain_cues(semantic_text)
        ):
            return None
        if (
            candidate.heading.startswith("### Development")
            and source_form_after_from
            and candidate.form == source_form_after_from
        ):
            return broad_prose_suggestion_row(
                candidate,
                language=language,
                role="source_protoform",
                reason="source form in development prose",
            )
        if contains_phrase(semantic_text, PROSE_SELECTED_PHRASES) or contains_phrase(semantic_text, TABLE_SELECTED_PHRASES):
            return broad_prose_suggestion_row(
                candidate,
                language=language,
                role="selected_input",
                reason="selected input described in prose",
            )
        if contains_phrase(semantic_text, TABLE_NEGATIVE_PHRASES) or "background" in semantic_text or "doublet" in semantic_text or "competing" in semantic_text or "such as" in semantic_text or "older references to" in semantic_text or "comparator" in semantic_text:
            return broad_prose_suggestion_row(
                candidate,
                language=language,
                role="comparison_form",
                reason="comparative or background source form in prose",
            )
        if contains_phrase(semantic_text, PROSE_SOURCE_CUES) or "reconstruction" in semantic_text or "comparative" in semantic_text:
            return broad_prose_suggestion_row(
                candidate,
                language=language,
                role="source_protoform",
                reason="citation or reconstructed source form in prose",
            )
        return None
    if (
        language == "oe"
        and candidate.heading.startswith("### Development")
        and (
            same_entry_old_english_hint(candidate)
            or "citation form" in semantic_text
            or "dictionary" in semantic_text
            or re.search(rf"\b(?:oe|old english)\s+{re.escape(candidate.form.casefold())}\b", semantic_text)
            or any(ch in candidate.form for ch in "þðæǣœȳċġǭǫáéíóúāēīōūḗḯ")
        )
    ):
        return broad_prose_suggestion_row(
            candidate,
            language="oe",
            role="comparison_form",
            reason="attested Old English comparison form in development prose",
        )
    if (
        language == "oe"
        and same_entry_old_english_hint(candidate)
        and candidate.heading.startswith(
            ("### Reconstruction", "### Lexical note", "### Dialect note", "### Development note")
        )
    ):
        return broad_prose_suggestion_row(
            candidate,
            language="oe",
            role="comparison_form",
            reason="attested Old English comparison form in surrounding prose",
        )
    if contains_phrase(semantic_text, PROSE_COMPARISON_CUES) or candidate.heading.startswith(
        ("### Old English evidence", "### Form comparison", "### Paradigm comparison", "### Form note")
    ):
        return broad_prose_suggestion_row(
            candidate,
            language=language or "oe",
            role="comparison_form",
            reason="attested comparison or dictionary form described in prose",
        )
    return None


def manifest_rows_by_model_entry_path() -> dict[str, dict[str, str]]:
    return {row["model_entry_path"]: row for row in parse_manifest_rows() if row.get("model_entry_path")}


def entry_target_forms(entry_row: dict[str, str] | None) -> set[str]:
    if not entry_row:
        return set()
    counterpart = (entry_row.get("counterpart") or "").strip()
    if not counterpart:
        return set()
    forms = {counterpart}
    if entry_row.get("derivation_class") == "reconstructed_oe":
        forms.add(f"*{counterpart}")
    return forms


def contains_phrase(text: str, phrases: tuple[str, ...]) -> bool:
    return any(phrase in text for phrase in phrases)


def explicit_language_hints(text: str) -> set[str]:
    hints: set[str] = set()
    lowered = text.casefold()
    full_patterns = [
        (r"\bold norse\b", "on"),
        (r"\bold saxon\b", "os"),
        (r"\bold high german\b", "ohg"),
        (r"\bold frisian\b|\bofri\b|\bofris\b", "ofris"),
        (r"\bgothic\b", "goth"),
        (r"\bold dutch\b", "odutch"),
        (r"\bmiddle dutch\b", "mdutch"),
        (r"\bdutch\b", "dutch"),
        (r"\bgerman\b", "german"),
        (r"\bmodern english\b", "modeng"),
        (r"\bmiddle english\b", "me"),
        (r"\bold irish\b", "oirish"),
        (r"\bold english\b|\bwest saxon\b|\banglian\b|\bnorthumbrian\b|\bmercian\b|\bkentish\b", "oe"),
        (r"\bproto-germanic\b", "pgmc"),
        (r"\bproto-west germanic\b|\bproto-west-germanic\b", "pwgmc"),
        (r"\bproto-northwest germanic\b|\bproto-northwest-germanic\b", "pnwgmc"),
        (r"\bproto-anglo-frisian\b|\bproto-anglofrisian\b", "paf"),
        (r"\bnorthern west germanic\b", "nsgmc"),
        (r"\bproto-indo-european\b|\bproto-indo-european\b|\bpie\b", "pie"),
        (
            r"\b(?:intermediate pre-oe stage|intermediate pre-old-english stage|"
            r"later hardening stage|pre-oe stage|pre-old-english stage|"
            r"model-internal stage|same derivation)\b",
            "preoe",
        ),
    ]
    for pattern, code in full_patterns:
        if re.search(pattern, lowered):
            hints.add(code)
    code_patterns = [
        (r"(?<![A-Za-z])OE(?![A-Za-z])", "oe"),
        (r"(?<![A-Za-z])ON(?![A-Za-z])", "on"),
        (r"(?<![A-Za-z])OS(?![A-Za-z])", "os"),
        (r"(?<![A-Za-z])OHG(?![A-Za-z])", "ohg"),
        (r"(?<![A-Za-z])OFri(?:s)?(?![A-Za-z])", "ofris"),
        (r"(?<![A-Za-z])Goth(?![A-Za-z])", "goth"),
        (r"(?<![A-Za-z])PGmc(?![A-Za-z])", "pgmc"),
        (r"(?<![A-Za-z])PWGmc(?![A-Za-z])", "pwgmc"),
        (r"(?<![A-Za-z])PNWGmc(?![A-Za-z])", "pnwgmc"),
        (r"(?<![A-Za-z])NWGmc(?![A-Za-z])", "pnwgmc"),
        (r"(?<![A-Za-z])PAF(?![A-Za-z])", "paf"),
        (r"(?<![A-Za-z])PIE(?![A-Za-z])", "pie"),
    ]
    for pattern, code in code_patterns:
        if re.search(pattern, text):
            hints.add(code)
    return hints


def infer_table_semantic_language(
    mention: TableFormMention,
    role: str,
    target_forms: set[str],
    *,
    derivation_class: str = "",
) -> tuple[str, bool]:
    row_text = mention.row_text
    cell_text = mention.cell_text
    hints = explicit_language_hints(cell_text) | explicit_language_hints(row_text)
    if mention.form in target_forms:
        if mention.form.startswith("*") and derivation_class != "reconstructed_oe":
            return "", False
        return "oe", True
    non_oe_hints = hints - {"oe"}
    if mention.form.startswith("*"):
        if role in {"selected_input", "source_protoform", "comparison_form"}:
            if "preoe" in hints:
                return "preoe", True
            if len(non_oe_hints) == 1:
                return next(iter(non_oe_hints)), True
            if len(non_oe_hints) > 1:
                return "", False
            # Reconstructed form with no stage signal: fail closed. A reconstruction
            # asterisk is not evidence of Proto-Germanic; route to the review/decision
            # queue instead of silently labelling it pgmc.
            return "", False
        if role in {"target_form", "regular_output"}:
            if derivation_class == "reconstructed_oe" and mention.form in target_forms:
                return "oe", True
            if "preoe" in hints:
                return "preoe", True
            if len(non_oe_hints) == 1:
                return next(iter(non_oe_hints)), True
            if len(non_oe_hints) > 1:
                return "", False
            # Reconstructed output with no stage signal: fail closed (never silent pgmc).
            return "", False
    if role in {"selected_input", "source_protoform"} and mention.form.startswith("*"):
        for code in ("preoe", "paf", "nsgmc", "pwgmc", "pnwgmc", "pgmc", "pie"):
            if code in hints:
                return code, True
        return "", False
    if role in {"target_form", "regular_output"}:
        if len(hints - {"oe"}) == 0:
            return "oe", True
    if role == "comparison_form":
        if len(non_oe_hints) > 1:
            return "", False
        if len(non_oe_hints) == 1:
            return next(iter(non_oe_hints)), True
        if mention.cell_kind in {"comparison", "output"} and len(hints - {"oe"}) == 0:
            return "oe", True
        if len(hints) == 1:
            return next(iter(hints)), True
        if mention.form in target_forms:
            return "oe", True
        return "oe", False
    return "", False


def is_already_indexed_nearby(
    candidate: CandidateOccurrence,
    by_source: dict[str, list[tuple[str, int, str]]],
    *,
    line_window: int = 5,
) -> bool:
    if candidate.candidate_origin == "table_candidate":
        return False
    for form, line_no, heading in by_source.get(candidate.source_path, []):
        if form != candidate.form:
            continue
        if candidate.heading and heading and candidate.heading == heading:
            return True
        if abs(candidate.line_no - line_no) <= line_window:
            return True
    return False


def candidate_category(form: str) -> str:
    if not form or ".md" in form or ".pdf" in form or "/" in form or "<" in form or ">" in form or "\\" in form:
        return "possible_garbage"
    if " " in form or "," in form or "_" in form:
        return "possible_garbage"
    if form in EXACT_FRAGMENT_FORMS:
        return "ignored_fragment"
    if form.startswith("*") and (len(form.lstrip("*")) <= 4 or form.endswith("-")):
        return "ignored_fragment"
    if form.startswith("-") or form.endswith("-") or "(" in form or ")" in form:
        return "ignored_fragment"
    if re.fullmatch(r"\*?[-]?[aeiouyāēīōūæǣǭǫ]+(?:þ|z|n|m)?", form):
        return "ignored_fragment"
    if re.fullmatch(r"[a-z]{1,2}", form):
        return "ignored_fragment"
    if re.fullmatch(r"\*?[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ]{1}", form):
        return "ignored_fragment"
    if not looks_formlike(form):
        return "possible_garbage"
    return "needs_review"


def load_overrides() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    if not OVERRIDES_PATH.exists():
        return [], []
    with OVERRIDES_PATH.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in reader]
    adds = [row for row in rows if row.get("action") == "add"]
    ignores = [row for row in rows if row.get("action") == "ignore"]
    return adds, ignores


def override_matches(override: dict[str, str], *, form: str, source_scope: str = "", source_ref: str = "", language: str = "", variety: str = "") -> bool:
    for key, value in (("form", form), ("source_scope", source_scope), ("source_ref", source_ref), ("language", language)):
        expected = override.get(key, "")
        if expected and expected != value:
            return False
    # Variety is matched exactly and fail-closed: a blank decision variety
    # matches ONLY a blank occurrence variety; it never acts as a wildcard, and
    # a parent variety never matches a child variety.
    if (override.get("variety", "") or "").strip() != (variety or "").strip():
        return False
    return True


def build_production_rows(
    add_overrides: list[dict[str, str]] | None = None,
    ignore_overrides: list[dict[str, str]] | None = None,
    *,
    include_table_semantic: bool = True,
    table_semantic_results: dict[str, list[dict[str, str]]] | None = None,
    broad_prose_decision_rows: list[dict[str, str]] | None = None,
) -> list[ProductionOccurrence]:
    manifest_rows = parse_manifest_rows()
    manifest_by_title = {
        (row["lexical_item"], row["counterpart"], row["protoform"]): row
        for row in manifest_rows
    }
    store: dict[tuple[str, str, str, str, str, str, str], ProductionOccurrence] = {}
    for row in manifest_rows:
        ref = heading_ref(row["lexical_item"], row["counterpart"], row["derivation_class"])
        oe_display = oe_target_display(row["counterpart"], row["derivation_class"])
        add_production(store, language="oe", form=row["counterpart"], display=oe_display, form_role="target_form", source_scope="lexical_heading", source_ref=ref, origin="manifest")
        add_production(store, language=require_reconstructed_stage(row.get("protoform_stage", ""), form=row["protoform"], scope="lexical_protoform", source_ref=ref), variety=(row.get("protoform_variety") or "").strip(), form=row["protoform"], form_role="source_protoform", source_scope="lexical_protoform", source_ref=ref, origin="manifest")
        if row["proto"] and row["proto"] != row["protoform"]:
            add_production(store, language=require_reconstructed_stage(row.get("proto_stage", ""), form=row["proto"], scope="lexical_proto", source_ref=ref), form=row["proto"], form_role="source_protoform", source_scope="lexical_proto", source_ref=ref, origin="manifest")

    # Also build a lookup by (title, expected) only — used to detect obsolete compact traces
    manifest_by_title_counterpart = {
        (row["lexical_item"], row["counterpart"]): row
        for row in manifest_rows
    }

    for entry in parse_compact_entries():
        manifest_row = manifest_by_title.get((entry["title"], entry["expected"], entry["proto"]))
        if manifest_row is not None:
            ref = heading_ref(manifest_row["lexical_item"], manifest_row["counterpart"], manifest_row["derivation_class"])
            oe_display = oe_target_display(manifest_row["counterpart"], manifest_row["derivation_class"])
        else:
            # Check whether a manifest row exists for the same title+counterpart but DIFFERENT protoform.
            # If so, the compact trace uses an obsolete proto (e.g., a corrected row where the active
            # manifest protoform has been updated). Do NOT add the obsolete trace_proto_input to
            # production; quarantine it by not adding it at all.
            active_row = manifest_by_title_counterpart.get((entry["title"], entry["expected"]))
            if active_row is not None:
                # Obsolete compact trace: title/counterpart exists in manifest but proto doesn't match.
                # This trace_proto_input is stale and must not pollute the active entry's index.
                continue
            ref = heading_ref(str(entry["title"]), str(entry["expected"]))
            oe_display = str(entry["expected"])
        if entry["proto_input"]:
            if manifest_row is not None:
                # A modelled selected input carries its declared historical stage
                # (e.g. heaven *xébun -> pwgmc). Fail closed on an absent/unknown stage.
                stage = require_reconstructed_stage(
                    manifest_row.get("protoform_stage", ""),
                    form=str(entry["proto_input"]),
                    scope="trace_proto_input",
                    source_ref=ref,
                )
                variety = (manifest_row.get("protoform_variety") or "").strip()
            else:
                # Corpus selected input with no model entry. Under the CAPR
                # convention PROTO is always the Proto-Germanic reconstruction,
                # so this is legitimately pgmc ONLY when the selected input IS
                # that PROTO (modulo stress-accent / compound-hyphen encoding).
                # A genuinely different (post-PGmc) selected input with no model
                # entry and no stage decision must NOT be silently coerced to
                # pgmc — fail closed instead (protoform-stage architecture).
                proto_head = str(entry.get("proto", "")).strip()
                proto_input = str(entry["proto_input"]).strip()
                same_as_proto = bool(proto_head) and (
                    transliterate_sort_key(proto_head) == transliterate_sort_key(proto_input)
                )
                if same_as_proto or not proto_head:
                    stage = "pgmc"
                else:
                    raise SystemExit(
                        f"protoform-stage architecture: selected input {proto_input!r} "
                        f"differs from PROTO {proto_head!r} for {entry['title']!r} but has "
                        f"no model entry and no sidecar stage decision; refusing to default "
                        f"to pgmc. Add a model entry / entry_stage_metadata.tsv decision."
                    )
                variety = ""
            add_production(store, language=stage, variety=variety, form=str(entry["proto_input"]), form_role="selected_input", source_scope="trace_proto_input", source_ref=ref, origin="compact")

    for row in explicit_tag_occurrences():
        if row["language"]:
            add_production(
                store,
                language=row["language"],
                variety=(row.get("variety") or "").strip(),
                form=row["form"],
                display=row["display"],
                sort_key=row["sort_key"],
                form_role=row["form_role"],
                source_scope=row["source_scope"],
                source_ref=row["source_ref"],
                occurrence_id=row.get("occurrence_id", ""),
                origin=row["origin"],
            )

    if add_overrides is None or ignore_overrides is None:
        add_overrides, ignore_overrides = load_overrides()
    for row in add_overrides:
        add_production(
            store,
            language=row["language"],
            variety=(row.get("variety") or "").strip(),
            form=row["form"],
            display=row["display"] or row["form"],
            sort_key=row["sort_key"] or transliterate_sort_key(row["display"] or row["form"]),
            form_role="comparison_form",
            source_scope=row["source_scope"] or "override",
            source_ref=row["source_ref"] or "override",
            origin="override",
            status="override",
        )

    filtered: list[ProductionOccurrence] = []
    for entry in store.values():
        ignored = any(
            override_matches(
                override,
                form=entry.form,
                source_scope=entry.source_scope,
                source_ref=entry.source_ref,
                language=entry.language,
                variety=entry.variety,
            )
            for override in ignore_overrides
        )
        if not ignored:
            filtered.append(entry)
    if include_table_semantic:
        semantic_results = table_semantic_results or collect_table_semantic_results(filtered)
        for row in semantic_results["auto_rows"] + semantic_results.get("decision_rows", []) + list(broad_prose_decision_rows or []):
            add_production(
                store,
                language=row["language"],
                variety=(row.get("variety") or "").strip(),
                form=row["form"],
                display=row["display"],
                sort_key=row["sort_key"],
                form_role=row["form_role"],
                source_scope=row["source_scope"],
                source_ref=row["source_ref"],
                origin=row["origin"],
                status=row["status"],
            )
        filtered = []
        for entry in store.values():
            ignored = any(
                override_matches(
                    override,
                    form=entry.form,
                    source_scope=entry.source_scope,
                    source_ref=entry.source_ref,
                    language=entry.language,
                    variety=entry.variety,
                )
                for override in ignore_overrides
            )
            if not ignored:
                filtered.append(entry)
    return sorted(
        filtered,
        key=lambda entry: (
            LANGUAGE_ORDER.index(entry.language) if entry.language in LANGUAGE_ORDER else len(LANGUAGE_ORDER),
            entry.sort_key,
            entry.display,
            entry.source_ref,
            entry.source_scope,
        ),
    )


def latest_matching_print_decision(
    row: ProductionOccurrence,
    decisions: list[dict[str, str]],
) -> dict[str, str] | None:
    matched: dict[str, str] | None = None
    for decision in decisions:
        if print_decision_matches_row(decision, row):
            matched = decision
    return matched


def default_print_exclusion_reason(
    row: ProductionOccurrence,
) -> str:
    if row.source_scope.startswith("reader_failure_"):
        return "reader_facing_pedagogical_example"
    if row.form_role == "regular_output":
        return "regular_output_default_exclusion"
    return ""


def split_print_main_rows(
    production_rows: list[ProductionOccurrence],
    decisions: list[dict[str, str]] | None = None,
) -> tuple[list[ProductionOccurrence], list[dict[str, str]]]:
    print_decisions = decisions if decisions is not None else load_print_decisions()
    for decision in print_decisions:
        matches = [row for row in production_rows if print_decision_matches_row(decision, row)]
        if not matches:
            raise ValueError(f"Stale print decision matches 0 production rows: {decision}")
        if len(matches) > 1:
            refs = sorted({row.source_ref for row in matches})
            raise ValueError(
                "Ambiguous print decision matches multiple production rows "
                f"({len(matches)}): {decision} -- matched source_refs={refs[:5]}"
            )

    included: list[ProductionOccurrence] = []
    excluded: list[dict[str, str]] = []
    for row in production_rows:
        matched_decision = latest_matching_print_decision(row, print_decisions)
        decision_action = (matched_decision or {}).get("action", "")
        decision_note = (matched_decision or {}).get("note", "")
        if decision_action == "include_main":
            included.append(row)
            continue
        if decision_action == "exclude_main":
            exclusion_reason = "excluded_by_print_decision"
        elif decision_action == "defer_print":
            exclusion_reason = "deferred_by_print_decision"
        else:
            exclusion_reason = default_print_exclusion_reason(row)
        if exclusion_reason:
            excluded.append(
                {
                    "language": row.language,
                    "variety": row.variety,
                    "form": row.form,
                    "display": row.display,
                    "sort_key": row.sort_key,
                    "form_role": row.form_role,
                    "source_scope": row.source_scope,
                    "source_ref": row.source_ref,
                    "occurrence_id": row.occurrence_id,
                    "origin": "; ".join(sorted(row.origins)),
                    "status": row.status,
                    "exclusion_reason": exclusion_reason,
                    "decision_action": decision_action,
                    "decision_note": decision_note,
                }
            )
        else:
            included.append(row)
    return included, excluded


def write_print_main_rows(path: Path, rows: list[ProductionOccurrence]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=PRODUCTION_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "language": row.language,
                    "variety": row.variety,
                    "form": _normalize_iv_form(row.form),
                    "display": _normalize_iv_form(row.display),
                    "sort_key": row.sort_key,
                    "form_role": row.form_role,
                    "source_scope": row.source_scope,
                    "source_ref": row.source_ref,
                    "occurrence_id": row.occurrence_id,
                    "origin": "; ".join(sorted(row.origins)),
                    "status": row.status,
                }
            )


def write_explicit_allow_sortkey(path: Path, rows: list[ProductionOccurrence]) -> None:
    """Write a sort-key-based allowlist for the Lua filter.

    The form-based allowlist in print_main.tsv can fail Lua matching when Pandoc
    stringifies span content as NFD but the TSV stores NFC. This file keys on
    (language, form_role, sort_key, occurrence_id, variety) where sort_key is always
    plain ASCII and occurrence_id is globally unique, so normalization never matters.
    The Lua filter uses this as a secondary allowlist that bypasses the form/display
    Unicode comparison.
    """
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            delimiter="\t",
            fieldnames=["language", "form_role", "sort_key", "occurrence_id", "variety"],
            lineterminator="\n",
        )
        writer.writeheader()
        seen: set[tuple[str, str, str, str, str]] = set()
        for row in rows:
            if row.source_scope != "explicit_tag":
                continue
            occ_id = row.occurrence_id
            if not occ_id:
                raise ValueError(f"explicit_tag row missing occurrence_id: {row.source_ref}")
            key = (row.language, row.form_role, row.sort_key, occ_id, row.variety)
            if key in seen:
                continue
            seen.add(key)
            writer.writerow({
                "language": row.language,
                "form_role": row.form_role,
                "sort_key": row.sort_key,
                "occurrence_id": occ_id,
                "variety": row.variety,
            })


def write_print_excluded_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=PRINT_EXCLUDED_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in PRINT_EXCLUDED_FIELDS})


PRINT_PROSE_RULE_WORDS = {"form", "output", "expected", "stage", "rule"}
SMALL_PRINT_SAMPLE_LANGUAGES = {"pwgmc", "goth", "dutch", "german", "modeng"}


def build_print_unique_rows(rows: list[ProductionOccurrence]) -> list[dict[str, str]]:
    grouped: dict[tuple[str, str, str, str], dict[str, object]] = {}
    for row in rows:
        printed_variety = VARIETY_REGISTRY.printed_label(row.variety) if row.variety else ""
        key = (row.language, row.display, row.sort_key, printed_variety)
        bucket = grouped.setdefault(
            key,
            {
                "language": row.language,
                "display": row.display,
                "sort_key": row.sort_key,
                "printed_variety": printed_variety,
                "source_varieties": set(),
                "occurrence_count": 0,
                "roles": set(),
                "source_scopes": set(),
                "sample_sources": [],
            },
        )
        bucket["occurrence_count"] = int(bucket["occurrence_count"]) + 1
        cast_roles = bucket["roles"]
        cast_scopes = bucket["source_scopes"]
        cast_sources = bucket["sample_sources"]
        cast_varieties = bucket["source_varieties"]
        assert isinstance(cast_roles, set) and isinstance(cast_scopes, set) and isinstance(cast_sources, list)
        assert isinstance(cast_varieties, set)
        cast_roles.add(row.form_role)
        cast_scopes.add(row.source_scope)
        if row.variety:
            cast_varieties.add(row.variety)
        if row.source_ref not in cast_sources and len(cast_sources) < 5:
            cast_sources.append(row.source_ref)

    unique_rows: list[dict[str, str]] = []
    for key in sorted(
        grouped,
        key=lambda item: (
            LANGUAGE_ORDER.index(item[0]) if item[0] in LANGUAGE_ORDER else len(LANGUAGE_ORDER),
            item[2],
            item[1],
            item[3],
        ),
    ):
        bucket = grouped[key]
        roles = sorted(bucket["roles"])  # type: ignore[arg-type]
        scopes = sorted(bucket["source_scopes"])  # type: ignore[arg-type]
        sources = bucket["sample_sources"]  # type: ignore[assignment]
        varieties = sorted(bucket["source_varieties"])  # type: ignore[arg-type]
        unique_rows.append(
            {
                "language": str(bucket["language"]),
                "display": str(bucket["display"]),
                "sort_key": str(bucket["sort_key"]),
                "printed_variety": str(bucket["printed_variety"]),
                "source_varieties": "; ".join(varieties),
                "occurrence_count": str(bucket["occurrence_count"]),
                "roles": "; ".join(roles),
                "source_scopes": "; ".join(scopes),
                "sample_sources": "; ".join(sources),
            }
        )
    return unique_rows


def write_print_unique_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=PRINT_UNIQUE_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in PRINT_UNIQUE_FIELDS})


def build_print_anomaly_rows(
    print_main_rows: list[ProductionOccurrence],
    decisions: list[dict[str, str]],
) -> list[dict[str, str]]:
    explicit_regular_include_keys = {
        (
            (row.get("language") or "").strip(),
            (row.get("form") or "").strip(),
            (row.get("form_role") or "").strip(),
            (row.get("source_ref") or "").strip(),
        )
        for row in decisions
        if (row.get("action") or "").strip() == "include_main"
        and (row.get("form_role") or "").strip() == "regular_output"
    }
    letter_pattern = r"[A-Za-zÀ-ɏḀ-ỿþðæǣœȳċġǭǫáéíóúāēīōūḗḯ]"
    rows: list[dict[str, str]] = []
    for row in print_main_rows:
        flags: list[str] = []
        hard = False
        normalized_display = row.display.casefold().lstrip("*").strip("`.,;:!?()[]{}“”\"' ")
        normalized_form = row.form.casefold().lstrip("*").strip("`.,;:!?()[]{}“”\"' ")
        if ">" in row.form or ">" in row.display:
            flags.append("derivational_expression")
            hard = True
        if "~" in row.form or "~" in row.display:
            flags.append("contains_tilde")
        if "|" in row.form or "|" in row.display:
            flags.append("contains_pipe")
        if "," in row.form or "," in row.display:
            flags.append("contains_comma")
        if ("/" in row.form or "/" in row.display) and row.form_role != "comparison_form":
            flags.append("contains_slash_non_comparison")
        if " " in row.form.strip() or " " in row.display.strip():
            flags.append("contains_space")
        if re.fullmatch(letter_pattern + "{1,2}", row.form.lstrip("*")):
            flags.append("bare_short_segment")
        if re.fullmatch(r"SC\d{2,4}", row.display) or re.fullmatch(r"SC\d{2,4}", row.form):
            flags.append("rule_label_like")
            hard = True
        if normalized_display in PRINT_PROSE_RULE_WORDS or normalized_form in PRINT_PROSE_RULE_WORDS:
            flags.append("prose_or_rule_word")
            hard = True
        # preoe rows in print_main are accepted historical-stage evidence; do not flag
        if row.source_scope.startswith("reader_failure_"):
            flags.append("reader_failure_scope")
            hard = True
        if row.form_role == "regular_output":
            key = (row.language, row.form, row.form_role, row.source_ref)
            if key in explicit_regular_include_keys:
                flags.append("regular_output_explicit_include")
            else:
                flags.append("regular_output_without_explicit_include")
                hard = True
        if not row.sort_key:
            flags.append("empty_sort_key")
            hard = True
        if not row.display:
            flags.append("empty_display")
            hard = True
        if row.display.startswith("*") and row.language in {"dutch", "german", "modeng"}:
            flags.append("starred_display_non_proto_context")
        if not flags:
            continue
        rows.append(
            {
                "language": row.language,
                "variety": row.variety,
                "form": row.form,
                "display": row.display,
                "sort_key": row.sort_key,
                "form_role": row.form_role,
                "source_scope": row.source_scope,
                "source_ref": row.source_ref,
                "anomaly_flags": "; ".join(sorted(flags)),
                "hard_error": "yes" if hard else "no",
                "note": "hard-policy violation" if hard else "soft-review signal",
            }
        )
    rows.sort(key=lambda item: (item["language"], item["sort_key"], item["display"], item["source_ref"]))
    return rows


def write_print_anomaly_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=PRINT_ANOMALY_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in PRINT_ANOMALY_FIELDS})


def reason_for_preoe_inclusion(row: ProductionOccurrence) -> str:
    if row.source_scope.startswith("reader_failure_"):
        return "Reader-facing failure-pattern capture."
    if row.source_scope in {"table_semantic_auto", "table_semantic_decision"}:
        return "Table semantic production promotion."
    if row.source_scope == "broad_prose_decision":
        return "Curated broad-prose production decision."
    if row.source_scope == "explicit_tag":
        return "Explicit .iv tag in source prose."
    if row.source_scope == "override":
        return "Manual add override."
    return f"Production source scope {row.source_scope}."


def proposed_preoe_print_status(
    row: ProductionOccurrence,
    decision: dict[str, str] | None,
) -> str:
    if decision is not None:
        if decision.get("action") == "include_main":
            return "include_if_source_backed"
        if decision.get("action") == "defer_print":
            return "needs_human_review"
        return "exclude_model_internal"
    if row.source_scope.startswith("reader_failure_"):
        return "move_to_example_index"
    if row.source_scope in {"explicit_tag", "override", "broad_prose_decision"}:
        return "include_if_source_backed"
    if row.form_role in {"source_protoform", "selected_input"}:
        return "needs_human_review"
    return "exclude_model_internal"


def build_preoe_review_rows(
    production_rows: list[ProductionOccurrence],
    decisions: list[dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    print_decisions = decisions or load_print_decisions()
    review_rows: list[dict[str, str]] = []
    for row in production_rows:
        if row.language != "preoe":
            continue
        matched_decision = latest_matching_print_decision(row, print_decisions)
        review_rows.append(
            {
                "form": row.form,
                "source_ref": row.source_ref,
                "source_scope": row.source_scope,
                "form_role": row.form_role,
                "reason_for_current_inclusion": reason_for_preoe_inclusion(row),
                "proposed_print_status": proposed_preoe_print_status(row, matched_decision),
                "note": (matched_decision or {}).get("note", ""),
            }
        )
    review_rows.sort(key=lambda item: (item["source_ref"], item["form"], item["form_role"]))
    return review_rows


def write_preoe_review(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=PREOE_REVIEW_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in PREOE_REVIEW_FIELDS})


def failure_example_roles_by_ref() -> dict[tuple[str, str], tuple[str, str, str]]:
    rel = CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix()
    mapping: dict[tuple[str, str], tuple[str, str, str]] = {}
    for line_no, line in enumerate(CHRONOLOGY_PATH.read_text(encoding="utf-8").splitlines(), start=1):
        source_ref = f"{rel}:{line_no}"
        for match in iter_failure_example_matches(line):
            input_form = match["input"]
            yielded = match["yield"]
            expected = match["expected"]
            if input_form and is_failure_whole_form(input_form):
                mapping[(input_form, source_ref)] = (
                    "example_input",
                    stage_to_language(match["label"], input_form),
                    "failure-pattern selected input",
                )
            if yielded and is_failure_whole_form(yielded):
                mapping[(yielded, source_ref)] = (
                    "yielded_output",
                    "preoe" if yielded.startswith("*") else "oe",
                    "failure-pattern yielded output",
                )
            if expected and is_failure_whole_form(expected):
                mapping[(expected, source_ref)] = (
                    "expected_output",
                    "preoe" if expected.startswith("*") else "oe",
                    "failure-pattern expected output",
                )
    return mapping


READER_EXAMPLE_STOPWORDS = {
    "form",
    "output",
    "expected",
    "stage",
    "rule",
    "rules",
    "input",
    "example",
    "examples",
    "chapter",
    "left",
    "right",
}


def is_reader_whole_form(form: str) -> bool:
    lowered = form.casefold()
    if lowered in READER_EXAMPLE_STOPWORDS or lowered in PROSE_GLOSS_FORMS or lowered in FALSE_POSITIVE_FORMS:
        return False
    if form.startswith("OE") and re.search(r"[A-Z]", form[2:]):
        return False
    if notation_or_metadata_reason(form):
        return False
    if "|" in form:
        return False
    if candidate_category(form) != "needs_review":
        return False
    return True


def is_failure_whole_form(form: str) -> bool:
    lowered = form.casefold()
    if lowered in READER_EXAMPLE_STOPWORDS or lowered in PROSE_GLOSS_FORMS or lowered in FALSE_POSITIVE_FORMS:
        return False
    if notation_or_metadata_reason(form):
        return False
    if "|" in form:
        return False
    if not looks_formlike(form):
        return False
    return len(form.lstrip("*")) >= 3


def classify_reader_example_role(
    candidate: CandidateOccurrence,
    failure_roles: dict[tuple[str, str], tuple[str, str, str]],
) -> tuple[str, str, str, bool]:
    failure_key = (candidate.form, candidate.source_ref)
    if failure_key in failure_roles:
        role, language, reason = failure_roles[failure_key]
        return role, language, reason, True
    notation_reason = broad_prose_notation_reason(candidate)
    if not is_reader_whole_form(candidate.form) or notation_reason:
        return (
            "notation_or_segment",
            infer_broad_prose_language(candidate),
            notation_reason or "non-formlike fragment or segment",
            False,
        )
    semantic_text = normalize_semantic_text(candidate.line_text)
    if candidate.form.startswith("*") and has_development_chain_cues(semantic_text):
        return ("model_stage", infer_broad_prose_language(candidate), "development-chain modeled stage", True)
    if "rather than expected" in semantic_text or "instead of expected" in semantic_text or "expected" in semantic_text:
        return ("expected_output", infer_broad_prose_language(candidate), "expected outcome in explanatory prose", True)
    if "yield" in semantic_text:
        return ("yielded_output", infer_broad_prose_language(candidate), "yielded outcome in explanatory prose", True)
    if candidate.form.startswith("*") and "from " in semantic_text:
        return ("example_input", infer_broad_prose_language(candidate), "input stage in explanatory prose", True)
    return ("diagnostic_comparator", infer_broad_prose_language(candidate), "diagnostic comparison in reader-facing prose", True)


def build_reader_facing_example_rows(
    print_main_rows: list[ProductionOccurrence],
) -> list[dict[str, str]]:
    rel = CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix()
    failure_roles = failure_example_roles_by_ref()
    line_map = {
        f"{rel}:{line_no}": re.sub(r"\s+", " ", line.strip())[:160]
        for line_no, line in enumerate(CHRONOLOGY_PATH.read_text(encoding="utf-8").splitlines(), start=1)
    }
    print_pairs = {(row.language, row.form) for row in print_main_rows}
    print_forms = {row.form for row in print_main_rows}
    rows: list[dict[str, str]] = []
    seen_pairs: set[tuple[str, str]] = set()
    for candidate in broad_candidates_from_path(CHRONOLOGY_PATH):
        key = (candidate.form, candidate.source_ref)
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        role, inferred_language, reason, is_whole_form = classify_reader_example_role(candidate, failure_roles)
        if (inferred_language, candidate.form) in print_pairs or candidate.form in print_forms:
            overlap = "yes"
        else:
            overlap = "no"
        rows.append(
            {
                "source_ref": candidate.source_ref,
                "nearest_heading": candidate.heading,
                "form": candidate.form,
                "inferred_language": inferred_language,
                "example_role": role,
                "main_index_overlap": overlap,
                "include_in_example_index": "yes" if is_whole_form and role != "notation_or_segment" else "no",
                "reason": reason,
                "context": re.sub(r"\s+", " ", candidate.line_text).strip()[:160],
            }
        )
    for (form, source_ref), (role, inferred_language, reason) in sorted(failure_roles.items()):
        key = (form, source_ref)
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        line_no = 0
        if ":" in source_ref:
            _, line_part = source_ref.rsplit(":", 1)
            if line_part.isdigit():
                line_no = int(line_part)
        heading = nearest_heading_for_source_line(rel, line_no) if line_no else ""
        if (inferred_language, form) in print_pairs or form in print_forms:
            overlap = "yes"
        else:
            overlap = "no"
        rows.append(
            {
                "source_ref": source_ref,
                "nearest_heading": heading,
                "form": form,
                "inferred_language": inferred_language,
                "example_role": role,
                "main_index_overlap": overlap,
                "include_in_example_index": "yes" if is_failure_whole_form(form) else "no",
                "reason": reason,
                "context": line_map.get(source_ref, ""),
            }
        )
    rows.sort(key=lambda item: (item["source_ref"], item["form"], item["example_role"]))
    return rows


def write_reader_facing_example_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=READER_FACING_EXAMPLE_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in READER_FACING_EXAMPLE_FIELDS})


def write_print_audit(
    production_rows: list[ProductionOccurrence],
    print_main_rows: list[ProductionOccurrence],
    print_excluded_rows: list[dict[str, str]],
    preoe_review_rows: list[dict[str, str]],
    reader_example_rows: list[dict[str, str]],
    print_unique_rows: list[dict[str, str]],
    print_anomaly_rows: list[dict[str, str]],
) -> None:
    exclusion_counts = Counter(row.get("exclusion_reason", "") for row in print_excluded_rows if row.get("exclusion_reason"))
    print_counts_by_language = Counter(row.language for row in print_main_rows)
    print_unique_by_language = {
        language: len({row.display for row in print_main_rows if row.language == language})
        for language in print_counts_by_language
    }
    print_role_counts = Counter(row.form_role for row in print_main_rows)
    preoe_status_counts = Counter(row.get("proposed_print_status", "") for row in preoe_review_rows if row.get("proposed_print_status"))
    reader_role_counts = Counter(row.get("example_role", "") for row in reader_example_rows if row.get("example_role"))
    include_yes = sum(1 for row in reader_example_rows if row.get("include_in_example_index") == "yes")
    include_no = sum(1 for row in reader_example_rows if row.get("include_in_example_index") == "no")
    included_rows = [row for row in reader_example_rows if row.get("include_in_example_index") == "yes"]
    included_role_counts = Counter(row.get("example_role", "") for row in included_rows if row.get("example_role"))
    included_language_counts = Counter(row.get("inferred_language", "") for row in included_rows)
    included_overlap_counts = Counter(row.get("main_index_overlap", "") for row in included_rows)
    included_starred = sum(1 for row in included_rows if row.get("form", "").startswith("*"))
    included_unstarred = len(included_rows) - included_starred
    included_oe_starred = sum(
        1
        for row in included_rows
        if row.get("inferred_language") == "oe" and row.get("form", "").startswith("*")
    )
    included_pgmc_oe_like = sum(
        1
        for row in included_rows
        if row.get("inferred_language") == "pgmc"
        and (
            not row.get("form", "").startswith("*")
            or bool(re.search(r"[æǣȳþðċġ]", row.get("form", "").casefold()))
        )
    )
    hard_anomalies = [row for row in print_anomaly_rows if row.get("hard_error") == "yes"]

    def sample_main(title: str, entries: list[ProductionOccurrence], *, limit: int = 8) -> list[str]:
        lines = [f"## {title}", ""]
        if not entries:
            lines.extend(["_None._", ""])
            return lines
        for row in entries[:limit]:
            lines.append(
                f"- `{row.display}` ({row.language}, {row.form_role}; {row.source_scope}; {row.source_ref})"
            )
        lines.append("")
        return lines

    def sample_excluded(title: str, rows: list[dict[str, str]], *, limit: int = 8) -> list[str]:
        lines = [f"## {title}", ""]
        if not rows:
            lines.extend(["_None._", ""])
            return lines
        for row in rows[:limit]:
            lines.append(
                f"- `{row.get('display', row.get('form', ''))}` "
                f"({row.get('language', '')}, {row.get('form_role', '')}; "
                f"{row.get('exclusion_reason', '')}; {row.get('source_ref', '')})"
            )
        lines.append("")
        return lines

    def sample_unique(title: str, entries: list[dict[str, str]], *, limit: int | None = None) -> list[str]:
        lines = [f"## {title}", ""]
        if not entries:
            lines.extend(["_None._", ""])
            return lines
        rows = entries if limit is None else entries[:limit]
        lines.append("| Language | Display | Sort key | Occurrences | Roles |")
        lines.append("| --- | --- | --- | ---: | --- |")
        for row in rows:
            lines.append(
                "| "
                + " | ".join(
                    [
                        row.get("language", ""),
                        f"`{row.get('display', '')}`",
                        row.get("sort_key", ""),
                        row.get("occurrence_count", ""),
                        row.get("roles", ""),
                    ]
                )
                + " |"
            )
        lines.append("")
        return lines

    lines = [
        "# Index verborum print audit",
        "",
        f"- Internal production occurrences: {len(production_rows)}",
        f"- Internal production unique forms: {len({(row.language, row.display) for row in production_rows})}",
        f"- Printed main occurrences: {len(print_main_rows)}",
        f"- Printed main unique forms: {len({(row.language, row.display) for row in print_main_rows})}",
        f"- Printed excluded occurrences: {len(print_excluded_rows)}",
        f"- Printed excluded unique forms: {len({(row.get('language', ''), row.get('display', '')) for row in print_excluded_rows})}",
        "",
        "## Print exclusions by reason",
        "",
    ]
    if exclusion_counts:
        for reason, count in sorted(exclusion_counts.items()):
            lines.append(f"- `{reason}`: {count}")
    else:
        lines.append("_None._")
    lines.extend(["", "## Printed main-index forms by language", "", "| Language | Occurrences | Unique forms |", "| --- | ---: | ---: |"])
    for language in LANGUAGE_ORDER:
        if print_counts_by_language.get(language):
            lines.append(f"| {LANGUAGE_TITLES[language]} | {print_counts_by_language[language]} | {print_unique_by_language[language]} |")
    lines.extend(["", "## Printed main-index forms by role", "", "| Role | Occurrences |", "| --- | ---: |"])
    for role in ("target_form", "source_protoform", "selected_input", "comparison_form", "regular_output", "evidence_form"):
        if print_role_counts.get(role):
            lines.append(f"| {role} | {print_role_counts[role]} |")
    lines.extend(["", "## Internal-only rows by reason", ""])
    if exclusion_counts:
        for reason, count in sorted(exclusion_counts.items()):
            lines.append(f"- `{reason}`: {count}")
    else:
        lines.append("_None._")
    lines.extend(
        [
            "",
            "## Pre-OE review rows by proposed status",
            "",
        ]
    )
    if preoe_status_counts:
        for status, count in sorted(preoe_status_counts.items()):
            lines.append(f"- `{status}`: {count}")
    else:
        lines.append("_None._")
    lines.extend(
        [
            "",
            "## Reader-facing example rows by role",
            "",
        ]
    )
    if reader_role_counts:
        for role, count in sorted(reader_role_counts.items()):
            lines.append(f"- `{role}`: {count}")
    else:
        lines.append("_None._")
    lines.extend(
        [
            "",
            f"- Reader-facing include_in_example_index=yes: {include_yes}",
            f"- Reader-facing include_in_example_index=no: {include_no}",
            "",
        ]
    )
    lines.extend(
        [
            "## Print-unique entry audit",
            "",
            f"- Unique printed entries: {len(print_unique_rows)}",
            f"- Print anomaly rows: {len(print_anomaly_rows)}",
            f"- Hard print anomalies: {len(hard_anomalies)}",
            "",
        ]
    )
    unique_oe = [row for row in print_unique_rows if row.get("language") == "oe"]
    unique_pgmc = [row for row in print_unique_rows if row.get("language") == "pgmc"]
    unique_small_languages = [row for row in print_unique_rows if row.get("language") in SMALL_PRINT_SAMPLE_LANGUAGES]
    lines.extend(sample_unique("Unique printed entries: first 20 Old English", unique_oe, limit=20))
    lines.extend(sample_unique("Unique printed entries: first 20 Proto-Germanic", unique_pgmc, limit=20))
    lines.extend(sample_unique("Unique printed entries: small language indexes (all)", unique_small_languages, limit=None))
    lines.extend(["## Reader-facing include=yes summary buckets", ""])
    lines.append("### Included rows by role")
    lines.append("")
    if included_role_counts:
        for role, count in sorted(included_role_counts.items()):
            lines.append(f"- `{role}`: {count}")
    else:
        lines.append("_None._")
    lines.extend(["", "### Included rows by inferred language", ""])
    if included_language_counts:
        for language, count in sorted(included_language_counts.items()):
            lines.append(f"- `{language or 'unknown'}`: {count}")
    else:
        lines.append("_None._")
    lines.extend(["", "### Included rows by main-index overlap", ""])
    if included_overlap_counts:
        for overlap, count in sorted(included_overlap_counts.items()):
            lines.append(f"- `{overlap or 'unknown'}`: {count}")
    else:
        lines.append("_None._")
    lines.extend(
        [
            "",
            f"- Included whole-form rows with asterisks: {included_starred}",
            f"- Included whole-form rows without asterisks: {included_unstarred}",
            f"- Included rows inferred_language=oe with leading asterisk: {included_oe_starred}",
            f"- Included rows inferred_language=pgmc but OE-output-like form shape: {included_pgmc_oe_like}",
            "",
        ]
    )
    lines.extend(sample_main("Included main-index rows (sample)", print_main_rows))
    lines.extend(
        sample_excluded(
            "Excluded regular-output rows (sample)",
            [row for row in print_excluded_rows if row.get("form_role") == "regular_output"],
        )
    )
    lines.extend(
        sample_excluded(
            "Excluded pre-OE rows (sample)",
            [row for row in print_excluded_rows if row.get("language") == "preoe"],
        )
    )
    lines.extend(
        sample_excluded(
            "Print anomalies (sample)",
            print_anomaly_rows,
        )
    )
    lines.extend(["## Reader-facing example rows (sample)", ""])
    reader_sample = sorted(reader_example_rows, key=lambda item: (item["source_ref"], item["form"]))[:8]
    if reader_sample:
        for row in reader_sample:
            lines.append(
                f"- `{row.get('form', '')}` "
                f"({row.get('inferred_language', '')}, {row.get('example_role', '')}; "
                f"include={row.get('include_in_example_index', '')}; {row.get('source_ref', '')})"
            )
    else:
        lines.append("_None._")
    lines.append("")
    PRINT_AUDIT_PATH.write_text("\n".join(lines), encoding="utf-8")


FALSE_POSITIVE_FORMS = {
    "attestation",
    "attested_variant",
    "cell",
    "breaking",
    "citation",
    "comparator",
    "computed",
    "derivation",
    "documented",
    "development",
    "evidence",
    "family",
    "form",
    "lowering",
    "regular",
    "output",
    "row",
    "tradition",
    "type",
    "umlaut",
    "voiced",
    "weak",
    "weak-tail",
    "selected",
    "expected",
    "attested",
    "same",
    "broader",
    "inherited",
    "ritual",
}

EXACT_FRAGMENT_FORMS = {
    "awj",
    "*awj",
    "gj",
    "*gj",
    "sk",
    "*sk",
    "cc",
    "cn-",
    "-gj-",
}


def guess_unresolved_category(candidate: CandidateOccurrence) -> str:
    text = candidate.line_text
    form = candidate.form
    label_patterns = [
        (r"\bold norse\b", "likely_on"),
        (r"\bold saxon\b", "likely_os"),
        (r"\bold high german\b", "likely_ohg"),
        (r"\bold frisian\b|\bofri\b|\bofris\b|\bofris\.", "likely_ofris"),
        (r"\bgothic\b|\bgoth\.", "likely_goth"),
        (r"\bold dutch\b", "likely_odutch"),
        (r"\bmiddle dutch\b", "likely_mdutch"),
        (r"\bdutch\b", "likely_dutch"),
        (r"\bgerman\b", "likely_german"),
        (r"\blatin\b|\blat\.", "likely_lat"),
        (r"\bgreek\b|\bgk\.", "likely_greek"),
        (r"\bsanskrit\b|\bskt\.", "likely_skt"),
        (r"\bmiddle english\b", "likely_me"),
        (r"\bmodern english\b", "likely_modeng"),
        (r"\bold irish\b", "likely_oirish"),
        (r"\bpgmc\b|\bproto-germanic\b", "likely_pgmc"),
        (r"\bpwgmc\b|\bproto-west germanic\b|\bproto-west-germanic\b", "likely_pwgmc"),
        (r"\bnwgmc\b|\bproto-northwest germanic\b|\bproto-northwest-germanic\b", "likely_nwgmc"),
        (r"\bold english\b", "likely_oe"),
    ]
    lowered = text.casefold()
    for pattern, category in label_patterns:
        if re.search(pattern, lowered):
            return category
    if form in FALSE_POSITIVE_FORMS:
        return "likely_false_positive"
    if candidate.heading.startswith("### Old English evidence"):
        return "likely_oe"
    if candidate.source_path.endswith("reader_facing_local_section_20.md"):
        return "likely_preoe" if form.startswith("*") else "likely_oe"
    if form.startswith("*"):
        return "likely_pgmc"
    if any(ch in form for ch in "þðæǣœȳċġǭǫáéíóúāēīōūḗḯ"):
        return "likely_oe"
    return "likely_false_positive"


def build_audit_rows(
    production_rows: list[ProductionOccurrence],
    candidates: list[CandidateOccurrence] | None = None,
    ignore_overrides: list[dict[str, str]] | None = None,
    table_semantic_results: dict[str, list[dict[str, str]]] | None = None,
) -> dict[str, list[dict[str, str]]]:
    production_occurrences = {(row.form, row.source_ref) for row in production_rows}
    nearby_occurrences = production_line_occurrences(production_rows)
    entry_coverage_index = build_entry_coverage_index(production_rows)
    reader_facing_path = CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix()
    if ignore_overrides is None:
        _, ignore_overrides = load_overrides()
    semantic_results = table_semantic_results or collect_table_semantic_results(production_rows)
    suggest_pairs = {(row["form"], row["source_ref"]) for row in semantic_results["suggest_pairs"]}
    ignore_pairs = {(row["form"], row["source_ref"]) for row in semantic_results["ignore_pairs"]}
    notation_pairs = {(row["form"], row["source_ref"]) for row in semantic_results.get("notation", [])}
    buckets: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    source_candidates = candidates
    if source_candidates is None:
        source_candidates = []
        for path in source_files_for_audit():
            source_candidates.extend(broad_candidates_from_path(path))
            source_candidates.extend(table_candidates_from_path(path))
    for candidate in source_candidates:
        if (candidate.form, candidate.source_ref) in seen:
            continue
        seen.add((candidate.form, candidate.source_ref))
        if (candidate.form, candidate.source_ref) in production_occurrences:
            continue
        category = candidate_category(candidate.form)
        if any(override_matches(override, form=candidate.form, source_ref=candidate.source_ref) for override in ignore_overrides):
            category = "ignored_by_override"
        elif (candidate.form, candidate.source_ref) in notation_pairs:
            category = "table_semantic_notation"
        elif (candidate.form, candidate.source_ref) in ignore_pairs:
            category = "table_semantic_ignored"
        elif (candidate.form, candidate.source_ref) in suggest_pairs:
            category = "table_semantic_suggestion"
        entry = {
            "form": candidate.form,
            "source_ref": candidate.source_ref,
            "source_path": candidate.source_path,
            "heading": candidate.heading,
            "context": re.sub(r"\s+", " ", candidate.line_text).strip()[:160],
            "sort_key": transliterate_sort_key(candidate.form),
            "candidate_origin": candidate.candidate_origin,
        }
        if category not in {"ignored_by_override", "table_semantic_notation", "table_semantic_ignored", "table_semantic_suggestion"}:
            if candidate.candidate_origin == "broad_prose_candidate" and candidate.source_path == reader_facing_path:
                category = "reader_facing_policy"
            else:
                notation_reason = broad_prose_notation_reason(candidate) if candidate.candidate_origin == "broad_prose_candidate" else ""
                same_entry_reason = same_entry_coverage_reason(candidate, entry_coverage_index) if candidate.candidate_origin == "broad_prose_candidate" else ""
                orthographic_reason = orthographic_variant_reason(candidate, entry_coverage_index) if candidate.candidate_origin == "broad_prose_candidate" else ""
                prose_reason = ordinary_prose_gloss_reason(candidate) if candidate.candidate_origin == "broad_prose_candidate" else ""
                broad_suggestion = (
                    infer_broad_prose_suggestion(candidate)
                    if candidate.candidate_origin == "broad_prose_candidate" and category == "needs_review"
                    else None
                )
                if notation_reason:
                    category = "broad_prose_notation"
                    entry["reason"] = notation_reason
                elif same_entry_reason:
                    category = "same_entry_covered"
                    entry["reason"] = same_entry_reason
                elif orthographic_reason:
                    category = "orthographic_variant"
                    entry["reason"] = orthographic_reason
                elif prose_reason:
                    category = "ordinary_prose_gloss"
                    entry["reason"] = prose_reason
                elif broad_suggestion:
                    category = "broad_prose_suggestion"
                    entry.update(broad_suggestion)
                elif category == "needs_review" and is_already_indexed_nearby(candidate, nearby_occurrences):
                    category = "already_indexed_nearby"
        if category == "needs_review":
            entry["category"] = guess_unresolved_category(candidate)
        buckets[category].append(entry)
    for rows in buckets.values():
        rows.sort(key=lambda row: (row.get("sort_key", ""), row["form"], row["source_ref"]))
    return buckets


def write_forms(rows: list[ProductionOccurrence]) -> None:
    with FORMS_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=PRODUCTION_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "language": row.language,
                    "variety": row.variety,
                    "form": _normalize_iv_form(row.form),
                    "display": _normalize_iv_form(row.display),
                    "sort_key": row.sort_key,
                    "form_role": row.form_role,
                    "source_scope": row.source_scope,
                    "source_ref": row.source_ref,
                    "occurrence_id": row.occurrence_id,
                    "origin": "; ".join(sorted(row.origins)),
                    "status": row.status,
                }
            )


def unresolved_baseline_key(entry: dict[str, str]) -> tuple[str, str, str, str, str]:
    return (
        (entry.get("form") or "").strip(),
        (entry.get("source_path") or "").strip(),
        (entry.get("heading") or "").strip(),
        (entry.get("category") or "").strip(),
        (entry.get("context") or "").strip(),
    )


def load_unresolved_baseline(path: Path) -> dict[tuple[str, str, str, str, str], dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return {
            unresolved_baseline_key({key: (value or "").strip() for key, value in row.items()}): {key: (value or "").strip() for key, value in row.items()}
            for row in reader
        }


def write_unresolved_baseline(path: Path, entries: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            delimiter="\t",
            fieldnames=["form", "source_path", "source_ref", "heading", "category", "sort_key", "context", "note"],
            lineterminator="\n",
        )
        writer.writeheader()
        for entry in sorted(entries, key=lambda row: (row.get("sort_key", ""), row["form"], row["source_ref"])):
            writer.writerow(
                {
                    "form": entry["form"],
                    "source_path": entry.get("source_path", ""),
                    "source_ref": entry["source_ref"],
                    "heading": entry.get("heading", ""),
                    "category": entry.get("category", ""),
                    "sort_key": entry.get("sort_key", ""),
                    "context": entry.get("context", ""),
                    "note": "",
                }
            )


def compare_against_baseline(
    entries: list[dict[str, str]],
    baseline: dict[tuple[str, str, str, str, str], dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    current = {unresolved_baseline_key(entry): entry for entry in entries}
    new_entries = [entry for key, entry in current.items() if key not in baseline]
    resolved_entries = [baseline[key] for key in baseline if key not in current]
    new_entries.sort(key=lambda row: (row.get("sort_key", ""), row["form"], row["source_ref"]))
    resolved_entries.sort(key=lambda row: (row.get("sort_key", ""), row.get("form", ""), row.get("source_ref", "")))
    return new_entries, resolved_entries


def write_audit(
    rows: list[ProductionOccurrence],
    buckets: dict[str, list[dict[str, str]]],
    baseline: dict[tuple[str, str, str, str, str], dict[str, str]],
    table_semantic_results: dict[str, list[dict[str, str]]] | None = None,
    print_main_rows: list[ProductionOccurrence] | None = None,
    print_excluded_rows: list[dict[str, str]] | None = None,
    preoe_review_rows: list[dict[str, str]] | None = None,
    reader_example_rows: list[dict[str, str]] | None = None,
) -> int:
    counts_by_language = Counter(row.language for row in rows)
    unique_by_language = {
        language: len({row.display for row in rows if row.language == language})
        for language in counts_by_language
    }
    needs_review_entries = buckets.get("needs_review", [])
    table_needs_review_entries = [
        entry for entry in needs_review_entries
        if entry.get("candidate_origin") == "table_candidate"
    ]
    semantic_results = table_semantic_results or {"auto_rows": [], "suggestions": [], "ignored": [], "notation": []}
    print_main = print_main_rows or []
    print_excluded = print_excluded_rows or []
    preoe_review = preoe_review_rows or []
    reader_examples = reader_example_rows or []
    print_counts_by_language = Counter(row.language for row in print_main)
    print_unique_by_language = {
        language: len({row.display for row in print_main if row.language == language})
        for language in print_counts_by_language
    }
    exclusion_counts = Counter(row.get("exclusion_reason", "") for row in print_excluded if row.get("exclusion_reason"))
    required_print_reasons = (
        "regular_output_default_exclusion",
        "reader_facing_pedagogical_example",
        "deferred_by_print_decision",
        "excluded_by_print_decision",
    )
    other_print_reasons = sorted(
        reason for reason in exclusion_counts
        if reason and reason not in required_print_reasons
    )
    excluded_trace_entries = excluded_intermediate_trace_forms()
    new_entries, resolved_entries = compare_against_baseline(needs_review_entries, baseline)
    table_deferred_count = sum(1 for row in load_table_decisions() if row.get("action") == "defer")
    lines = [
        "# Index verborum audit",
        "",
        f"- Internal production occurrences: {len(rows)}",
        f"- Internal production unique forms: {len({(row.language, row.display) for row in rows})}",
        f"- Printed main-index occurrences: {len(print_main)}",
        f"- Printed main-index unique forms: {len({(row.language, row.display) for row in print_main})}",
        f"- Print-excluded occurrences: {len(print_excluded)}",
        f"- Print-excluded unique forms: {len({(row.get('language', ''), row.get('display', '')) for row in print_excluded})}",
        f"- Print exclusions (regular_output_default_exclusion): {exclusion_counts.get('regular_output_default_exclusion', 0)}",
        f"- Print exclusions (reader_facing_pedagogical_example): {exclusion_counts.get('reader_facing_pedagogical_example', 0)}",
        f"- Print exclusions (deferred_by_print_decision): {exclusion_counts.get('deferred_by_print_decision', 0)}",
        f"- Print exclusions (excluded_by_print_decision): {exclusion_counts.get('excluded_by_print_decision', 0)}",
        f"- Internal-only rows (regular_output_default_exclusion): {exclusion_counts.get('regular_output_default_exclusion', 0)}",
        f"- Internal-only rows (reader_facing_pedagogical_example): {exclusion_counts.get('reader_facing_pedagogical_example', 0)}",
        f"- Internal-only rows (deferred_by_print_decision): {exclusion_counts.get('deferred_by_print_decision', 0)}",
        f"- Internal-only rows (excluded_by_print_decision): {exclusion_counts.get('excluded_by_print_decision', 0)}",
        *[
            f"- Print exclusions ({reason}): {exclusion_counts[reason]}"
            for reason in other_print_reasons
        ],
        *[
            f"- Internal-only rows ({reason}): {exclusion_counts[reason]}"
            for reason in other_print_reasons
        ],
        f"- Pre-OE review rows: {len(preoe_review)}",
        f"- Reader-facing example candidate rows: {len(reader_examples)}",
        f"- Reader-facing rows include_in_example_index=yes: {sum(1 for row in reader_examples if row.get('include_in_example_index') == 'yes')}",
        f"- Reader-facing rows include_in_example_index=no: {sum(1 for row in reader_examples if row.get('include_in_example_index') == 'no')}",
        f"- Audit-only candidates needing review: {len(needs_review_entries)}",
        f"- True remaining unresolved: {len(needs_review_entries)}",
        f"- Table-scanned unresolved candidates: {len(table_needs_review_entries)}",
        f"- Already indexed in same entry: {len(buckets.get('same_entry_covered', []))}",
        f"- Broad-prose notation / compound expressions: {len(buckets.get('broad_prose_notation', []))}",
        f"- Broad-prose evidence suggestions: {len(buckets.get('broad_prose_suggestion', []))}",
        f"- Curated broad-prose deferred: {len(buckets.get('broad_prose_deferred', []))}",
        f"- Curated broad-prose ignored: {len(buckets.get('broad_prose_curated_ignored', []))}",
        f"- Reader-facing examples quarantined (separate example index policy): {len(buckets.get('reader_facing_policy', []))}",
        f"- Ordinary prose/gloss ignored: {len(buckets.get('ordinary_prose_gloss', []))}",
        f"- Orthographic/normalization variants: {len(buckets.get('orthographic_variant', []))}",
        f"- Table semantic auto-promoted: {len(semantic_results.get('auto_rows', []))}",
        f"- Table semantic suggestions: {len(semantic_results.get('suggestions', []))}",
        f"- Table semantic deferred decisions: {table_deferred_count}",
        f"- Table semantic ignored: {len(semantic_results.get('ignored', []))}",
        f"- Table semantic notation / compound expressions: {len(semantic_results.get('notation', []))}",
        f"- Already indexed nearby: {len(buckets.get('already_indexed_nearby', []))}",
        f"- Ignored fragments or sequences: {len(buckets.get('ignored_fragment', [])) + len(buckets.get('ignored_by_override', []))}",
        f"- Possible extraction garbage: {len(buckets.get('possible_garbage', []))}",
        f"- Excluded intermediate trace forms: {len(excluded_trace_entries)}",
        f"- New unresolved candidates relative to baseline: {len(new_entries)}",
        f"- Baseline candidates now resolved or ignored: {len(resolved_entries)}",
        "",
        "## Internal production forms by language",
        "",
        "| Language | Occurrences | Unique forms |",
        "| --- | ---: | ---: |",
    ]
    for language in LANGUAGE_ORDER:
        if counts_by_language.get(language):
            lines.append(f"| {LANGUAGE_TITLES[language]} | {counts_by_language[language]} | {unique_by_language[language]} |")
    lines.extend(["", "## Examples of internal production forms", ""])
    for language in LANGUAGE_ORDER:
        sample = [row for row in rows if row.language == language][:5]
        if not sample:
            continue
        lines.append(f"### {LANGUAGE_TITLES[language]}")
        lines.append("")
        for row in sample:
            lines.append(f"- `{row.display}` ({row.source_scope}; {row.source_ref})")
        lines.append("")

    role_counts = Counter(row.form_role for row in rows)
    lines.extend(["## Internal production forms by role", "", "| Role | Occurrences |", "| --- | ---: |"])
    for role in (
        "target_form",
        "source_protoform",
        "selected_input",
        "comparison_form",
        "regular_output",
        "evidence_form",
    ):
        if role_counts.get(role):
            lines.append(f"| {role} | {role_counts[role]} |")
    lines.append("")

    lines.extend(["## Printed main-index forms by language", "", "| Language | Occurrences | Unique forms |", "| --- | ---: | ---: |"])
    for language in LANGUAGE_ORDER:
        if print_counts_by_language.get(language):
            lines.append(f"| {LANGUAGE_TITLES[language]} | {print_counts_by_language[language]} | {print_unique_by_language[language]} |")
    lines.append("")

    print_role_counts = Counter(row.form_role for row in print_main)
    lines.extend(["## Printed main-index forms by role", "", "| Role | Occurrences |", "| --- | ---: |"])
    for role in (
        "target_form",
        "source_protoform",
        "selected_input",
        "comparison_form",
        "regular_output",
        "evidence_form",
    ):
        if print_role_counts.get(role):
            lines.append(f"| {role} | {print_role_counts[role]} |")
    lines.append("")

    lines.extend(["## Internal-only rows by reason", "", "| Reason | Occurrences |", "| --- | ---: |"])
    if exclusion_counts:
        for reason, count in sorted(exclusion_counts.items()):
            lines.append(f"| {reason} | {count} |")
    else:
        lines.append("| _none_ | 0 |")
    lines.append("")

    def render_bucket(title: str, entries: list[dict[str, str]], columns: tuple[str, ...] = ("form", "source_ref")) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not entries:
            lines.append("_None._")
            lines.append("")
            return
        label_map = {
            "form": "Form",
            "source_ref": "Source",
            "category": "Category",
            "count": "Count",
            "source_path": "Source file",
            "heading": "Nearest heading",
            "context": "Context",
            "candidate_origin": "Candidate origin",
            "suggested_language": "Suggested language",
            "suggested_role": "Suggested role",
            "reason": "Reason",
            "confidence": "Confidence",
        }
        lines.append("| " + " | ".join(label_map[col] for col in columns) + " |")
        lines.append("| " + " | ".join("---" for _ in columns) + " |")
        for entry in entries:
            parts = []
            for col in columns:
                value = entry.get(col, "")
                parts.append(f"`{value}`" if col == "form" else str(value))
            lines.append("| " + " | ".join(parts) + " |")
        lines.append("")

    guess_groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for entry in needs_review_entries:
        guess_groups[entry["category"]].append(entry)
    for group in guess_groups.values():
        group.sort(key=lambda row: (row.get("sort_key", ""), row["form"], row["source_ref"]))
    render_bucket(
        "Already indexed in same entry",
        buckets.get("same_entry_covered", []),
        columns=("form", "source_ref", "heading", "reason"),
    )
    render_bucket(
        "Broad-prose notation / compound expressions",
        buckets.get("broad_prose_notation", []),
        columns=("form", "source_ref", "reason"),
    )
    render_bucket(
        "Broad-prose evidence suggestions",
        buckets.get("broad_prose_suggestion", []),
        columns=("form", "source_ref", "suggested_language", "suggested_role", "reason"),
    )
    render_bucket(
        "Curated broad-prose deferred",
        buckets.get("broad_prose_deferred", []),
        columns=("form", "source_ref", "suggested_language", "suggested_role", "reason"),
    )
    render_bucket(
        "Curated broad-prose ignored",
        buckets.get("broad_prose_curated_ignored", []),
        columns=("form", "source_ref", "reason"),
    )
    render_bucket(
        "Reader-facing examples quarantined (separate example index policy)",
        buckets.get("reader_facing_policy", []),
        columns=("form", "source_ref", "heading", "context"),
    )
    render_bucket(
        "Ordinary prose/gloss ignored",
        buckets.get("ordinary_prose_gloss", []),
        columns=("form", "source_ref", "reason"),
    )
    render_bucket(
        "Orthographic/normalization variant of indexed form",
        buckets.get("orthographic_variant", []),
        columns=("form", "source_ref", "reason"),
    )
    likely_columns = ("form", "source_ref", "candidate_origin")
    render_bucket("Likely Old English forms", guess_groups.get("likely_oe", []), columns=likely_columns)
    render_bucket("Likely Proto-Germanic forms", guess_groups.get("likely_pgmc", []), columns=likely_columns)
    render_bucket("Likely Proto-West Germanic forms", guess_groups.get("likely_pwgmc", []), columns=likely_columns)
    render_bucket("Likely Proto-Northwest Germanic forms", guess_groups.get("likely_nwgmc", []), columns=likely_columns)
    render_bucket("Likely pre-Old-English or model-internal forms", guess_groups.get("likely_preoe", []), columns=likely_columns)
    render_bucket("Likely Old Norse forms", guess_groups.get("likely_on", []), columns=likely_columns)
    render_bucket("Likely Old Saxon forms", guess_groups.get("likely_os", []), columns=likely_columns)
    render_bucket("Likely Old High German forms", guess_groups.get("likely_ohg", []), columns=likely_columns)
    render_bucket("Likely Old Frisian forms", guess_groups.get("likely_ofris", []), columns=likely_columns)
    render_bucket("Likely Gothic forms", guess_groups.get("likely_goth", []), columns=likely_columns)
    render_bucket("Likely Old Dutch forms", guess_groups.get("likely_odutch", []), columns=likely_columns)
    render_bucket("Likely Middle Dutch forms", guess_groups.get("likely_mdutch", []), columns=likely_columns)
    render_bucket("Likely Dutch forms", guess_groups.get("likely_dutch", []), columns=likely_columns)
    render_bucket("Likely German forms", guess_groups.get("likely_german", []), columns=likely_columns)
    render_bucket("Likely Latin forms", guess_groups.get("likely_lat", []), columns=likely_columns)
    render_bucket("Likely Greek forms", guess_groups.get("likely_greek", []), columns=likely_columns)
    render_bucket("Likely Sanskrit forms", guess_groups.get("likely_skt", []), columns=likely_columns)
    render_bucket("Likely Middle English forms", guess_groups.get("likely_me", []), columns=likely_columns)
    render_bucket("Likely Modern English linguistic forms", guess_groups.get("likely_modeng", []), columns=likely_columns)
    render_bucket("Likely Old Irish forms", guess_groups.get("likely_oirish", []), columns=likely_columns)
    render_bucket("Likely ordinary-language false positives", guess_groups.get("likely_false_positive", []), columns=likely_columns)
    render_bucket(
        "Table-scanned unresolved candidates",
        [entry for entry in needs_review_entries if entry.get("candidate_origin") == "table_candidate"],
        columns=("form", "source_ref", "heading", "context"),
    )
    render_bucket(
        "Table semantic suggestions",
        semantic_results.get("suggestions", []),
        columns=("form", "source_ref", "suggested_language", "suggested_role", "reason"),
    )
    render_bucket(
        "Table semantic ignored",
        semantic_results.get("ignored", []),
        columns=("form", "source_ref", "reason"),
    )
    render_bucket(
        "Table semantic notation / compound expressions",
        semantic_results.get("notation", []),
        columns=("form", "source_ref", "reason"),
    )
    render_bucket("Already indexed nearby", buckets.get("already_indexed_nearby", []), columns=("form", "source_ref", "heading", "candidate_origin"))
    render_bucket("Ignored fragments or sequences", buckets.get("ignored_fragment", []))
    render_bucket("Ignored by override", buckets.get("ignored_by_override", []))
    render_bucket("Possible extraction garbage", buckets.get("possible_garbage", []))
    render_bucket("Excluded intermediate trace forms", excluded_trace_entries[:50], columns=("form", "source_ref", "heading"))

    top_forms = Counter(entry["form"] for entry in needs_review_entries)
    render_bucket(
        "Top repeated unresolved forms",
        [{"form": form, "count": count} for form, count in top_forms.most_common(20)],
        columns=("form", "count"),
    )
    by_source = Counter(entry["source_path"] for entry in needs_review_entries)
    render_bucket(
        "Unresolved forms by source file",
        [{"source_path": source, "count": count} for source, count in by_source.most_common(20)],
        columns=("source_path", "count"),
    )
    table_by_source = Counter(
        entry["source_path"]
        for entry in needs_review_entries
        if entry.get("candidate_origin") == "table_candidate"
    )
    render_bucket(
        "Top unresolved table files",
        [{"source_path": source, "count": count} for source, count in table_by_source.most_common(20)],
        columns=("source_path", "count"),
    )
    render_bucket("New unresolved candidates relative to baseline", new_entries, columns=("form", "source_ref", "category", "heading"))
    render_bucket("Resolved or ignored baseline candidates", resolved_entries, columns=("form", "source_ref", "category", "heading"))
    AUDIT_PATH.write_text("\n".join(lines), encoding="utf-8")
    unresolved = len(needs_review_entries)
    if unresolved:
        print(f"Warning: unresolved index candidates = {unresolved}; see {AUDIT_PATH}")
    return unresolved


def ensure_override_file() -> None:
    if OVERRIDES_PATH.exists():
        return
    with OVERRIDES_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=OVERRIDE_FIELDS, lineterminator="\n")
        writer.writeheader()


def ensure_table_decisions_file() -> None:
    if TABLE_DECISIONS_PATH.exists():
        return
    with TABLE_DECISIONS_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=TABLE_DECISION_FIELDS, lineterminator="\n")
        writer.writeheader()


def ensure_broad_prose_decisions_file() -> None:
    if BROAD_PROSE_DECISIONS_PATH.exists():
        return
    with BROAD_PROSE_DECISIONS_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=BROAD_PROSE_DECISION_FIELDS, lineterminator="\n")
        writer.writeheader()


def ensure_print_decisions_file() -> None:
    if PRINT_DECISIONS_PATH.exists():
        return
    with PRINT_DECISIONS_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=PRINT_DECISION_FIELDS, lineterminator="\n")
        writer.writeheader()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="Alias for --strict-mode=all.")
    parser.add_argument(
        "--strict-mode",
        choices=("off", "baseline", "all"),
        default="off",
        help="Strictness policy for unresolved audit candidates.",
    )
    parser.add_argument(
        "--baseline",
        type=Path,
        default=UNRESOLVED_BASELINE_PATH,
        help="Baseline TSV used by --strict-mode=baseline.",
    )
    parser.add_argument(
        "--write-unresolved-baseline",
        action="store_true",
        help="Rewrite the unresolved-candidate baseline from the current needs_review set.",
    )
    args = parser.parse_args()
    run_sort_key_assertions()
    BOOK_DIR.mkdir(parents=True, exist_ok=True)
    ensure_override_file()
    ensure_table_decisions_file()
    ensure_broad_prose_decisions_file()
    ensure_print_decisions_file()
    rewrite_readme_language_block()
    base_rows = build_production_rows(include_table_semantic=False)
    table_semantic_results = collect_table_semantic_results(base_rows)
    write_table_suggestions(TABLE_SUGGESTIONS_PATH, table_semantic_results["suggestions"])
    initial_production_rows = build_production_rows(table_semantic_results=table_semantic_results)
    initial_audit_buckets = build_audit_rows(initial_production_rows, table_semantic_results=table_semantic_results)
    _, broad_prose_decision_rows = apply_broad_prose_decisions(initial_audit_buckets)
    production_rows = build_production_rows(
        table_semantic_results=table_semantic_results,
        broad_prose_decision_rows=broad_prose_decision_rows,
    )
    print_decisions = load_print_decisions()
    print_main_rows, print_excluded_rows = split_print_main_rows(production_rows, print_decisions)
    print_unique_rows = build_print_unique_rows(print_main_rows)
    print_anomaly_rows = build_print_anomaly_rows(print_main_rows, print_decisions)
    preoe_review_rows = build_preoe_review_rows(production_rows, print_decisions)
    reader_facing_example_rows = build_reader_facing_example_rows(print_main_rows)
    write_index_registry_header(print_main_rows)
    write_forms(production_rows)
    write_print_main_rows(PRINT_MAIN_PATH, print_main_rows)
    write_print_excluded_rows(PRINT_EXCLUDED_PATH, print_excluded_rows)
    write_emission_views()
    write_print_unique_rows(PRINT_UNIQUE_PATH, print_unique_rows)
    write_print_anomaly_rows(PRINT_ANOMALIES_PATH, print_anomaly_rows)
    write_preoe_review(PREOE_REVIEW_PATH, preoe_review_rows)
    write_reader_facing_example_rows(READER_FACING_EXAMPLES_PATH, reader_facing_example_rows)
    write_print_audit(
        production_rows,
        print_main_rows,
        print_excluded_rows,
        preoe_review_rows,
        reader_facing_example_rows,
        print_unique_rows,
        print_anomaly_rows,
    )
    audit_buckets = build_audit_rows(production_rows, table_semantic_results=table_semantic_results)
    audit_buckets, _ = apply_broad_prose_decisions(audit_buckets)
    write_broad_prose_suggestions(BROAD_PROSE_SUGGESTIONS_PATH, audit_buckets.get("broad_prose_suggestion", []))
    baseline = load_unresolved_baseline(args.baseline.expanduser().resolve())
    needs_review_entries = audit_buckets.get("needs_review", [])
    if args.write_unresolved_baseline:
        write_unresolved_baseline(args.baseline.expanduser().resolve(), needs_review_entries)
        baseline = load_unresolved_baseline(args.baseline.expanduser().resolve())
    unresolved = write_audit(
        production_rows,
        audit_buckets,
        baseline,
        table_semantic_results=table_semantic_results,
        print_main_rows=print_main_rows,
        print_excluded_rows=print_excluded_rows,
        preoe_review_rows=preoe_review_rows,
        reader_example_rows=reader_facing_example_rows,
    )
    strict_mode = "all" if args.strict else args.strict_mode
    if strict_mode == "all":
        raise SystemExit(1 if unresolved else 0)
    if strict_mode == "baseline":
        new_entries, _ = compare_against_baseline(needs_review_entries, baseline)
        raise SystemExit(1 if new_entries else 0)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
