# Short pre-w diphthongs and the retained j-created long tier

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

## SC033. Retained j-created long-diphthong representation (`OEEwLongDiphthong`) {#rule-OEEwLongDiphthong}

```foma
define OEEwLongDiphthong [
    {*e} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*i} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*é} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*í} {*w} -> {*ēo} {*w} || _ OEEwLongContext
];
```

The conditioner is now restricted to the second \emph{w} followed
by \emph{j}, not a general following vowel or weak ending:

```foma
define OEEwLongContext [{*w} {*j}];
```

*Hīew* 'hue' retains this j-created path, whereas *cneowe* does not
enter it. Campbell distinguishes the \emph{iwj} class from the
low-vowel \emph{awj} class and gives the West Saxon \emph{īew}
reflex [@Campbell1959, p. 46, §120.2].

The retained mapping is a disclosed representation component, not
a newly established historical \emph{ew} to long \emph{ēow} law.
Hue's selected e-vowel input still omits the separate earlier
raising assumed by the source's i-vowel account. Its successful
final spelling does not prove that omitted intermediate or date
this mapping to an independently demonstrated West Saxon event.
The stable rule label is retained for continuity, without assigning
the technical component an invented historical stage or confidence.

## SC106. Retained j-created glide residual (`OEJWWSimplification`) {#rule-OEJWWSimplification}

```foma
define OEJWWSimplification [
    {*w} {*w} -> {*w} || _ {*j}
];
```

This technical component simplifies hue's remaining \emph{wwj}
representation after promotion. It does not restore nominative
\emph{w} in knee and does not duplicate inherited short-Vww
reanalysis. The distinct endingless and inflected histories remain
visible even where later paradigm leveling makes their spellings
converge [@Campbell1959, pp. 45--47, 232--233;
@Fulk2018, p. 154].
