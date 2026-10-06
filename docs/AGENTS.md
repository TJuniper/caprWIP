# Agent routing

There is no generic mandatory step choreography, per-message response
format, probe ritual, or command-approval tier in this repository. (An old
workflow of that kind is archived, non-authoritative, at
`docs/archive/legacy-agent-workflow.md`.)

An explicit user request to complete a task — including completing,
committing and pushing a Germanic sound-change adjudication — **is** the
authorization for the edits, commits and pushes it requires. No further
approval gate applies.

## Germanic sound-change adjudication (the default active workstream)

Use the narrow canonical interface. Do not search the repository, inspect
Docker mounts, locate `.bin` files, or run `foma`/`flookup` by hand.

1. `python3 Germanic/tools/adjudicate.py --next`
2. `python3 Germanic/tools/adjudicate.py SCNNN --prepare` — reading packet
3. `python3 Germanic/tools/adjudicate.py SCNNN --evidence` — rebuilds the
   FSTs in the container and prints the live firing census and witness
   pre/post forms
4. Investigate the scholarship; edit SOURCE files per
   `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md`
5. `python3 Germanic/tools/adjudicate.py SCNNN --finalize`
6. `cd Germanic/tests && python3 -m pytest -q`
7. Commit and push.

Start at `Germanic/docs/README.md` for what is SOURCE / GENERATED / ARCHIVE.

## Everything else

Follow `.github/copilot-instructions.md` and the user's instruction.
Anything that runs `foma`/`flookup` runs inside the backend container
(`docker compose exec -T backend ...`); for adjudication work this is
already encapsulated by `--evidence`.
