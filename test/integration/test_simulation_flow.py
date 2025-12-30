"""
Integration tests for simulation engine with ADR-012-017 support.
"""
import pytest
from pathlib import Path
import tempfile
import yaml

from src.simulation.engine import SimulationEngine
from src.kb_core.kb_loader import KBLoader


@pytest.fixture
def temp_kb(tmp_path):
    """Create a temporary KB directory with test data."""
    kb_root = tmp_path / "kb"

    # Create directory structure
    (kb_root / "items" / "materials").mkdir(parents=True, exist_ok=True)
    (kb_root / "processes").mkdir(parents=True, exist_ok=True)
    (kb_root / "recipes").mkdir(parents=True, exist_ok=True)
    (kb_root / "boms").mkdir(parents=True, exist_ok=True)

    return kb_root


@pytest.fixture
def temp_sim_dir(tmp_path):
    """Create temporary simulation directory."""
    return tmp_path / "simulations"


def write_yaml(path: Path, data: dict):
    """Helper to write YAML files."""
    with path.open('w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)


class TestProcessStartWithAgentDuration:
    """Test starting processes with agent-provided duration."""

    def test_start_process_agent_duration(self, temp_kb, temp_sim_dir):
        """Should start process with agent-provided duration."""
        # Create a simple process
        write_yaml(temp_kb / "processes" / "test_process.yaml", {
            'id': 'test_process',
            'kind': 'process',
            'process_type': 'continuous',
            'inputs': [
                {'item_id': 'iron_ore', 'qty': 1.0, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'iron', 'qty': 0.9, 'unit': 'kg'}
            ],
            'time_model': {
                'type': 'linear_rate',
                'rate': 10.0,
                'rate_unit': 'kg/hr',
                'scaling_basis': 'iron'
            },
            'energy_model': {
                'type': 'per_unit',
                'value': 0.5,
                'unit': 'kWh/kg',
                'scaling_basis': 'iron'
            }
        })

        # Create raw material
        write_yaml(temp_kb / "items" / "materials" / "iron_ore.yaml", {
            'id': 'iron_ore',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg'
        })

        # Create output item
        write_yaml(temp_kb / "items" / "materials" / "iron.yaml", {
            'id': 'iron',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg'
        })

        # Load KB
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create engine and import iron ore
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)
        engine.import_item("iron_ore", 10.0, "kg")

        # Start process with agent-provided duration
        result = engine.start_process(
            process_id="test_process",
            scale=1.0,
            duration_hours=2.0  # Agent provides duration
        )

        # Should succeed
        assert result["success"] is True
        assert result["duration_hours"] == 2.0
        assert result["ends_at"] == 2.0

        # Should have consumed inputs
        assert "iron_ore" not in engine.state.inventory or engine.state.inventory["iron_ore"].quantity == 9.0

        # Should have active process
        assert len(engine.state.active_processes) == 1
        assert engine.state.active_processes[0].ends_at == 2.0

    def test_start_process_insufficient_inputs(self, temp_kb, temp_sim_dir):
        """Should fail if insufficient inputs."""
        # Create process
        write_yaml(temp_kb / "processes" / "test_process.yaml", {
            'id': 'test_process',
            'kind': 'process',
            'process_type': 'continuous',
            'inputs': [
                {'item_id': 'iron_ore', 'qty': 1.0, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'iron', 'qty': 0.9, 'unit': 'kg'}
            ],
            'time_model': {
                'type': 'linear_rate',
                'rate': 10.0,
                'rate_unit': 'kg/hr',
                'scaling_basis': 'iron'
            }
        })

        # Load KB
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create engine (no inventory)
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)

        # Try to start process
        result = engine.start_process(
            process_id="test_process",
            scale=1.0,
            duration_hours=2.0
        )

        # Should fail
        assert result["success"] is False
        assert result["error"] == "insufficient_inputs"


class TestProcessStartWithCalculatedDuration:
    """Test starting processes with calculated duration (ADR-012)."""

    def test_start_process_calculated_duration(self, temp_kb, temp_sim_dir):
        """Should calculate duration from time_model when not provided."""
        # Create process with time_model
        write_yaml(temp_kb / "processes" / "smelting.yaml", {
            'id': 'smelting',
            'kind': 'process',
            'process_type': 'continuous',
            'inputs': [
                {'item_id': 'iron_ore', 'qty': 1.0, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'iron', 'qty': 0.9, 'unit': 'kg'}
            ],
            'time_model': {
                'type': 'linear_rate',
                'rate': 10.0,  # 10 kg/hr
                'rate_unit': 'kg/hr',
                'scaling_basis': 'iron'
            }
        })

        # Create items
        write_yaml(temp_kb / "items" / "materials" / "iron_ore.yaml", {
            'id': 'iron_ore',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg'
        })

        write_yaml(temp_kb / "items" / "materials" / "iron.yaml", {
            'id': 'iron',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg'
        })

        # Load KB
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create engine and import materials
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)
        engine.import_item("iron_ore", 10.0, "kg")

        # Start process with output quantity (duration will be calculated)
        result = engine.start_process(
            process_id="smelting",
            scale=1.0,
            output_quantity=9.0,  # Want 9 kg iron
            output_unit="kg"
        )

        # Should succeed with calculated duration
        assert result["success"] is True
        # Duration should be 9 kg / 10 kg/hr = 0.9 hours
        assert result["duration_hours"] == pytest.approx(0.9, rel=0.01)


class TestRuntimeValidation:
    """Test runtime validation before process execution (ADR-017)."""

    def test_runtime_validation_catches_errors(self, temp_kb, temp_sim_dir):
        """Should catch validation errors before starting process."""
        # Create process with validation errors (missing scaling_basis)
        write_yaml(temp_kb / "processes" / "broken_process.yaml", {
            'id': 'broken_process',
            'kind': 'process',
            'process_type': 'continuous',
            'inputs': [
                {'item_id': 'iron_ore', 'qty': 1.0, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'iron', 'qty': 0.9, 'unit': 'kg'}
            ],
            'time_model': {
                'type': 'linear_rate',
                'rate': 10.0,
                'rate_unit': 'kg/hr'
                # Missing scaling_basis!
            }
        })

        # Load KB
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create engine
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)
        engine.import_item("iron_ore", 10.0, "kg")

        # Try to start process
        result = engine.start_process(
            process_id="broken_process",
            scale=1.0,
            duration_hours=1.0
        )

        # Should fail validation
        assert result["success"] is False
        assert result["error"] == "validation_error"
        assert "validation_errors" in result


class TestEnergyCalculation:
    """Test energy calculation using ADR-014 energy models."""

    def test_energy_calculation_on_completion(self, temp_kb, temp_sim_dir):
        """Should calculate energy when process completes."""
        # Create process with energy model
        write_yaml(temp_kb / "processes" / "energy_process.yaml", {
            'id': 'energy_process',
            'kind': 'process',
            'process_type': 'continuous',
            'inputs': [
                {'item_id': 'iron_ore', 'qty': 1.0, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'iron', 'qty': 0.9, 'unit': 'kg'}
            ],
            'time_model': {
                'type': 'linear_rate',
                'rate': 10.0,
                'rate_unit': 'kg/hr',
                'scaling_basis': 'iron'
            },
            'energy_model': {
                'type': 'per_unit',
                'value': 2.0,  # 2 kWh per kg iron
                'unit': 'kWh/kg',
                'scaling_basis': 'iron'
            }
        })

        # Create items
        write_yaml(temp_kb / "items" / "materials" / "iron_ore.yaml", {
            'id': 'iron_ore',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg'
        })

        write_yaml(temp_kb / "items" / "materials" / "iron.yaml", {
            'id': 'iron',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg'
        })

        # Load KB
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create engine
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)
        engine.import_item("iron_ore", 10.0, "kg")

        # Start process
        result = engine.start_process(
            process_id="energy_process",
            scale=1.0,
            duration_hours=1.0
        )
        assert result["success"] is True

        # Advance time to complete process
        advance_result = engine.advance_time(1.0)

        # Should have calculated energy
        assert advance_result["completed_count"] == 1
        completed_proc = advance_result["completed"][0]

        # Energy should be 0.9 kg * 2 kWh/kg = 1.8 kWh
        assert completed_proc["energy_kwh"] == pytest.approx(1.8, rel=0.01)
        assert engine.state.total_energy_kwh == pytest.approx(1.8, rel=0.01)


class TestBuildMachine:
    """Test machine building from BOMs."""

    def test_build_machine_success(self, temp_kb, temp_sim_dir):
        """Should build machine from components."""
        # Create component items
        write_yaml(temp_kb / "items" / "materials" / "steel_plate.yaml", {
            'id': 'steel_plate',
            'kind': 'material',
            'mass': 5.0,
            'unit': 'kg'
        })

        write_yaml(temp_kb / "items" / "materials" / "motor.yaml", {
            'id': 'motor',
            'kind': 'part',
            'mass': 2.0,
            'unit': 'kg'
        })

        # Create machine item
        write_yaml(temp_kb / "items" / "materials" / "test_machine.yaml", {
            'id': 'test_machine',
            'kind': 'machine',
            'mass': 10.0,
            'unit': 'kg'
        })

        # Create BOM
        write_yaml(temp_kb / "boms" / "test_machine.yaml", {
            'machine_id': 'test_machine',
            'components': [
                {'item_id': 'steel_plate', 'quantity': 2, 'unit': 'count'},
                {'item_id': 'motor', 'quantity': 1, 'unit': 'count'}
            ]
        })

        # Load KB
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create engine and import components
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)
        engine.import_item("steel_plate", 2, "count")
        engine.import_item("motor", 1, "count")

        # Build machine
        result = engine.build_machine("test_machine")

        # Should succeed
        assert result["success"] is True
        assert "test_machine" in engine.state.machines_built
        assert engine.has_item("test_machine", 1, "count")

        # Components should be consumed
        assert not engine.has_item("steel_plate", 1, "count")
        assert not engine.has_item("motor", 1, "count")


class TestInventoryManagement:
    """Test inventory operations."""

    def test_add_same_unit(self, temp_kb, temp_sim_dir):
        """Should add items with same unit."""
        kb = KBLoader(temp_kb, use_validated_models=False)
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)

        engine.add_to_inventory("iron", 5.0, "kg")
        engine.add_to_inventory("iron", 3.0, "kg")

        assert engine.state.inventory["iron"].quantity == 8.0
        assert engine.state.inventory["iron"].unit == "kg"

    def test_subtract_inventory(self, temp_kb, temp_sim_dir):
        """Should subtract items from inventory."""
        kb = KBLoader(temp_kb, use_validated_models=False)
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)

        engine.add_to_inventory("iron", 10.0, "kg")
        result = engine.subtract_from_inventory("iron", 3.0, "kg")

        assert result is True
        assert engine.state.inventory["iron"].quantity == 7.0

    def test_subtract_insufficient(self, temp_kb, temp_sim_dir):
        """Should fail to subtract if insufficient."""
        kb = KBLoader(temp_kb, use_validated_models=False)
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)

        engine.add_to_inventory("iron", 5.0, "kg")
        result = engine.subtract_from_inventory("iron", 10.0, "kg")

        assert result is False
        assert engine.state.inventory["iron"].quantity == 5.0


class TestTimeAdvancement:
    """Test time advancement and process completion."""

    def test_advance_time_completes_processes(self, temp_kb, temp_sim_dir):
        """Should complete processes when advancing time."""
        # Create simple process
        write_yaml(temp_kb / "processes" / "quick_process.yaml", {
            'id': 'quick_process',
            'kind': 'process',
            'process_type': 'batch',
            'inputs': [
                {'item_id': 'input_material', 'qty': 1.0, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'output_material', 'qty': 1.0, 'unit': 'kg'}
            ],
            'time_model': {
                'type': 'batch',
                'hr_per_batch': 1.0
            }
        })

        # Create items
        write_yaml(temp_kb / "items" / "materials" / "input_material.yaml", {
            'id': 'input_material',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg'
        })

        write_yaml(temp_kb / "items" / "materials" / "output_material.yaml", {
            'id': 'output_material',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg'
        })

        # Load KB
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create engine
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)
        engine.import_item("input_material", 10.0, "kg")

        # Start process
        engine.start_process("quick_process", scale=1.0, duration_hours=1.0)

        # Advance time
        result = engine.advance_time(1.0)

        # Should complete
        assert result["completed_count"] == 1
        assert "output_material" in engine.state.inventory
        assert engine.state.inventory["output_material"].quantity == 1.0

    def test_preview_step(self, temp_kb, temp_sim_dir):
        """Should preview without committing changes."""
        # Create process
        write_yaml(temp_kb / "processes" / "test_process.yaml", {
            'id': 'test_process',
            'kind': 'process',
            'process_type': 'batch',
            'inputs': [
                {'item_id': 'iron_ore', 'qty': 1.0, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'iron', 'qty': 1.0, 'unit': 'kg'}
            ],
            'time_model': {
                'type': 'batch',
                'hr_per_batch': 2.0
            }
        })

        # Create items
        write_yaml(temp_kb / "items" / "materials" / "iron_ore.yaml", {
            'id': 'iron_ore',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg'
        })

        write_yaml(temp_kb / "items" / "materials" / "iron.yaml", {
            'id': 'iron',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg'
        })

        # Load KB
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        # Create engine
        engine = SimulationEngine("test_sim", kb, temp_sim_dir)
        engine.import_item("iron_ore", 10.0, "kg")
        engine.start_process("test_process", scale=1.0, duration_hours=2.0)

        # Preview
        preview = engine.preview_step(2.0)

        # Should show what would complete
        assert preview["completing_count"] == 1
        assert preview["new_time"] == 2.0

        # But inventory shouldn't change
        assert "iron" not in engine.state.inventory
        assert engine.state.current_time_hours == 0.0
