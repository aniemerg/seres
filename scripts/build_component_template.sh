#!/bin/bash
# Template for building components using CLI commands
#
# Usage:
#   ./scripts/build_component_template.sh <sim_id> <component_name> <recipe_id>
#
# Example:
#   ./scripts/build_component_template.sh motor_build drive_motor_medium recipe_drive_motor_medium_v1
#
# This template demonstrates the standard workflow for building components
# using the base_builder CLI commands. Customize the imports section for
# your specific component's requirements.

set -e  # Exit on any error

# Arguments
SIM_ID=${1:-"build_$(date +%s)"}
COMPONENT=${2:-"drive_motor_medium"}
RECIPE=${3:-"recipe_${COMPONENT}_v1"}

echo "================================================================================"
echo "COMPONENT BUILD - $COMPONENT"
echo "================================================================================"
echo "Simulation ID: $SIM_ID"
echo "Recipe: $RECIPE"
echo ""

# Helper function for CLI commands
cmd() {
    python -m base_builder.cli_commands "$@"
}

# Step 1: View initial state
echo "=== Step 1: Initial State ==="
cmd view-state --sim-id $SIM_ID || echo "(New simulation)"
echo ""

# Step 2: Import bootstrap equipment
echo "=== Step 2: Importing Bootstrap Equipment ==="
echo "Importing labor bots..."
cmd import --sim-id $SIM_ID --item labor_bot_general_v0 --quantity 2 --unit unit

echo "Importing machines..."
cmd import --sim-id $SIM_ID --item stamping_press_basic --quantity 1 --unit unit
cmd import --sim-id $SIM_ID --item coil_winding_machine --quantity 1 --unit unit
cmd import --sim-id $SIM_ID --item press_brake_v0 --quantity 1 --unit unit
echo ""

# Step 3: Import materials
# ⚠️ CUSTOMIZE THIS SECTION FOR YOUR COMPONENT
echo "=== Step 3: Importing Materials ==="
echo "NOTE: In production, replace these imports with ISRU processing!"
echo ""

echo "Importing raw materials..."
cmd import --sim-id $SIM_ID --item electrical_steel_sheet --quantity 40 --unit kg
cmd import --sim-id $SIM_ID --item aluminum_wire --quantity 28.4 --unit kg
cmd import --sim-id $SIM_ID --item iron_metal_pure --quantity 25 --unit kg
cmd import --sim-id $SIM_ID --item coil_insulation_material --quantity 1.4 --unit kg

echo ""
echo "Importing components..."
cmd import --sim-id $SIM_ID --item bearing_set_heavy --quantity 4 --unit kg
cmd import --sim-id $SIM_ID --item fastener_kit_medium --quantity 1 --unit kg
echo ""

# Step 4: Check inventory before build
echo "=== Step 4: Pre-Build Inventory ==="
cmd view-state --sim-id $SIM_ID | grep -A 50 "Inventory"
echo ""

# Step 5: Build component using recipe
echo "=== Step 5: Running Recipe ==="
echo "Building $COMPONENT using recipe $RECIPE..."
cmd run-recipe --sim-id $SIM_ID --recipe $RECIPE --quantity 1
echo ""

# Step 6: Preview time advancement
echo "=== Step 6: Preview ==="
echo "Previewing what will happen in next 19 hours..."
cmd preview --sim-id $SIM_ID --hours 19
echo ""

# Step 7: Execute - advance time
echo "=== Step 7: Executing (advancing time) ==="
echo "Advancing time by 19 hours to complete production..."
cmd advance-time --sim-id $SIM_ID --hours 19
echo ""

# Step 8: Verify component was built
echo "=== Step 8: Final State ==="
echo "Checking for $COMPONENT in inventory..."
cmd view-state --sim-id $SIM_ID | grep -i "$COMPONENT" || echo "⚠️  Component not found in inventory"
echo ""

echo "================================================================================"
echo "✓ Build sequence complete!"
echo "================================================================================"
echo ""
echo "View full state: python -m base_builder.cli_commands view-state --sim-id $SIM_ID"
echo "Simulation logs: simulations/$SIM_ID/simulation.jsonl"
echo ""

# Summary
echo "=== Summary ==="
cmd view-state --sim-id $SIM_ID | grep "Total mass"
echo ""
