# First-break chronology graph summary

GENERATED FILE — DO NOT EDIT. Source: `registry/sc_registry.tsv` +
`registry/chronology_edges.tsv`. Generator:
`Germanic/tools/generate_registry_views.py`.

**Ordinary chronology** means a first-break relation between modeled
sound-change rules. Runner-limited boundaries, no-break search
boundaries and technical markers are diagnostic observations, not
chronology constraints.

## Totals

- total node count: `72`
- total edge count: `138`

### Node counts by card_type

| card_type | count |
| --- | ---: |
| `boundary_observation` | 2 |
| `broad_far` | 7 |
| `mixed` | 14 |
| `negative_boundary` | 9 |
| `one_sided_chronology` | 7 |
| `reciprocal_or_near_reciprocal` | 25 |
| `retired` | 1 |
| `runner_limited_or_technical` | 1 |
| `source_partial_chain` | 6 |

### Edge counts by relation_type

| relation_type | count |
| --- | ---: |
| `broad_far_chronology` | 16 |
| `near_reciprocal_chronology` | 2 |
| `no_break_search_boundary` | 21 |
| `one_sided_chronology` | 40 |
| `reciprocal_chronology` | 34 |
| `runner_limited_boundary` | 19 |
| `technical_computational` | 6 |

## Chronology edges

1. `SC015 -> SC036` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `world`; forms: PGmc `*wír-àldu` yields expected OE `weorold`, but the later-shifted variant yields `wuruld`
1. `SC016 -> SC017` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `yoke`; forms: PGmc `*júką` yields expected OE `ġeoc`, but the later-shifted variant yields `ġoc`
1. `SC017 -> SC016` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `yoke`; forms: PGmc `*júką` yields expected OE `ġeoc`, but the earlier-shifted variant yields `ġoc`
1. `SC017 -> SC019` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `nose; shovel; sorrow`; forms: PGmc `*núsō` yields expected OE `nosu`, but the later-shifted variant yields `nusu`; PGmc `*skúflō` likewise yields `sċufl` instead of expected `sċofl`; PGmc `*súrgō` yields `surg` instead of expected `sorg`
1. `SC019 -> SC017` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `nose; shovel; sorrow`; forms: PGmc `*núsō` yields expected OE `nosu`, but the earlier-shifted variant yields `nusu`; PGmc `*skúflō` likewise yields `sċufl` instead of expected `sċofl`; PGmc `*súrgō` yields `surg` instead of expected `sorg`
1. `SC019 -> SC020` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `rest`; forms: PGmc `*rástōz` yields expected OE `ræste`, but the later-shifted variant yields `rast`
1. `SC020 -> SC019` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `rest`; forms: PGmc `*rástōz` yields expected OE `ræste`, but the earlier-shifted variant yields `rast`
1. `SC020 -> SC040` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `beaver; bough; cud; field; flood`; forms: PGmc `*bébruz` yields expected OE `befer`, but the later-shifted variant yields `befro`; PGmc `*kwéðuz` likewise yields `cwedo` instead of expected `cwedu`; PGmc `*félθuz` yields `feldo` instead of `feld`
1. `SC023 -> SC047` (broad_far_chronology; independently_demonstrated; witness role: counterfeeding_negative) — lexemes: `do`; forms: PGmc `*dōną` yields expected OE `dōn`, but the later-shifted variant yields `+?` (no output)
1. `SC024 -> SC025` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `month; spoon`; forms: PGmc `*mḗnōθz` yields expected OE `mōnaþ`, but with SC024 displaced after SC025/SC101 the cascade yields `mānaþ`; `*spḗnuz` likewise yields `spān` instead of `spōn`
1. `SC024 -> SC101` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `sheep; year; sleep`; forms: PGmc `*skḗpą` yields expected OE `sċēap`, but with SC024 displaced after SC025/SC101 the cascade yields `sċāp`; `*jḗrą` yields `ġār` instead of `ġēar`; `*slḗpaną` yields `slāpan` instead of `slǣpan`
1. `SC024 -> SC102` (one_sided_chronology; independently_demonstrated; witness role: feeding) — lexemes: `sow`; forms: PGmc `*sḗaną` yields expected OE `sāwan`, but with SC102 displaced before SC024 the insertion environment `{*ā} _ V` never exists (the pre-SC024 form is still `*sēaną`), so no hiatus *w is ever inserted and the output lacks the historical consonant (`**sāan`-type)
1. `SC025 -> SC004` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `stone; home`; forms: PGmc `*stáinaz` yields expected OE `stān` and `*xáimaz` yields `hām`; with SC004 displaced before SC025 (the equivalent test after the SC025/SC104 split) the new *ā < *ai is nasalized and then rounded, and the cascade yields `stōn` and `hōm`
1. `SC103 -> SC104` (one_sided_chronology; independently_demonstrated; witness role: feeding) — lexemes: `thought`; forms: PGmc `*θánxtē` 'thought (3sg pret.)' > OE `þōhte`. SC103 creates the nasalized low vowel and deletes the nasal (`*θ*á*n*x*t*ē` > `*θ*ã*x*t*ē`); SC104 then rounds exactly that vowel (`*θ*ã*x*t*ē` > `*θ*ō*x*t*ē`). Counterfactual composition in the opposite order leaves `*θ*ã*x*t*ē` unrounded, because SC104 has no `{*ã}` to read until SC103 has applied — a live feeding relation, not merely a stage entailment. This is the low-vowel (*aNx) branch of SC103; the high-vowel branch, exemplified by `fist` (`*fúnxstiz`), never reaches SC104
1. `SC103 -> SC028` (one_sided_chronology; stage_entailed; witness role: feeding) — lexemes: `fist`; forms: *funxstiz > *fuxstiz > *fustiz
1. `SC101 -> SC004` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `loath; rope; token; soul; ghost`; forms: PGmc `*láiθaz` yields expected OE `lāþ`, but with SC101 displaced after SC004 the cascade yields `lǣþ`; likewise `rǣp`, `tǣcn`, `sǣwol`, `ġēast` for `rāp`, `tācn`, `sāwol`, `gāst`
1. `SC101 -> SC056` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `sheep; year`; forms: PGmc `*skḗpą` yields expected OE `sċēap`, but with SC101 displaced after SC056 the cascade yields `sċǣp`; `*jḗrą` likewise yields `ġǣr` instead of `ġēar`
1. `SC026 -> SC027` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `goose; youth`; forms: PGmc `*gánsz` yields `ġeas` instead of expected `gōs` when SC026 is shifted later; PGmc `*júgunθ` yields `ġeogoþ` instead of expected `ġeoguþ`. This is an EXECUTABLE dependency, not a historical interval: SC026 must read the nasal that SC027 deletes (sc026-sc027-nasal-spirant-adjudication.md). `fist` withdrawn as a witness — its nasal loss is the pan-Germanic pre-*x change SC103
1. `SC027 -> SC026` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `goose; youth`; forms: PGmc `*gánsz` yields `ġeas` instead of expected `gōs` when SC027 is shifted earlier; PGmc `*júgunθ` yields `ġeogoþ` instead of expected `ġeoguþ`. Executable dependency, not a historical interval (sc026-sc027-nasal-spirant-adjudication.md). `fist` withdrawn as a witness — its nasal loss is the pan-Germanic pre-*x change SC103
1. `SC010 -> SC029` (one_sided_chronology; independently_demonstrated; witness role: feeding) — lexemes: `hay; strew`; forms: PGmc `*xáwją` geminates to `*xáwwją` at SC010, which SC029 resolves to `*xáuj`, yielding expected OE `hīeġ`; PGmc `*stráwjaną` likewise geminates to `*stráwwjaną` and resolves to `*stráujaną`, yielding expected `strīeġan`. Without the SC010 step neither form reaches SC029 in its geminate input shape.
1. `SC029 -> SC030` (reciprocal_chronology; independently_demonstrated; witness role: feeding) — lexemes: `hay; strew`; forms: PGmc `*xáwją` yields expected OE `hīeġ`, but the later-shifted variant yields `hauġ`; PGmc `*stráwjaną` likewise yields `strauian` instead of expected `strīeġan`
1. `SC030 -> SC029` (reciprocal_chronology; independently_demonstrated; witness role: feeding) — lexemes: `hay; strew`; forms: PGmc `*xáwją` yields expected OE `hīeġ`, but the earlier-shifted variant yields `hauġ`; PGmc `*stráwjaną` likewise yields `strauian` instead of expected `strīeġan`
1. `SC030 -> SC032` (reciprocal_chronology; independently_demonstrated; witness role: feeding) — lexemes: `believe; bow; bread; dream; flea`; forms: PGmc `*galáubijaną` yields expected OE `ġelīefan`, but the later-shifted variant yields `+?` (no output); PGmc `*bráudą` likewise yields no output instead of expected `brēad`; PGmc `*dráugmaz` yields no output instead of expected `drēam`
1. `SC008 -> SC031` (one_sided_chronology; independently_demonstrated; witness role: feeding) — lexemes: `four; you`; forms: Coronal+w assimilation supplies ww, and short-Vww reanalysis supplies eu/iu plus retained w.
1. `SC032 -> SC030` (reciprocal_chronology; independently_demonstrated; witness role: feeding) — lexemes: `believe; bow; bread; dream; flea`; forms: PGmc `*galáubijaną` yields expected OE `ġelīefan`, but the earlier-shifted variant yields `+?` (no output); PGmc `*báug` likewise yields no output instead of expected `bēag`; PGmc `*bráudą` yields no output instead of expected `brēad`
1. `SC032 -> SC040` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `head`; forms: PGmc `*xáubudą` yields expected OE `hēafod`, but the later-shifted variant yields `hēafud`
1. `SC036 -> SC019` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `soul`; forms: PGmc `*sáiwalō` yields expected OE `sāwol`, but the earlier-shifted variant yields `sāwel`
1. `SC036 -> SC040` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `soul; world`; forms: PGmc `*sáiwalō` yields expected OE `sāwol`, but the later-shifted variant yields `sāwul`; PGmc `*wír-àldu` likewise yields `weoruld` instead of expected `weorold`
1. `SC039 -> SC040` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `widow`; forms: PGmc `*wíduwōn` yields expected OE `wuduwe`, but the later-shifted variant yields `wudowe`
1. `SC040 -> SC039` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `widow`; forms: PGmc `*wíduwōn` yields expected OE `wuduwe`, but the earlier-shifted variant yields `wudowe`
1. `SC040 -> SC072` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `youth`; forms: PGmc `*júgunθ` yields expected OE `ġeoguþ`, but the later-shifted variant yields `ġeogoþ`
1. `SC041 -> SC020` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `beard; bosom; bottom; calf; coat`; forms: PGmc `*bárdaz` yields expected OE `beard`, but the earlier-shifted variant yields `bearda`; PGmc `*kámbaz` likewise yields `camba` instead of expected `camb`
1. `SC041 -> SC046` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `craft; dale; day; hazel; mast`; forms: PGmc `*kráftaz` yields expected OE `cræft`, but the later-shifted variant yields `craft`; PGmc `*dágaz` likewise yields `dag` instead of expected `dæġ`
1. `SC042 -> SC020` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `rest`; forms: PGmc `*rástōz` yields expected OE `ræste`, but the earlier-shifted variant yields `rasta`
1. `SC043 -> SC044` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `slay`; forms: PGmc `*sláxaną` yields expected OE `slēan`, but the later-shifted variant yields `sleaan | slēaan`
1. `SC044 -> SC043` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `slay`; forms: PGmc `*sláxaną` yields expected OE `slēan`, but the earlier-shifted variant yields `sleaan | slēaan`
1. `SC044 -> SC045` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `fee; fight; flax; knight; laugh`; forms: PGmc `*féxu` yields expected OE `feoh`, but the later-shifted variant yields `fehu`; PGmc `*féxtaną` likewise yields `fehtan` instead of expected `feohtan`
1. `SC045 -> SC044` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `fee; fight; flax; knight; laugh`; forms: PGmc `*féxu` yields expected OE `feoh`, but the earlier-shifted variant yields `fehu`; PGmc `*féxtaną` likewise yields `fehtan` instead of expected `feohtan`
1. `SC045 -> SC060` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `six`; forms: PGmc `*séxs` yields expected OE `six`, but the later-shifted variant yields `sihs`
1. `SC046 -> SC043` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `bake; fare; flask; grave; haw`; forms: PGmc `*bákaną` yields expected OE `bacan`, but the earlier-shifted variant yields `bæcan`; PGmc `*fáraną` likewise yields `færan` instead of expected `faran`
1. `SC046 -> SC048` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `bake; fare; grave; lade; wade`; forms: PGmc `*bákaną` yields expected OE `bacan`, but the later-shifted variant yields `bæcan`; PGmc `*wádaną` likewise yields `wædan` instead of expected `wadan`
1. `SC047 -> SC034` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `straw`; forms: PGmc `*stráwą` yields expected OE `strēaw`, but the earlier-shifted variant yields `stræw`
1. `SC047 -> SC048` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `bake; begin; believe; bind; bore`; forms: PGmc `*bákaną` yields expected OE `bacan`, but the later-shifted variant yields `bacen`; PGmc `*bíndaną` likewise yields `binden` instead of expected `bindan`
1. `SC048 -> SC047` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `bake; begin; believe; bind; bore`; forms: PGmc `*bákaną` yields expected OE `bacan`, but the earlier-shifted variant yields `bacen`; PGmc `*bíndaną` likewise yields `binden` instead of expected `bindan`
1. `SC048 -> SC059` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `steal; weave`; forms: PGmc `*stélaną` yields expected OE `stelan`, but the later-shifted variant yields `steolan`; PGmc `*wébaną` likewise yields `weofan` instead of expected `wefan`
1. `SC049 -> SC037` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `rainbow`; forms: PGmc `*régna-bùgô` yields expected OE `reġnboga`, but the earlier-shifted variant yields `reġnfoga`
1. `SC050 -> SC052` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `stretch`; forms: PGmc `*strákkijaną` yields expected OE `streċċan`, but the later-shifted variant yields `strecċan`
1. `SC051 -> SC046` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `flask; wash`; forms: PGmc `*fláskōn` yields expected OE `flasce`, but the earlier-shifted variant yields `flæsċe`; PGmc `*wáskaną` likewise yields `wæsċan` instead of expected `wascan`
1. `SC051 -> SC056` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `shaft; shear; sheep; shield`; forms: PGmc `*skáftą` yields expected OE `sċeaft`, but the later-shifted variant yields `sċæft`; PGmc `*skéraną` likewise yields `sċeran` instead of expected `sċieran`
1. `SC052 -> SC050` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `stretch`; forms: PGmc `*strákkijaną` yields expected OE `streċċan`, but the earlier-shifted variant yields `strecċan`
1. `SC052 -> SC055` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `cow; lung`; forms: PGmc `*kūi` yields expected OE `cȳ`, but the later-shifted variant yields `ċȳ`; PGmc `*lúnganjō` likewise yields `lunġen` instead of expected `lungen`
1. `SC054 -> SC020` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `sea`; forms: PGmc `*sáiwiz` yields expected OE `sǣ`, but the earlier-shifted variant yields `sǣw`
1. `SC054 -> SC063` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `sea`; forms: PGmc `*sáiwiz` yields expected OE `sǣ`, but the later-shifted variant again yields `sǣw`
1. `SC055 -> SC052` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `cow; lung`; forms: PGmc `*kūi` yields expected OE `cȳ`, but the earlier-shifted variant yields `ċȳ`; PGmc `*lúnganjō` likewise yields `lunġen` instead of expected `lungen`
1. `SC057 -> SC052` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `bow; follow; hedge; seek; singe`; forms: PGmc `*báugijaną` yields expected OE `bīeġan`, but the earlier-shifted variant yields `bēaġan`; PGmc `*sōkijaną` likewise yields `sōċan` instead of expected `sēċan`
1. `SC059 -> SC048` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `give; shear; steal; weave`; forms: PGmc `*gébaną` yields expected OE `ġiefan`, but the earlier-shifted variant yields `ġeofan`; PGmc `*stélaną` likewise yields `steolan` instead of expected `stelan`
1. `SC059 -> SC078` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `steal; weave`; forms: PGmc `*stélaną` yields expected OE `stelan`, but the later-shifted variant yields `steolan`; PGmc `*wébaną` likewise yields `weofan` instead of expected `wefan`
1. `SC060 -> SC055` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `might; night`; forms: PGmc `*máxtiz` yields expected OE `miht`, but the earlier-shifted variant yields `mieht`; PGmc `*náxti` likewise yields `nieht` instead of expected `niht`
1. `SC061 -> SC023` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `do`; forms: PGmc `*dōną` yields expected OE `dōn`, but the earlier-shifted variant yields no output (`+?` in the TSV)
1. `SC063 -> SC055` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `belly; birth; breeches; bride; cow`; forms: PGmc `*kūi` yields expected OE `cȳ`, but the earlier-shifted variant yields `cū`; PGmc `*brūdiz` likewise yields `brūd` instead of expected `brȳd`
1. `SC063 -> SC072` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `fright`; forms: PGmc `*fúrxtīnaz` yields expected OE `fyrhte`, but the later-shifted variant yields `fyrht`
1. `SC064 -> SC041` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `fright`; forms: PGmc `*fúrxtīnaz` yields expected OE `fyrhte`, but the earlier-shifted variant yields `fyrhten`
1. `SC064 -> SC072` (near_reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `fright`; forms: PGmc `*fúrxtīnaz` yields expected OE `fyrhte`, but the later-shifted variant again yields `fyrhten`
1. `SC066 -> SC055` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `nettle; spindle`; forms: PGmc `*nátilōn` yields expected OE `netle`, but the earlier-shifted variant yields `nætle`; PGmc `*spénnilō` likewise yields `spenl` instead of expected `spinl`
1. `SC066 -> SC068` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `spindle`; forms: PGmc `*spénnilō` yields expected OE `spinl`, but the later-shifted variant yields `spinnl`
1. `SC068 -> SC066` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `spindle`; forms: PGmc `*spénnilō` yields expected OE `spinl`, but the earlier-shifted variant yields `spinnl`
1. `SC069 -> SC023` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `adder; earth; flask; heart; line`; forms: PGmc `*nḗdrōn` yields expected OE `nǣdre`, but the earlier-shifted variant yields `nǣdran`; PGmc `*érθōn` likewise yields `eorþan` instead of expected `eorþe`; PGmc `*fláskōn` yields `flascan` instead of `flasce`
1. `SC070 -> SC052` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `lung`; forms: PGmc `*lúnganjō` yields expected OE `lungen`, but the earlier-shifted variant yields `lunġen`
1. `SC070 -> SC071` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `bore (3sg); learn (3sg); lick (3sg); make (3sg); month`; forms: PGmc `*búrōθi` yields expected OE `boraþ`, but the later-shifted variant yields `boreþ`; PGmc `*mḗnōθz` likewise yields `mōneþ` instead of expected `mōnaþ`
1. `SC071 -> SC070` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `bore (3sg); learn (3sg); lick (3sg); make (3sg); month`; forms: PGmc `*búrōθi` yields expected OE `boraþ`, but the earlier-shifted variant yields `boreþ`; PGmc `*líznōθi` likewise yields `liorneþ` instead of expected `liornaþ`
1. `SC072 -> SC064` (near_reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `fright`; forms: PGmc `*fúrxtīnaz` yields expected OE `fyrhte`, but the earlier-shifted variant yields `fyrhten`
1. `SC072 -> SC073` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `adder; earth; father; find; flask`; forms: PGmc `*nḗdrōn` yields expected OE `nǣdre`, but the later-shifted variant yields `nǣdræ`; PGmc `*fádēr` likewise yields `fædær` instead of expected `fæder`
1. `SC073 -> SC072` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `adder; earth; father; find; flask`; forms: PGmc `*nḗdrōn` yields expected OE `nǣdre`, but the earlier-shifted variant yields `nǣdræ`; PGmc `*fádēr` likewise yields `fædær` instead of expected `fæder`
1. `SC073 -> SC085` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `toe`; forms: PGmc `*táixōn` yields expected OE `tā`, but the later-shifted variant yields `tāæ`
1. `SC074 -> SC072` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `fright`; forms: PGmc `*fúrxtīnaz` yields expected OE `fyrhte`, but the earlier-shifted variant yields `fyrhti`
1. `SC074 -> SC075` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `shilling`; forms: PGmc `*skíllingaz` yields expected OE `sċilling`, but the later-shifted variant yields `sċilleng`
1. `SC075 -> SC074` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `shilling`; forms: PGmc `*skíllingaz` yields expected OE `sċilling`, but the earlier-shifted variant yields `sċilleng`
1. `SC078 -> SC070` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `bake; begin; believe; bind; bore`; forms: PGmc `*bákaną` yields expected OE `bacan`, but the earlier-shifted variant yields `bacen`; PGmc `*bíndaną` likewise yields `binden` instead of expected `bindan`
1. `SC078 -> SC086` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `flee; slay`; forms: PGmc `*fléuxaną` yields expected OE `flēon`, but the later-shifted variant yields `flēoan`; PGmc `*sláxaną` likewise yields `sleaan` instead of expected `slēan`
1. `SC079 -> SC055` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `believe; bow; fast; follow; heal`; forms: PGmc `*galáubijaną` yields expected OE `ġelīefan`, but the earlier-shifted variant yields `ġelēafan`; PGmc `*báugijaną` likewise yields `bēaġan` instead of expected `bīeġan`; PGmc `*fúlgijaną` yields `fulġan` instead of `fylġan`
1. `SC079 -> SC080` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `lung`; forms: PGmc `*lúnganjō` yields expected OE `lungen`, but the later-shifted variant yields `lungenn`
1. `SC080 -> SC079` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `lung`; forms: PGmc `*lúnganjō` yields expected OE `lungen`, but the earlier-shifted variant yields `lungenn`
1. `SC081 -> SC055` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `strew`; forms: PGmc `*stráwjaną` yields expected OE `strīeġan`, but the earlier-shifted variant yields `strēaġan`
1. `SC081 -> SC082` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `strew`; forms: PGmc `*stráwjaną` yields expected OE `strīeġan`, but the later-shifted variant yields `strīeian`
1. `SC082 -> SC081` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `strew`; forms: PGmc `*stráwjaną` yields expected OE `strīeġan`, but the earlier-shifted variant yields `strīeian`
1. `SC082 -> SC083` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `bore; handle; learn; lick; make`; forms: PGmc `*búrōjaną` yields expected OE `borian`, but the later-shifted variant yields `boreian`; PGmc `*xándlōjaną` likewise yields `handleian` instead of expected `handlian`; PGmc `*mákōjaną` yields `maceian` instead of `macian`
1. `SC083 -> SC082` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `bore; handle; learn; lick; make`; forms: PGmc `*búrōjaną` yields expected OE `borian`, but the earlier-shifted variant yields `boreian`; PGmc `*líznōjaną` likewise yields `liorneian` instead of expected `liornian`; PGmc `*líkkōjaną` yields `licceian` instead of `liccian`
1. `SC085 -> SC073` (one_sided_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `toe`; forms: PGmc `*táixōn` yields expected OE `tā`, but the earlier-shifted variant yields `tāæ`
1. `SC085 -> SC086` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `flee; slay; ten; toe`; forms: PGmc `*fléuxaną` yields expected OE `flēon`, but the later-shifted variant yields `flēoan`; PGmc `*sláxaną` likewise yields `sleaan` instead of expected `slēan`; PGmc `*téxun` yields `teoon` instead of `tēon`; PGmc `*táixōn` yields `tāe` instead of `tā`
1. `SC086 -> SC085` (reciprocal_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `flee; slay; ten; toe`; forms: PGmc `*fléuxaną` yields expected OE `flēon`, but the earlier-shifted variant yields `flēoan`; PGmc `*sláxaną` likewise yields `sleaan` instead of expected `slēan`; PGmc `*téxun` yields `teoon` instead of `tēon`; PGmc `*táixōn` yields `tāe` instead of `tā`
1. `SC087 -> SC044` (broad_far_chronology; independently_demonstrated; witness role: displacement_witness) — lexemes: `burst`; forms: PGmc `*bréstaną` yields expected OE `berstan`, but the earlier-shifted variant yields `beorstan`
1. `SC056 -> SC055` (one_sided_chronology; independently_demonstrated; witness role: feeding) — lexemes: `guest`; forms: ae > ea by ordinary PD; ea > ie by mutation

## Boundary and technical observations

1. `SC014 -> PWGmcChanges` (runner_limited_boundary)
1. `SC014 -> SC087` (no_break_search_boundary)
1. `SC015 -> PWGmcChanges` (runner_limited_boundary)
1. `SC016 -> PWGmcChanges` (runner_limited_boundary)
1. `SC018 -> PWGmcChanges` (runner_limited_boundary)
1. `SC018 -> SC087` (no_break_search_boundary)
1. `SC022 -> PWGmcChanges` (runner_limited_boundary)
1. `SC022 -> SC087` (no_break_search_boundary)
1. `SC023 -> PWGmcChanges` (runner_limited_boundary)
1. `SC024 -> EarlyEnglishLineChanges` (runner_limited_boundary)
1. `SC102 -> SC101` (no_break_search_boundary)
1. `SC025 -> SC104` (technical_computational)
1. `SC026 -> SC104` (technical_computational)
1. `SC026 -> PWGmcChanges` (runner_limited_boundary)
1. `SC027 -> SC087` (no_break_search_boundary)
1. `SC029 -> PWGmcChanges` (runner_limited_boundary)
1. `SC035 -> PWGmcChanges` (runner_limited_boundary)
1. `SC035 -> SC107` (technical_computational)
1. `SC037 -> PWGmcChanges` (runner_limited_boundary)
1. `SC037 -> SC038` (technical_computational)
1. `SC039 -> PWGmcChanges` (runner_limited_boundary)
1. `SC042 -> SC108` (technical_computational)
1. `SC108 -> SC042` (technical_computational)
1. `SC049 -> SC087` (no_break_search_boundary)
1. `SC050 -> PWGmcChanges` (runner_limited_boundary)
1. `SC053 -> PWGmcChanges` (runner_limited_boundary)
1. `SC053 -> SC087` (no_break_search_boundary)
1. `SC057 -> SC087` (no_break_search_boundary)
1. `SC058 -> PWGmcChanges` (runner_limited_boundary)
1. `SC058 -> SC087` (no_break_search_boundary)
1. `SC060 -> SC087` (no_break_search_boundary)
1. `SC061 -> SC087` (no_break_search_boundary)
1. `SC065 -> PWGmcChanges` (runner_limited_boundary)
1. `SC065 -> SC087` (no_break_search_boundary)
1. `SC067 -> PWGmcChanges` (runner_limited_boundary)
1. `SC067 -> SC087` (no_break_search_boundary)
1. `SC068 -> SC087` (no_break_search_boundary)
1. `SC069 -> SC087` (no_break_search_boundary)
1. `SC071 -> SC087` (no_break_search_boundary)
1. `SC075 -> SC087` (no_break_search_boundary)
1. `SC076 -> PWGmcChanges` (runner_limited_boundary)
1. `SC076 -> SC087` (no_break_search_boundary)
1. `SC080 -> SC087` (no_break_search_boundary)
1. `SC083 -> SC087` (no_break_search_boundary)
1. `SC086 -> SC087` (no_break_search_boundary)
1. `SC087 -> RUNNER_LIMIT` (runner_limited_boundary)
