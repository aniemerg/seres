#!/usr/bin/env python3
"""
Build drive_motor_medium using the base_builder simulation.
"""

from base_builder.interactive import *

def main():
    print("=" * 80)
    print("DRIVE MOTOR MEDIUM - Production Sequence")
    print("=" * 80)

    # Initialize simulation
    print("\n1. Initializing simulation...")
    result = init_simulation('drive_motor_build')
    print(f"   Status: {result['status']}")
    print(f"   Sim ID: {result['sim_id']}")

    # Check state
    print("\n2. Checking initial state...")
    state = view_state()
    print(f"   Time: {state['current_time_hours']} hours")
    print(f"   Inventory items: {len(state['inventory'])}")
    print(f"   Machines: {len(state['machines_built'])}")

    # Bootstrap: Import necessary equipment
    print("\n3. Importing bootstrap equipment...")

    # Import labor bots for operations
    print("   Importing labor_bot_general_v0...")
    result = import_item("labor_bot_general_v0", 2, "unit")
    print(f"   Result: {result}")

    # Import necessary machines for motor production
    print("   Importing press_brake_v0...")
    result = import_item("press_brake_v0", 1, "unit")
    print(f"   Result: {result}")

    print("   Importing stamping_press_basic...")
    result = import_item("stamping_press_basic", 1, "unit")
    print(f"   Result: {result}")

    print("   Importing coil_winding_machine...")
    result = import_item("coil_winding_machine", 1, "unit")
    print(f"   Result: {result}")

    # Import coil insulation (can't make from regolith)
    print("   Importing coil_insulation_material...")
    result = import_item("coil_insulation_material", 1.4, "kg")
    print(f"   Result: {result}")

    # Import/add the components we already made (from knowledge, not actually in inventory)
    # For this demo, we'll import them to simulate having built them
    print("\n4. Importing previously-built components...")
    print("   (Simulating bearing_set_heavy and fastener_kit_medium from previous session)")
    result = import_item("bearing_set_heavy", 4.0, "kg")
    print(f"   Result: {result}")

    result = import_item("fastener_kit_medium", 1.0, "kg")
    print(f"   Result: {result}")

    # Now we need materials for the motor components
    print("\n5. Importing raw materials (TODO: replace with ISRU mining/processing)...")

    # Electrical steel for laminations
    print("   Importing electrical_steel_sheet...")
    result = import_item("electrical_steel_sheet", 40.0, "kg")
    print(f"   Result: {result}")

    # Aluminum wire for coils
    print("   Importing aluminum_wire...")
    result = import_item("aluminum_wire", 28.4, "kg")
    print(f"   Result: {result}")

    # Iron for housing and shaft
    print("   Importing iron_metal_pure...")
    result = import_item("iron_metal_pure", 25.0, "kg")
    print(f"   Result: {result}")

    # Check state after imports
    print("\n6. Checking state after imports...")
    state = view_state()
    print(f"   Inventory items: {len(state['inventory'])}")
    print(f"   Total imports mass: {state.get('total_imports_mass_kg', 0):.1f} kg")

    # Now build the motor using the recipe
    print("\n7. Building drive_motor_medium using recipe...")
    print("   Running recipe_drive_motor_medium_v1...")

    try:
        result = run_recipe("recipe_drive_motor_medium_v1", quantity=1)
        print(f"   Result: {result}")

        # Get the duration from result
        duration = result.get('duration_hours', 19.0)
        print(f"   Recipe will take {duration} hours")

        # Preview what will happen
        print("\n8. Previewing production...")
        preview = preview_step(duration)
        print(f"   Preview: {preview[:500]}..." if len(str(preview)) > 500 else f"   Preview: {preview}")

        # Execute - advance time to complete the recipe
        print(f"\n9. Advancing time ({duration} hours)...")
        result = advance_time(duration)
        print(f"   Result: {result}")

    except Exception as e:
        print(f"   Error: {e}")
        import traceback
        traceback.print_exc()
        print("\n   Trying alternative: building from assembly process...")

        # Alternative: Use the assembly process directly
        try:
            result = start_process("drive_motor_medium_assembly_v0", scale=1, duration_hours=4)
            print(f"   Started process: {result}")

            # Preview what will happen
            print("\n8. Previewing assembly...")
            preview = preview_step(4)
            print(f"   Preview: {preview}")

            # Execute
            print("\n9. Advancing time (4 hours for assembly)...")
            result = advance_time(4)
            print(f"   Result: {result}")

        except Exception as e2:
            print(f"   Error with process: {e2}")
            import traceback
            traceback.print_exc()

    # Final state
    print("\n10. Final state...")
    state = view_state()
    print(f"   Time: {state['current_time_hours']} hours")
    print(f"   Inventory items: {len(state['inventory'])}")
    print(f"   Total imports: {state.get('total_imports_mass_kg', 0):.1f} kg")

    if 'inventory' in state:
        print("\n   Inventory:")
        for item_id, details in state['inventory'].items():
            if 'drive_motor' in item_id or 'motor' in item_id:
                print(f"     - {item_id}: {details}")

    print("\n" + "=" * 80)
    print("Production sequence complete!")
    print("=" * 80)

if __name__ == "__main__":
    main()
