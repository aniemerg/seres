"""
Integration tests for ADR-020 enhanced simulation engine.

Tests end-to-end workflow with:
- Event-driven scheduling
- Machine reservations
- Recipe orchestration
- Dependency-based execution
"""
from pathlib import Path

import pytest
import yaml

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine
from src.simulation.scheduler import EventType


@pytest.fixture
def kb_root(tmp_path):
    """Create minimal test KB."""
    kb = tmp_path / "kb"
    (kb / "processes").mkdir(parents=True)
    (kb / "recipes").mkdir(parents=True)
    (kb / "items" / "materials").mkdir(parents=True)
    (kb / "items" / "machines").mkdir(parents=True)
    (kb / "units").mkdir(parents=True)

    # Unit definitions (include kit/set in count units)
    with open(kb / "units" / "units.yaml", "w") as f:
        yaml.dump({
            "id": "unit_definitions_test_v0",
            "name": "Unit Definitions (test)",
            "units": {
                "mass": ["kg", "g"],
                "count": ["count", "unit", "kit", "set"],
                "time": ["hour"],
            },
            "conversions": [
                {"from": "g", "to": "kg", "factor": 0.001},
                {"from": "kit", "to": "count", "factor": 1.0},
                {"from": "set", "to": "count", "factor": 1.0},
                {"from": "hour", "to": "hour", "factor": 1.0},
            ],
        }, f)

    # Create a simple process
    with open(kb / "processes" / "test_process_v0.yaml", "w") as f:
        yaml.dump({
            "id": "test_process_v0",
            "kind": "process",
            "process_type": "batch",
            "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
            "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0,
            },
            "resource_requirements": [
                {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
            ],
        }, f)

    # Create a process with partial machine reservation
    with open(kb / "processes" / "test_process_partial_v0.yaml", "w") as f:
        yaml.dump({
            "id": "test_process_partial_v0",
            "kind": "process",
            "process_type": "batch",
            "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
            "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0,
            },
            "resource_requirements": [
                {"machine_id": "test_machine_full", "qty": 1.0, "unit": "count"},
                {"machine_id": "test_machine_partial", "qty": 5.0, "unit": "hr"},
            ],
        }, f)

    # Process that requires a machine imported after reservation manager init
    with open(kb / "processes" / "test_process_late_machine_v0.yaml", "w") as f:
        yaml.dump({
            "id": "test_process_late_machine_v0",
            "kind": "process",
            "process_type": "batch",
            "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
            "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0,
            },
            "resource_requirements": [
                {"machine_id": "lathe", "qty": 1.0, "unit": "count"}
            ],
        }, f)

    # Process that uses a machine imported with a count-like unit (kit)
    with open(kb / "processes" / "test_process_kit_machine_v0.yaml", "w") as f:
        yaml.dump({
            "id": "test_process_kit_machine_v0",
            "kind": "process",
            "process_type": "batch",
            "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
            "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
            "time_model": {
                "type": "batch",
                "hr_per_batch": 1.0,
            },
            "resource_requirements": [
                {"machine_id": "toolkit", "qty": 1.0, "unit": "count"}
            ],
        }, f)

    # Create material items
    with open(kb / "items" / "materials" / "ore.yaml", "w") as f:
        yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)

    with open(kb / "items" / "materials" / "metal.yaml", "w") as f:
        yaml.dump({"id": "metal", "kind": "material", "unit": "kg", "mass": 1.0}, f)

    # Create machine
    with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
        yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)

    with open(kb / "items" / "machines" / "test_machine_partial.yaml", "w") as f:
        yaml.dump({
            "id": "test_machine_partial",
            "kind": "machine",
            "unit": "count",
            "mass": 50.0
        }, f)

    with open(kb / "items" / "machines" / "test_machine_full.yaml", "w") as f:
        yaml.dump({
            "id": "test_machine_full",
            "kind": "machine",
            "unit": "count",
            "mass": 75.0
        }, f)

    with open(kb / "items" / "machines" / "lathe.yaml", "w") as f:
        yaml.dump({
            "id": "lathe",
            "kind": "machine",
            "unit": "count",
            "mass": 80.0
        }, f)

    with open(kb / "items" / "machines" / "toolkit.yaml", "w") as f:
        yaml.dump({
            "id": "toolkit",
            "kind": "machine",
            "unit": "count",
            "mass": 5.0
        }, f)

    return kb


@pytest.fixture
def sim_dir(tmp_path):
    return tmp_path / "simulations"


class TestBasicProcessScheduling:
    """Test basic process scheduling with ADR-020."""

    def test_schedule_single_process(self, kb_root, sim_dir):
        """Schedule and complete a single process."""
        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)

        # Import initial resources
        engine.import_item("ore", 10.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        # Schedule process
        result = engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            duration_hours=1.0,
        )

        if not result["success"]:
            print(f"Error: {result}")
        assert result["success"]
        assert "process_run_id" in result
        assert result["duration_hours"] == 1.0

        # Check scheduler state
        assert len(engine.scheduler.event_queue) == 2  # start and complete events
        assert engine.scheduler.current_time == 0.0

        # Advance time to completion
        advance_result = engine.advance_time(1.0)

        assert advance_result["new_time"] == 1.0
        assert advance_result["processes_completed"] == 1
        assert len(advance_result["completed"]) == 1

        # Check outputs added
        assert engine.has_item("metal", 1.0, "kg")

    def test_schedule_sequential_processes(self, kb_root, sim_dir):
        """Schedule two sequential processes."""
        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)

        # Import resources
        engine.import_item("ore", 10.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        # Schedule first process
        result1 = engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            duration_hours=1.0,
        )
        assert result1["success"]

        # Schedule second process (sequential - different time)
        result2 = engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            start_time=1.0,  # Starts after first completes
            duration_hours=1.0,
        )
        assert result2["success"]

        # Advance to completion of both
        advance_result = engine.advance_time(2.0)

        assert advance_result["processes_completed"] == 2
        assert engine.has_item("metal", 2.0, "kg")

    def test_machine_conflict_detection(self, kb_root, sim_dir):
        """Machine conflict prevents concurrent processes."""
        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)

        # Import resources (only 1 furnace)
        engine.import_item("ore", 10.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        # Schedule first process
        result1 = engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            start_time=0.0,
            duration_hours=2.0,
        )
        assert result1["success"]

        # Try to schedule overlapping process - should fail
        result2 = engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            start_time=1.0,  # Overlaps with first
            duration_hours=2.0,
        )
        assert not result2["success"]

    def test_capacity_updates_after_new_machine_import(self, kb_root, sim_dir):
        """Reservation manager should see machines imported after initialization."""
        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)

        engine.import_item("ore", 10.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        # Initialize reservation manager via first process
        result1 = engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            duration_hours=1.0,
        )
        assert result1["success"]

        # Import new machine after manager init and schedule a process using it
        engine.import_item("lathe", 1.0, "count")
        result2 = engine.start_process(
            process_id="test_process_late_machine_v0",
            scale=1.0,
            duration_hours=1.0,
            start_time=1.5,
        )
        assert result2["success"]

    def test_count_like_unit_machines_available(self, kb_root, sim_dir):
        """Machines imported with count-like units (kit) should be reservable."""
        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)

        engine.import_item("ore", 10.0, "kg")
        engine.import_item("toolkit", 1.0, "kit")

        result = engine.start_process(
            process_id="test_process_kit_machine_v0",
            scale=1.0,
            duration_hours=1.0,
        )
        assert result["success"]

    def test_events_persisted_to_log(self, kb_root, sim_dir):
        """Verify that process start and complete events are written to events.jsonl."""
        import json

        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        sim_id = "test_event_persistence"
        # Match CLI pattern: sim_dir should be the full path to this specific simulation
        full_sim_dir = sim_dir / sim_id
        engine = SimulationEngine(sim_id, kb, full_sim_dir)

        # Import initial resources
        engine.import_item("ore", 10.0, "kg")
        engine.import_item("furnace", 1.0, "count")
        engine.save()  # Flush import events

        # Schedule and complete a process
        result = engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            duration_hours=1.0,
        )
        assert result["success"]

        # Advance time to complete the process
        advance_result = engine.advance_time(1.0)
        assert advance_result["processes_completed"] == 1

        # Save events to log
        engine.save()

        # Read the log file and verify events are present
        log_file = full_sim_dir / "events.jsonl"

        # Debug: check if directory exists
        assert full_sim_dir.exists(), f"Simulation directory should exist at {full_sim_dir}"

        # Debug: list what files are there
        if full_sim_dir.exists():
            files = list(full_sim_dir.glob("*"))
            print(f"Files in sim directory: {files}")

        assert log_file.exists(), f"Log file should exist at {log_file}"

        events = []
        with open(log_file, "r") as f:
            for line in f:
                events.append(json.loads(line))

        # Verify we have the expected event types
        event_types = [e.get("type") for e in events]

        # Key assertion: process_scheduled and process_start events should be logged
        assert "process_scheduled" in event_types, f"Should have process_scheduled event. Got event types: {event_types}"
        assert "process_start" in event_types, f"Should have process_start event. Got event types: {event_types}"
        assert "process_complete" in event_types, "Should have process_complete event"

        # Verify process_scheduled event has correct structure
        process_scheduled_events = [e for e in events if e.get("type") == "process_scheduled"]
        assert len(process_scheduled_events) == 1, "Should have exactly one process_scheduled event"

        ps_event = process_scheduled_events[0]
        assert ps_event.get("process_id") == "test_process_v0"
        assert ps_event.get("scale") == 1.0
        assert ps_event.get("scheduled_start_time") == 0.0
        assert ps_event.get("scheduled_end_time") == 1.0
        assert ps_event.get("duration_hours") == 1.0
        assert ps_event.get("process_run_id")

        # Verify process_start event has correct structure
        process_start_events = [e for e in events if e.get("type") == "process_start"]
        assert len(process_start_events) == 1, "Should have exactly one process_start event"

        ps_event = process_start_events[0]
        assert ps_event.get("process_id") == "test_process_v0"
        assert ps_event.get("scale") == 1.0
        assert ps_event.get("actual_start_time") == 0.0
        assert ps_event.get("process_run_id")

        # Verify process_complete event has correct structure
        process_complete_events = [e for e in events if e.get("type") == "process_complete"]
        assert len(process_complete_events) == 1, "Should have exactly one process_complete event"

        pc_event = process_complete_events[0]
        assert pc_event.get("process_id") == "test_process_v0"
        assert pc_event.get("time_hours") == 1.0
        assert "outputs" in pc_event
        # Check that outputs contain the expected item
        outputs = pc_event.get("outputs", {})
        assert "metal" in outputs

    def test_scheduler_persistence_across_loads(self, kb_root, sim_dir):
        """Verify scheduler state persists across save/load cycles (ADR-021 core requirement)."""
        import json

        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        sim_id = "persistence_test"
        full_sim_dir = sim_dir / sim_id

        # Phase 1: Create engine, schedule process, save
        engine1 = SimulationEngine(sim_id, kb, full_sim_dir)
        engine1.import_item("ore", 10.0, "kg")
        engine1.import_item("furnace", 1.0, "count")

        result = engine1.start_process(
            process_id="test_process_v0",
            scale=1.0,
            duration_hours=5.0,
        )
        assert result["success"]
        process_run_id = result["process_run_id"]

        # Verify scheduled in engine1
        assert len(engine1.scheduler.active_processes) == 1, "Should have 1 active process before save"
        assert process_run_id in engine1.scheduler.active_processes, "Process should be in scheduler"

        # Verify process details
        process_run = engine1.scheduler.active_processes[process_run_id]
        assert process_run.process_id == "test_process_v0"
        assert process_run.start_time == 0.0
        assert process_run.duration_hours == 5.0
        assert process_run.end_time == 5.0

        engine1.save()

        # Phase 2: Load in fresh engine, verify scheduler state reconstructed
        engine2 = SimulationEngine(sim_id, kb, full_sim_dir)
        success = engine2.load()
        assert success, "Load should succeed"

        # CRITICAL ASSERTIONS: Scheduler state reconstructed from process_scheduled events
        assert engine2.scheduler.current_time == 0.0, "Scheduler time should be synced"
        assert len(engine2.scheduler.active_processes) == 1, "Should have reconstructed 1 active process"
        assert process_run_id in engine2.scheduler.active_processes, f"Process {process_run_id} should be reconstructed"

        # Verify reconstructed process details
        process_run2 = engine2.scheduler.active_processes[process_run_id]
        assert process_run2.process_id == "test_process_v0"
        assert process_run2.start_time == 0.0
        assert process_run2.duration_hours == 5.0
        assert process_run2.end_time == 5.0
        assert process_run2.scale == 1.0

        # Verify inputs/outputs reconstructed
        assert "ore" in process_run2.inputs_consumed
        assert "metal" in process_run2.outputs_pending

        # Verify machine reservations reconstructed
        assert "furnace" in process_run2.machines_reserved
        assert process_run2.machines_reserved["furnace"] == 1.0

        # Phase 3: Advance time in engine2, verify process completes
        advance_result = engine2.advance_time(5.0)
        assert advance_result["processes_completed"] == 1, "Should complete 1 process"

        # Verify process no longer active
        assert len(engine2.scheduler.active_processes) == 0, "No processes should be active after completion"

        # Verify outputs produced
        assert engine2.has_item("metal", 1.0, "kg"), "Should have produced metal output"

    def test_partial_reservation_persistence(self, kb_root, sim_dir):
        """Verify PARTIAL reservations are reconstructed correctly, skipping already-released ones."""
        import json

        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        sim_id = "partial_res_test"
        full_sim_dir = sim_dir / sim_id

        # Phase 1: Schedule process with PARTIAL reservation
        engine1 = SimulationEngine(sim_id, kb, full_sim_dir)
        engine1.import_item("ore", 10.0, "kg")
        engine1.import_item("test_machine_partial", 1.0, "count")
        engine1.import_item("test_machine_full", 1.0, "count")

        # This process should have a PARTIAL reservation (unit='hr')
        result = engine1.start_process(
            process_id="test_process_partial_v0",
            scale=1.0,
            duration_hours=10.0,
        )
        assert result["success"]
        process_run_id = result["process_run_id"]

        engine1.save()

        # Phase 2: Load at t=0, verify reservation exists
        engine2 = SimulationEngine(sim_id, kb, full_sim_dir)
        engine2.load()

        # Check reservation manager has the partial reservation
        reserved = engine2.reservation_manager.get_reserved_qty(
            machine_id="test_machine_partial",
            start_time=0.0,
            end_time=5.0  # Partial release at 5 hours
        )
        assert reserved > 0, "Reservation should exist at t=0"

        # Phase 3: Advance time past release, save, reload
        engine2.advance_time(6.0)  # Past the release_time
        engine2.save()

        # Phase 4: Load at t=6, verify partial reservation NOT restored
        engine3 = SimulationEngine(sim_id, kb, full_sim_dir)
        engine3.load()

        # The partial reservation should have been released and not restored
        # But the process should still be active (ends at t=10)
        assert process_run_id in engine3.scheduler.active_processes, "Process should still be active"

        # Check that machine is no longer reserved (partial release happened)
        reserved = engine3.reservation_manager.get_reserved_qty(
            machine_id="test_machine_partial",
            start_time=6.0,
            end_time=10.0
        )
        # Should be 0 because the partial reservation was released at t=5
        assert reserved == 0, "Machine should not be reserved after partial release"


class TestRecipeOrchestration:
    """Test recipe orchestration with dependencies."""

    @pytest.fixture
    def recipe_kb(self, tmp_path):
        """Create KB with multi-step recipe."""
        kb = tmp_path / "kb"
        (kb / "processes").mkdir(parents=True)
        (kb / "recipes").mkdir(parents=True)
        (kb / "items" / "materials").mkdir(parents=True)
        (kb / "items" / "machines").mkdir(parents=True)

        # Step 1: ore -> ingot
        with open(kb / "processes" / "smelt_v0.yaml", "w") as f:
            yaml.dump({
                "id": "smelt_v0",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "ingot", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [
                    {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        # Step 2: ingot -> part
        with open(kb / "processes" / "forge_v0.yaml", "w") as f:
            yaml.dump({
                "id": "forge_v0",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ingot", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "part", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [
                    {"machine_id": "forge", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        # Recipe with dependencies
        with open(kb / "recipes" / "recipe_part_v0.yaml", "w") as f:
            yaml.dump({
                "id": "recipe_part_v0",
                "target_item_id": "part",
                "variant_id": "v0",
                "steps": [
                    {"process_id": "smelt_v0", "dependencies": []},
                    {"process_id": "forge_v0", "dependencies": [0]},  # Depends on step 0
                ],
            }, f)

        # Materials
        with open(kb / "items" / "materials" / "ore.yaml", "w") as f:
            yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)

        with open(kb / "items" / "materials" / "ingot.yaml", "w") as f:
            yaml.dump({"id": "ingot", "kind": "material", "unit": "kg", "mass": 1.0}, f)

        with open(kb / "items" / "materials" / "part.yaml", "w") as f:
            yaml.dump({"id": "part", "kind": "material", "unit": "kg", "mass": 1.0}, f)

        # Machines
        with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
            yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)

        with open(kb / "items" / "machines" / "forge.yaml", "w") as f:
            yaml.dump({"id": "forge", "kind": "machine", "unit": "count", "mass": 100.0}, f)

        return kb

    def test_recipe_with_dependencies(self, recipe_kb, sim_dir):
        """Recipe steps execute in dependency order."""
        kb = KBLoader(recipe_kb, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)

        # Import resources
        engine.import_item("ore", 10.0, "kg")
        engine.import_item("furnace", 1.0, "count")
        engine.import_item("forge", 1.0, "count")

        # Run recipe
        result = engine.run_recipe(recipe_id="recipe_part_v0")

        assert result["success"]
        assert result["total_steps"] == 2
        assert result["scheduled_steps"] >= 1  # At least step 0 scheduled

        # Advance time - step 0 should complete and step 1 should start
        engine.advance_time(1.0)

        # With the fix, step 1 starts immediately after step 0 completes,
        # consuming the intermediate product (ingot). Check that step 1 is active.
        progress = engine.orchestrator.get_recipe_progress(result["recipe_run_id"])
        assert progress['active_steps'] == 1, "Step 1 should be active after step 0 completes"

        # Advance more - step 1 should complete
        engine.advance_time(1.0)

        # Check final product
        assert engine.has_item("part", 1.0, "kg")

        # Recipe should be complete
        recipe_run_id = result["recipe_run_id"]
        assert engine.orchestrator.is_recipe_complete(recipe_run_id)

    def test_recipe_progress_tracking(self, recipe_kb, sim_dir):
        """Track recipe progress through execution."""
        kb = KBLoader(recipe_kb, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)

        # Import resources
        engine.import_item("ore", 10.0, "kg")
        engine.import_item("furnace", 1.0, "count")
        engine.import_item("forge", 1.0, "count")

        # Run recipe
        result = engine.run_recipe(recipe_id="recipe_part_v0")
        recipe_run_id = result["recipe_run_id"]

        # Initial progress
        progress = engine.orchestrator.get_recipe_progress(recipe_run_id)
        assert progress["total_steps"] == 2
        assert progress["completed_steps"] == 0
        assert not progress["is_completed"]

        # Complete first step
        engine.advance_time(1.0)
        progress = engine.orchestrator.get_recipe_progress(recipe_run_id)
        assert progress["completed_steps"] == 1
        assert progress["progress_percent"] == pytest.approx(50.0)

        # Complete second step
        engine.advance_time(1.0)
        progress = engine.orchestrator.get_recipe_progress(recipe_run_id)
        assert progress["completed_steps"] == 2
        assert progress["progress_percent"] == pytest.approx(100.0)
        assert progress["is_completed"]


class TestUtilityMethods:
    """Test utility and query methods."""

    def test_get_schedule_summary(self, kb_root, sim_dir):
        """Get scheduler state summary."""
        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)
        engine.import_item("ore", 10.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        # Schedule process
        engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            duration_hours=1.0,
        )

        summary = engine.get_schedule_summary()
        assert summary["current_time"] == 0.0
        assert summary["queued_events"] > 0
        assert summary["next_event_time"] == 0.0

    def test_machine_utilization(self, kb_root, sim_dir):
        """Calculate machine utilization."""
        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)
        engine.import_item("ore", 10.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        # Schedule process using furnace for 1 hour
        engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            duration_hours=1.0,
        )

        # Utilization over 0-2h should be 50% (used 1h out of 2h)
        util = engine.get_machine_utilization("furnace", (0.0, 2.0))
        assert util == pytest.approx(0.5)


class TestAdr020Gaps:
    """Tests that enforce ADR-020 behaviors currently missing."""

    def test_step_override_time_model_applied(self, tmp_path, sim_dir):
        """Step-level time_model overrides should affect scheduled duration."""
        kb = tmp_path / "kb"
        (kb / "processes").mkdir(parents=True)
        (kb / "recipes").mkdir(parents=True)
        (kb / "items" / "materials").mkdir(parents=True)
        (kb / "items" / "machines").mkdir(parents=True)

        with open(kb / "processes" / "base_proc.yaml", "w") as f:
            yaml.dump({
                "id": "base_proc",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 2.0},
                "resource_requirements": [
                    {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        with open(kb / "recipes" / "recipe_override.yaml", "w") as f:
            yaml.dump({
                "id": "recipe_override",
                "target_item_id": "metal",
                "variant_id": "v0",
                "steps": [{
                    "process_id": "base_proc",
                    "dependencies": [],
                    "time_model": {"type": "batch", "hr_per_batch": 1.0},
                }],
            }, f)

        with open(kb / "items" / "materials" / "ore.yaml", "w") as f:
            yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "materials" / "metal.yaml", "w") as f:
            yaml.dump({"id": "metal", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
            yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)

        kb_loader = KBLoader(kb, use_validated_models=False)
        kb_loader.load_all()
        engine = SimulationEngine("test_sim", kb_loader, sim_dir)
        engine.import_item("ore", 1.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        result = engine.run_recipe(recipe_id="recipe_override")
        assert result["success"]

        start_events = [
            e for e in engine.scheduler.event_queue._heap
            if e.event_type == EventType.PROCESS_START
        ]
        assert len(start_events) == 1
        assert start_events[0].data["duration_hours"] == 1.0

    def test_step_override_inputs_are_used(self, tmp_path, sim_dir):
        """Step-level inputs override process inputs during scheduling."""
        kb = tmp_path / "kb"
        (kb / "processes").mkdir(parents=True)
        (kb / "recipes").mkdir(parents=True)
        (kb / "items" / "materials").mkdir(parents=True)
        (kb / "items" / "machines").mkdir(parents=True)

        with open(kb / "processes" / "base_proc.yaml", "w") as f:
            yaml.dump({
                "id": "base_proc",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "base_input", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "output", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [
                    {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        with open(kb / "recipes" / "recipe_override_inputs.yaml", "w") as f:
            yaml.dump({
                "id": "recipe_override_inputs",
                "target_item_id": "output",
                "variant_id": "v0",
                "inputs": [{"item_id": "override_input", "qty": 1.0, "unit": "kg"}],
                "steps": [{
                    "process_id": "base_proc",
                    "inputs": [{"item_id": "override_input", "qty": 1.0, "unit": "kg"}],
                }],
            }, f)

        with open(kb / "items" / "materials" / "base_input.yaml", "w") as f:
            yaml.dump({"id": "base_input", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "materials" / "override_input.yaml", "w") as f:
            yaml.dump({"id": "override_input", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "materials" / "output.yaml", "w") as f:
            yaml.dump({"id": "output", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
            yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)

        kb_loader = KBLoader(kb, use_validated_models=False)
        kb_loader.load_all()
        engine = SimulationEngine("test_sim", kb_loader, sim_dir)
        engine.import_item("override_input", 1.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        result = engine.run_recipe(recipe_id="recipe_override_inputs")
        assert result["success"]

        start_events = [
            e for e in engine.scheduler.event_queue._heap
            if e.event_type == EventType.PROCESS_START
        ]
        assert len(start_events) == 1
        inputs = start_events[0].data["inputs_consumed"]
        assert "override_input" in inputs

    def test_dependent_step_respects_overrides(self, tmp_path, sim_dir):
        """Dependent steps should apply step-level overrides when scheduled."""
        kb = tmp_path / "kb"
        (kb / "processes").mkdir(parents=True)
        (kb / "recipes").mkdir(parents=True)
        (kb / "items" / "materials").mkdir(parents=True)
        (kb / "items" / "machines").mkdir(parents=True)

        with open(kb / "processes" / "proc_a.yaml", "w") as f:
            yaml.dump({
                "id": "proc_a",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "mid", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [
                    {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        with open(kb / "processes" / "proc_b.yaml", "w") as f:
            yaml.dump({
                "id": "proc_b",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "base_input", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "base_output", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [
                    {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        with open(kb / "recipes" / "recipe_override_dependent.yaml", "w") as f:
            yaml.dump({
                "id": "recipe_override_dependent",
                "target_item_id": "override_output",
                "variant_id": "v0",
                "steps": [
                    {"process_id": "proc_a", "dependencies": []},
                    {
                        "process_id": "proc_b",
                        "dependencies": [0],
                        "inputs": [{"item_id": "override_input", "qty": 1.0, "unit": "kg"}],
                        "outputs": [{"item_id": "override_output", "qty": 1.0, "unit": "kg"}],
                    },
                ],
            }, f)

        for item_id in ("ore", "mid", "base_input", "override_input", "base_output", "override_output"):
            with open(kb / "items" / "materials" / f"{item_id}.yaml", "w") as f:
                yaml.dump({"id": item_id, "kind": "material", "unit": "kg", "mass": 1.0}, f)

        with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
            yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)

        kb_loader = KBLoader(kb, use_validated_models=False)
        kb_loader.load_all()
        engine = SimulationEngine("test_sim", kb_loader, sim_dir)
        engine.import_item("ore", 1.0, "kg")
        engine.import_item("override_input", 1.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        result = engine.run_recipe(recipe_id="recipe_override_dependent")
        assert result["success"]

        engine.advance_time(1.0)
        engine.advance_time(1.0)

        assert engine.has_item("override_output", 1.0, "kg")
        assert not engine.has_item("base_output", 1.0, "kg")

    def test_steps_without_dependencies_run_sequentially(self, tmp_path, sim_dir):
        """Steps without explicit dependencies should execute in order."""
        kb = tmp_path / "kb"
        (kb / "processes").mkdir(parents=True)
        (kb / "recipes").mkdir(parents=True)
        (kb / "items" / "materials").mkdir(parents=True)
        (kb / "items" / "machines").mkdir(parents=True)

        with open(kb / "processes" / "proc_a.yaml", "w") as f:
            yaml.dump({
                "id": "proc_a",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "mid", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [
                    {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        with open(kb / "processes" / "proc_b.yaml", "w") as f:
            yaml.dump({
                "id": "proc_b",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "mid", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "output", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [
                    {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        with open(kb / "recipes" / "recipe_sequential.yaml", "w") as f:
            yaml.dump({
                "id": "recipe_sequential",
                "target_item_id": "output",
                "variant_id": "v0",
                "steps": [
                    {"process_id": "proc_a"},
                    {"process_id": "proc_b"},
                ],
            }, f)

        for item_id in ("ore", "mid", "output"):
            with open(kb / "items" / "materials" / f"{item_id}.yaml", "w") as f:
                yaml.dump({"id": item_id, "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
            yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)

        kb_loader = KBLoader(kb, use_validated_models=False)
        kb_loader.load_all()
        engine = SimulationEngine("test_sim", kb_loader, sim_dir)
        engine.import_item("ore", 1.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        result = engine.run_recipe(recipe_id="recipe_sequential")
        assert result["success"]
        assert result["scheduled_steps"] == 1

    def test_missing_inputs_do_not_create_outputs(self, kb_root, sim_dir):
        """Lack of input reservation should not allow extra outputs."""
        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)
        engine.import_item("ore", 1.0, "kg")
        engine.import_item("furnace", 2.0, "count")

        result1 = engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            duration_hours=1.0,
            start_time=0.0,
        )
        assert result1["success"]

        result2 = engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            duration_hours=1.0,
            start_time=0.0,
        )
        assert result2["success"]

        engine.advance_time(1.0)
        assert engine.has_item("metal", 1.0, "kg")
        assert not engine.has_item("metal", 2.0, "kg")

    def test_output_units_preserved(self, tmp_path, sim_dir):
        """Outputs should be added using their declared unit, not forced to kg."""
        kb = tmp_path / "kb"
        (kb / "processes").mkdir(parents=True)
        (kb / "recipes").mkdir(parents=True)
        (kb / "items" / "materials").mkdir(parents=True)
        (kb / "items" / "machines").mkdir(parents=True)

        with open(kb / "processes" / "count_proc.yaml", "w") as f:
            yaml.dump({
                "id": "count_proc",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "widget", "qty": 1.0, "unit": "count"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [
                    {"machine_id": "press", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        with open(kb / "items" / "materials" / "ore.yaml", "w") as f:
            yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "materials" / "widget.yaml", "w") as f:
            yaml.dump({"id": "widget", "kind": "material", "unit": "count", "mass": 1.0}, f)
        with open(kb / "items" / "machines" / "press.yaml", "w") as f:
            yaml.dump({"id": "press", "kind": "machine", "unit": "count", "mass": 100.0}, f)

        kb_loader = KBLoader(kb, use_validated_models=False)
        kb_loader.load_all()
        engine = SimulationEngine("test_sim", kb_loader, sim_dir)
        engine.import_item("ore", 1.0, "kg")
        engine.import_item("press", 1.0, "count")

        result = engine.start_process(
            process_id="count_proc",
            scale=1.0,
            duration_hours=1.0,
        )
        assert result["success"]
        engine.advance_time(1.0)

        assert "widget" in engine.state.inventory
        assert engine.state.inventory["widget"].unit == "count"

    def test_energy_booked_on_process_start(self, tmp_path, sim_dir):
        """Energy usage should be accumulated when a process starts."""
        kb = tmp_path / "kb"
        (kb / "processes").mkdir(parents=True)
        (kb / "items" / "materials").mkdir(parents=True)
        (kb / "items" / "machines").mkdir(parents=True)

        with open(kb / "processes" / "energy_proc.yaml", "w") as f:
            yaml.dump({
                "id": "energy_proc",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "energy_model": {
                    "type": "per_unit",
                    "value": 2.0,
                    "unit": "kWh/kg",
                    "scaling_basis": "metal",
                },
                "resource_requirements": [
                    {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        with open(kb / "items" / "materials" / "ore.yaml", "w") as f:
            yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "materials" / "metal.yaml", "w") as f:
            yaml.dump({"id": "metal", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
            yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)

        kb_loader = KBLoader(kb, use_validated_models=False)
        kb_loader.load_all()
        engine = SimulationEngine("test_sim", kb_loader, sim_dir)
        engine.import_item("ore", 1.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        result = engine.start_process(
            process_id="energy_proc",
            scale=1.0,
            duration_hours=1.0,
        )
        assert result["success"]
        engine.advance_time(1.0)

        assert engine.state.total_energy_kwh > 0.0

    def test_machine_conflict_pauses_recipe(self, tmp_path, sim_dir):
        """Machine conflicts should pause recipe runs instead of failing immediately."""
        kb = tmp_path / "kb"
        (kb / "processes").mkdir(parents=True)
        (kb / "recipes").mkdir(parents=True)
        (kb / "items" / "materials").mkdir(parents=True)
        (kb / "items" / "machines").mkdir(parents=True)

        with open(kb / "processes" / "proc_a.yaml", "w") as f:
            yaml.dump({
                "id": "proc_a",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "ingot", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [
                    {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        with open(kb / "processes" / "proc_b.yaml", "w") as f:
            yaml.dump({
                "id": "proc_b",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "plate", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [
                    {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
                ],
            }, f)

        with open(kb / "recipes" / "recipe_conflict.yaml", "w") as f:
            yaml.dump({
                "id": "recipe_conflict",
                "target_item_id": "plate",
                "variant_id": "v0",
                "steps": [
                    {"process_id": "proc_a", "dependencies": []},
                    {"process_id": "proc_b", "dependencies": []},
                ],
            }, f)

        with open(kb / "items" / "materials" / "ore.yaml", "w") as f:
            yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "materials" / "ingot.yaml", "w") as f:
            yaml.dump({"id": "ingot", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "materials" / "plate.yaml", "w") as f:
            yaml.dump({"id": "plate", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
            yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)

        kb_loader = KBLoader(kb, use_validated_models=False)
        kb_loader.load_all()
        engine = SimulationEngine("test_sim", kb_loader, sim_dir)
        engine.import_item("ore", 10.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        result = engine.run_recipe(recipe_id="recipe_conflict")
        assert result["success"]

    def test_process_complete_event_includes_run_id(self, kb_root, sim_dir):
        """Process complete events should include process_run_id."""
        kb = KBLoader(kb_root, use_validated_models=False)
        kb.load_all()

        engine = SimulationEngine("test_sim", kb, sim_dir)
        engine.import_item("ore", 1.0, "kg")
        engine.import_item("furnace", 1.0, "count")

        result = engine.start_process(
            process_id="test_process_v0",
            scale=1.0,
            duration_hours=1.0,
        )
        assert result["success"]
        engine.advance_time(1.0)

        complete_events = [
            e for e in engine.event_buffer
            if getattr(e, "type", None) == "process_complete"
        ]
        assert complete_events
        event_data = complete_events[0].model_dump()
        assert "process_run_id" in event_data

    def test_machine_release_event_scheduled_for_partial(self, tmp_path, sim_dir):
        """Partial reservations should schedule a machine release event."""
        kb = tmp_path / "kb"
        (kb / "processes").mkdir(parents=True)
        (kb / "items" / "materials").mkdir(parents=True)
        (kb / "items" / "machines").mkdir(parents=True)

        with open(kb / "processes" / "partial_proc.yaml", "w") as f:
            yaml.dump({
                "id": "partial_proc",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 8.0},
                "resource_requirements": [
                    {"machine_id": "operator", "qty": 1.0, "unit": "count"},
                    {"machine_id": "furnace", "qty": 6.0, "unit": "hr"},
                ],
            }, f)

        with open(kb / "items" / "materials" / "ore.yaml", "w") as f:
            yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "materials" / "metal.yaml", "w") as f:
            yaml.dump({"id": "metal", "kind": "material", "unit": "kg", "mass": 1.0}, f)
        with open(kb / "items" / "machines" / "operator.yaml", "w") as f:
            yaml.dump({"id": "operator", "kind": "machine", "unit": "count", "mass": 100.0}, f)
        with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
            yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)

        kb_loader = KBLoader(kb, use_validated_models=False)
        kb_loader.load_all()
        engine = SimulationEngine("test_sim", kb_loader, sim_dir)
        engine.import_item("ore", 1.0, "kg")
        engine.import_item("operator", 1.0, "count")
        engine.import_item("furnace", 1.0, "count")

        result = engine.start_process(
            process_id="partial_proc",
            scale=1.0,
            duration_hours=8.0,
        )
        assert result["success"]

        release_events = [
            e for e in engine.scheduler.event_queue._heap
            if e.event_type == EventType.MACHINE_RELEASE
        ]
        assert release_events
