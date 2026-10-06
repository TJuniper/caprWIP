# ARCHIVED: legacy generic agent workflow (not authoritative)

Purpose: keep the agent productive without thrashing, while avoiding “approve every tiny command”.

This file defines:
- what the agent is allowed to run without asking
- hard stop conditions that prevent loops
- a step-by-step workflow that forces reality checks before edits

---

## Non-negotiable evidence rule

You may not mark any checklist item DONE unless you paste:
1) the exact command you ran, and
2) 3–15 lines of its output (or the exit status).

If output is huge, show first 5 lines + last 5 lines.

If a step fails, you must diagnose that failure. Do not proceed to later steps.

---

## Container-only rule (stop thrash)

Any command that uses foma/flookup OR any Python script that shells out to them MUST run via:
  docker compose exec backend sh -lc 'cd /usr/app && <COMMAND>'

If you see any of these substrings:
  - FileNotFoundError: 'flookup'
  - flookup: not found
  - foma: not found
then STOP and return to Step 1 (environment sanity). Do not propose code changes.

---

## “Run” definition

A “run” means a single assistant turn / message.

---

## Response format (EVERY message)

1) Goal (1 sentence)  
2) Hypothesis (1 sentence, max 1 per run)  
3) Evidence (bullets; each bullet includes command + 1–2 key output lines)  
4) Next batch to run (1–5 commands) and what success looks like  
   - If a needed command is Tier 3, STOP and ask for approval before running it.

---

## Command autonomy tiers

The agent may execute Tier 1 and Tier 2 commands without asking.
Tier 3 commands always require explicit user approval first.

### Tier 1 (read-only inspection)
Allowed automatically, in batches:
- `pwd`, `ls -la`, `stat`, `head`, `tail`, `cat` (no redirects), `rg`, `find` (non-destructive)
- `git status -sb`, `git diff`, `git diff --stat`, `git log -n 10 --oneline --decorate`
- `docker info`
- `docker compose ps`, `docker compose logs --tail <N>`
- `docker compose exec <svc> sh -lc '<read-only commands only>'`

### Tier 2 (build/test/runtime, no source edits)
Allowed automatically, in batches, but must respect budgets and stop rules:
- the project’s canonical build commands (`make …`, `./scripts/...`, `npm test`, etc.)
- `docker compose up -d` (only if `docker compose ps` shows nothing running)
- `foma … info`, `flookup …`, report generation commands

### Tier 3 (mutating or risky)
Always ask first:
- any file edits (including `apply_patch`, `sed -i`, `perl -pi`, scripts that write files)
- any `git add`, `git commit`, `git push`, branching, resets, checkouts
- any command with write sinks or destructive ops: `>`, `>>`, `tee`, `rm`, `mv`

#### Tier 3 detection rule
If the command contains any of:
`>`, `>>`, `tee`, `sed -i`, `perl -pi`, `apply_patch`, `rm `, `mv `,
`git add`, `git commit`, `git push`, `git reset`, `git checkout`, `git switch`
then it is Tier 3.

---

## Hard limits (prevents hell loops)

- Max 1 hypothesis per run.
- Max 1 patch per run.
- Max 25 lines changed per patch (excluding whitespace).
- Max 2 retries per command. If still failing, STOP and report outputs + best diagnosis.
- Max 10 commands per step.
- Max 30 commands per run.
- Max 2 identical failures in a row (same key error substring). Then STOP and diagnose.
- No broad refactors, no cleanup, no renames unless required by the current hypothesis.
- Never run the same command twice unless a prerequisite has changed (example: Docker started).

### No ping-pong rule
Do not alternate between two probes (example: `docker compose ps` and `docker info`) more than once.
If a probe indicates a missing prerequisite, the next action must address that prerequisite directly.

---

## Checkpoints (when to ask)

Ask before:
- any Tier 3 command
- any action that would discard work (reset, clean, checkout, deleting files)
- any commit, ever (commits only when user explicitly requests)

---

# Workflow checklist

----------------------------------------------------------------------
## STEP 0 — Establish reality (must be first)

0.1 Show where we are (Tier 1):
- Command: `pwd`
- Command: `ls -la`

DONE when both commands are shown with output.

0.2 Show repo status (Tier 1):
- Command: `git status -sb`

DONE when output is shown.

If Step 0 cannot be completed, STOP.

----------------------------------------------------------------------
## STEP 1 — Environment sanity (Docker + mounts)

1.1 Confirm docker compose works (Tier 1):
- Command: `docker compose ps`

DONE when output is shown.

1.2 Confirm container working directory + mounts (Tier 1):
Do not assume `/usr/app` layout.
- Command: `docker compose exec backend sh -lc 'pwd; ls -la /usr/app | head -n 50'`

DONE when output is shown.

1.3 Confirm the FST directory exists inside the container (Tier 1):
- Command:
  `docker compose exec backend sh -lc 'ls -la /usr/app/fsts || ls -la /usr/app/server/fsts || true'`

DONE when output is shown and you identify the correct existing path.

1.4 Confirm required tools exist inside the container (Tier 1):
- Command:
  `docker compose exec backend sh -lc 'command -v foma; command -v flookup; python3 --version'`

DONE when all are shown and both foma and flookup resolve to paths.
If either is missing, STOP (environment is not ready).

If Step 1 cannot be completed, STOP. Do not edit code.

----------------------------------------------------------------------
## STEP 2 — Build sanity (compile must be real + inspect artifacts)

2.1 Identify the canonical build command (Tier 1) if unknown:
- Command: `ls -la scripts Makefile package.json pyproject.toml`
- Command: `rg -n "foma|build.*fst|fsts" .`

DONE when you state the build command you will use (with evidence).

2.2 Clean rebuild the target FST(s) (Tier 2):
- Command: `<repo canonical build command>`

DONE when the build command is shown and exits successfully.

2.3 Inspect output bins with sizes + timestamps (Tier 1 or 2, whichever applies):
- Command: `docker compose exec backend sh -lc 'ls -lah <FST_BIN_DIR>/*.bin | tail -n +1'`
- Command: `docker compose exec backend sh -lc 'stat -c "%y %s %n" <FST_BIN_DIR>/*.bin | sort'`

DONE when output is shown.

2.4 Tiny-bin rule:
Anything < 1KB is “failed build until proven otherwise”.
If any tiny bins exist, treat Step 2 as FAILED and go to Step 2.5.

2.5 If tiny bins exist, prove the network is non-degenerate (Tier 2):
- Command:
  `docker compose exec backend sh -lc 'foma -q -e "load <PATH_TO_BIN>; info; quit"'`

DONE only when info output is shown and the network is not degenerate (not “a few states/arcs” unless expected).

If Step 2 fails, STOP. Do not generate reports.

----------------------------------------------------------------------
## STEP 3 — Minimal functional test (probe forms, no reports yet)

Pick EXACTLY 3 probe forms (two known-good + one known-bad). Freeze these for the run.

3.1 Run flookup with explicit stdin (Tier 2):
- Command:
  `docker compose exec backend sh -lc 'printf "%s\n" "<probe1>" "<probe2>" "<probe3>" | flookup -i <PATH_TO_BIN>'`

DONE when output is shown and at least one probe yields a nontrivial output
(not empty, not only “+?”, not only [PAD]/blank-equivalents).

If Step 3 fails, STOP. Do not generate reports.

----------------------------------------------------------------------
## STEP 4 — Only now: reports + single-issue patch

4.1 Generate the report ONCE and capture stdout/stderr (Tier 2):
- Command: `<report command>`
NOTE: Report commands must be executed via `docker compose exec backend ...` (never on host).

DONE when report output is shown.

4.2 Choose 3 failing items from the report and freeze them as regression tests:
- List them verbatim in your message.

4.3 Patch ONE issue (Tier 3, requires approval):
Before editing:
- Show: `git diff` (Tier 1) to confirm current baseline.

Patch:
- Make a minimal change (<= 25 lines changed excluding whitespace).
- Show: `git diff` of only the relevant hunk.

Then re-run:
- Step 2 (rebuild)
- Step 3 (same probes)
- Step 4.1 (report)
and verify at least 1 of the 3 frozen failing items improved with no regressions.

DONE when you can point to specific before/after for at least 1 of the 3 failing items.

Commits are not allowed unless the user explicitly requests a commit.

---

## FOMA-specific footgun guards (apply whenever touching .foma/.regex/.fst scripts)

A) Name-length truncation guard  
- Keep all foma network names <= 35 chars.
- If a generated name might exceed that, introduce a short stable alias and use it everywhere.
- After any alias change, prove it with `foma ... info` on the intended network.

B) “Commented out definition but still composed” guard  
- If a rule/transducer is disabled, its use must be disabled too.
- Add an explicit check (choose one):
  1) a build-time grep that fails if a disabled symbol is referenced, or
  2) replace disabled rules with explicit identity/no-op networks so composition still works

C) Build must fail loudly  
- Any build script must run with `set -e` (or equivalent) so undefined references stop the build.
- If the tooling cannot fail, add post-build validation (Step 2.5 becomes mandatory).

D) **Optional context trap (CRITICAL)**  
- In foma replacement rules, parentheses around the context make it **OPTIONAL**:
  ```foma
  # WRONG - applies everywhere because context is optional!
  {X} -> {Y} || _ (context)
  
  # CORRECT - context is required
  {X} -> {Y} || _ context
  ```
- This caused the A-restoration bug (2026-02-06): rule applied unconditionally for months.
- **Always test replacement rules with `apply down` on strings that should NOT transform.**
- When debugging "rule applies too broadly", check for extra parentheses FIRST.

---

## Local references policy

Search local docs before the web.
References live in:
- `docs/references/`
- `docs/REFERENCES.md`

---

## Sample behavior (good)

The agent should batch Tier 1 commands, then stop only at real checkpoints.

Example Step 0 message:
- Evidence includes outputs for:
  `pwd`
  `ls -la`
  `git status -sb`
- Next batch (1–5 commands) might be:
  `docker compose ps`
  `docker compose exec backend sh -lc 'pwd; ls -la /usr/app | head -n 50'`

If `docker compose ps` fails with “Cannot connect to the Docker daemon”,
the agent must STOP after reporting that output and say the prerequisite is:
“Start Docker Desktop / ensure daemon is running”.
It must not loop by re-running the same probe repeatedly.

---

ARCHIVED 2026-02: this generic debugging-autonomy workflow (command tiers,
Step 0-4 choreography, per-message response format, probe rituals) is no
longer an active instruction source. It conflicts with the Germanic
adjudication control plane. See docs/AGENTS.md for the current routing rule.
