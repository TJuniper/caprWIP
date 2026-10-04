# Short pre-w diphthongs and the j-created glide chain

## Historical discussion

Ordinary diphthongization before singleton \emph{w} must be distinguished
from long diphthong formation in endingless forms and from the
independently created \emph{wwj} sequences. Their similar Old English
spellings do not establish one sound law assigning long quantity
before every retained vowel ending.

For *cneowe* 'knee (dat.sg.)', the regular pre-ending stem has short
\emph{eo}. Hogg explicitly identifies the dative as a short-diphthong
example, and Campbell and Luick distinguish its genitive and dative
from the long endingless form
[@HoggGrammar2011, pp. 21--22, 86, §§2.33, 5.22;
@Campbell1959, pp. 232--233, §584; @Luick1914, p. 139, §134].
Ringe and Taylor likewise distinguish short \emph{cneow-} before
syllabic endings from long endingless *cnēo* 'knee'. The final
\emph{w} of *cnēow* 'knee' is generalized from the obliques, not
retained by an unrestricted prevocalic lengthening law
[@RingeTaylor2014, pp. 187--188, 387, §§6.2.4, 7.2.4].

The selected comparison is therefore the dative *cneowe*, from the
constructed PGmc dative \emph{*knéwai}, while citation
\emph{*knéwą} remains the lexeme-level reconstruction. Fulk prefers
the \emph{*-ai} analysis for the West Germanic dative line but
discusses alternatives; the complete selected input is a paradigm
construction, not a quotation of a whole-word reconstruction
[@Fulk2018, p. 147, §7.8].

Its short diphthong is supplied by
[SC044 OEBreaking](#rule-OEBreaking), with the source's exclusion
before a following high front vocalic. Long quantity could later
spread from endingless forms into obliques, but that leveling is
not the selected short dative's sound-law history. Campbell describes
the extension; Ringe and Taylor qualify the knee quantity inference
because decisive verse evidence is elusive
[@Campbell1959, p. 233; @RingeTaylor2014, p. 387].

Earlier inherited-glide reanalysis is independently represented by
[SC031 OEWWSimplification](#rule-OEWWSimplification). Chew, dew,
four, hew and you complete its products through
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).
The operation below neither repeats that inherited event nor
implements the regular singleton history
[@RingeTaylor2014, pp. 41--42, 65--66, 171--175].

## SC033. J-created palatalized-glide reanalysis (`OEEwLongDiphthong`) {#rule-OEEwLongDiphthong}

```foma
define OEEwLongDiphthong [
    {*i} {*w} {*w} -> {*iu} {*w} || _ {*j},
    {*í} {*w} {*w} -> {*íu} {*w} || _ {*j}
];
```

*Hīew* 'hue' enters with inherited PGmc \emph{*xíwją}, following
Ringe and Taylor's explicit \emph{*hiwją}. Their palatalized geminate
develops through \emph{*iuw} before the separately realized long
diphthong. The conditioner is palatalized \emph{w}, carried here as
\emph{ww+j} and subsequently \emph{w+j}; this does not assert a
second independent phoneme where the authors leave the phonemic
analysis unclear [@RingeTaylor2014, pp. 53, 250].

Orel's \emph{*xewjan} and Kroonen's \emph{*heuja-} remain competing
e reconstructions, not earlier stages invented to reconcile the
authors. Their derivational explanations differ. The realized-i choice
uses the inherited raising account, not a later hue-specific law
[@Orel2003, pp. 171--172; @Kroonen2013, p. 224;
@Ringe2017, pp. 151--153; @Fulk2018, p. 59].
Campbell supports the contrasting \emph{iwj} outcome, but Fulk
questions traditional geminate dismantling and its consonantal
premises. The detailed lexical account preserves those objections
[@Campbell1959, p. 46; @Fulk2018, pp. 71--72, 126].

The stable component now supplies offglide reanalysis, not long
quantity. Singleton \emph{iwj}, nonpalatal \emph{iww}, unraised
\emph{ewwj} and the separate low-vowel \emph{awj} history are excluded.
Knee remains a short singleton-w comparison. No exact historical
date or independent confidence is fabricated for this support encoding.

## SC106. Retained j-created glide compatibility (`OEJWWSimplification`) {#rule-OEJWWSimplification}

```foma
define OEJWWSimplification [
    {*w} {*w} -> {*w} || _ {*j}
];
```

The unchanged technical operation remains composed for compatibility.
Hue's reanalysis already leaves a singleton glide, so it no longer
feeds this simplification. Absence of a current application does not
establish universal redundancy or a newly dated historical event.
It neither restores nominative \emph{w} in knee nor duplicates
earlier inherited short-Vww reanalysis.

## SC110. Palatalized-glide long-io realization (`OEJGlideIO`) {#rule-OEJGlideIO}

```foma
define OEJGlideIO [
    [{*iu}|{*íu}] -> {*īo} || _ {*w} {*j}
];
```

The palatalized-glide product realizes long \emph{īo}, not the
ordinary long \emph{ēo} supplied by
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).
Ringe and Taylor explicitly supply pre-OE long \emph{īow} and early
West Saxon long \emph{īew}; the retained semivowel still conditions
mutation [@RingeTaylor2014, p. 250].
Existing [SC055 OEIUmlaut](#rule-OEIUmlaut) supplies the latter
change. Ordinary inherited \emph{iu} without this palatal
conditioner remains outside the component, as does short
\emph{io}. This distinct realization does not adjudicate all the
inherited atomic and split-symbol clauses in
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).
