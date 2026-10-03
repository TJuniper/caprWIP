# SC043: ordinary English stressed fronting

Current authority is the adopted component decision in section 12 and
`audits/sc043-adjudication.md`. Sections 1-10 preserve the earlier pilot
scaffold; their names, positions and whole-bundle chronology are historical,
not current specifications. Section 11 preserves the pre-split census and
research proposal; its former no-adoption boundary is superseded.

## 1. Role in the book

SC043 is a strong pilot case for the sound-change half of the book because all of the main dossier layers already exist in usable form. It has a substantial literature dossier, a pilot change-entry scaffold, a compact and historically interpretable chronology card, and a short FOMA definition whose consequences are easy to narrate through familiar examples such as `day`, `beard`, and `bake`.

It is also a good pilot because it shows what the sound-change half of the book should do well: not merely name a rule, but explain how a formally implemented change sits inside a larger cascade in which later rules can both depend on it and partly hide it. Anglo-Frisian Brightening is therefore a good test of whether a mini-chapter can move cleanly from handbook phonology to formal implementation to local chronology without letting the graph/export layer become the main object.

## 2. Name and basic formulation

- **change_id:** `SC043`
- **display_name:** `Anglo Frisian Brightening`
- **rule_name:** `AngloFrisianBrightening`
- **current_order:** `43`
- **card:** `Germanic/docs/sound_changes/order_tests/chronology_cards/SC043-anglo-frisian-brightening.md`

Short formulation: SC043 fronts low Germanic `a` to fronted `æ`-type outputs outside nasal environments, with a special long-final clause for the surviving bimoric `*-ō > *-ā` pathway. In the live EnglishProtoToOE cascade, this fronting creates the input that later rules such as OE Breaking and OE A Restoration either exploit or partially reverse.

## 3. Traditional description and literature

The literature dossier confirms that the standard handbook picture is stable. Campbell gives the classical statement: **"By a very early change Prim. Gmc. a > æ in OE and OFris. when not followed by a nasal consonant."** Hogg gives the most familiar modern label pair and formulation: **"This vowel normally fronted to /ae/ by the sound change of Anglo-Frisian Brightening (or First Fronting)."** Ringe and Taylor sharpen the relative chronology by stating that retraction must be later than both fronting and breaking, while Fulk gives a compact bridge from brightening to later breaking and retraction patterns.

What is standard in the literature is therefore clear:

1. low `a` fronts outside nasal environments;
2. the change is early;
3. OE Breaking presupposes that fronted input;
4. later restoration/retraction is later than the fronting event.

What remains uncertain or disputed is not the local rule itself so much as its wider historical framing. The dossier notes Campbell's caution that English and Frisian may not simply reflect one undifferentiated shared event, and Ringe and Taylor leave open whether the wider spread of fronted outcomes happened mainly on the continent or in Britain. There is also a presentational question about how prominently to foreground the unstressed-vowel side of the change in book prose.

What CAPR adds is not a new historical claim but a tighter formal and chronological articulation. The repository formalization makes explicit:

1. an unstressed clause;
2. a stressed clause;
3. a long-final clause linked to the surviving-bimoric `ō` pathway;
4. a locally testable order relation to SC042, SC044, and SC046.

That combination turns a familiar handbook change into a mini-chapter that can show how formal implementation, chronology testing, and literary exposition fit together.

## 4. Formal implementation

The relevant FOMA material in `Germanic/fsts/germanic.txt` is short enough to quote directly:

```foma
define AngloFrisianBrighteningUnstressed [
    {*a} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
define AngloFrisianBrighteningStressed [
    {*á} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal | .#.]
];
define AngloFrisianBrighteningLongFinal [
    {*ā} -> {*ǣ} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
define AngloFrisianBrightening [
    AngloFrisianBrighteningUnstressed .o.
    AngloFrisianBrighteningStressed .o.
    AngloFrisianBrighteningLongFinal
];
```

This is mostly a straightforward formalization of the handbook rule, but two caveats matter.

First, the **unstressed clause** is more model-explicit than many short textbook descriptions, though the literature dossier notes that Hogg gives support for extending first fronting into the unstressed system. Second, the **long-final clause** is best read as a formal approximation used to preserve a historically motivated chain across SC042 and later unstressed-long-vowel shortening. In other words, the rule is historically serious, but the exact shape of the FOMA definition is tuned to how this cascade represents intermediate states rather than to a single line in any one handbook.

**Long-final clause narrowing (corpus-maturation pass 01).** The clause was introduced solely for the surviving-bimoric pathway — unstressed final `*-ā` (from `*-ō`) in polysyllables [@RingeTaylor2014, §3.1 pp. 58–59; §6.8.3 pp. 299–300] — but its original context `_ .#.` was broader than that intent and wrongly captured the long `ā` of stressed monosyllables created by SC097 monosyllabic final `*-z` loss. The decisive case is OE *hwā* 'who': Ringe & Taylor derive "PGmc *hwaz > PWGmc *hwaz > OE, OF hwā" with the back vowel intact [@RingeTaylor2014, p. 86]; Campbell states flatly that "the form with West Gmc. lengthening (OE *hwǣ) does not exist" [@Campbell1959, §125, p. 49]; Brunner concurs that no `æ`/`ē` forms occur beside *hwā* [@SieversBrunner1965, §137 Anm. 1, p. 129]. The clause now requires a preceding nucleus (the same "preceded by another nucleus" guard used by `PWGmcSurvivingBimoricOUnrounding`), restricting it to exactly the polysyllabic surviving-bimoric class the sources describe. Validated: all 380 legacy corpus outputs unchanged; `*xwáz` now yields *hwā*. See `audits/corpus-maturation-01-candidate-adjudication.md` §1.

## 5. Place in the cascade

In `EnglishProtoToOE`, SC043 sits inside a very tight local cluster:

```foma
.o. PWGmcFinalBareALoss
.o. PWGmcSurvivingBimoricOUnrounding
.o. AngloFrisianBrightening
.o. OEBreaking
.o. OEVelarFricativePalatalization
.o. OEARestoration
```

For book purposes, the important point is that Anglo-Frisian Brightening is not an isolated vowel shift. It is a **pivot**:

1. SC042 feeds it on the left in the surviving-bimoric `ō` pathway;
2. SC044 depends on it immediately on the right;
3. SC046 later undoes part of its work in back-vowel environments;
4. the export layer also shows a contextual earlier-side support row from `SC035 -> SC043`.

The current graph/export layer records these neighboring relations:

1. **core:** `SC042 < SC043` (reciprocal support)
2. **core:** `SC043 < SC044` (reciprocal support)
3. **core:** `SC043 < SC046`
4. **core:** `SC034 < SC043`
5. **contextual:** `SC035 < SC043`

That makes SC043 especially useful as a pilot mini-chapter: it is locally well anchored, but it also has enough forward and backward links to demonstrate how one rule can organize a small section of the cascade.

## 6. Order-testing evidence

The chronology card gives a **safe computational window of `43-43`**. In other words, the rule is tightly fixed at its current point.

- **earlier boundary:** `SC042` PWGmc Surviving Bimoric O Unrounding
- **representative failure:** `rest`
- **later boundary:** `SC044` OE Breaking
- **representative failure:** `slay`

The evidence is best described as **local and reciprocal**, with an additional contextual earlier-side support row from SC035. The earlier boundary is historically interpretable because the `rest` derivation only reaches the attested fronted/restored output when the SC042 pathway has already produced the right input. The later boundary is equally interpretable because breaking must operate on the fronted vowel created by SC043; if SC043 is delayed, `*sláxaną` yields `sleaan | slēaan` instead of `slēan`.

What this evidence **does** show is that the live cascade has a robust local dependency:

1. SC043 must follow SC042;
2. SC043 must precede SC044;
3. SC043 must also precede SC046 in the wider local neighborhood.

What it **does not** prove by itself is the full historical interpretation of Anglo-Frisian subgrouping or the entire prehistoric chronology of fronting, breaking, and restoration. The order-testing layer records transducer failure behavior. It is strongest when it confirms local dependencies already expected from the literature, which is exactly what happens here.

## 7. Interpretation for the book

For the book, SC043 should be treated as an early fronting rule whose importance lies not only in its own outputs but also in the way later OE developments repeatedly presuppose and then partly obscure it. That is the core narrative value of the chapter.

The prose should therefore present Anglo-Frisian Brightening as an **enabling change**: it creates the front-vowel stage on which breaking operates and from which later restoration retreats in specific environments. In literary terms, this is not a chapter about a single visible surface reflex; it is a chapter about a stage that is often recoverable only because later rules still betray its prior existence.

## 8. Relation to neighbouring changes

1. **SC042 PWGmc Surviving Bimoric O Unrounding:** immediate left-hand reciprocal partner; important for `rest` and for the long-final clause in the implementation.
2. **SC044 OE Breaking:** immediate right-hand reciprocal partner; brightening must feed breaking.
3. **SC046 OE A Restoration:** later rule that reverses part of SC043's effect before back-vowel environments; crucial for forms like `bake` and `fare`.
4. **SC034 OE Aw Long Diphthong:** earlier core neighbor in the export layer, useful as a wider local anchor.
5. **SC035 OE Prefix A Reduction Early:** contextual earlier-side support only; worth noting, but not a core local adjacency claim.

These links show why SC043 is better treated as a **cluster-organizing** chapter than as a rule described in isolation.

## 9. Remaining uncertainty

1. The chapter still needs a human decision on whether to foreground **Anglo-Frisian Brightening** or **First Fronting** as the primary heading term.
2. The unstressed clause in the FOMA rule is defensible, but the final book prose should decide how prominently to feature it.
3. The wider historical question of English-Frisian subgrouping should be handled carefully; the local chronology is strong, but the broader historiography remains more cautious.
4. Final publication-quality quotations should still be checked against page images where appropriate, even though the current dossier is already strong enough for prose drafting.
5. The eventual volume will need a stylistic decision about how tightly to bind SC043 to the later chapters on Breaking and A Restoration.

## 10. Proposed book-section outline

1. **Anglo-Frisian Brightening / First Fronting**
2. **The basic change: `a > æ` outside nasal environments**
3. **How later OE rules mask the fronted stage**
4. **Formal implementation in CAPR**
5. **Why SC042 must precede it**
6. **Why SC044 must follow it**
7. **Restoration and the partial retreat from brightening**
8. **What the local chronology shows, and what it does not show**
9. **Open historiographical cautions**

## 11. F component packet: three domains, three decision boundaries

Post-SC004 continuation: the distinct coordinated a/au variant has executed
all 387 selected rows without changing finals. Exactly twenty au paths
are delayed and converge before breaking. The noncanonical
`audits/sc043-ordinary-fronting-proposal.md` recommends component-specific
ordinary-English placement while retaining the current serialization;
it does not adopt a whole-bundle SC043 restaging. Earlier census/source
assessments below remain supporting research, not new verdicts.

### Identity and question

SOURCE-only research packet, 2026-10-03, base `67a18cfb`, branch
`update`. No canonical adjudication or adoption is
made here. The literal incumbent identifier is **EAFBrightening**, not
the older `AngloFrisianBrightening` spelling quoted in the scaffold above.
The Anglo-Frisian synthesis §8.4 remains the comparative authority.

Question: does one English stressed short-a/au episode justify placing all
three SC043 clauses together? Confirmation would require independently
matching source domains and chronology for the unstressed and long-final
members. Different quantity/input histories or absent exact conditioners
refute the whole-bundle inference. English episode identity and inherited
common-stem identity must be tested separately.

### Current state and literal component inventory

The actual registry characterization is `eaf`, `anglo_frisian`,
unadjudicated, despite its pipeline/historical display labels saying Old
English. The earlier packet's `oe`, `english_specific` description was
incorrect. The staged interpretation is an object of research, not
silently adopted metadata. The post-SC004 coordinated experiment uses
the distinct `oe_post_ai_fronting_recipes.json` baseline.
Executable composition is unstressed, stressed, then long-final:

| Component | Literal incumbent rewrite/condition | Source-backed target and disposition |
|---|---|---|
| F-short-stressed | `{*á} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal \| .#.]` | Ordinary nonnasal short fronting; working English episode shared with au treatment, not automatically common-stem. **RETAIN control / DEFER placement or identity edit**. |
| F-short-unstressed | `{*a} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal]` | Unaccented a fronting, with a tautosyllabic-nasal exception and a distinct heterosyllabic-nasal history. **RETAIN control / DEFER exact syllabic/stress decomposition and dating**. |
| F-long-final | `{*ā} -> {*ǣ} || EnglishStarVocalic [EnglishStarConsonant \| EnglishPalatalConsonant]+ _ .#.` | Surviving bimoric final-vowel path in polysyllables, not ordinary short-a fronting. **RETAIN nucleus guard and incumbent control / DEFER event identity or reassignment**. |

The first two networks remain separately composed: parallel replacement
context-union is a known implementation hazard. `EnglishStarNasal` is m/n.
The unstressed member excludes final bare a; earlier PWGmc loss means it is
not an extant generic input at this point. The long-final preceding-nucleus
guard is not optional and must not be dropped to simplify a research recipe.

### Diagnosis: complete live census and witness roles

`SC043 --evidence`, serialized on 2026-10-03 after verifying backend health,
`/usr/app/fsts`, foma and flookup, reports **90/387** changed selected rows.
The literal token replacements partition those observations into **80
stressed-short**, **12 unstressed-short**, **1 long-final** row applications.
These overlap: berry1946 and water2274 change both short members;
rest2152 changes stressed-short and long-final. Thus 93 member applications
are not 93 distinct corpus rows.

Complete stressed-short firing population:

```text
1934 bake; 1938 bast; 1939 bath; 1940 beard; 1945 belly; 1946 berry;
1975 calf; 1981 craft; 1984 dale; 1985 day; 2002 fall; 2003 fare;
2004 fast; 2005 father; 2008 fern; 2016 flask; 2017 flax; 2025 fold;
2037 gall; 2045 grass; 2046 grave; 2049 guest; 2050 hail; 2052 hall;
2056 harm; 2057 harvest; 2058 have; 2059 haw; 2060 hawk; 2062 hazel;
2069 hedge; 2077 hold; 2088 lade; 2090 lap; 2092 laugh; 2117 make;
2118 malt; 2120 march; 2121 mast; 2125 might; 2130 nail; 2132 nave;
2133 navel; 2138 net; 2139 nettle; 2140 night; 2141 nightmare;
2149 raven; 2152 rest; 2165 sake; 2166 salt; 2167 salve; 2168 sap;
2173 set; 2175 shaft; 2195 slay; 2204 spar; 2205 spare; 2212 staff;
2216 stem; 2226 stretch; 2234 swallow; 2240 tap; 2245 thatch;
2266 wade; 2267 wain; 2268 wake; 2269 warp; 2271 wart; 2272 wash;
2273 wasp; 2274 water; 2275 wax (noun); 2276 wax (verb); 2284 whale;
2289 wield; 2297 wold; 2305 yarn; 2309 make (iptv.2sg); 2310 make (3sg).
```

Complete unstressed-short population:

```text
1936 ban; 1946 berry; 1965 brand; 2029 four; 2053 hammer; 2079 honey;
2119 man; 2230 summer; 2235 swan; 2250 thistle; 2274 water; 2296 withy.
```

Complete long-final population: **2152 rest**.

All ninety changed rows also belong to legacy-380; its member counts
are likewise 80/12/1, with the same overlap.

All are live applications of their literal clause. The census does not
show that every surviving a was historically eligible at one event:
the unstressed clause blocks all m/n contexts while later SC048 and
unstressed-fronting machinery handle parts of the syllabic distinction.
This representation interface is unresolved, not a newly diagnosed
out-of-domain historical repair. The long-final witness is a narrow
corpus-visible proxy, not the full historical unstressed system.

| Stable control | Observed pre/post or prerequisite | Evidential role |
|---|---|---|
| day1985 | `*dág > *dæg` | Live stressed fronting; final dotted spelling is not a merger chronology. |
| land2089 | a before n is outside the stressed rule | Negative nasal control; not an application witness. |
| hammer2053 | `*xámaras > *xámæræs` | Internal unstressed applications; stressed root is blocked by m. |
| rest2152 | `*rástā > *ræstǣ` | Live short and long changes; SC042 feeds the final component. |
| who2322 | Stressed monosyllabic ā must not match the long-final guard | Protected out-of-domain negative, never a repair target. |
| fare2003 | `*fáraną > *færaną`, later restoration | Live fronting/restoration, but final equivalence cannot decide restored versus never-fronted histories. |

### Literature and historical analysis

Campbell links ordinary short fronting and au-first-element fronting;
Nielsen describes their traditional contemporaneity; Luick's account
contains a separate earlier offglide premise
[@Campbell1939, p. 91; @Nielsen2001, pp. 514–515;
@Luick1914, pp. 130–133, §§119–120]. Conditional daughter-English
ai contraction before fronting excludes the identified ordinary event
from the common stem; the premise does not establish the dates of
the other clauses. Rival common-au and restricted-fronting histories
remain comparative alternatives [@Goblirsch1991, pp. 17, 20–21;
@Kortlandt2008, pp. 267–268; @Repansek2012, p. 82].

For unstressed a, Campbell states normal fronting except before nasals
and explicitly separates heterosyllabic nasals
[@Campbell1959, pp. 140–141, §§333–334]. That supports a historical
unstressed fronting, not CAPR's context-free assignment of the entire
syllabic history to the stressed event. Earlier bare-a loss is independently
described [@RingeTaylor2014, pp. 45–46].

For long-final material, the surviving-bimoric path and later shortening
have direct support [@RingeTaylor2014, pp. 58–59, 299–300].
The who negative is source-backed: *hwā*, not *hwǣ*
[@RingeTaylor2014, p. 86; @Campbell1959, p. 49, §125;
@SieversBrunner1965, p. 129, §137 Anm. 1].
Encoding retained quantity as ā then ǣ is a CAPR proxy for that path.
The short-a/au identity evidence cannot date it.

Chronology classification: SC042 < F-long-final is a model-local feeding
interface; ordinary fronting < conventional breaking/restoration is the
working historical reconstruction. No new edge is promoted here. The
old total “43–43 window” above describes displacement behavior, not
independent historical dating for all three components.

### Recommendations, propagation boundary and residue

Exact production diff: **none**. Retain all incumbent clauses as controls.
Defer the three production decisions separately: stressed English event
identity/placement; unstressed syllabic conditioner and layer; long-final
event identity/placement. None inherits approval from another.

Prerequisite checklist:

1. Identity/full-corpus assay on 387 stable rows, preserving the seven
   existing mismatches and all 380 legacy outputs unless an exact change
   is separately approved.
2. Paired day1985/land2089; bread1966/stone2220; fare2003/day1985;
   actual original-front inputs versus mutation-created fronts.
3. Unstressed hammer2053/thistle2250 positives; before-nasal and final
   bare-a negatives; heterosyllabic -anaz versus coda -an controls with
   source-verified cell/input stage. Check SC047/048 and later fronting
   interfaces rather than inventing a grammatical exception.
4. Rest2152 positive at both SC042 and final fronting; who2322
   negative; preserve the required preceding nucleus and downstream
   quantity shortening. Source-only fixtures for other final quantities
   require input/readiness verification, not corpus admission.

At that research stage no production change was approved. The subsequent
approved component adoption is recorded below.
Unresolved conditions are localized: stressed inherited identity depends
on the ai premise; exact unstressed syllabification and historical layering
remain unspecified; the long-final proxy must remain quantity/domain
distinct even if the English short-a/au episode is later adopted.

## 12. Adopted component identity

SC043 now names only ordinary stressed fronting:
`EAFBrightening = [ EAFBrighteningStressed ]`.
The literal three bodies and their execution order are unchanged; the
unstressed and final helpers are independently visible as support stages
SC107 and SC108. They have no invented historical stage, scope, confidence
or verdict. Current evidence counts refer to each component separately;
the 90-row and 80/12/1 partition above is the pre-split composite census.

The completed ordinary component is characterized as
`preoe/english_specific`, REFORMULATE/SPLIT. Campbell 1939 pp.90-91 and
Campbell 1959 pp.52-53 support the conventional completed-contraction
before ordinary-fronting account. Fulk 2018 p.73 connects ordinary a/au
fronting but qualifies the earlier ai nucleus; Ringe-Taylor 2014
pp.170-175 explicitly rejects a necessary plain-vowel/diphthong-nucleus
identity. Thus this is a reasoned daughter working account, not unanimous
dating or rejection of all restricted ancestral tendencies. Confidence A
is retained for the independently secure ordinary law, not treated as
proof of the disputed nucleus premise.

The earlier helper is not the whole unstressed history. SC070's
`OEUnstressedAFronting` already handles fronting before heterosyllabic
nasals after the separate coda-nasal treatment
[@Campbell1959, pp. 140-141, §§333-334]. Keeping the earlier helper
protects its actual internal-a applications and intervening feeders;
there is no justified deletion or second newly discovered historical law.
Early and late shortened-o inputs need separate interface controls.

Rest changes both root and ending: `*rástā -> *ræstǣ`.
Only the ending dependency connects SC042 to SC108. SC042 deliberately
carries its output quantity; later SC072 shortening and SC073 merger
complete the ending [@RingeTaylor2014, pp. 58-59, 299-300].
That encoding does not demonstrate an independent historical long-a
fronting. Who's stressed monosyllable remains a negative
[@Campbell1959, p. 49, §125].

Believe's prefix dependency is reclassified to SC107; the old composite
card is preserved. Root fronting/breaking and restoration still concern
SC043. The rest/prefix relations are technical constraints, not newly
promoted historical dates. No corpus/input or baseline migration is made.
The current reader quotes the actual EAF helper names and literal bodies;
the regression uses the shared FST parser to compare its four excerpts
with production.
