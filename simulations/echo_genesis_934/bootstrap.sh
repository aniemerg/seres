#!/bin/bash
# Bootstrap echo_genesis_934 with minimal imports
set -e

SIM_ID="echo_genesis_934"

echo "Bootstrapping simulation: $SIM_ID"
echo "======================================"
echo ""

# Import a starter labor bot to operate machines
echo "1. Importing starter labor bot..."
python -m src.cli sim import --sim-id $SIM_ID --item labor_bot_general_v0 --quantity 1 --unit unit

# Import critical components that have no recipes
echo "2. Importing components without recipes..."
python -m src.cli sim import --sim-id $SIM_ID --item harmonic_drive_reducer_medium --quantity 6 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item battery_backup_small --quantity 1 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item force_torque_sensor_6axis --quantity 1 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item safety_controller_plc --quantity 1 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item servo_drive_controller --quantity 6 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item touch_sensor_capacitive --quantity 2 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item cable_drag_chain --quantity 2 --unit unit
python -m src.cli sim import --sim-id $SIM_ID --item led_ring_light --quantity 2 --unit unit

echo ""
echo "✓ Bootstrap complete"
echo ""
echo "Imported items:"
python -m src.cli sim view-state --sim-id $SIM_ID
