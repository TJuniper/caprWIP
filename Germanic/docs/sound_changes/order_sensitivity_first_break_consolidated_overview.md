# Order-sensitivity first-break consolidated overview

## Coverage summary

The current searchable explicit-chain first-break corpus now covers **70** chronology cards:

1. `SC014`-`SC019`
2. `SC020`-`SC037` and `SC039`-`SC061`
3. `SC063`-`SC076`
4. `SC078`-`SC083`
5. `SC085`-`SC087`

This is the complete currently searchable explicit-chain coverage represented in `chronology_card_index.tsv` and `sound_change_order_sensitivity.tsv`. `next_batch_candidates.tsv` now has **no** remaining `recommended_for_next_batch = yes` rows and **no** remaining `queued` ordinary explicit-chain batch candidates. Further progress is therefore more likely to come from:

1. consolidation and reuse of the current chronology corpus
2. runner improvements that expose bundled or non-explicit stages such as `PWGmcChanges`
3. targeted ad hoc tests for especially valuable broad/far or negative cases

## Terminology note

In this documentation, **ordinary chronology** means a first-break relation between modeled sound-change rules. Technical markers, bundled runner stages such as `PWGmcChanges`, and no-break search boundaries are still useful computational evidence, but they are not ordinary sound-change chronology constraints.

## Strong reciprocal / near-reciprocal constraints

The clearest reciprocal or near-reciprocal relations currently documented are:

1. `SC016` / `SC017`: PGmc `*júką` > expected OE `ġeoc`, variant `ġoc`.
2. `SC017` / `SC019`: PGmc `*núsō` > `nosu` / `nusu`, `*skúflō` > `sċofl` / `sċufl`, `*súrgō` > `sorg` / `surg`; `rust` and `wool` are changed-still-passing context only.
3. `SC019` / `SC020`: PGmc `*rástōz` > `ræste` / `rast`.
4. `SC026` / `SC027`: PGmc `*fúnxstiz` > `fȳst` / `fyst`, `*gánsz` > `gōs` / `ġeas`, `*júgunθ` > `ġeoguþ` / `ġeogoþ`.
5. `SC029` / `SC030`: PGmc `*xáwwją` > `hīeġ` / `hauġ`, `*stráwjaną` > `strīeġan` / `strauian`.
6. `SC030` / `SC032`: a reciprocal 18-row no-output boundary, e.g. PGmc `*galáubijaną` > expected OE `ġelīefan`, variant `+?`; `*bráudą` > `brēad`, variant `+?`.
7. `SC031` / `SC034`: PGmc `*dáwwō` > `dēaw` / `dawu`, `*xáwwaną` > `hēawan` / `hawan`.
8. `SC039` / `SC040`: PGmc `*wíduwōn` > `wuduwe` / `wudowe`.
9. `SC042` / `SC043`: `SC042` later breaks across `SC043`, and `SC043` earlier breaks across `SC042`.
10. `SC043` / `SC044`: `SC043` later breaks across `SC044`, and `SC044` earlier breaks across `SC043`.
11. `SC044` / `SC045`: `SC044` later breaks across `SC045`, and `SC045` earlier breaks across `SC044`.
12. `SC047` / `SC048`: the reciprocal 87-row broad `-en` failure set, e.g. `bacan` / `bacen`, `bindan` / `binden`.
13. `SC052` / `SC055`: the local reciprocal `cow` / `lung` corridor.
14. `SC055` / `SC056`: the reciprocal `gift` / `sheath` corridor around `ġift` / `ġieft` and `sċēaþ` / `sċǣþ`.
15. `SC064` / `SC072`: the reciprocal `fright` boundary (`fyrhte` / `fyrhten` class evidence).
16. `SC066` / `SC068`: the reciprocal `spindle` boundary (`spinl` / `spinnl`).
17. `SC070` / `SC071`: the reciprocal six-row unstressed-vowel set, including `boraþ` / `boreþ` and `mōnaþ` / `mōneþ`.
18. `SC072` / `SC073`: the reciprocal broad unstressed-vowel boundary.
19. `SC074` / `SC075`: the reciprocal `shilling` boundary (`sċilling` / `sċilleng`).
20. `SC079` / `SC080`: PGmc `*lúnganjō` > `lungen` / `lungenn`.
21. `SC081` / `SC082`: PGmc `*stráwjaną` > `strīeġan` / `strīeian`.
22. `SC082` / `SC083`: the reciprocal eight-row verbal `-ian` / `-eian` set, e.g. `borian` / `boreian`, `handlian` / `handleian`, `macian` / `maceian`.
23. `SC085` / `SC086`: the reciprocal contraction set, e.g. `flēon` / `flēoan`, `slēan` / `sleaan`, `tēon` / `teoon`, `tā` / `tāe`.

These are the strongest currently reusable chronology anchors because both sides of the relation are already present in the index or because one side directly reciprocates an already interpreted adjacent card.

## Broad / far constraints

Several first breaks are ordinary sound-change chronology relations but far enough from the current rule position that they should be narrated as **broad/far computational constraints**, not as tight local adjacency claims:

1. `SC015` later across `SC036`: PGmc `*wír-àldu` > expected OE `weorold`, variant `wuruld`.
2. `SC020` later across `SC040`: the later side is historically real but broad, with eleven newly failing rows rather than a local adjacency.
3. `SC021` later across `SC040`: PGmc `*xémonų` > expected OE `heofon`, variant `heofun`.
4. `SC023` later across `SC047`: PGmc `*dōną` > expected OE `dōn`, variant `+?`.
5. `SC024` later across `SC056`: the later side is historically real but broad, centered on `sheep` and `year`.
6. `SC033` later across `SC044`: a broad long-diphthong boundary rather than a local adjacency claim.
7. `SC036` earlier across `SC019`: the current failure set is narrow and centered on `soul`, but the boundary is still broad/far.
8. `SC040` later across `SC072`: historically real, but not a local neighboring-stage constraint.
9. `SC041` earlier across `SC020`: the broad 64-row earlier limit with many spurious `-a`-final outputs.
10. `SC047` later and `SC048` earlier: the reciprocal 87-row `-en` failure set.
11. `SC069` earlier across `SC023`: e.g. `*nḗdrōn` > `nǣdre` / `nǣdran`, `*érθōn` > `eorþe` / `eorþan`.
12. `SC072` later and `SC073` earlier: the broad reciprocal unstressed-vowel / `-æ` boundary.
13. `SC078` earlier across `SC070`: another broad 87-row `-en` failure set.
14. `SC079` earlier across `SC055`: e.g. `*galáubijaną` > `ġelīefan` / `ġelēafan`, `*báugijaną` > `bīeġan` / `bēaġan`.
15. `SC081` earlier across `SC055`: PGmc `*stráwjaną` > `strīeġan` / `strēaġan`.
16. `SC087` earlier across `SC044`: PGmc `*bréstaną` > `berstan` / `beorstan`.

The important interpretive rule is the same across all of these: a real first break can still be too broad or too distant to justify local adjacency prose.

## Negative / boundary cards

The current index marks the following rules as **negative / boundary cards**, meaning no ordinary chronology first break was found on either side within the searchable corridor:

1. `SC014`
2. `SC018`
3. `SC022` (Common Germanic; executable holding-zone placement)
4. `SC025`
5. `SC028`
6. `SC053`
7. `SC058`
8. `SC065`
9. `SC067`
10. `SC076`

For each of these, the earlier search is runner-limited by bundled `PWGmcChanges`, the later search reaches the current `SC087` boundary with no real break, or both.

## Runner-limited / technical-marker / scaffolding cases

### Earlier searches that stop at bundled `PWGmcChanges`

The current earlier runner-limited set is:

`SC014`, `SC015`, `SC016`, `SC018`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC028`, `SC029`, `SC035`, `SC037`, `SC039`, `SC050`, `SC053`, `SC058`, `SC065`, `SC067`, `SC076`

Retired `SC021` is no longer part of the current earlier runner-limited set.
Its old first-break result is archival project history only; current
chronology uses SC071/SC099/SC100.

These are search-boundary observations, not ordinary sound-change chronology earlier boundaries.

### Real computational breaks that are not ordinary sound-change chronology constraints

The current corpus includes three such cases:

1. `SC031` earlier across bundled `PWGmcChanges`: e.g. `*fédwōr` > `fēower` / `fēowwer`.
2. `SC033` earlier across bundled `PWGmcChanges`: e.g. `*fédwōr` > `fēower` / `feower`.
3. `SC037` later across technical-marker `SC038`: PGmc `*régna-bùgô` > `reġnboga` / `reġnefoga`.

These are real computational first breaks, but they should be kept separate from ordinary sound-change chronology claims because they cross bundled or technical stages.

## Later no-break-before-`SC087` cases

The current later no-break-before-boundary set is:

`SC014`, `SC018`, `SC022`, `SC025`, `SC027`, `SC028`, `SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`, `SC080`, `SC083`, `SC086`

These are **search-boundary observations only**. They show that the runner found no real later break before the current `SC087` limit; they do **not** show that the rule historically had to precede `SC087`.

`SC087` itself is a special terminal case: its later search reaches the current runner limit beyond order `86`, so even that result is a limit-of-search observation rather than a discovered later ordinary chronology boundary.

## Remaining work / next options

There is no remaining ordinary explicit-chain batch to recommend from `next_batch_candidates.tsv`. The highest-value next options are now:

1. **Runner work** to expose or split bundled stages such as `PWGmcChanges`, so that earlier negative / runner-limited sides can be probed historically.
2. **Quality audit** of card / index / summary consistency, especially for broad/far flags, reciprocal labels, and changed-still-passing caveats.
3. **Visualization / graph export** of the reciprocal and near-reciprocal network, now that the searchable explicit-chain corpus is effectively complete.
4. **Targeted ad hoc tests** for especially valuable broad/far and negative cases, rather than another contiguous batch.
5. **Separate handling for non-explicit rules and technical markers**, especially if the project wants a chronology layer that distinguishes ordinary sound changes from search scaffolding more explicitly.

The immediate documentation task after this overview is not more batch running; it is deciding which of those follow-on paths will produce the most useful next layer of chronology evidence.
