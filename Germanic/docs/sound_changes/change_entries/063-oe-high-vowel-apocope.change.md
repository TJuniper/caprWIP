CHANGE_ID: SC063
CURRENT_ORDER: 63
ENTRY_TYPE: historical_sound_change
INCLUDE_IN_VOLUME: yes
HISTORICAL_STAGE: Old English
PIPELINE_STAGE: Old English
CANONICAL_CHANGE_ID: SC063
RULE_SOURCE: Germanic/fsts/germanic.txt (define OEHighVowelApocope, line 2874)
TRACE_OCCURRENCE_COUNT: 65
STATUS: pilot_complete

# OE High Vowel Apocope

## Rule

FOMA_RULE: OEHighVowelApocope
RULE_SUMMARY: deletes final high vowels in heavy disyllabic and trisyllabic environments, with order-sensitive exceptions and extensions

## Literature dossier

DOSSIER: literature_dossiers/063-oe-high-vowel-apocope.dossier.md
LITERATURE_STATUS: pilot_complete
MATRIX_ROWS: 10
KEY_SOURCES: Luick1914; Campbell1959; HoggPhonology1992; RingeTaylor2014; Fulk2018

## Conditioning

CORE: final i/u loss after heavy syllables and in the key trisyllabic environments; close interaction with earlier syncope and a few morphologically conditioned retentions

## Current position in the stack

BOOK_ENTRY: BE062
TRACE_EXAMPLES: beaver; beech; belly; bier; birth

## Order-sensitivity tests

STATUS: not_started
HIGH_VALUE_NEIGHBORS: medial syncope; weak-tail reduction; j-loss after heavy syllables

## Lexical diagnostics

COMPACT_TRACE: see beaver, belly, bier, birth, flood, hand, hearth, harvest slices in oe_derivation_class_trace_report.compact.md

## Assessment

ASSESSMENT: pilot_complete; the literature strongly supports the current weight-sensitive rule, but the trisyllabic and exceptional retention cases are high-value order-sensitivity targets

## Open questions

OPEN_QUESTIONS: how far the live final-x and hiatus clauses should be foregrounded in prose; which trisyllabic retention cases deserve explicit order-sensitivity fixtures
