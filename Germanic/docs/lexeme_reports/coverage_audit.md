# Old English lexeme-report coverage audit

- Total OE rows with real counterpart: 387
- Manifest entries loaded: 12
- Rows requiring lexeme report: 155
- Required rows with manifest-backed production reports: 11
- Required rows with source material available but no manifest-backed production report: 140
- Required rows with no source material found: 4
- Regular rows with empty NOTE and no report required: 1
- Regular rows with empty NOTE but supporting material present: 231
- Rows with STATUS=format_test manifest entries: 1
- Regular rows with NOTE (report required): 78
- Non-regular rows with empty NOTE (report required because of DERIVATION_CLASS): 11

## Counts by DERIVATION_CLASS

| DERIVATION_CLASS | Total rows | Required | Manifest-backed production reports | Source material available | No source material found |
| :--- | :--- | :--- | :--- | :--- | :--- |
| attested_variant | 4 | 4 | 1 | 3 | 0 |
| early_analogy | 36 | 36 | 2 | 34 | 0 |
| known_unmodelled | 2 | 2 | 2 | 0 | 0 |
| late_analogy | 27 | 27 | 4 | 23 | 0 |
| reconstructed_oe | 3 | 3 | 1 | 2 | 0 |
| regular | 310 | 78 | 0 | 74 | 4 |
| unexplained_unmodelled | 5 | 5 | 1 | 4 | 0 |

## Required rows with manifest-backed production reports

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage category | Production status | Production report / source-material path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1936 | ban | bannes | late_analogy | yes | manifest | pilot | pilot/ban.md | NOTE, DERIVATION_CLASS=late_analogy, production_report |
| 1946 | berry | berġes | late_analogy | yes | manifest | pilot | pilot/berry.md | NOTE, DERIVATION_CLASS=late_analogy, production_report |
| 1959 | bottom | botm | early_analogy | yes | manifest | pilot | pilot/bottom.md | NOTE, DERIVATION_CLASS=early_analogy, production_report |
| 1973 | buck | bucc | unexplained_unmodelled | yes | manifest | pilot | pilot/buck.md | NOTE, DERIVATION_CLASS=unexplained_unmodelled, production_report |
| 1981 | craft | cræft | early_analogy | yes | manifest | pilot | pilot/craft.md | NOTE, DERIVATION_CLASS=early_analogy, production_report |
| 1983 | cud | cwedu | attested_variant | yes | manifest | pilot | pilot/cud.md | NOTE, DERIVATION_CLASS=attested_variant, production_report |
| 2013 | fire | fȳre | known_unmodelled | yes | manifest | pilot | pilot/fire.md | NOTE, DERIVATION_CLASS=known_unmodelled, production_report |
| 2151 | reek | rēac | reconstructed_oe | yes | manifest | pilot | pilot/reek.md | NOTE, DERIVATION_CLASS=reconstructed_oe, production_report |
| 2203 | span | spanne | late_analogy | yes | manifest | pilot | pilot/span.md | NOTE, DERIVATION_CLASS=late_analogy, production_report |
| 2240 | tap | tæppa | known_unmodelled | yes | manifest | pilot | pilot/tap.md | NOTE, DERIVATION_CLASS=known_unmodelled, production_report |
| 2250 | thistle | þistles | late_analogy | yes | manifest | pilot | pilot/thistle.md | NOTE, DERIVATION_CLASS=late_analogy, production_report |

## Required rows with source material available but no manifest-backed production report

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage category | Production status | Production report / source-material path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1934 | bake | bacan | regular | yes | source_material | - | dev_notes_slices/1934-bake-bacan.md, model_entries/1934-bake-bacan.model.md, model_entries/1934-bake-bacan.model_implementation_report.md, model_entries/1934-bake-bacan.reviewer_checklist.md, model_entries/1934-bake-bacan.source_ledger.md, packets/1934-bake-bacan.md, research_memos/1934-bake-bacan.md | NOTE |
| 1942 | beech | bōc | regular | yes | source_material | - | dev_notes_slices/1942-beech-bōc.md, model_entries/1942-beech-bōc.model.md, model_entries/1942-beech-bōc.reviewer_checklist.md, model_entries/1942-beech-bōc.source_ledger.md, packets/1942-beech-bōc.md, research_memos/1942-beech-bōc.md | NOTE |
| 1943 | begin | beġinnan | regular | yes | source_material | - | dev_notes_slices/1943-begin-beġinnan.md, model_entries/1943-begin-beġinnan.model.md, model_entries/1943-begin-beġinnan.model_implementation_report.md, model_entries/1943-begin-beġinnan.reviewer_checklist.md, model_entries/1943-begin-beġinnan.source_ledger.md, packets/1943-begin-beġinnan.md, research_memos/1943-begin-beġinnan.md | NOTE |
| 1949 | bier | bǣr | regular | yes | source_material | - | dev_notes_slices/1949-bier-bǣr.md, model_entries/1949-bier-bǣr.model.md, model_entries/1949-bier-bǣr.model_implementation_report.md, model_entries/1949-bier-bǣr.reviewer_checklist.md, model_entries/1949-bier-bǣr.source_ledger.md, packets/1949-bier-bǣr.md, research_memos/1949-bier-bǣr.md | NOTE |
| 1951 | birth | byrd | regular | yes | source_material | - | dev_notes_slices/1951-birth-byrd.md, model_entries/1951-birth-byrd.model.md, model_entries/1951-birth-byrd.model_implementation_report.md, model_entries/1951-birth-byrd.reviewer_checklist.md, model_entries/1951-birth-byrd.source_ledger.md, packets/1951-birth-byrd.md, research_memos/1951-birth-byrd.md | NOTE |
| 1954 | bone | bān | regular | yes | source_material | - | dev_notes_slices/1954-bone-bān.md, model_entries/1954-bone-bān.model.md, model_entries/1954-bone-bān.model_implementation_report.md, model_entries/1954-bone-bān.reviewer_checklist.md, model_entries/1954-bone-bān.source_ledger.md, packets/1954-bone-bān.md, research_memos/1954-bone-bān.md | NOTE |
| 1958 | both | bū | regular | yes | source_material | - | dev_notes_slices/1958-both-bū.md, model_entries/1958-both-bū.model.md, model_entries/1958-both-bū.model_implementation_report.md, model_entries/1958-both-bū.reviewer_checklist.md, model_entries/1958-both-bū.source_ledger.md, packets/1958-both-bū.md, packets/1962-bow-bēag.md, research_memos/1958-both-bū.md | NOTE |
| 1961 | bow | bīeġan | regular | yes | source_material | - | dev_notes_slices/1961-bow-bīeġan.md, model_entries/1961-bow-bīeġan.model.md, model_entries/1961-bow-bīeġan.model_implementation_report.md, model_entries/1961-bow-bīeġan.reviewer_checklist.md, model_entries/1961-bow-bīeġan.source_ledger.md, packets/1961-bow-bīeġan.md, research_memos/1961-bow-bīeġan.md | NOTE |
| 1962 | bow | bēag | late_analogy | yes | source_material | - | dev_notes_slices/1962-bow-bēag.md, model_entries/1962-bow-bēag.model.md, model_entries/1962-bow-bēag.model_implementation_report.md, model_entries/1962-bow-bēag.reviewer_checklist.md, model_entries/1962-bow-bēag.source_ledger.md, research_memos/1962-bow-bēag.md | NOTE, DERIVATION_CLASS=late_analogy |
| 1965 | brand | brandes | early_analogy | no | source_material | - | dev_notes_slices/1965-brand-brandes.md, model_entries/1965-brand-brandes.model.md, model_entries/1965-brand-brandes.model_implementation_report.md, model_entries/1965-brand-brandes.reviewer_checklist.md, model_entries/1965-brand-brandes.source_ledger.md, model_entries/production_batch_01_report.md, packets/1965-brand-brandes.md, research_memos/1965-brand-brandes.md | DERIVATION_CLASS=early_analogy |
| 1968 | breast | brēost | early_analogy | no | source_material | - | dev_notes_slices/1968-breast-brēost.md, model_entries/1968-breast-brēost.model.md, model_entries/1968-breast-brēost.model_implementation_report.md, model_entries/1968-breast-brēost.reviewer_checklist.md, model_entries/1968-breast-brēost.source_ledger.md, packets/1968-breast-brēost.md, research_memos/1968-breast-brēost.md | DERIVATION_CLASS=early_analogy |
| 1969 | breeches | brēċ | regular | yes | source_material | - | dev_notes_slices/1969-breeches-brēċ.md, model_entries/1969-breeches-brēċ.model.md, model_entries/1969-breeches-brēċ.model_implementation_report.md, model_entries/1969-breeches-brēċ.reviewer_checklist.md, model_entries/1969-breeches-brēċ.source_ledger.md, research_memos/1969-breeches-brēċ.md | NOTE |
| 1975 | calf | ċealf | regular | yes | source_material | - | dev_notes_slices/1975-calf-ċealf.md, model_entries/1975-calf-ċealf.model.md, model_entries/1975-calf-ċealf.model_implementation_report.md, model_entries/1975-calf-ċealf.reviewer_checklist.md, model_entries/1975-calf-ċealf.source_ledger.md, packets/1975-calf-ċealf.md, research_memos/1975-calf-ċealf.md | NOTE |
| 1979 | corn | corn | regular | yes | source_material | - | dev_notes_slices/1979-corn-corn.md, model_entries/1979-corn-corn.model.md, model_entries/1979-corn-corn.model_implementation_report.md, model_entries/1979-corn-corn.reviewer_checklist.md, model_entries/1979-corn-corn.source_ledger.md, model_entries/production_batch_07_report.md, packets/1979-corn-corn.md, research_memos/1979-corn-corn.md | NOTE |
| 1980 | cow | cȳ | late_analogy | yes | source_material | - | dev_notes_slices/1980-cow-cȳ.md, model_entries/1980-cow-cȳ.model.md, model_entries/1980-cow-cȳ.model_implementation_report.md, model_entries/1980-cow-cȳ.reviewer_checklist.md, model_entries/1980-cow-cȳ.source_ledger.md, packets/1980-cow-cȳ.md, research_memos/1980-cow-cȳ.md, writing_skill/scaling_plan.md | NOTE, DERIVATION_CLASS=late_analogy |
| 1987 | deed | dǣd | regular | yes | source_material | - | dev_notes_slices/1987-deed-dǣd.md, model_entries/1987-deed-dǣd.model.md, model_entries/1987-deed-dǣd.model_implementation_report.md, model_entries/1987-deed-dǣd.reviewer_checklist.md, model_entries/1987-deed-dǣd.source_ledger.md, research_memos/1987-deed-dǣd.md | NOTE |
| 1990 | dill | dile | early_analogy | yes | source_material | - | dev_notes_slices/1990-dill-dile.md, model_entries/1990-dill-dile.model.md, model_entries/1990-dill-dile.model_implementation_report.md, model_entries/1990-dill-dile.source_ledger.md, packets/1990-dill-dile.md, research_memos/1990-dill-dile.md | NOTE, DERIVATION_CLASS=early_analogy |
| 1992 | door | dor | regular | yes | source_material | - | dev_notes_slices/1992-door-dor.md, model_entries/1992-door-dor.model.md, model_entries/1992-door-dor.model_implementation_report.md, model_entries/1992-door-dor.reviewer_checklist.md, model_entries/1992-door-dor.source_ledger.md, model_entries/2183-shoulder-sċuldrum.model.md, model_entries/2183-shoulder-sċuldrum.source_ledger.md, packets/1992-door-dor.md, research_memos/1992-door-dor.md | NOTE |
| 2003 | fare | faran | regular | yes | source_material | - | dev_notes_slices/2003-fare-faran.md, model_entries/2003-fare-faran.model.md, model_entries/2003-fare-faran.model_implementation_report.md, model_entries/2003-fare-faran.reviewer_checklist.md, model_entries/2003-fare-faran.source_ledger.md, packets/2003-fare-faran.md, research_memos/2003-fare-faran.md | NOTE |
| 2004 | fast | festan | early_analogy | yes | source_material | - | dev_notes_slices/2004-fast-festan.md, model_entries/2004-fast-festan.model.md, model_entries/2004-fast-festan.source_ledger.md, packets/2004-fast-festan.md, research_memos/2004-fast-festan.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2007 | fell | fell | regular | yes | source_material | - | dev_notes_slices/2007-fell-fell.md, model_entries/2007-fell-fell.model.md, model_entries/2007-fell-fell.model_implementation_report.md, model_entries/2007-fell-fell.reviewer_checklist.md, model_entries/2007-fell-fell.source_ledger.md, packets/2007-fell-fell.md, research_memos/2007-fell-fell.md, research_memos/batch_15_summary.md | NOTE |
| 2008 | fern | fearn | regular | yes | source_material | - | dev_notes_slices/2008-fern-fearn.md, model_entries/2008-fern-fearn.model.md, model_entries/2008-fern-fearn.model_implementation_report.md, model_entries/2008-fern-fearn.reviewer_checklist.md, model_entries/2008-fern-fearn.source_ledger.md, packets/2008-fern-fearn.md, research_memos/2008-fern-fearn.md | NOTE |
| 2009 | field | feld | regular | yes | source_material | - | dev_notes_slices/2009-field-feld.md, model_entries/2009-field-feld.model.md, model_entries/2009-field-feld.model_implementation_report.md, model_entries/2009-field-feld.reviewer_checklist.md, model_entries/2009-field-feld.source_ledger.md, packets/2009-field-feld.md, research_memos/2009-field-feld.md | NOTE |
| 2011 | find | fundene | late_analogy | yes | source_material | - | dev_notes_slices/2011-find-fundene.md, model_entries/2011-find-fundene.model.md, model_entries/2011-find-fundene.model_implementation_report.md, model_entries/2011-find-fundene.reviewer_checklist.md, model_entries/2011-find-fundene.source_ledger.md, packets/2011-find-fundene.md, research_memos/2011-find-fundene.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2016 | flask | flasce | early_analogy | no | source_material | - | dev_notes_slices/2016-flask-flasce.md, model_entries/2016-flask-flasce.model.md, model_entries/2016-flask-flasce.source_ledger.md, packets/2016-flask-flasce.md, research_memos/2016-flask-flasce.md | DERIVATION_CLASS=early_analogy |
| 2022 | fly | flēogan | regular | yes | source_material | - | dev_notes_slices/2022-fly-flēogan.md, model_entries/2022-fly-flēogan.model.md, model_entries/2022-fly-flēogan.model_implementation_report.md, model_entries/2022-fly-flēogan.reviewer_checklist.md, model_entries/2022-fly-flēogan.source_ledger.md, packets/2022-fly-flēogan.md, research_memos/2022-fly-flēogan.md | NOTE |
| 2027 | follow | fylġan | early_analogy | yes | source_material | - | dev_notes_slices/2027-follow-fylġan.md, model_entries/2027-follow-fylġan.model.md, model_entries/2027-follow-fylġan.model_implementation_report.md, model_entries/2027-follow-fylġan.reviewer_checklist.md, model_entries/2027-follow-fylġan.source_ledger.md, packets/2027-follow-fylġan.md, research_memos/2027-follow-fylġan.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2028 | forlorn | lēosan | regular | yes | source_material | - | dev_notes_slices/2028-forlorn-lēosan.md, model_entries/2028-forlorn-lēosan.model.md, model_entries/2028-forlorn-lēosan.model_implementation_report.md, model_entries/2028-forlorn-lēosan.reviewer_checklist.md, model_entries/2028-forlorn-lēosan.source_ledger.md, packets/2028-forlorn-lēosan.md, research_memos/2028-forlorn-lēosan.md | NOTE |
| 2030 | fowl | fugol | unexplained_unmodelled | yes | source_material | - | dev_notes_slices/2030-fowl-fugol.md, model_entries/2030-fowl-fugol.model.md, model_entries/2030-fowl-fugol.model_implementation_report.md, model_entries/2030-fowl-fugol.reviewer_checklist.md, model_entries/2030-fowl-fugol.source_ledger.md, research_memos/2030-fowl-fugol.md | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2034 | fright | fyrhte | late_analogy | yes | source_material | - | dev_notes_slices/2034-fright-fyrhte.md, model_entries/2034-fright-fyrhte.model.md, model_entries/2034-fright-fyrhte.model_implementation_report.md, model_entries/2034-fright-fyrhte.reviewer_checklist.md, model_entries/2034-fright-fyrhte.source_ledger.md, packets/2034-fright-fyrhte.md, research_memos/2034-fright-fyrhte.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2037 | gall | ġealla | early_analogy | no | source_material | - | dev_notes_slices/2037-gall-ġealla.md, model_entries/2037-gall-ġealla.model.md, model_entries/2037-gall-ġealla.source_ledger.md, packets/2037-gall-ġealla.md, research_memos/2037-gall-ġealla.md | DERIVATION_CLASS=early_analogy |
| 2038 | gang | gang | regular | yes | source_material | - | dev_notes_slices/2038-gang-gang.md, model_entries/2038-gang-gang.model.md, model_entries/2038-gang-gang.model_implementation_report.md, model_entries/2038-gang-gang.reviewer_checklist.md, model_entries/2038-gang-gang.source_ledger.md, model_entries/production_batch_08_report.md, packets/2038-gang-gang.md, research_memos/2038-gang-gang.md, research_memos/batch_17_summary.md | NOTE |
| 2041 | give | ġiefan | regular | yes | source_material | - | dev_notes_slices/2041-give-ġiefan.md, model_entries/2041-give-ġiefan.model.md, model_entries/2041-give-ġiefan.model_implementation_report.md, model_entries/2041-give-ġiefan.reviewer_checklist.md, model_entries/2041-give-ġiefan.source_ledger.md, packets/2041-give-ġiefan.md, research_memos/2041-give-ġiefan.md | NOTE |
| 2043 | gold | gold | regular | yes | source_material | - | dev_notes_slices/2043-gold-gold.md, model_entries/2043-gold-gold.model.md, model_entries/2043-gold-gold.model_implementation_report.md, model_entries/2043-gold-gold.reviewer_checklist.md, model_entries/2043-gold-gold.source_ledger.md, packets/2043-gold-gold.md, research_memos/2043-gold-gold.md | NOTE |
| 2046 | grave | grafan | regular | yes | source_material | - | dev_notes_slices/2046-grave-grafan.md, model_entries/2046-grave-grafan.model.md, model_entries/2046-grave-grafan.model_implementation_report.md, model_entries/2046-grave-grafan.reviewer_checklist.md, model_entries/2046-grave-grafan.source_ledger.md, packets/2046-grave-grafan.md, research_memos/2046-grave-grafan.md | NOTE |
| 2049 | guest | ġiest | regular | yes | source_material | - | dev_notes_slices/2049-guest-ġiest.md, model_entries/2049-guest-ġiest.model.md, model_entries/2049-guest-ġiest.model_implementation_report.md, model_entries/2049-guest-ġiest.reviewer_checklist.md, model_entries/2049-guest-ġiest.source_ledger.md, packets/2049-guest-ġiest.md, research_memos/2049-guest-ġiest.md | NOTE |
| 2051 | hair | hǣr | regular | yes | source_material | - | dev_notes_slices/2051-hair-hǣr.md, model_entries/2051-hair-hǣr.model.md, model_entries/2051-hair-hǣr.model_implementation_report.md, model_entries/2051-hair-hǣr.reviewer_checklist.md, model_entries/2051-hair-hǣr.source_ledger.md, packets/2051-hair-hǣr.md, research_memos/2051-hair-hǣr.md | NOTE |
| 2053 | hammer | hameres | late_analogy | yes | source_material | - | dev_notes_slices/2053-hammer-hameres.md, model_entries/2053-hammer-hameres.model.md, model_entries/2053-hammer-hameres.model_implementation_report.md, model_entries/2053-hammer-hameres.reviewer_checklist.md, model_entries/2053-hammer-hameres.source_ledger.md, packets/2053-hammer-hameres.md, research_memos/2053-hammer-hameres.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2057 | harvest | hierfest | regular | yes | source_material | - | dev_notes_slices/2057-harvest-hierfest.md, model_entries/2057-harvest-hierfest.model.md, model_entries/2057-harvest-hierfest.model_implementation_report.md, model_entries/2057-harvest-hierfest.reviewer_checklist.md, model_entries/2057-harvest-hierfest.source_ledger.md, research_memos/2057-harvest-hierfest.md | NOTE |
| 2058 | have | hæfeþ | late_analogy | yes | source_material | - | dev_notes_slices/2058-have-hæfeþ.md, model_entries/2058-have-hæfeþ.model.md, model_entries/2058-have-hæfeþ.model_implementation_report.md, model_entries/2058-have-hæfeþ.reviewer_checklist.md, model_entries/2058-have-hæfeþ.source_ledger.md, packets/2058-have-hæfeþ.md, research_memos/2058-have-hæfeþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2068 | heaven | heofon | early_analogy | yes | source_material | - | dev_notes_slices/2068-heaven-heofon.md, dev_notes_slices/deferred_sound_change_material.md, model_entries/2068-heaven-heofon.model.md, model_entries/2068-heaven-heofon.source_ledger.md, packets/2068-heaven-heofon.md, research_memos/2068-heaven-heofon.md, research_memos/batch_07_summary.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2069 | hedge | heġġ | regular | yes | source_material | - | dev_notes_slices/2069-hedge-heġġ.md, model_entries/2069-hedge-heġġ.model.md, model_entries/2069-hedge-heġġ.model_implementation_report.md, model_entries/2069-hedge-heġġ.reviewer_checklist.md, model_entries/2069-hedge-heġġ.source_ledger.md, packets/2069-hedge-heġġ.md, research_memos/2069-hedge-heġġ.md | NOTE |
| 2070 | helm | helm | regular | yes | source_material | - | dev_notes_slices/2070-helm-helm.md, model_entries/2070-helm-helm.model.md, model_entries/2070-helm-helm.model_implementation_report.md, model_entries/2070-helm-helm.reviewer_checklist.md, model_entries/2070-helm-helm.source_ledger.md, packets/2070-helm-helm.md, research_memos/2070-helm-helm.md | NOTE |
| 2071 | help | helpan | regular | yes | source_material | - | model_entries/2071-help-helpan.reviewer_checklist.md, research_memos/2071-help-helpan.md | NOTE |
| 2075 | hind | hind | regular | yes | source_material | - | dev_notes_slices/2075-hind-hind.md, model_entries/2075-hind-hind.model.md, model_entries/2075-hind-hind.model_implementation_report.md, model_entries/2075-hind-hind.reviewer_checklist.md, model_entries/2075-hind-hind.source_ledger.md, packets/2075-hind-hind.md, research_memos/2075-hind-hind.md | NOTE |
| 2077 | hold | healdan | regular | yes | source_material | - | dev_notes_slices/2077-hold-healdan.md, model_entries/2077-hold-healdan.model.md, model_entries/2077-hold-healdan.model_implementation_report.md, model_entries/2077-hold-healdan.reviewer_checklist.md, model_entries/2077-hold-healdan.source_ledger.md, research_memos/2077-hold-healdan.md | NOTE |
| 2082 | horn | horn | regular | yes | source_material | - | dev_notes_slices/2082-horn-horn.md, model_entries/2082-horn-horn.model.md, model_entries/2082-horn-horn.model_implementation_report.md, model_entries/2082-horn-horn.reviewer_checklist.md, model_entries/2082-horn-horn.source_ledger.md, model_entries/production_batch_09_report.md, packets/2082-horn-horn.md, packets/2251-thorn-þorn.md, production_backlog.md, research_memos/2082-horn-horn.md, research_memos/batch_21_summary.md, research_memos/batch_31_summary.md | NOTE |
| 2086 | knight | cniht | early_analogy | yes | source_material | - | dev_notes_slices/2086-knight-cniht.md, model_entries/2086-knight-cniht.model.md, model_entries/2086-knight-cniht.source_ledger.md, packets/2086-knight-cniht.md, research_memos/2086-knight-cniht.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2087 | knob | cnobba | reconstructed_oe | yes | source_material | - | dev_notes_slices/2087-knob-cnobba.md, model_entries/2087-knob-cnobba.model.md, model_entries/2087-knob-cnobba.model_implementation_report.md, model_entries/2087-knob-cnobba.reviewer_checklist.md, model_entries/2087-knob-cnobba.source_ledger.md, model_entries/pilot_batch_completion_report.md, model_entries/pilot_batch_revision_report.md, packets/2087-knob-cnobba.md, research_memos/2087-knob-cnobba.md | NOTE, DERIVATION_CLASS=reconstructed_oe |
| 2088 | lade | hladan | early_analogy | yes | source_material | - | dev_notes_slices/2088-lade-hladan.md, model_entries/2088-lade-hladan.model.md, model_entries/2088-lade-hladan.source_ledger.md, packets/2088-lade-hladan.md, research_memos/2088-lade-hladan.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2090 | lap | lappa | early_analogy | no | source_material | - | dev_notes_slices/2090-lap-lappa.md, model_entries/2090-lap-lappa.model.md, model_entries/2090-lap-lappa.source_ledger.md, model_entries/production_batch_02_report.md, packets/2090-lap-lappa.md, research_memos/2090-lap-lappa.md | DERIVATION_CLASS=early_analogy |
| 2092 | laugh | hliehhan | early_analogy | yes | source_material | - | dev_notes_slices/2092-laugh-hliehhan.md, model_entries/2092-laugh-hliehhan.model.md, model_entries/2092-laugh-hliehhan.source_ledger.md, packets/2092-laugh-hliehhan.md, research_memos/2092-laugh-hliehhan.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2093 | lead | lǣdan | regular | yes | source_material | - | dev_notes_slices/2093-lead-lǣdan.md, model_entries/2093-lead-lǣdan.model.md, model_entries/2093-lead-lǣdan.model_implementation_report.md, model_entries/2093-lead-lǣdan.reviewer_checklist.md, model_entries/2093-lead-lǣdan.source_ledger.md, packets/2093-lead-lǣdan.md, research_memos/2093-lead-lǣdan.md | NOTE |
| 2095 | learn | liornian | regular | yes | source_material | - | dev_notes_slices/2095-learn-liornian.md, model_entries/2095-learn-liornian.model.md, model_entries/2095-learn-liornian.model_implementation_report.md, model_entries/2095-learn-liornian.reviewer_checklist.md, model_entries/2095-learn-liornian.source_ledger.md, packets/2095-learn-liornian.md, research_memos/2095-learn-liornian.md, research_memos/batch_22_summary.md | NOTE |
| 2100 | lid | hlid | regular | yes | source_material | - | dev_notes_slices/2100-lid-hlid.md, model_entries/2100-lid-hlid.model.md, model_entries/2100-lid-hlid.model_implementation_report.md, model_entries/2100-lid-hlid.reviewer_checklist.md, model_entries/2100-lid-hlid.source_ledger.md, packets/2100-lid-hlid.md, research_memos/2100-lid-hlid.md | NOTE |
| 2102 | light | līehtan | regular | yes | source_material | - | dev_notes_slices/2102-light-līehtan.md, model_entries/2102-light-līehtan.model.md, model_entries/2102-light-līehtan.model_implementation_report.md, model_entries/2102-light-līehtan.reviewer_checklist.md, model_entries/2102-light-līehtan.source_ledger.md, research_memos/2102-light-līehtan.md | NOTE |
| 2104 | linden | lind | regular | yes | source_material | - | dev_notes_slices/2104-linden-lind.md, model_entries/2104-linden-lind.model.md, model_entries/2104-linden-lind.model_implementation_report.md, model_entries/2104-linden-lind.reviewer_checklist.md, model_entries/2104-linden-lind.source_ledger.md, model_entries/production_batch_10_report.md, packets/2104-linden-lind.md, research_memos/2104-linden-lind.md, research_memos/batch_23_summary.md | NOTE |
| 2107 | live | lifeþ | late_analogy | yes | source_material | - | dev_notes_slices/2107-live-lifeþ.md, model_entries/2107-live-lifeþ.model.md, model_entries/2107-live-lifeþ.reviewer_checklist.md, model_entries/2107-live-lifeþ.source_ledger.md, model_entries/production_batch_02_revision_report.md, packets/2107-live-lifeþ.md, research_memos/2107-live-lifeþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2109 | loam | lām | early_analogy | no | source_material | - | dev_notes_slices/2109-loam-lām.md, model_entries/2109-loam-lām.model.md, model_entries/2109-loam-lām.source_ledger.md, packets/2109-loam-lām.md, research_memos/2109-loam-lām.md | DERIVATION_CLASS=early_analogy |
| 2114 | lung | lungen | early_analogy | yes | source_material | - | dev_notes_slices/2114-lung-lungen.md, model_entries/2114-lung-lungen.model.md, model_entries/2114-lung-lungen.model_implementation_report.md, model_entries/2114-lung-lungen.source_ledger.md, packets/2114-lung-lungen.md, research_memos/2114-lung-lungen.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2119 | man | mannes | late_analogy | yes | source_material | - | dev_notes_slices/2119-man-mannes.md, model_entries/2119-man-mannes.model.md, model_entries/2119-man-mannes.source_ledger.md, research_memos/2119-man-mannes.md, research_memos/batch_08_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2120 | march | mearc | regular | yes | source_material | - | dev_notes_slices/2120-marrow-mearg.md, model_entries/2120-march-mearc.production_exception.md, model_entries/production_phase_close_audit.md, model_entries/production_phase_close_cleanup_01_report.md, packets/2120-march-mearc.md, research_memos/2120-march-mearc.md | NOTE |
| 2124 | meed | meorde | late_analogy | yes | source_material | - | dev_notes_slices/2124-meadow-mǣd.md, model_entries/2124-meed-meorde.model.md, model_entries/2124-meed-meorde.source_ledger.md, research_memos/2124-meed-meorde.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2126 | milk | meoloc | regular | yes | source_material | - | dev_notes_slices/2126-milk-meoloc.md, model_entries/2126-milk-meoloc.model.md, model_entries/2126-milk-meoloc.reviewer_checklist.md, model_entries/2126-milk-meoloc.source_ledger.md, packets/2126-milk-meoloc.md, research_memos/2126-milk-meoloc.md | NOTE |
| 2129 | mother | mōder | regular | yes | source_material | - | dev_notes_slices/2129-mother-mōder.md, model_entries/2129-mother-mōder.model_implementation_report.md, model_entries/2129-mother-mōder.reviewer_checklist.md, model_entries/2129-mother-mōder.source_ledger.md, research_memos/2129-mother-mōder.md | NOTE |
| 2133 | navel | nafola | early_analogy | yes | source_material | - | dev_notes_slices/2133-navel-nafola.md, model_entries/2133-navel-nafola.model.md, model_entries/2133-navel-nafola.model_implementation_report.md, model_entries/2133-navel-nafola.reviewer_checklist.md, model_entries/2133-navel-nafola.source_ledger.md, packets/2133-navel-nafola.md, packets/2186-show-sċēawian.md, research_memos/2133-navel-nafola.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2134 | neck | hnecca | early_analogy | no | source_material | - | dev_notes_slices/2134-neck-hnecca.md, model_entries/2134-neck-hnecca.model.md, model_entries/2134-neck-hnecca.source_ledger.md, packets/2134-neck-hnecca.md, research_memos/2134-neck-hnecca.md | DERIVATION_CLASS=early_analogy |
| 2136 | needle | nǣdl | early_analogy | yes | source_material | - | dev_notes_slices/2136-needle-nǣdl.md, model_entries/2136-needle-nǣdl.model.md, model_entries/2136-needle-nǣdl.model_implementation_report.md, model_entries/2136-needle-nǣdl.source_ledger.md, packets/2136-needle-nǣdl.md, research_memos/2136-needle-nǣdl.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2138 | net | nett | regular | yes | source_material | - | dev_notes_slices/2138-net-nett.md, model_entries/2138-net-nett.model.md, model_entries/2138-net-nett.model_implementation_report.md, model_entries/2138-net-nett.reviewer_checklist.md, model_entries/2138-net-nett.source_ledger.md, packets/2138-net-nett.md, research_memos/2138-net-nett.md | NOTE |
| 2140 | night | niht | late_analogy | yes | source_material | - | dev_notes_slices/2140-night-niht.md, model_entries/2140-night-niht.model.md, model_entries/2140-night-niht.model_implementation_report.md, model_entries/2140-night-niht.reviewer_checklist.md, model_entries/2140-night-niht.source_ledger.md, research_memos/2140-night-niht.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2141 | nightmare | mare | regular | yes | source_material | - | dev_notes_slices/2141-nightmare-mare.md, model_entries/2141-nightmare-mare.model.md, model_entries/2141-nightmare-mare.model_implementation_report.md, model_entries/2141-nightmare-mare.reviewer_checklist.md, model_entries/2141-nightmare-mare.source_ledger.md, packets/2141-nightmare-mare.md, research_memos/2141-nightmare-mare.md, research_memos/batch_25_summary.md | NOTE |
| 2143 | nose | nosu | early_analogy | no | source_material | - | dev_notes_slices/2143-nose-nosu.md, model_entries/2143-nose-nosu.model.md, model_entries/2143-nose-nosu.model_implementation_report.md, model_entries/2143-nose-nosu.reviewer_checklist.md, model_entries/2143-nose-nosu.source_ledger.md, packets/2143-nose-nosu.md, research_memos/2143-nose-nosu.md | DERIVATION_CLASS=early_analogy |
| 2152 | rest | ræste | late_analogy | yes | source_material | - | dev_notes_slices/2152-rest-ræste.md, model_entries/2152-rest-ræste.model.md, model_entries/2152-rest-ræste.model_implementation_report.md, model_entries/2152-rest-ræste.reviewer_checklist.md, model_entries/2152-rest-ræste.source_ledger.md, packets/2152-rest-ræste.md, research_memos/2152-rest-ræste.md, research_memos/batch_09_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2155 | coat | rocc | regular | yes | source_material | - | dev_notes_slices/2155-coat-rocc.md, model_entries/2155-coat-rocc.model.md, model_entries/2155-coat-rocc.model_implementation_report.md, model_entries/2155-coat-rocc.reviewer_checklist.md, model_entries/2155-coat-rocc.source_ledger.md, packets/2155-coat-rocc.md, research_memos/2155-coat-rocc.md | NOTE |
| 2162 | rust | rust | unexplained_unmodelled | yes | source_material | - | dev_notes_slices/2162-rust-rust.md, dev_notes_slices/PILOT_SUMMARY.md, model_entries/2162-rust-rust.model.md, model_entries/2162-rust-rust.model_implementation_report.md, model_entries/2162-rust-rust.reviewer_checklist.md, model_entries/2162-rust-rust.source_ledger.md, model_entries/production_batch_03_report.md, research_memos/2162-rust-rust.md, research_memos/batch_04_summary.md | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2168 | sap | sæp | early_analogy | yes | source_material | - | dev_notes_slices/2168-sap-sæp.md, model_entries/2168-sap-sæp.model.md, model_entries/2168-sap-sæp.model_implementation_report.md, model_entries/2168-sap-sæp.reviewer_checklist.md, model_entries/2168-sap-sæp.source_ledger.md, packets/2168-sap-sæp.md, research_memos/2168-sap-sæp.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2169 | sea | sǣ | early_analogy | yes | source_material | - | dev_notes_slices/2169-sea-sǣ.md, model_entries/2169-sea-sǣ.model.md, model_entries/2169-sea-sǣ.model_implementation_report.md, model_entries/2169-sea-sǣ.reviewer_checklist.md, model_entries/2169-sea-sǣ.source_ledger.md, model_entries/production_batch_04_report.md, model_entries/production_batch_04_revision_report.md, packets/2169-sea-sǣ.md, research_memos/2169-sea-sǣ.md, research_memos/batch_26_summary.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2179 | sheep | sċēap | regular | yes | source_material | - | dev_notes_slices/2179-sheep-sċēap.md, model_entries/2179-sheep-sċēap.model.md, model_entries/2179-sheep-sċēap.model_implementation_report.md, model_entries/2179-sheep-sċēap.reviewer_checklist.md, model_entries/2179-sheep-sċēap.source_ledger.md, packets/2179-sheep-sċēap.md, research_memos/2179-sheep-sċēap.md, research_memos/batch_27_summary.md | NOTE |
| 2181 | shilling | sċilling | regular | yes | source_material | - | dev_notes_slices/2181-shilling-sċilling.md, dev_notes_slices/2218-stilt-stilte.md, model_entries/2181-shilling-sċilling.model.md, model_entries/2181-shilling-sċilling.model_implementation_report.md, model_entries/2181-shilling-sċilling.reviewer_checklist.md, model_entries/2181-shilling-sċilling.source_ledger.md, packets/2181-shilling-sċilling.md, research_memos/2181-shilling-sċilling.md | NOTE |
| 2183 | shoulder | sċuldrum | late_analogy | yes | source_material | - | dev_notes_slices/2183-shoulder-sċuldrum.md, model_entries/2183-shoulder-sċuldrum.model_implementation_report.md, model_entries/2183-shoulder-sċuldrum.reviewer_checklist.md, packets/2183-shoulder-sċuldrum.md, research_memos/2183-shoulder-sċuldrum.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2184 | shove | sċēaf | late_analogy | yes | source_material | - | dev_notes_slices/2184-shove-sċēaf.md, model_entries/2184-shove-sċēaf.model.md, model_entries/2184-shove-sċēaf.model_implementation_report.md, model_entries/2184-shove-sċēaf.reviewer_checklist.md, model_entries/2184-shove-sċēaf.source_ledger.md, packets/2184-shove-sċēaf.md, research_memos/2184-shove-sċēaf.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2186 | show | sċēawian | regular | yes | source_material | - | dev_notes_slices/2186-show-sċēawian.md, model_entries/2186-show-sċēawian.model.md, model_entries/2186-show-sċēawian.model_implementation_report.md, model_entries/2186-show-sċēawian.reviewer_checklist.md, model_entries/2186-show-sċēawian.source_ledger.md, research_memos/2186-show-sċēawian.md | NOTE |
| 2189 | sieve | sife | early_analogy | no | source_material | - | dev_notes_slices/2189-sieve-sife.md, model_entries/2189-sieve-sife.model.md, model_entries/2189-sieve-sife.model_implementation_report.md, model_entries/2189-sieve-sife.reviewer_checklist.md, model_entries/2189-sieve-sife.source_ledger.md, packets/2189-sieve-sife.md, research_memos/2189-sieve-sife.md | DERIVATION_CLASS=early_analogy |
| 2196 | sleep | slǣpan | regular | yes | source_material | - | dev_notes_slices/2196-sleep-slǣpan.md, model_entries/2196-sleep-slǣpan.model.md, model_entries/2196-sleep-slǣpan.model_implementation_report.md, model_entries/2196-sleep-slǣpan.reviewer_checklist.md, model_entries/2196-sleep-slǣpan.source_ledger.md, packets/2196-sleep-slǣpan.md, research_memos/2196-sleep-slǣpan.md, research_memos/batch_28_summary.md | NOTE |
| 2198 | smear | smierwan | regular | yes | source_material | - | dev_notes_slices/2198-smear-smierwan.md, model_entries/2198-smear-smierwan.model.md, model_entries/2198-smear-smierwan.model_implementation_report.md, model_entries/2198-smear-smierwan.reviewer_checklist.md, model_entries/2198-smear-smierwan.source_ledger.md, research_memos/2198-smear-smierwan.md | NOTE |
| 2202 | span | spannan | regular | yes | source_material | - | dev_notes_slices/2202-span-spannan.md, model_entries/2202-span-spannan.model.md, model_entries/2202-span-spannan.model_implementation_report.md, model_entries/2202-span-spannan.reviewer_checklist.md, model_entries/2202-span-spannan.source_ledger.md, packets/2202-span-spannan.md, research_memos/2202-span-spannan.md | NOTE |
| 2204 | spar | spearra | regular | yes | source_material | - | dev_notes_slices/2204-spar-spearra.md, model_entries/2204-spar-spearra.model.md, model_entries/2204-spar-spearra.model_implementation_report.md, model_entries/2204-spar-spearra.reviewer_checklist.md, model_entries/2204-spar-spearra.source_ledger.md, packets/2204-spar-spearra.md, research_memos/2204-spar-spearra.md | NOTE |
| 2205 | spare | sparian | early_analogy | yes | source_material | - | dev_notes_slices/2205-spare-sparian.md, model_entries/2205-spare-sparian.model.md, model_entries/2205-spare-sparian.model_implementation_report.md, model_entries/2205-spare-sparian.reviewer_checklist.md, model_entries/2205-spare-sparian.source_ledger.md, packets/2205-spare-sparian.md, research_memos/2205-spare-sparian.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2212 | staff | stæf | early_analogy | yes | source_material | - | dev_notes_slices/2212-staff-stæf.md, model_entries/2212-staff-stæf.model.md, model_entries/2212-staff-stæf.model_implementation_report.md, model_entries/2212-staff-stæf.reviewer_checklist.md, model_entries/2212-staff-stæf.source_ledger.md, packets/2212-staff-stæf.md, research_memos/2212-staff-stæf.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2216 | stem | stefn | early_analogy | yes | source_material | - | dev_notes_slices/2216-stem-stefn.md, model_entries/2216-stem-stefn.model.md, model_entries/2216-stem-stefn.model_implementation_report.md, model_entries/2216-stem-stefn.reviewer_checklist.md, model_entries/2216-stem-stefn.source_ledger.md, packets/2216-stem-stefn.md, research_memos/2216-stem-stefn.md, research_memos/batch_29_summary.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2217 | still | stillan | regular | yes | source_material | - | dev_notes_slices/2217-still-stillan.md, model_entries/2217-still-stillan.model.md, model_entries/2217-still-stillan.model_implementation_report.md, model_entries/2217-still-stillan.reviewer_checklist.md, model_entries/2217-still-stillan.source_ledger.md, packets/2217-still-stillan.md, research_memos/2217-still-stillan.md | NOTE |
| 2227 | strew | strīeġan | reconstructed_oe | yes | source_material | - | dev_notes_slices/2227-strew-strīeġan.md, model_entries/2227-strew-strīeġan.model.md, model_entries/2227-strew-strīeġan.model_implementation_report.md, model_entries/2227-strew-strīeġan.reviewer_checklist.md, model_entries/2227-strew-strīeġan.source_ledger.md, research_memos/2227-strew-strīeġan.md | NOTE, DERIVATION_CLASS=reconstructed_oe |
| 2230 | summer | sumer | regular | yes | source_material | - | dev_notes_slices/2230-summer-sumer.md, model_entries/2230-summer-sumer.model.md, model_entries/2230-summer-sumer.model_implementation_report.md, model_entries/2230-summer-sumer.reviewer_checklist.md, model_entries/2230-summer-sumer.source_ledger.md, model_entries/production_batch_11_report.md, packets/2230-summer-sumer.md, research_memos/2230-summer-sumer.md | NOTE |
| 2232 | sunder | sundrian | regular | yes | source_material | - | dev_notes_slices/2232-sunder-sundrian.md, model_entries/2232-sunder-sundrian.model.md, model_entries/2232-sunder-sundrian.model_implementation_report.md, model_entries/2232-sunder-sundrian.reviewer_checklist.md, model_entries/2232-sunder-sundrian.source_ledger.md, packets/2232-sunder-sundrian.md, research_memos/2232-sunder-sundrian.md | NOTE |
| 2234 | swallow | swealwe | regular | yes | source_material | - | dev_notes_slices/2234-swallow-swealwe.md, model_entries/2234-swallow-swealwe.model.md, model_entries/2234-swallow-swealwe.model_implementation_report.md, model_entries/2234-swallow-swealwe.reviewer_checklist.md, model_entries/2234-swallow-swealwe.source_ledger.md, packets/2234-swallow-swealwe.md, research_memos/2234-swallow-swealwe.md | NOTE |
| 2235 | swan | swanes | early_analogy | no | source_material | - | dev_notes_slices/2235-swan-swanes.md, model_entries/2235-swan-swanes.model.md, model_entries/2235-swan-swanes.model_implementation_report.md, model_entries/2235-swan-swanes.reviewer_checklist.md, model_entries/2235-swan-swanes.source_ledger.md, packets/2235-swan-swanes.md, research_memos/2235-swan-swanes.md, research_memos/batch_30_summary.md | DERIVATION_CLASS=early_analogy |
| 2238 | swine | swīn | regular | yes | source_material | - | dev_notes_slices/2238-swine-swīn.md, model_entries/2238-swine-swīn.model.md, model_entries/2238-swine-swīn.model_implementation_report.md, model_entries/2238-swine-swīn.reviewer_checklist.md, model_entries/2238-swine-swīn.source_ledger.md, packets/2238-swine-swīn.md, research_memos/2238-swine-swīn.md | NOTE |
| 2242 | ten | tēon | attested_variant | yes | source_material | - | dev_notes_slices/2242-ten-tēon.md, model_entries/2242-ten-tēon.model.md, model_entries/2242-ten-tēon.model_implementation_report.md, model_entries/2242-ten-tēon.reviewer_checklist.md, model_entries/2242-ten-tēon.source_ledger.md, research_memos/2242-ten-tēon.md | NOTE, DERIVATION_CLASS=attested_variant |
| 2248 | think | þenċan | regular | yes | source_material | - | dev_notes_slices/2248-think-þenċan.md, model_entries/2248-think-þenċan.model.md, model_entries/2248-think-þenċan.model_implementation_report.md, model_entries/2248-think-þenċan.reviewer_checklist.md, model_entries/2248-think-þenċan.source_ledger.md, packets/2248-think-þenċan.md, research_memos/2248-think-þenċan.md | NOTE |
| 2251 | thorn | þorn | regular | yes | source_material | - | dev_notes_slices/2251-thorn-þorn.md, model_entries/2251-thorn-þorn.model.md, model_entries/2251-thorn-þorn.model_implementation_report.md, model_entries/2251-thorn-þorn.reviewer_checklist.md, model_entries/2251-thorn-þorn.source_ledger.md, research_memos/2251-thorn-þorn.md | NOTE |
| 2252 | thousand | þūsend | early_analogy | yes | source_material | - | dev_notes_slices/2252-thousand-þūsend.md, model_entries/2252-thousand-þūsend.model.md, model_entries/2252-thousand-þūsend.model_implementation_report.md, model_entries/2252-thousand-þūsend.reviewer_checklist.md, model_entries/2252-thousand-þūsend.source_ledger.md, packets/2252-thousand-þūsend.md, research_memos/2252-thousand-þūsend.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2254 | three | þrīe | attested_variant | yes | source_material | - | dev_notes_slices/2254-three-þrīe.md, model_entries/2254-three-þrīe.model.md, model_entries/2254-three-þrīe.model_implementation_report.md, model_entries/2254-three-þrīe.reviewer_checklist.md, model_entries/2254-three-þrīe.source_ledger.md, packets/2254-three-þrīe.md, research_memos/2254-three-þrīe.md, research_memos/batch_06_summary.md | NOTE, DERIVATION_CLASS=attested_variant |
| 2257 | tide | tīd | regular | yes | source_material | - | dev_notes_slices/2257-tide-tīd.md, model_entries/2257-tide-tīd.model.md, model_entries/2257-tide-tīd.model_implementation_report.md, model_entries/2257-tide-tīd.reviewer_checklist.md, model_entries/2257-tide-tīd.source_ledger.md, packets/2257-tide-tīd.md, research_memos/2257-tide-tīd.md | NOTE |
| 2258 | timber | timber | early_analogy | yes | source_material | - | dev_notes_slices/2258-timber-timber.md, model_entries/2258-timber-timber.model.md, model_entries/2258-timber-timber.model_implementation_report.md, model_entries/2258-timber-timber.reviewer_checklist.md, model_entries/2258-timber-timber.source_ledger.md, model_entries/production_batch_05_report.md, packets/2258-timber-timber.md, research_memos/2258-timber-timber.md, research_memos/batch_32_summary.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2260 | token | tācn | regular | yes | source_material | - | dev_notes_slices/2260-token-tācn.md, model_entries/2260-token-tācn.model.md, model_entries/2260-token-tācn.model_implementation_report.md, model_entries/2260-token-tācn.reviewer_checklist.md, model_entries/2260-token-tācn.source_ledger.md, research_memos/2260-token-tācn.md | NOTE |
| 2263 | town | tūn | regular | yes | source_material | - | dev_notes_slices/2263-town-tūn.md, model_entries/2263-town-tūn.model.md, model_entries/2263-town-tūn.model_implementation_report.md, model_entries/2263-town-tūn.reviewer_checklist.md, model_entries/2263-town-tūn.source_ledger.md, model_entries/production_batch_12_report.md, packets/2263-town-tūn.md, research_memos/2263-town-tūn.md | NOTE |
| 2266 | wade | wadan | regular | yes | source_material | - | dev_notes_slices/2266-wade-wadan.md, model_entries/2266-wade-wadan.model.md, model_entries/2266-wade-wadan.model_implementation_report.md, model_entries/2266-wade-wadan.reviewer_checklist.md, model_entries/2266-wade-wadan.source_ledger.md, packets/2266-wade-wadan.md, research_memos/2266-wade-wadan.md | NOTE |
| 2268 | wake | wacan | early_analogy | yes | source_material | - | dev_notes_slices/2268-wake-wacan.md, model_entries/2268-wake-wacan.model.md, model_entries/2268-wake-wacan.model_implementation_report.md, model_entries/2268-wake-wacan.reviewer_checklist.md, model_entries/2268-wake-wacan.source_ledger.md, packets/2268-wake-wacan.md, research_memos/2268-wake-wacan.md, research_memos/batch_33_summary.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2270 | warp | weorpan | regular | yes | source_material | - | dev_notes_slices/2270-warp-weorpan.md, model_entries/2270-warp-weorpan.model.md, model_entries/2270-warp-weorpan.model_implementation_report.md, model_entries/2270-warp-weorpan.reviewer_checklist.md, model_entries/2270-warp-weorpan.source_ledger.md, packets/2270-warp-weorpan.md, research_memos/2270-warp-weorpan.md | NOTE |
| 2272 | wash | wascan | regular | yes | source_material | - | dev_notes_slices/2272-wash-wascan.md, model_entries/2272-wash-wascan.model.md, model_entries/2272-wash-wascan.model_implementation_report.md, model_entries/2272-wash-wascan.reviewer_checklist.md, model_entries/2272-wash-wascan.source_ledger.md, packets/2272-wash-wascan.md, research_memos/2272-wash-wascan.md | NOTE |
| 2273 | wasp | wæfs | attested_variant | yes | source_material | - | dev_notes_slices/2273-wasp-wæfs.md, model_entries/2273-wasp-wæfs.model.md, model_entries/2273-wasp-wæfs.model_implementation_report.md, model_entries/2273-wasp-wæfs.reviewer_checklist.md, model_entries/2273-wasp-wæfs.source_ledger.md, packets/2273-wasp-wæfs.md, research_memos/2273-wasp-wæfs.md | NOTE, DERIVATION_CLASS=attested_variant |
| 2274 | water | wæter | early_analogy | yes | source_material | - | dev_notes_slices/2274-water-wæter.md, model_entries/2274-water-wæter.model.md, model_entries/2274-water-wæter.model_implementation_report.md, model_entries/2274-water-wæter.reviewer_checklist.md, model_entries/2274-water-wæter.source_ledger.md, packets/2274-water-wæter.md, research_memos/2274-water-wæter.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2276 | wax | weaxan | regular | yes | source_material | - | dev_notes_slices/2276-wax-weaxan.md, model_entries/2276-wax-weaxan.model.md, model_entries/2276-wax-weaxan.model_implementation_report.md, model_entries/2276-wax-weaxan.source_ledger.md, research_memos/2276-wax-weaxan.md | NOTE |
| 2277 | way | weġ | regular | yes | source_material | - | dev_notes_slices/2277-way-weġ.md, model_entries/2277-way-weġ.model.md, model_entries/2277-way-weġ.model_implementation_report.md, model_entries/2277-way-weġ.reviewer_checklist.md, model_entries/2277-way-weġ.source_ledger.md, packets/2277-way-weġ.md, research_memos/2277-way-weġ.md | NOTE |
| 2278 | weapon | wǣpn | regular | yes | source_material | - | dev_notes_slices/2278-weapon-wǣpn.md, model_entries/2278-weapon-wǣpn.model.md, model_entries/2278-weapon-wǣpn.model_implementation_report.md, model_entries/2278-weapon-wǣpn.reviewer_checklist.md, model_entries/2278-weapon-wǣpn.source_ledger.md, model_entries/production_batch_13_report.md, packets/2278-weapon-wǣpn.md, research_memos/2278-weapon-wǣpn.md | NOTE |
| 2284 | whale | hwæl | early_analogy | yes | source_material | - | dev_notes_slices/2284-whale-hwæl.md, model_entries/2284-whale-hwæl.model.md, model_entries/2284-whale-hwæl.model_implementation_report.md, model_entries/2284-whale-hwæl.reviewer_checklist.md, model_entries/2284-whale-hwæl.source_ledger.md, packets/2284-whale-hwæl.md, research_memos/2284-whale-hwæl.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2286 | whine | hwīnan | early_analogy | no | source_material | - | dev_notes_slices/2286-whine-hwīnan.md, model_entries/2286-whine-hwīnan.model.md, model_entries/2286-whine-hwīnan.source_ledger.md, model_entries/production_batch_05_revision_report.md, packets/2286-whine-hwīnan.md, research_memos/2286-whine-hwīnan.md | DERIVATION_CLASS=early_analogy |
| 2293 | will | willa | regular | yes | source_material | - | dev_notes_slices/2293-will-willa.md, model_entries/2293-will-willa.model.md, model_entries/2293-will-willa.model_implementation_report.md, model_entries/2293-will-willa.reviewer_checklist.md, model_entries/2293-will-willa.source_ledger.md, packets/2293-will-willa.md, research_memos/2293-will-willa.md | NOTE |
| 2294 | wind | windan | regular | yes | source_material | - | dev_notes_slices/2294-wind-windan.md, model_entries/2294-wind-windan.model.md, model_entries/2294-wind-windan.model_implementation_report.md, model_entries/2294-wind-windan.reviewer_checklist.md, model_entries/2294-wind-windan.source_ledger.md, packets/2294-wind-windan.md, research_memos/2294-wind-windan.md | NOTE |
| 2296 | withy | wīþiġ | early_analogy | yes | source_material | - | dev_notes_slices/2296-withy-wīþiġ.md, model_entries/2296-withy-wīþiġ.model.md, model_entries/2296-withy-wīþiġ.reviewer_checklist.md, model_entries/2296-withy-wīþiġ.source_ledger.md, packets/2296-withy-wīþiġ.md, research_memos/2296-withy-wīþiġ.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2297 | wold | weald | regular | yes | source_material | - | dev_notes_slices/2297-wold-weald.md, model_entries/2297-wold-weald.model.md, model_entries/2297-wold-weald.model_implementation_report.md, model_entries/2297-wold-weald.reviewer_checklist.md, model_entries/2297-wold-weald.source_ledger.md, research_memos/2297-wold-weald.md | NOTE |
| 2298 | wolf | wulf | unexplained_unmodelled | yes | source_material | - | dev_notes_slices/2298-wolf-wulf.md, model_entries/2298-wolf-wulf.model.md, model_entries/2298-wolf-wulf.reviewer_checklist.md, model_entries/2298-wolf-wulf.source_ledger.md, packets/2298-wolf-wulf.md, research_memos/2298-wolf-wulf.md | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2300 | wool | wull | unexplained_unmodelled | yes | source_material | - | dev_notes_slices/2300-wool-wull.md, model_entries/2300-wool-wull.model.md, model_entries/2300-wool-wull.model_implementation_report.md, model_entries/2300-wool-wull.reviewer_checklist.md, model_entries/2300-wool-wull.source_ledger.md, packets/2300-wool-wull.md, research_memos/2300-wool-wull.md | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2302 | world | weorold | early_analogy | yes | source_material | - | dev_notes_slices/2302-world-weorold.md, model_entries/2302-world-weorold.model.md, model_entries/2302-world-weorold.reviewer_checklist.md, model_entries/2302-world-weorold.source_ledger.md, packets/2302-world-weorold.md, research_memos/2302-world-weorold.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2305 | yarn | ġearn | regular | yes | source_material | - | dev_notes_slices/2305-yarn-ġearn.md, model_entries/2305-yarn-ġearn.model.md, model_entries/2305-yarn-ġearn.model_implementation_report.md, model_entries/2305-yarn-ġearn.reviewer_checklist.md, model_entries/2305-yarn-ġearn.source_ledger.md, packets/2305-yarn-ġearn.md, research_memos/2305-yarn-ġearn.md | NOTE |
| 2308 | youth | ġeoguþ | early_analogy | yes | source_material | - | dev_notes_slices/2308-youth-ġeoguþ.md, model_entries/2308-youth-ġeoguþ.model.md, model_entries/2308-youth-ġeoguþ.reviewer_checklist.md, model_entries/2308-youth-ġeoguþ.source_ledger.md, packets/2308-youth-ġeoguþ.md, research_memos/2308-youth-ġeoguþ.md, research_memos/batch_37_summary.md | NOTE, DERIVATION_CLASS=early_analogy |
| 2309 | make (iptv.2sg) | maca | late_analogy | yes | source_material | - | dev_notes_slices/2309-make-iptv-2sg-maca.md, model_entries/2309-make-(iptv.2sg)-maca.reviewer_checklist.md, model_entries/2309-make-(iptv.2sg)-maca.source_ledger.md, model_entries/2310-make-(3sg)-macaþ.model.md, packets/2309-make-(iptv.2sg)-maca.md, research_memos/2309-make-(iptv.2sg)-maca.md, research_memos/batch_11_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2310 | make (3sg) | macaþ | late_analogy | yes | source_material | - | dev_notes_slices/2310-make-(3sg)-macaþ.md, model_entries/2310-make-(3sg)-macaþ.reviewer_checklist.md, packets/2310-make-(3sg)-macaþ.md, research_memos/2310-make-(3sg)-macaþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2311 | bore (iptv.2sg) | bora | late_analogy | yes | source_material | - | dev_notes_slices/2311-bore-(iptv.2sg)-bora.md, model_entries/2311-bore-(iptv.2sg)-bora.model.md, model_entries/2311-bore-(iptv.2sg)-bora.model_implementation_report.md, model_entries/2311-bore-(iptv.2sg)-bora.reviewer_checklist.md, model_entries/2311-bore-(iptv.2sg)-bora.source_ledger.md, model_entries/2312-bore-(3sg)-boraþ.model.md, packets/2311-bore-(iptv.2sg)-bora.md, research_memos/2311-bore-(iptv.2sg)-bora.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2312 | bore (3sg) | boraþ | late_analogy | yes | source_material | - | dev_notes_slices/2312-bore-(3sg)-boraþ.md, model_entries/2312-bore-(3sg)-boraþ.model_implementation_report.md, model_entries/2312-bore-(3sg)-boraþ.reviewer_checklist.md, model_entries/2312-bore-(3sg)-boraþ.source_ledger.md, research_memos/2312-bore-(3sg)-boraþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2313 | learn (iptv.2sg) | liorna | late_analogy | yes | source_material | - | dev_notes_slices/2313-learn-iptv-2sg-liorna.md, model_entries/2313-learn-(iptv.2sg)-liorna.model.md, model_entries/2313-learn-(iptv.2sg)-liorna.model_implementation_report.md, model_entries/2313-learn-(iptv.2sg)-liorna.reviewer_checklist.md, model_entries/2313-learn-(iptv.2sg)-liorna.source_ledger.md, model_entries/2314-learn-(3sg)-liornaþ.model.md, research_memos/2313-learn-(iptv.2sg)-liorna.md, research_memos/batch_12_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2314 | learn (3sg) | liornaþ | late_analogy | yes | source_material | - | dev_notes_slices/2314-learn-(3sg)-liornaþ.md, model_entries/2314-learn-(3sg)-liornaþ.model_implementation_report.md, model_entries/2314-learn-(3sg)-liornaþ.reviewer_checklist.md, model_entries/2314-learn-(3sg)-liornaþ.source_ledger.md, research_memos/2314-learn-(3sg)-liornaþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2315 | lick (iptv.2sg) | licca | late_analogy | yes | source_material | - | dev_notes_slices/2315-lick-iptv-2sg-licca.md, model_entries/2315-lick-(iptv.2sg)-licca.model_implementation_report.md, model_entries/2315-lick-(iptv.2sg)-licca.reviewer_checklist.md, model_entries/2315-lick-(iptv.2sg)-licca.source_ledger.md, packets/2315-lick-(iptv.2sg)-licca.md, research_memos/2315-lick-(iptv.2sg)-licca.md, research_memos/batch_13_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2316 | lick (3sg) | liccaþ | late_analogy | yes | source_material | - | dev_notes_slices/2316-lick-(3sg)-liccaþ.md, model_entries/2316-lick-(3sg)-liccaþ.model_implementation_report.md, model_entries/2316-lick-(3sg)-liccaþ.reviewer_checklist.md, model_entries/2316-lick-(3sg)-liccaþ.source_ledger.md, research_memos/2316-lick-(3sg)-liccaþ.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2317 | show (iptv.2sg) | sċēawa | late_analogy | yes | source_material | - | dev_notes_slices/2317-show-(iptv.2sg)-sċēawa.md, model_entries/2317-show-(iptv.2sg)-sċēawa.model.md, model_entries/2317-show-(iptv.2sg)-sċēawa.model_implementation_report.md, model_entries/2317-show-(iptv.2sg)-sċēawa.reviewer_checklist.md, model_entries/2317-show-(iptv.2sg)-sċēawa.source_ledger.md, model_entries/production_batch_06_report.md, packets/2317-show-(iptv.2sg)-sċēawa.md, research_memos/2317-show-(iptv.2sg)-sċēawa.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2318 | show (3sg) | sċēawaþ | late_analogy | yes | source_material | - | dev_notes_slices/2318-show-(3sg)-sċēawaþ.md, model_entries/2318-show-(3sg)-sċēawaþ.model.md, model_entries/2318-show-(3sg)-sċēawaþ.model_implementation_report.md, model_entries/2318-show-(3sg)-sċēawaþ.reviewer_checklist.md, model_entries/2318-show-(3sg)-sċēawaþ.source_ledger.md, research_memos/2318-show-(3sg)-sċēawaþ.md, research_memos/batch_14_summary.md | NOTE, DERIVATION_CLASS=late_analogy |
| 2322 | who | hwā | regular | yes | source_material | - | model_entries/2322-who-hwā.model.md, model_entries/2322-who-hwā.source_ledger.md, research_memos/2322-who-hwā.md | NOTE |
| 2326 | you | ēow | regular | yes | source_material | - | model_entries/2326-you-ēow.model.md, model_entries/2326-you-ēow.source_ledger.md, research_memos/2326-you-ēow.md | NOTE |
| 2330 | thought | þōhte | regular | yes | source_material | - | model_entries/2330-thought-þōhte.model.md, model_entries/2330-thought-þōhte.source_ledger.md, packets/2330-thought-þōhte.md, research_memos/2330-thought-þōhte.md | NOTE |
| 2332 | hue | hīew | regular | yes | source_material | - | model_entries/2332-hue-hīew.model.md, model_entries/2332-hue-hīew.source_ledger.md, research_memos/2332-hue-hīew.md | NOTE |

## Required rows with no source material found

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage category | Production status | Production report / source-material path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2055 | handle | handlian | regular | yes | none | - | - | NOTE |
| 2327 | wound | wundude | regular | yes | none | - | - | NOTE |
| 2328 | sow | sāwan | regular | yes | none | - | - | NOTE |
| 2329 | betray | lǣwan | regular | yes | none | - | - | NOTE |

## Regular rows with empty NOTE and no report required

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage category | Production status | Production report / source-material path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2127 | month | mōnaþ | regular | no | none | - | - | none |

## Regular rows with empty NOTE but supporting material present

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage category | Production status | Production report / source-material path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1933 | adder | nǣdre | regular | no | manifest_format_test | format_test | pilot/adder.md | none |
| 1937 | barrow | beorg | regular | no | source_material | - | dev_notes_slices/1937-barrow-beorg.md | none |
| 1938 | bast | bæst | regular | no | source_material | - | dev_notes_slices/1938-bast-bæst.md | none |
| 1939 | bath | bæþ | regular | no | source_material | - | dev_notes_slices/1939-bath-bæþ.md | none |
| 1940 | beard | beard | regular | no | source_material | - | dev_notes_slices/1940-beard-beard.md | none |
| 1941 | beaver | befer | regular | no | source_material | - | dev_notes_slices/1941-beaver-befer.md, dev_notes_slices/1994-dove-dūfe.md | none |
| 1944 | believe | ġelīefan | regular | no | source_material | - | dev_notes_slices/1944-believe-ġelīefan.md | none |
| 1945 | belly | bielġ | regular | no | source_material | - | dev_notes_slices/1945-belly-bielġ.md | none |
| 1950 | bind | bindan | regular | no | source_material | - | dev_notes_slices/1950-bind-bindan.md | none |
| 1952 | blood | blōd | regular | no | source_material | - | dev_notes_slices/1952-blood-blōd.md | none |
| 1953 | board | bord | regular | no | source_material | - | dev_notes_slices/1953-board-bord.md | none |
| 1955 | book | bōc | regular | no | source_material | - | dev_notes_slices/1955-book-bōc.md, model_entries/1955-book-bōc.model.md, model_entries/1955-book-bōc.model_implementation_report.md, model_entries/1955-book-bōc.reviewer_checklist.md, model_entries/1955-book-bōc.source_ledger.md | none |
| 1956 | bore | borian | regular | no | source_material | - | dev_notes_slices/1956-bore-borian.md | none |
| 1957 | bosom | bōsm | regular | no | source_material | - | dev_notes_slices/1957-bosom-bōsm.md | none |
| 1960 | bough | bōg | regular | no | source_material | - | dev_notes_slices/1960-bough-bōg.md | none |
| 1963 | bow | boga | regular | no | source_material | - | dev_notes_slices/1963-bow-boga.md | none |
| 1964 | bower | būr | regular | no | source_material | - | dev_notes_slices/1964-bower-būr.md | none |
| 1966 | bread | brēad | regular | no | source_material | - | dev_notes_slices/1966-bread-brēad.md | none |
| 1967 | break | brecan | regular | no | source_material | - | dev_notes_slices/1967-break-brecan.md | none |
| 1970 | bride | brȳd | regular | no | source_material | - | dev_notes_slices/1970-bride-brȳd.md | none |
| 1971 | bring | bringan | regular | no | source_material | - | dev_notes_slices/1971-bring-bringan.md | none |
| 1972 | brook | brūcan | regular | no | source_material | - | dev_notes_slices/1972-brook-brūcan.md | none |
| 1974 | burst | berstan | regular | no | source_material | - | dev_notes_slices/1974-burst-berstan.md | none |
| 1976 | chew | ċēowan | regular | no | source_material | - | dev_notes_slices/1976-chew-ċēowan.md | none |
| 1977 | climb | climban | regular | no | source_material | - | dev_notes_slices/1977-climb-climban.md | none |
| 1978 | comb | camb | regular | no | source_material | - | dev_notes_slices/1978-comb-camb.md | none |
| 1982 | crop | cropp | regular | no | source_material | - | dev_notes_slices/1982-crop-cropp.md | none |
| 1984 | dale | dæl | regular | no | source_material | - | dev_notes_slices/1984-dale-dæl.md | none |
| 1985 | day | dæġ | regular | no | source_material | - | dev_notes_slices/1985-day-dæġ.md | none |
| 1986 | deal | dǣl | regular | no | source_material | - | dev_notes_slices/1986-deal-dǣl.md | none |
| 1988 | deer | dēor | regular | no | source_material | - | dev_notes_slices/1988-deer-dēor.md | none |
| 1989 | dew | dēaw | regular | no | source_material | - | dev_notes_slices/1989-dew-dēaw.md | none |
| 1991 | do | dōn | regular | no | source_material | - | dev_notes_slices/1991-do-dōn.md | none |
| 1993 | dough | dāg | regular | no | source_material | - | dev_notes_slices/1993-dough-dāg.md | none |
| 1995 | dream | drēam | regular | no | source_material | - | dev_notes_slices/1995-dream-drēam.md | none |
| 1996 | drench | drenċ | regular | no | source_material | - | dev_notes_slices/1996-drench-drenċ.md | none |
| 1997 | drink | drincan | regular | no | source_material | - | dev_notes_slices/1997-drink-drincan.md | none |
| 1998 | drive | drīfan | regular | no | source_material | - | dev_notes_slices/1998-drive-drīfan.md | none |
| 1999 | earth | eorþe | regular | no | source_material | - | dev_notes_slices/1999-earth-eorþe.md | none |
| 2000 | eat | etan | regular | no | source_material | - | dev_notes_slices/2000-eat-etan.md | none |
| 2001 | eel | ǣl | regular | no | source_material | - | dev_notes_slices/2001-eel-ǣl.md | none |
| 2002 | fall | feallan | regular | no | source_material | - | dev_notes_slices/2002-fall-feallan.md | none |
| 2005 | father | fæder | regular | no | source_material | - | dev_notes_slices/2005-father-fæder.md | none |
| 2006 | fee | feoh | regular | no | source_material | - | dev_notes_slices/2006-fee-feoh.md | none |
| 2010 | fight | feohtan | regular | no | source_material | - | dev_notes_slices/2010-fight-feohtan.md | none |
| 2012 | finger | finger | regular | no | source_material | - | dev_notes_slices/2012-finger-finger.md | none |
| 2014 | fish | fisċ | regular | no | source_material | - | dev_notes_slices/2014-fish-fisċ.md | none |
| 2015 | fist | fȳst | regular | no | source_material | - | dev_notes_slices/2015-fist-fȳst.md | none |
| 2017 | flax | fleax | regular | no | source_material | - | dev_notes_slices/2017-flax-fleax.md | none |
| 2018 | flea | flēah | regular | no | source_material | - | dev_notes_slices/2018-flea-flēah.md, model_entries/2018-flea-flēah.model.md, model_entries/2018-flea-flēah.model_implementation_report.md, model_entries/2018-flea-flēah.reviewer_checklist.md, model_entries/2018-flea-flēah.source_ledger.md | none |
| 2019 | flee | flēon | regular | no | source_material | - | dev_notes_slices/2019-flee-flēon.md | none |
| 2020 | flesh | flǣsċ | regular | no | source_material | - | dev_notes_slices/2020-flesh-flǣsċ.md | none |
| 2021 | flood | flōd | regular | no | source_material | - | dev_notes_slices/2021-flood-flōd.md | none |
| 2023 | foal | fola | regular | no | source_material | - | dev_notes_slices/2023-foal-fola.md | none |
| 2024 | fodder | fōdor | regular | no | source_material | - | dev_notes_slices/2024-fodder-fōdor.md | none |
| 2025 | fold | fealdan | regular | no | source_material | - | dev_notes_slices/2025-fold-fealdan.md | none |
| 2026 | folk | folc | regular | no | source_material | - | dev_notes_slices/2026-folk-folc.md | none |
| 2029 | four | fēower | regular | no | source_material | - | dev_notes_slices/2029-four-fēower.md | none |
| 2031 | fox | fox | regular | no | source_material | - | dev_notes_slices/2031-fox-fox.md | none |
| 2032 | freeze | frēosan | regular | no | source_material | - | dev_notes_slices/2032-freeze-frēosan.md | none |
| 2033 | friend | frēond | regular | no | source_material | - | dev_notes_slices/2033-friend-frēond.md | none |
| 2035 | frost | forst | regular | no | source_material | - | dev_notes_slices/2035-frost-forst.md | none |
| 2036 | furrow | furh | regular | no | source_material | - | dev_notes_slices/2036-furrow-furh.md | none |
| 2039 | ghost | gāst | regular | no | source_material | - | dev_notes_slices/2039-ghost-gāst.md | none |
| 2040 | gift | ġift | regular | no | source_material | - | dev_notes_slices/2040-gift-ġift.md | none |
| 2042 | god | god | regular | no | source_material | - | dev_notes_slices/2042-god-god.md | none |
| 2044 | goose | gōs | regular | no | source_material | - | dev_notes_slices/2044-goose-gōs.md, model_entries/2044-goose-gōs.model.md, model_entries/2044-goose-gōs.model_implementation_report.md, model_entries/2044-goose-gōs.reviewer_checklist.md, model_entries/2044-goose-gōs.source_ledger.md | none |
| 2045 | grass | græs | regular | no | source_material | - | dev_notes_slices/2045-grass-græs.md | none |
| 2047 | gripe | grīpan | regular | no | source_material | - | dev_notes_slices/2047-gripe-grīpan.md | none |
| 2048 | ground | grund | regular | no | source_material | - | dev_notes_slices/2048-ground-grund.md | none |
| 2050 | hail | hæġl | regular | no | source_material | - | dev_notes_slices/2050-hail-hæġl.md | none |
| 2052 | hall | heall | regular | no | source_material | - | dev_notes_slices/2052-hall-heall.md | none |
| 2054 | hand | hand | regular | no | source_material | - | dev_notes_slices/2054-hand-hand.md, dev_notes_slices/2055-handle-handlian.md, packets/2055-handle-handlian.md, production_backlog_implementation_report.md, research_memos/2055-handle-handlian.md, research_memos/batch_19_summary.md | none |
| 2056 | harm | hearm | regular | no | source_material | - | dev_notes_slices/2056-harm-hearm.md | none |
| 2059 | haw | haga | regular | no | source_material | - | dev_notes_slices/2059-haw-haga.md | none |
| 2060 | hawk | hafoc | regular | no | source_material | - | dev_notes_slices/2060-hawk-hafoc.md | none |
| 2061 | hay | hīeġ | regular | no | source_material | - | dev_notes_slices/2061-hay-hīeġ.md | none |
| 2062 | hazel | hæsl | regular | no | source_material | - | dev_notes_slices/2062-hazel-hæsl.md | none |
| 2063 | head | hēafod | regular | no | source_material | - | dev_notes_slices/2063-head-hēafod.md | none |
| 2064 | heal | hǣlan | regular | no | source_material | - | dev_notes_slices/2064-heal-hǣlan.md | none |
| 2065 | heart | heorte | regular | no | source_material | - | dev_notes_slices/2065-heart-heorte.md | none |
| 2066 | hearth | heorþ | regular | no | source_material | - | dev_notes_slices/2066-hearth-heorþ.md | none |
| 2067 | heath | hǣþ | regular | no | source_material | - | dev_notes_slices/2067-heath-hǣþ.md | none |
| 2072 | help | help | regular | no | source_material | - | dev_notes_slices/2071-help-helpan.md, dev_notes_slices/2072-help-help.md, model_entries/2071-help-helpan.model.md, model_entries/2071-help-helpan.model_implementation_report.md, model_entries/2071-help-helpan.source_ledger.md, packets/2071-help-helpan.md, research_memos/batch_20_summary.md | none |
| 2073 | herd | heord | regular | no | source_material | - | dev_notes_slices/2073-herd-heord.md | none |
| 2074 | hew | hēawan | regular | no | source_material | - | dev_notes_slices/2074-hew-hēawan.md | none |
| 2076 | hoard | hord | regular | no | source_material | - | dev_notes_slices/2076-hoard-hord.md | none |
| 2078 | home | hām | regular | no | source_material | - | dev_notes_slices/2078-home-hām.md | none |
| 2079 | honey | huniġ | regular | no | source_material | - | dev_notes_slices/2079-honey-huniġ.md | none |
| 2080 | hood | hōd | regular | no | source_material | - | dev_notes_slices/2080-hood-hōd.md | none |
| 2081 | hoof | hōf | regular | no | source_material | - | dev_notes_slices/2081-hoof-hōf.md | none |
| 2083 | hound | hund | regular | no | source_material | - | dev_notes_slices/2083-hound-hund.md | none |
| 2084 | knead | cnedan | regular | no | source_material | - | dev_notes_slices/2084-knead-cnedan.md | none |
| 2085 | knee | cnēow | regular | no | source_material | - | dev_notes_slices/2085-knee-cnēow.md | none |
| 2089 | land | land | regular | no | source_material | - | dev_notes_slices/2089-land-land.md | none |
| 2091 | last | lǣstan | regular | no | source_material | - | dev_notes_slices/2091-last-lǣstan.md | none |
| 2094 | leaf | lēaf | regular | no | source_material | - | dev_notes_slices/2094-leaf-lēaf.md | none |
| 2096 | leather | leþer | regular | no | source_material | - | dev_notes_slices/2096-leather-leþer.md | none |
| 2097 | leek | lēac | regular | no | source_material | - | dev_notes_slices/2097-leek-lēac.md | none |
| 2098 | let | lǣtan | regular | no | source_material | - | dev_notes_slices/2098-let-lǣtan.md | none |
| 2099 | lick | liccian | regular | no | source_material | - | dev_notes_slices/2099-lick-liccian.md, model_entries/2315-lick-(iptv.2sg)-licca.model.md, model_entries/2316-lick-(3sg)-liccaþ.model.md | none |
| 2101 | life | līf | regular | no | source_material | - | dev_notes_slices/2101-life-līf.md | none |
| 2103 | lime | līm | regular | no | source_material | - | dev_notes_slices/2103-lime-līm.md | none |
| 2105 | line | līne | regular | no | source_material | - | dev_notes_slices/2105-line-līne.md | none |
| 2106 | list | līste | regular | no | source_material | - | dev_notes_slices/2106-list-līste.md | none |
| 2108 | liver | lifer | regular | no | source_material | - | dev_notes_slices/2108-liver-lifer.md | none |
| 2110 | loath | lāþ | regular | no | source_material | - | dev_notes_slices/2110-loath-lāþ.md | none |
| 2111 | lock | loc | regular | no | source_material | - | dev_notes_slices/1935-ball-beall.md, dev_notes_slices/1947-bid-bēodan.md, dev_notes_slices/1948-bid-bid.md, dev_notes_slices/2111-lock-loc.md, model_entries/1936-ban-bannes.source_ledger.md, model_entries/1946-berry-berġes.source_ledger.md, model_entries/1983-cud-cwedu.source_ledger.md, model_entries/1990-dill-dile.reviewer_checklist.md, model_entries/2004-fast-festan.model_implementation_report.md, model_entries/2004-fast-festan.reviewer_checklist.md, model_entries/2016-flask-flasce.model_implementation_report.md, model_entries/2016-flask-flasce.reviewer_checklist.md, model_entries/2037-gall-ġealla.model_implementation_report.md, model_entries/2037-gall-ġealla.reviewer_checklist.md, model_entries/2068-heaven-heofon.model_implementation_report.md, model_entries/2068-heaven-heofon.reviewer_checklist.md, model_entries/2086-knight-cniht.model_implementation_report.md, model_entries/2086-knight-cniht.reviewer_checklist.md, model_entries/2088-lade-hladan.model_implementation_report.md, model_entries/2088-lade-hladan.reviewer_checklist.md, model_entries/2090-lap-lappa.model_implementation_report.md, model_entries/2090-lap-lappa.reviewer_checklist.md, model_entries/2092-laugh-hliehhan.model_implementation_report.md, model_entries/2092-laugh-hliehhan.reviewer_checklist.md, model_entries/2107-live-lifeþ.model_implementation_report.md, model_entries/2109-loam-lām.model_implementation_report.md, model_entries/2109-loam-lām.reviewer_checklist.md, model_entries/2114-lung-lungen.reviewer_checklist.md, model_entries/2119-man-mannes.model_implementation_report.md, model_entries/2119-man-mannes.reviewer_checklist.md, model_entries/2124-meed-meorde.model_implementation_report.md, model_entries/2124-meed-meorde.reviewer_checklist.md, model_entries/2126-milk-meoloc.model_implementation_report.md, model_entries/2134-neck-hnecca.model_implementation_report.md, model_entries/2134-neck-hnecca.reviewer_checklist.md, model_entries/2136-needle-nǣdl.reviewer_checklist.md, model_entries/2286-whine-hwīnan.model_implementation_report.md, model_entries/2286-whine-hwīnan.reviewer_checklist.md, model_entries/2296-withy-wīþiġ.model_implementation_report.md, model_entries/2298-wolf-wulf.model_implementation_report.md, model_entries/2302-world-weorold.model_implementation_report.md, model_entries/2308-youth-ġeoguþ.model_implementation_report.md, model_entries/2310-make-(3sg)-macaþ.model_implementation_report.md, model_entries/citation_locator_closure_audit.md, model_entries/citation_locator_conditional_sources_report.md, model_entries/citation_locator_full_corpus_high_confidence_report.md, model_entries/citation_locator_pilot_01_report.md, model_entries/citation_locator_rescue_pilot_02_report.md, model_entries/citation_locator_source_inventory.md, research_memos/batch_24_summary.md, writing_skill/README.md, writing_skill/reviewer_checklist.md, writing_skill/source_ledger_template.md | none |
| 2112 | lock | locc | regular | no | source_material | - | dev_notes_slices/2112-lock-locc.md | none |
| 2113 | louse | lūs | regular | no | source_material | - | dev_notes_slices/2113-louse-lūs.md, model_entries/2113-louse-lūs.model.md, model_entries/2113-louse-lūs.model_implementation_report.md, model_entries/2113-louse-lūs.reviewer_checklist.md, model_entries/2113-louse-lūs.source_ledger.md | none |
| 2115 | lust | lust | regular | no | source_material | - | dev_notes_slices/2115-lust-lust.md | none |
| 2116 | lye | lēag | regular | no | source_material | - | dev_notes_slices/2116-lye-lēag.md | none |
| 2117 | make | macian | regular | no | source_material | - | dev_notes_slices/2117-make-macian.md, model_entries/2309-make-(iptv.2sg)-maca.model.md, model_entries/2310-make-(3sg)-macaþ.source_ledger.md | none |
| 2118 | malt | mealt | regular | no | source_material | - | dev_notes_slices/2118-malt-mealt.md | none |
| 2121 | mast | mæst | regular | no | source_material | - | dev_notes_slices/2121-mast-mæst.md | none |
| 2122 | meal | mǣl | regular | no | source_material | - | dev_notes_slices/2122-meal-mǣl.md, dev_notes_slices/2127-meal-melu.md | none |
| 2123 | mean | mǣnan | regular | no | source_material | - | dev_notes_slices/2123-mean-mǣnan.md | none |
| 2125 | might | miht | regular | no | source_material | - | dev_notes_slices/2125-meet-mētan.md | none |
| 2128 | mood | mōd | regular | no | source_material | - | dev_notes_slices/2128-mood-mōd.md, model_entries/2129-mother-mōder.model.md, packets/2129-mother-mōder.md | none |
| 2130 | nail | næġl | regular | no | source_material | - | dev_notes_slices/2130-nail-næġl.md | none |
| 2131 | name | nama | regular | no | source_material | - | dev_notes_slices/2131-name-nama.md | none |
| 2132 | nave | nafu | regular | no | source_material | - | dev_notes_slices/2132-nave-nafu.md | none |
| 2135 | need | nīed | regular | no | source_material | - | dev_notes_slices/2135-need-nīed.md | none |
| 2137 | nest | nest | regular | no | source_material | - | dev_notes_slices/2137-nest-nest.md | none |
| 2139 | nettle | netle | regular | no | source_material | - | dev_notes_slices/2139-nettle-netle.md | none |
| 2142 | nine | nigon | regular | no | source_material | - | dev_notes_slices/2142-nine-nigon.md | none |
| 2144 | one | ān | regular | no | source_material | - | dev_notes_slices/2144-one-ān.md | none |
| 2145 | oven | ofn | regular | no | source_material | - | dev_notes_slices/2145-oven-ofn.md | none |
| 2146 | ox | oxa | regular | no | source_material | - | dev_notes_slices/2146-ox-oxa.md | none |
| 2147 | rain | reġn | regular | no | source_material | - | dev_notes_slices/2147-rain-reġn.md | none |
| 2148 | rainbow | reġnboga | regular | no | source_material | - | dev_notes_slices/2148-rainbow-reġnboga.md | none |
| 2149 | raven | hræfn | regular | no | source_material | - | dev_notes_slices/2149-raven-hræfn.md | none |
| 2150 | read | rǣdan | regular | no | source_material | - | dev_notes_slices/2150-read-rǣdan.md | none |
| 2153 | ride | rīdan | regular | no | source_material | - | dev_notes_slices/2153-ride-rīdan.md | none |
| 2154 | rind | rind | regular | no | source_material | - | dev_notes_slices/2154-rind-rind.md | none |
| 2157 | rood | rōd | regular | no | source_material | - | dev_notes_slices/2157-rood-rōd.md | none |
| 2158 | room | rūm | regular | no | source_material | - | dev_notes_slices/2158-room-rūm.md | none |
| 2159 | rope | rāp | regular | no | source_material | - | dev_notes_slices/2159-rope-rāp.md | none |
| 2160 | rudder | rōþor | regular | no | source_material | - | dev_notes_slices/2160-rudder-rōþor.md | none |
| 2161 | run | rinnan | regular | no | source_material | - | dev_notes_slices/2161-run-rinnan.md | none |
| 2163 | rye | ryġe | regular | no | source_material | - | dev_notes_slices/2163-rye-ryġe.md | none |
| 2164 | sail | seġl | regular | no | source_material | - | dev_notes_slices/2164-sail-seġl.md | none |
| 2165 | sake | sacu | regular | no | source_material | - | dev_notes_slices/2165-sake-sacu.md | none |
| 2166 | salt | sealt | regular | no | source_material | - | dev_notes_slices/2166-salt-sealt.md | none |
| 2167 | salve | sealf | regular | no | source_material | - | dev_notes_slices/2167-salve-sealf.md | none |
| 2170 | seam | sēam | regular | no | source_material | - | dev_notes_slices/2170-seam-sēam.md | none |
| 2171 | seek | sēċan | regular | no | source_material | - | dev_notes_slices/2171-seek-sēċan.md | none |
| 2172 | send | sendan | regular | no | source_material | - | dev_notes_slices/2172-send-sendan.md | none |
| 2173 | set | settan | regular | no | source_material | - | dev_notes_slices/2173-set-settan.md | none |
| 2174 | seven | seofon | regular | no | source_material | - | dev_notes_slices/2174-seven-seofon.md | none |
| 2175 | shaft | sċeaft | regular | no | source_material | - | dev_notes_slices/2175-shaft-sċeaft.md | none |
| 2176 | shame | sċamu | regular | no | source_material | - | dev_notes_slices/2176-shame-sċamu.md | none |
| 2177 | shear | sċieran | regular | no | source_material | - | dev_notes_slices/2177-shear-sċieran.md | none |
| 2178 | sheath | sċēaþ | regular | no | source_material | - | dev_notes_slices/2178-sheath-sċēaþ.md | none |
| 2180 | shield | sċield | regular | no | source_material | - | dev_notes_slices/2180-shield-sċield.md | none |
| 2182 | shine | sċīnan | regular | no | source_material | - | dev_notes_slices/2182-shine-sċīnan.md | none |
| 2185 | shovel | sċofl | regular | no | source_material | - | dev_notes_slices/2185-shovel-sċofl.md | none |
| 2187 | shower | sċūr | regular | no | source_material | - | dev_notes_slices/2187-shower-sċūr.md | none |
| 2188 | side | sīde | regular | no | source_material | - | dev_notes_slices/2188-side-sīde.md | none |
| 2190 | sing | singan | regular | no | source_material | - | dev_notes_slices/2190-sing-singan.md | none |
| 2191 | singe | senġan | regular | no | source_material | - | dev_notes_slices/2191-singe-senġan.md | none |
| 2192 | sister | swester | regular | no | source_material | - | dev_notes_slices/2192-sister-swester.md | none |
| 2193 | sit | sittan | regular | no | source_material | - | dev_notes_slices/2193-sit-sittan.md | none |
| 2194 | six | six | regular | no | source_material | - | dev_notes_slices/2194-six-six.md | none |
| 2195 | slay | slēan | regular | no | source_material | - | dev_notes_slices/2195-slay-slēan.md | none |
| 2197 | slime | slīm | regular | no | source_material | - | dev_notes_slices/2197-slime-slīm.md | none |
| 2199 | snow | snāw | regular | no | source_material | - | dev_notes_slices/2199-snow-snāw.md | none |
| 2200 | sorrow | sorg | regular | no | source_material | - | dev_notes_slices/2200-sorrow-sorg.md | none |
| 2201 | soul | sāwol | regular | no | source_material | - | dev_notes_slices/2201-soul-sāwol.md | none |
| 2206 | spear | speoru | regular | no | source_material | - | dev_notes_slices/2206-spear-speoru.md, packets/2102-light-līehtan.md | none |
| 2207 | spin | spinnan | regular | no | source_material | - | dev_notes_slices/2207-spin-spinnan.md | none |
| 2208 | spindle | spinl | regular | no | source_material | - | dev_notes_slices/2208-spindle-spinl.md | none |
| 2209 | spoon | spōn | regular | no | source_material | - | dev_notes_slices/2209-spoon-spōn.md | none |
| 2210 | spread | sprǣdan | regular | no | source_material | - | dev_notes_slices/2210-spread-sprǣdan.md | none |
| 2211 | spur | spora | regular | no | source_material | - | dev_notes_slices/2211-spur-spora.md | none |
| 2213 | start | styrtan | regular | no | source_material | - | dev_notes_slices/2213-start-styrtan.md | none |
| 2214 | starve | steorfan | regular | no | source_material | - | dev_notes_slices/2214-starve-steorfan.md | none |
| 2215 | steal | stelan | regular | no | source_material | - | dev_notes_slices/2215-steal-stelan.md | none |
| 2219 | stock | stocc | regular | no | source_material | - | dev_notes_slices/2219-stock-stocc.md | none |
| 2220 | stone | stān | regular | no | source_material | - | dev_notes_slices/2220-stone-stān.md | none |
| 2221 | stool | stōl | regular | no | source_material | - | dev_notes_slices/2221-stool-stōl.md | none |
| 2222 | stork | storc | regular | no | source_material | - | dev_notes_slices/2222-stork-storc.md | none |
| 2223 | storm | storm | regular | no | source_material | - | dev_notes_slices/2223-storm-storm.md | none |
| 2224 | straw | strēaw | regular | no | source_material | - | dev_notes_slices/2224-straw-strēaw.md | none |
| 2225 | stream | strēam | regular | no | source_material | - | dev_notes_slices/2225-stream-strēam.md | none |
| 2226 | stretch | streċċan | regular | no | source_material | - | dev_notes_slices/2226-stretch-streċċan.md | none |
| 2228 | string | strenġ | regular | no | source_material | - | dev_notes_slices/2228-string-strenġ.md | none |
| 2229 | stud | stōd | regular | no | source_material | - | dev_notes_slices/2229-stud-stōd.md | none |
| 2231 | sun | sunne | regular | no | source_material | - | dev_notes_slices/2231-sun-sunne.md | none |
| 2233 | sup | sūpan | regular | no | source_material | - | dev_notes_slices/2233-sup-sūpan.md | none |
| 2236 | swell | swellan | regular | no | source_material | - | dev_notes_slices/2236-swell-swellan.md | none |
| 2237 | swim | swimman | regular | no | source_material | - | dev_notes_slices/2237-swim-swimman.md | none |
| 2239 | sword | sweord | regular | no | source_material | - | dev_notes_slices/2239-sword-sweord.md | none |
| 2241 | team | tēam | regular | no | source_material | - | dev_notes_slices/2241-team-tēam.md | none |
| 2243 | thane | þeġn | regular | no | source_material | - | dev_notes_slices/2243-thane-þeġn.md | none |
| 2244 | thanks | þanc | regular | no | source_material | - | dev_notes_slices/2244-thanks-þanc.md | none |
| 2245 | thatch | þæc | regular | no | source_material | - | dev_notes_slices/2245-thatch-þæc.md | none |
| 2246 | thief | þēof | regular | no | source_material | - | dev_notes_slices/2246-thief-þēof.md | none |
| 2247 | thing | þing | regular | no | source_material | - | dev_notes_slices/2247-thing-þing.md | none |
| 2249 | thirst | þurst | regular | no | source_material | - | dev_notes_slices/2249-thirst-þurst.md | none |
| 2253 | thrash | þresċan | regular | no | source_material | - | dev_notes_slices/2253-thrash-þresċan.md | none |
| 2255 | thunder | þunor | regular | no | source_material | - | dev_notes_slices/2255-thunder-þunor.md | none |
| 2256 | tick | ticca | regular | no | source_material | - | dev_notes_slices/2256-tick-ticca.md | none |
| 2259 | toe | tā | regular | no | source_material | - | dev_notes_slices/2259-toe-tā.md, packets/2260-token-tācn.md | none |
| 2261 | tongs | tang | regular | no | source_material | - | dev_notes_slices/2261-tongs-tang.md | none |
| 2262 | tongue | tunge | regular | no | source_material | - | dev_notes_slices/2262-tongue-tunge.md | none |
| 2264 | tread | tredan | regular | no | source_material | - | dev_notes_slices/2264-tread-tredan.md | none |
| 2265 | trough | trog | regular | no | source_material | - | dev_notes_slices/2265-trough-trog.md | none |
| 2267 | wain | wæġn | regular | no | source_material | - | dev_notes_slices/2267-wain-wæġn.md | none |
| 2269 | warp | wearp | regular | no | source_material | - | dev_notes_slices/2269-warp-wearp.md | none |
| 2271 | wart | wearte | regular | no | source_material | - | dev_notes_slices/2271-wart-wearte.md | none |
| 2275 | wax | weax | regular | no | source_material | - | dev_notes_slices/2275-wax-weax.md, model_entries/2276-wax-weaxan.reviewer_checklist.md, packets/2276-wax-weaxan.md | none |
| 2279 | weasel | wesle | regular | no | source_material | - | dev_notes_slices/2279-weasel-wesle.md | none |
| 2280 | weather | weder | regular | no | source_material | - | dev_notes_slices/2280-weather-weder.md | none |
| 2281 | weave | wefan | regular | no | source_material | - | dev_notes_slices/2281-weave-wefan.md | none |
| 2282 | west | westene | regular | no | source_material | - | dev_notes_slices/2282-west-westene.md | none |
| 2283 | wether | weþer | regular | no | source_material | - | dev_notes_slices/2283-wether-weþer.md | none |
| 2285 | while | hwīl | regular | no | source_material | - | dev_notes_slices/2285-while-hwīl.md | none |
| 2287 | whore | hōre | regular | no | source_material | - | dev_notes_slices/2287-whore-hōre.md | none |
| 2288 | widow | wuduwe | regular | no | source_material | - | dev_notes_slices/2288-widow-wuduwe.md | none |
| 2289 | wield | wealdan | regular | no | source_material | - | dev_notes_slices/2289-wield-wealdan.md | none |
| 2290 | wife | wīf | regular | no | source_material | - | dev_notes_slices/2290-wife-wīf.md | none |
| 2291 | wight | wiht | regular | no | source_material | - | dev_notes_slices/2291-wight-wiht.md | none |
| 2292 | will | willan | regular | no | source_material | - | dev_notes_slices/2292-will-willan.md | none |
| 2295 | winter | winter | regular | no | source_material | - | dev_notes_slices/2295-winter-winter.md | none |
| 2299 | wonder | wundor | regular | no | source_material | - | dev_notes_slices/2299-wonder-wundor.md | none |
| 2301 | word | word | regular | no | source_material | - | dev_notes_slices/2301-word-word.md, packets/1936-ban-bannes.md, packets/1946-berry-berġes.md, packets/1969-breeches-brēċ.md, packets/1973-buck-bucc.md, packets/1981-craft-cræft.md, packets/1987-deed-dǣd.md, packets/2030-fowl-fugol.md, packets/2057-harvest-hierfest.md, packets/2077-hold-healdan.md, packets/2119-man-mannes.md, packets/2124-meed-meorde.md, packets/2140-night-niht.md, packets/2151-reek-rēac.md, packets/2162-rust-rust.md, packets/2198-smear-smierwan.md, packets/2227-strew-strīeġan.md, packets/2242-ten-tēon.md, packets/2250-thistle-þistles.md, packets/2297-wold-weald.md, packets/2312-bore-(3sg)-boraþ.md, packets/2313-learn-(iptv.2sg)-liorna.md, packets/2314-learn-(3sg)-liornaþ.md, packets/2316-lick-(3sg)-liccaþ.md, packets/2318-show-(3sg)-sċēawaþ.md, packets/2322-who-hwā.md, packets/2326-you-ēow.md, packets/2332-hue-hīew.md, writing_skill/book_entry_template.md | none |
| 2303 | worm | wyrm | regular | no | source_material | - | dev_notes_slices/2303-worm-wyrm.md | none |
| 2304 | wring | wringan | regular | no | source_material | - | dev_notes_slices/2304-wring-wringan.md | none |
| 2306 | year | ġēar | regular | no | source_material | - | dev_notes_slices/2306-year-ġēar.md | none |
| 2307 | yoke | ġeoc | regular | no | source_material | - | dev_notes_slices/2307-yoke-ġeoc.md | none |

## Rows with STATUS=format_test manifest entries

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage category | Production status | Production report / source-material path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1933 | adder | nǣdre | regular | no | manifest_format_test | format_test | pilot/adder.md | none |

## Ambiguous source-material file matches

- dev_notes_slices/2156-roe-hrogn.md -> ambiguous among 2111:loc, 2301:word
- dev_notes_slices/orphan_fragments.md -> ambiguous among 2068:heofon, 2139:netle, 2174:seofon
- model_entries/1942-beech-bōc.model_implementation_report.md -> ambiguous among 1942:bōc, 1955:bōc
- model_entries/2309-make-(iptv.2sg)-maca.model_implementation_report.md -> ambiguous among 2111:loc, 2309:maca
- model_entries/production_batch_14_report.md -> ambiguous among 1936:bannes, 1946:berġes, 2203:spanne
- research_memos/batch_03_summary.md -> ambiguous among 1946:berġes, 2013:fȳre, 2087:cnobba
- research_memos/batch_05_summary.md -> ambiguous among 1954:bān, 2144:ān, 2242:tēon
- research_memos/batch_16_summary.md -> ambiguous among 2008:fearn, 2016:flasce
- research_memos/batch_18_summary.md -> ambiguous among 2041:ġiefan, 2046:grafan
- research_memos/batch_34_summary.md -> ambiguous among 2274:wæter, 2275:weax, 2276:weaxan, 2278:wǣpn
- research_memos/batch_35_summary.md -> ambiguous among 2284:hwæl, 2286:hwīnan, 2293:willa
- research_memos/batch_36_summary.md -> ambiguous among 2297:weald, 2302:weorold, 2305:ġearn
- writing_skill/anti_patterns.md -> ambiguous among 1992:dor, 2054:hand, 2111:loc, 2301:word

## Unmatched source-material files

- packet_quality_notes.md

