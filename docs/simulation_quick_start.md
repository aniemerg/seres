# Simulation Quick Start Guide

**For**: Future Claude Code sessions starting new simulations

**Purpose**: Get up to speed quickly on how to design and run effective simulations based on past learnings.

---

## Step 1: Review Past Learnings (2-3 minutes)

Before starting ANY simulation, read these files in order:

1. **`docs/simulation_best_practices.md`** (5 min)
   - Skip to "Successful Simulation Patterns" section
   - Identify which pattern matches your goal
   - Note the "Common Bottlenecks" section

2. **`docs/simulation_learnings.json`** (programmatic) OR **`docs/simulation_learnings.md`** (human-readable)
   - Check "supply_chains" for items you plan to manufacture
   - Review "imports" to see what's commonly imported
   - Look for similar simulation names

3. **`src/simulation/cli.py`**
   - Quick reference for simulation API

---

## Step 2: Define Your Simulation Goal

Be specific about what you're testing:

❌ **Bad**: "Test building some stuff"
✅ **Good**: "Verify labor bot arm assembly from imported aluminum stock"

❌ **Bad**: "Test motor production"
✅ **Good**: "Build drive_motor_medium using only lunar-manufactured iron parts + imported electronics"

**Template**:
```
Simulation Goal: [one sentence description]
Success Criteria:
- [ ] [Specific output item] appears in inventory
- [ ] Total time < [X hours]
- [ ] No errors
- [ ] Only [Y items] imported (rest manufactured)
```

---

## Step 3: Map Dependencies

Use the KB to trace all dependencies:

```bash
# Find recipe for item
grep -r "target_item_id: robot_arm_link_aluminum" kb/recipes/

# View recipe inputs
cat kb/recipes/recipe_robot_arm_link_aluminum_v0.yaml

# Check if inputs have recipes
for item in aluminum_alloy_ingot fastener_kit_medium; do
  echo "=== $item ==="
  grep -l "target_item_id: $item" kb/recipes/*.yaml || echo "  → IMPORT"
done
```

**Create dependency tree** (example):
```
robot_arm_link_aluminum
├── aluminum_alloy_ingot
│   └── alumina_powder (from anorthite)
│       └── regolith_lunar_highlands
│           └── [IMPORT or mining process]
└── fastener_kit_medium
    └── [IMPORT - no lunar recipe yet]
```

**Decision**: Which items to import vs. manufacture?

---

## Step 4: Calculate Material Requirements

For EACH recipe in your dependency tree:

1. List input quantities
2. Multiply by number of units you plan to build
3. Add 20% buffer
4. Sum up totals

**Example**:
```
Goal: Build 1 robot_arm_link_aluminum

recipe_robot_arm_link_aluminum_v0:
  - aluminum_alloy_ingot: 10.0 kg
  - fastener_kit_medium: 1 unit

Totals needed:
  - aluminum_alloy_ingot: 10.0 × 1.2 = 12.0 kg
  - fastener_kit_medium: 1 × 1.2 = 2 units (round up)
```

If manufacturing aluminum from regolith:
```
aluminum_alloy_ingot (12 kg needed)
  ← recipe_aluminum_from_alumina_v0 (input: 15 kg alumina_powder)
    ← recipe_alumina_extraction_v0 (input: 30 kg regolith_lunar_highlands)
      ← mining_highlands_v0 (8 hours per 100 kg)

Total regolith needed: 30 kg
Mining time: ~2.5 hours
Processing time: ~8 hours
Total: ~10.5 hours before you can start arm fabrication
```

---

## Step 5: Write Simulation Script

Based on pattern from `simulation_best_practices.md`:

```bash
SIM_ID="example_sim"
python -m src.cli sim init --sim-id $SIM_ID
python -m src.cli sim import --sim-id $SIM_ID --item labor_bot_general_v0 --quantity 1 --unit unit
python -m src.cli sim run-recipe --sim-id $SIM_ID --recipe <recipe_id> --quantity 1
python -m src.cli sim preview --sim-id $SIM_ID --hours <hours>
python -m src.cli sim advance-time --sim-id $SIM_ID --hours <hours>
python -m src.cli sim view-state --sim-id $SIM_ID
```

---

## Step 6: Run and Monitor

Run commands directly in your shell:

```bash
cd /path/to/self-replicating-system-modeling
python -m src.cli sim view-state --sim-id $SIM_ID
python -m src.cli sim preview --sim-id $SIM_ID --hours <hours>
python -m src.cli sim advance-time --sim-id $SIM_ID --hours <hours>
```

**Monitor as it runs**:
- Check for error messages
- Use `python -m src.cli sim view-state --sim-id $SIM_ID` after each major step
- Verify inventory matches expectations

---

## Step 7: Analyze Results

After simulation completes:

```bash
# Generate analysis
python scripts/analysis/analyze_simulations.py robot_arm_test_dec21

# Review the report
cat docs/simulation_learnings.md | grep -A 20 "robot_arm_test_dec21"
```

**Questions to answer**:
- ✓ Did all recipes complete successfully?
- ✓ Did outputs appear in inventory?
- ✓ Were there any errors?
- ✓ How long did it take?
- ✓ What was imported vs. manufactured?

---

## Common Issues & Solutions

### Issue: "Insufficient [item]" error

**Cause**: Not enough materials imported OR dependent recipe didn't run yet

**Solution**:
```bash
python -m src.cli sim view-state --sim-id $SIM_ID
python -m src.cli sim import --sim-id $SIM_ID --item missing_item_id --quantity <n> --unit unit
python -m src.cli sim run-recipe --sim-id $SIM_ID --recipe recipe_name_v0 --quantity 1
```

### Issue: Recipe references non-existent process

**Cause**: Process ID in recipe doesn't match any KB process

**Solution**:
```bash
# Find correct process ID
grep -r "id: welding" kb/processes/

# Update recipe or use correct process_id
```

### Issue: "No such item" error

**Cause**: Item ID mismatch (e.g., `copper_metal` vs `copper_rod_ingot`)

**Solution**:
```bash
# Search KB for similar items
grep -r "copper" kb/items/materials/ | grep "^id:"

# Use exact ID from KB
```

### Issue: Simulation time way longer than expected

**Cause**: Didn't account for sequential dependencies

**Solution**:
- Use `python -m src.cli sim advance-time --sim-id $SIM_ID --hours <n>` to fast-forward
- Check process duration with `python -m src.cli sim view-state --sim-id $SIM_ID`
- Consider parallelizing independent processes

---

## Templates

### Component Test Template
```bash
SIM_ID="test_NAME_dec21"
python -m src.cli sim init --sim-id $SIM_ID
python -m src.cli sim import --sim-id $SIM_ID --item labor_bot_general_v0 --quantity 1 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item INPUT1 --quantity QTY1 --unit UNIT1
python -m src.cli sim run-recipe --sim-id $SIM_ID --recipe recipe_NAME_v0 --quantity 1
python -m src.cli sim preview --sim-id $SIM_ID --hours <hours>
python -m src.cli sim advance-time --sim-id $SIM_ID --hours <hours>
python -m src.cli sim view-state --sim-id $SIM_ID
```

### Assembly Test Template
```bash
SIM_ID="assembly_MACHINE_dec21"
python -m src.cli sim init --sim-id $SIM_ID
python -m src.cli sim import --sim-id $SIM_ID --item labor_bot_general_v0 --quantity 1 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item component1 --quantity 2 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item component2 --quantity 1 --unit kg

python -m src.cli sim run-recipe --sim-id $SIM_ID --recipe recipe_subassembly_A_v0 --quantity 1
python -m src.cli sim advance-time --sim-id $SIM_ID --hours <hours>
python -m src.cli sim run-recipe --sim-id $SIM_ID --recipe recipe_subassembly_B_v0 --quantity 1
python -m src.cli sim advance-time --sim-id $SIM_ID --hours <hours>
python -m src.cli sim run-recipe --sim-id $SIM_ID --recipe recipe_final_MACHINE_v0 --quantity 1
python -m src.cli sim advance-time --sim-id $SIM_ID --hours <hours>
python -m src.cli sim view-state --sim-id $SIM_ID
```

---

## Pro Tips

1. **Name simulations descriptively**: `motor_build_v2` better than `test_sim`
2. **Always import labor_bot first**: It's your base machine for almost everything
3. **Import 20% extra materials**: Avoid mid-simulation shortages
4. **Use `python -m src.cli sim view-state --sim-id $SIM_ID` liberally**: Check inventory after each milestone
5. **Test recipes individually first**: Before chaining them together
6. **Document your intent**: Add comments explaining what you're testing
7. **Check past simulations**: Someone may have already tested what you need
8. **Run analysis after**: `python scripts/analysis/analyze_simulations.py [sim_name]`

---

## Example: Full Walkthrough

**Goal**: Test manufacturing thermal_management_system for labor bot

**Step 1**: Review recipe
```bash
cat kb/recipes/recipe_thermal_management_system_v0.yaml
```

**Step 2**: Map dependencies
```
thermal_management_system
├── copper_rod_ingot (1.2 kg)
├── aluminum_alloy_ingot (1.0 kg)
└── deionized_water (0.05 kg)
```

**Step 3**: Check if inputs have recipes
```bash
grep "target_item_id: copper_rod_ingot" kb/recipes/*.yaml    # Has recipe
grep "target_item_id: aluminum_alloy_ingot" kb/recipes/*.yaml # Has recipe
grep "target_item_id: deionized_water" kb/recipes/*.yaml     # Has recipe
```

**Step 4**: Decision - Import vs manufacture?
- For quick test: IMPORT all inputs
- For full chain: MANUFACTURE from regolith (adds ~50 hours)

**Step 5**: Write script (import strategy)
```bash
SIM_ID="thermal_mgmt_test_dec21"
python -m src.cli sim init --sim-id $SIM_ID
python -m src.cli sim import --sim-id $SIM_ID --item labor_bot_general_v0 --quantity 1 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item copper_rod_ingot --quantity 1.5 --unit kg
python -m src.cli sim import --sim-id $SIM_ID --item aluminum_alloy_ingot --quantity 1.2 --unit kg
python -m src.cli sim import --sim-id $SIM_ID --item deionized_water --quantity 0.1 --unit kg
python -m src.cli sim run-recipe --sim-id $SIM_ID --recipe recipe_thermal_management_system_v0 --quantity 1
python -m src.cli sim preview --sim-id $SIM_ID --hours <hours>
python -m src.cli sim advance-time --sim-id $SIM_ID --hours <hours>
python -m src.cli sim view-state --sim-id $SIM_ID
```

**Step 7**: Analyze
```bash
python scripts/analysis/analyze_simulations.py thermal_mgmt_test_dec21
```

---

## Next Steps

After your simulation succeeds:

1. **Document learnings**: Add to `simulation_best_practices.md` if you discovered something new
2. **Update supply chains**: If you tested a new production chain, document it
3. **Share insights**: Note any bottlenecks or optimization opportunities
4. **Iterate**: Try more complex variants (e.g., manufacture inputs instead of importing)

---

**Remember**: The goal isn't just to run simulations, but to learn what works, what's efficient, and what's realistic for lunar manufacturing bootstrapping!
