#!/bin/bash
# Import key manufacturing machines for testing
set -e

SIM_ID="echo_genesis_934"

echo "Importing manufacturing machines..."
echo "===================================="

# Metal working machines
python -m src.cli sim import --sim-id $SIM_ID --item casting_furnace_v0 --quantity 1 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item crucible_refractory --quantity 1 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item casting_mold_set --quantity 1 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item milling_machine_general_v0 --quantity 1 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item cutting_tools_general --quantity 1 --unit unit

# Add some aluminum ingots to test
python -m src.cli sim import --sim-id $SIM_ID --item aluminum_alloy_ingot --quantity 50 --unit kg

echo ""
echo "✓ Machines imported"
