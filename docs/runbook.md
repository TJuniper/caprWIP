# CAPR Runbook

Use this checklist when you need to bring the stack up, exercise the UI/FST
editor, and capture a regression snapshot. Combine it with the deeper guidance
in `SETUP.md` / `USAGE.md` as needed.

## 1. Start services
1. From the repo root, ensure Docker is available, then run:
   ```bash
   docker compose up -d
   ```
   - Expect backend on `http://127.0.0.1:5001` and frontend on `http://127.0.0.1:8080`.
2. Launch Caddy in a second terminal to stitch the API + UI together:
   ```bash
   caddy run --config Caddyfile.dev
   ```
   - Default proxy port is `:5002`; adjust in `Caddyfile.dev` if needed.

## 2. Load data in the UI
1. Visit `http://localhost:5002`.
2. Use the "Available input sources" dropdown to select your TSV file.
   - **Note:** Docker mounts `Germanic/` by default. To use Burmish, edit 
     `docker-compose.yml` volume mounts to point to `Burmish/` instead.
3. Confirm a matching FST text file exists in the mounted `fsts/` directory.
4. When starting from a blank FST, flip to the FST editor tab *before* pressing
   "Load" to avoid the broken board view (see `USAGE.md`).

## 3. Record work / hand off
1. Update `Germanic/docs/CURRENT_STATE.md` if the current phase or next
   task changed, and record sound-change adjudication work in the registry
   and memos per `Germanic/docs/sound_changes/registry/CONTROL_PLANE.md`.
   (`Germanic/docs/archive/DEV_NOTES.md` is an archived historical log —
   do not append to it.)
2. If you touched the FSTs, update status in `Germanic/docs/germanic_transducer_report.md`.

## 4. Tear down
When finished, shut the stack down:
```bash
caddy stop  # or Ctrl+C the running Caddy process
docker compose down
```

## 5. Germanic-specific operations

### Compile FST and run mismatch report
```bash
docker compose exec -T backend bash -c "cd /usr/app && foma -q -l fsts/germanic.txt -e quit"
docker compose exec -T backend python3 tools/oe_mismatch_report.py
```

### Check bin sync
```bash
docker compose exec -T backend python3 tools/oe_bin_sync_check.py
```

## 6. Foma syntax gotchas

### Optional vs required context (CRITICAL)
```foma
# WRONG - parentheses make context OPTIONAL, rule applies everywhere!
{X} -> {Y} || _ (context)

# CORRECT - context is required
{X} -> {Y} || _ context
```

### Testing contexts
Always test replacement rules with `apply down` on strings that should NOT match:
```foma
regex MyRule;
apply down {test_string_without_context}  # Should stay unchanged
apply down {test_string_with_context}     # Should transform
```

### Multichar symbols
Use brace tokens `{*u}{*n}` when testing; raw `*u*n` may not match intended symbols.
