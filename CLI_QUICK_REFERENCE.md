# CLI Quick Reference Card

## Basic Commands

```bash
# View state
python -m base_builder.cli_commands view-state --sim-id <sim>

# Import item
python -m base_builder.cli_commands import --sim-id <sim> --item <id> --quantity <n> --unit <unit>

# Start process
python -m base_builder.cli_commands start-process --sim-id <sim> --process <id> --duration <hours>

# Preview time
python -m base_builder.cli_commands preview --sim-id <sim> --hours <n>

# Advance time
python -m base_builder.cli_commands advance-time --sim-id <sim> --hours <n>

# List sims
python -m base_builder.cli_commands list
```

## Workflow Pattern

```bash
SIM="my_simulation"

# 1. Check state
python -m base_builder.cli_commands view-state --sim-id $SIM

# 2. Start process
python -m base_builder.cli_commands start-process --sim-id $SIM \
  --process <process_id> --scale 1 --duration <hours>

# 3. Preview (always!)
python -m base_builder.cli_commands preview --sim-id $SIM --hours <hours>

# 4. Execute
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours <hours>

# 5. Verify
python -m base_builder.cli_commands view-state --sim-id $SIM
```

## Common Examples

```bash
# Mine regolith
python -m base_builder.cli_commands start-process --sim-id $SIM \
  --process regolith_mining_highlands_v0 --duration 8
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours 8

# Import materials
python -m base_builder.cli_commands import --sim-id $SIM \
  --item carbon_anode --quantity 2 --unit kg

# Check inventory
python -m base_builder.cli_commands view-state --sim-id $SIM | grep <item>
```

For full documentation see: `docs/CLI_COMMANDS_GUIDE.md`
