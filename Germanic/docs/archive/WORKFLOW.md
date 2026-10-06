# Germanic (OE) Working Procedures

**Current default phase (freeze 2026-05-09): lexical write-up and publication preparation.** Read `Germanic/docs/CANONICAL_STATE.md` first for authoritative current status and source hierarchy.

This file now primarily documents how to reopen or verify **sound-change / FST debugging** work if phonology needs to be revisited later.

## Default Research Practice: Three-Agent Source Audit

For any change that touches sound-change chronology, conditioning, or prosodic
tier (anything where “what do the standard grammars say?” matters), **default
to a three-agent parallel research audit** before proposing or implementing:

1. **German-language grammars agent** — Brunner, Bülbring, Luick, Kaluza,
   Sievers–Brunner, Ringe vol. 1 (where relevant).
2. **English-language grammars agent** — Campbell, Hogg, Hogg & Fulk,
   Fulk (comparative), Ringe & Taylor vol. 2, Minkova, Lass.
3. **Modeling / internal-docs agent** — reads our own `DEV_NOTES.md`,
   `prosodic_tier_research.md`, relevant FST definitions, and surveys
   computational/notational best practice for the issue at hand.

Launch them in parallel via `task` with `agent_type: explore` and
`mode: background`. Each gets a tightly scoped prompt asking for section
numbers, direct quotes, and an honest "the source does not address this"
when warranted.

After the three reports land, synthesize into a new `§N.N.N` subsection of
`DEV_NOTES.md` (research first), then run empirical probes against the FST
bins / TSV, append a `§N.N.N-probes` subsection, and only then propose an
implementation. This is the pattern used for §17.10.36-q3 (j-strengthening
after front diphthongs).

## Directory Structure
- `Germanic/fsts/germanic.txt` - Main FST source code
- `Germanic/data/germanic-aligned-final.tsv` - Proto → OE data
- `Germanic/tools/` - All utility scripts (mismatch reports, tracing, etc.)
- `Germanic/docs/debug_snapshots/` - Output reports
- `Germanic/docs/DEV_NOTES.md` - Development documentation and decisions

## Key Scripts in Germanic/tools/

| Script | Purpose | Usage |
|--------|---------|-------|
| `oe_mismatch_report.py` | **Primary mismatch report** | `docker compose exec backend python3 /usr/app/tools/oe_mismatch_report.py` |
| `trace_old_english_sandbox.py` | Trace single derivation | See below |
| `run_oe_reports.py` | Run all reports | `docker compose exec backend python3 /usr/app/tools/run_oe_reports.py` |

## Compiling the FST

**CRITICAL**: The FST file does NOT end with `quit`, so you MUST use `-e quit`:

```bash
docker compose exec backend bash -c "cd /usr/app && foma -q -l fsts/germanic.txt -e quit"
```

Takes ~2 minutes. Without `-e quit` it hangs forever at the interactive prompt.

## Running the Mismatch Report

```bash
docker compose exec backend python3 /usr/app/tools/oe_mismatch_report.py
```

Output: `Germanic/docs/debug_snapshots/oe_mismatch_report.txt`

## Testing a Single Derivation

```bash
# Apply-down (proto → surface)
docker compose exec backend bash -c "echo 'x a l d a n' | flookup old_english.bin"

# Apply-up (surface → proto) - use -i flag
docker compose exec backend bash -c "echo 'healdan' | flookup -i old_english.bin"
```

**Note**: Input uses spaces between characters, NO asterisk prefix.

## After Changing germanic.txt

1. Recompile FST: `docker compose exec backend bash -c "cd /usr/app && foma -q -l fsts/germanic.txt -e quit"`
2. Run mismatch report: `docker compose exec backend python3 /usr/app/tools/oe_mismatch_report.py`
3. Check output: `cat Germanic/docs/debug_snapshots/oe_mismatch_report.txt`

## After Changing TSV Data

1. No FST recompile needed
2. Just run mismatch report again

## Common Mistakes to Avoid

1. **Don't try to use the web API for reports** - use the Python scripts directly
2. **Don't forget `-e quit`** when running foma
3. **Don't wait synchronously for long tasks** - foma compilation is ~2 min, not 45 min
4. **Scripts are in `Germanic/tools/`** not `server/` or root

## Mismatch Fix Workflow

**IMPORTANT**: Never change the TSV without explicit user approval.

### Step 1: Run Mismatch Report
```bash
docker compose exec backend python3 /usr/app/tools/oe_mismatch_report.py
cat Germanic/docs/debug_snapshots/oe_mismatch_report.txt
```

### Step 2: Categorize Issues
The report groups mismatches into buckets:
- **no_output**: Form doesn't compile - grammar issue
- **Core phonology buckets**: breaking, i-umlaut, etc.
- **TSV/data fixes**: Wrong protoform or target

### Step 3: Research Before Fixing
For each mismatch, BEFORE proposing changes:

1. **Check the literature** - consult:
   - Campbell's OE Grammar
   - Fulk's Comparative Grammar
   - R/T vol.1 and vol.2
   - Kroonen's Etymological Dictionary
   
2. **Document findings** in Germanic/docs/DEV_NOTES.md:
   - What the sources say
   - What the sound change should be
   - Why the current output is wrong
   
3. **Trace the derivation** to understand where it goes wrong:
   ```bash
   docker compose exec backend python3 /usr/app/tools/trace_old_english_sandbox.py "protoform"
   ```

4. **Present options to user** with citations

### Step 4: Discuss with User
- Present the research findings
- Explain the options (FST rule fix vs TSV data fix)
- Get explicit approval before any TSV changes

### Step 5: Implement Fix
Only after user approval:
- If FST change: edit germanic.txt, recompile, rerun report
- If TSV change: edit TSV with full documentation in NOTES column

### What NOT to Do
- ❌ Change TSV without discussion
- ❌ Assume the fix without checking sources
- ❌ Skip documentation
- ❌ Make multiple changes without testing between them

## Input Format for FST

**Proto forms in the FST use concatenated characters, NOT space-separated:**
- ✓ Correct: `bakăną`, `funxwstiz`  
- ✗ Wrong: `b a k a n`, `f u n x w s t i z`

The TSV stores space-separated (column 2), but FST input is concatenated.

To test a derivation:
```bash
docker compose exec backend bash -c "cd /usr/app && foma -e 'load old_english.bin' -e 'down funxwstiz' -e 'quit'"
```

---

## Agent Notes (for AI assistants)

### Common Mistakes to Avoid

1. **ALWAYS use Docker** for compilation and mismatch reports:
   ```bash
   # CORRECT:
   docker compose exec backend bash -c "cd /usr/app && foma -q -l fsts/germanic.txt -e quit"
   docker compose exec backend python3 /usr/app/tools/oe_mismatch_report.py
   
   # WRONG (creates inconsistent .bin files):
   cd server && foma -q -f fsts/germanic.txt
   python3 server/tools/oe_mismatch_report.py
   ```

2. **Always include `-e quit`** when running foma. Without it, foma hangs at interactive prompt.

3. **Don't use `foma -l` or `source`** — use `foma -q -l file.txt -e quit` (load is a foma internal command, not a flag behavior).

4. **The .bin files in root vs server/** can get out of sync. Docker writes to `/usr/app/` which maps to `server/` in the repo.

5. **When mismatch counts seem inconsistent**, recompile using Docker and re-run the report.

### Quick Reference

```bash
# Compile (takes ~2 min)
docker compose exec backend bash -c "cd /usr/app && foma -q -l fsts/germanic.txt -e quit"

# Report
docker compose exec backend python3 /usr/app/tools/oe_mismatch_report.py

# Test single word
docker compose exec backend bash -c "echo 'b a k a n ą' | flookup old_english.bin"

# Check count
head -1 Germanic/docs/debug_snapshots/oe_mismatch_report.txt
```
