"""
Tests for Closure Analysis Tool
"""
import pytest
from pathlib import Path
import tempfile
import yaml

from src.indexer.closure_analysis import ClosureAnalyzer, format_closure_report
from src.kb_core.kb_loader import KBLoader


@pytest.fixture
def temp_kb(tmp_path):
    """Create a temporary KB directory with test data."""
    kb_root = tmp_path / "kb"

    # Create directory structure
    (kb_root / "items" / "materials").mkdir(parents=True, exist_ok=True)
    (kb_root / "items" / "parts").mkdir(parents=True, exist_ok=True)
    (kb_root / "items" / "machines").mkdir(parents=True, exist_ok=True)
    (kb_root / "imports").mkdir(parents=True, exist_ok=True)
    (kb_root / "recipes").mkdir(parents=True, exist_ok=True)
    (kb_root / "processes").mkdir(parents=True, exist_ok=True)
    (kb_root / "boms").mkdir(parents=True, exist_ok=True)

    return kb_root


def write_yaml(path: Path, data: dict):
    """Helper to write YAML files."""
    with path.open('w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)


class TestBasicMachineAnalysis:
    """Test basic machine closure analysis."""

    def test_simple_machine_with_bom(self, temp_kb):
        """Should analyze a simple machine with BOM."""
        # Create raw material
        write_yaml(temp_kb / "items" / "materials" / "steel_raw.yaml", {
            'id': 'steel_raw',
            'kind': 'material',
            'name': 'Raw Steel',
            'mass': 10.0,
            'unit': 'kg',
            'is_raw_material': True
        })

        # Create part with recipe
        write_yaml(temp_kb / "items" / "parts" / "steel_plate.yaml", {
            'id': 'steel_plate',
            'kind': 'part',
            'name': 'Steel Plate',
            'mass': 5.0,
            'unit': 'kg',
            'recipe': 'recipe_steel_plate'
        })

        # Create recipe
        write_yaml(temp_kb / "recipes" / "recipe_steel_plate.yaml", {
            'id': 'recipe_steel_plate',
            'kind': 'recipe',
            'target_item_id': 'steel_plate',
            'inputs': [
                {'item_id': 'steel_raw', 'qty': 1.0, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'steel_plate', 'qty': 1.0, 'unit': 'kg'}
            ],
            'steps': []
        })

        # Create machine
        write_yaml(temp_kb / "items" / "machines" / "test_machine.yaml", {
            'id': 'test_machine',
            'kind': 'machine',
            'name': 'Test Machine',
            'mass': 100.0,
            'unit': 'kg',
            'bom': 'test_machine'
        })

        # Create BOM
        write_yaml(temp_kb / "boms" / "test_machine.yaml", {
            'machine_id': 'test_machine',
            'components': [
                {'item_id': 'steel_plate', 'qty': 2.0, 'unit': 'count'}
            ]
        })

        # Load and analyze
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        result = analyzer.analyze_machine('test_machine')

        # Assertions
        assert result['machine_id'] == 'test_machine'
        assert result['machine_name'] == 'Test Machine'
        assert result['total_mass'] == 100.0

        # Should have raw material
        assert 'steel_raw' in result['raw_materials']
        assert result['raw_materials']['steel_raw']['qty'] == 2.0  # 2 plates * 1 kg each

        # Should have ISRU percentage
        assert result['isru_percent'] > 0
        assert result['imported_percent'] == 0
        assert len(result['errors']) == 0

    def test_machine_with_imported_component(self, temp_kb):
        """Should classify imported items correctly."""
        # Create imported item
        write_yaml(temp_kb / "imports" / "import_electronics.yaml", {
            'id': 'import_electronics',
            'kind': 'part',
            'name': 'Imported Electronics',
            'mass': 2.0,
            'unit': 'kg',
            'is_import': True
        })

        # Create machine
        write_yaml(temp_kb / "items" / "machines" / "smart_machine.yaml", {
            'id': 'smart_machine',
            'kind': 'machine',
            'name': 'Smart Machine',
            'mass': 50.0,
            'unit': 'kg',
            'bom': 'smart_machine'
        })

        # Create BOM
        write_yaml(temp_kb / "boms" / "smart_machine.yaml", {
            'machine_id': 'smart_machine',
            'components': [
                {'item_id': 'import_electronics', 'qty': 1.0, 'unit': 'count'}
            ]
        })

        # Load and analyze
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        result = analyzer.analyze_machine('smart_machine')

        # Assertions
        assert 'import_electronics' in result['imported_items']
        assert result['imported_items']['import_electronics']['qty'] == 1.0
        assert result['imported_mass'] == 2.0
        assert result['imported_percent'] == 100.0
        assert result['isru_percent'] == 0.0


class TestRawMaterialDetection:
    """Test raw material classification."""

    def test_explicit_is_raw_material_field(self, temp_kb):
        """Should detect raw material by is_raw_material field."""
        write_yaml(temp_kb / "items" / "materials" / "ore.yaml", {
            'id': 'ore',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg',
            'is_raw_material': True
        })

        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        item = kb.get_item('ore')
        item_dict = analyzer._to_dict(item)

        assert analyzer._is_raw_material('ore', item_dict) is True

    def test_raw_material_by_folder(self, temp_kb):
        """Items outside raw_materials folder are not raw materials."""
        write_yaml(temp_kb / "items" / "materials" / "iron_ore.yaml", {
            'id': 'iron_ore',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg',
            'defined_in': 'kb/items/materials/iron_ore.yaml'
        })

        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        item = kb.get_item('iron_ore')
        item_dict = analyzer._to_dict(item)

        assert analyzer._is_raw_material('iron_ore', item_dict) is False

    def test_raw_material_by_notes(self, temp_kb):
        """Should detect raw material by BASE marker in notes."""
        write_yaml(temp_kb / "items" / "materials" / "base_metal.yaml", {
            'id': 'base_metal',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg',
            'notes': 'BASE material extracted from ground'
        })

        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        item = kb.get_item('base_metal')
        item_dict = analyzer._to_dict(item)

        assert analyzer._is_raw_material('base_metal', item_dict) is True


class TestImportedItemDetection:
    """Test imported item classification."""

    def test_explicit_is_import_field(self, temp_kb):
        """Should detect import by is_import field."""
        write_yaml(temp_kb / "imports" / "chip.yaml", {
            'id': 'chip',
            'kind': 'part',
            'mass': 0.1,
            'unit': 'kg',
            'is_import': True
        })

        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        item = kb.get_item('chip')
        item_dict = analyzer._to_dict(item)

        assert analyzer._is_imported('chip', item_dict) is True

    def test_import_by_prefix(self, temp_kb):
        """Should detect import by import_ prefix."""
        write_yaml(temp_kb / "imports" / "import_widget.yaml", {
            'id': 'import_widget',
            'kind': 'part',
            'mass': 1.0,
            'unit': 'kg'
        })

        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        item = kb.get_item('import_widget')
        item_dict = analyzer._to_dict(item)

        assert analyzer._is_imported('import_widget', item_dict) is True


class TestMassCalculations:
    """Test mass calculation logic."""

    def test_calculate_mass_kg_to_kg(self, temp_kb):
        """Should calculate mass for kg to kg conversion."""
        analyzer = ClosureAnalyzer(KBLoader(temp_kb))

        item = {'mass': 10.0, 'unit': 'kg'}
        mass = analyzer._calculate_mass(item, qty=5.0, unit='kg')

        assert mass == 5.0  # qty in kg

    def test_calculate_mass_count_to_kg(self, temp_kb):
        """Should calculate mass for count to kg conversion."""
        analyzer = ClosureAnalyzer(KBLoader(temp_kb))

        item = {'mass': 2.5, 'unit': 'kg'}
        mass = analyzer._calculate_mass(item, qty=4.0, unit='count')

        assert mass == 10.0  # 4 * 2.5 kg

    def test_calculate_mass_none_item(self, temp_kb):
        """Should handle None item gracefully."""
        analyzer = ClosureAnalyzer(KBLoader(temp_kb))

        mass = analyzer._calculate_mass(None, qty=5.0, unit='kg')

        assert mass == 0.0


class TestCircularDependencies:
    """Test circular dependency handling."""

    def test_circular_dependency_detection(self, temp_kb):
        """Should detect circular dependencies and treat as bootstrap import."""
        # Create items that reference each other
        write_yaml(temp_kb / "items" / "parts" / "part_a.yaml", {
            'id': 'part_a',
            'kind': 'part',
            'mass': 10.0,
            'unit': 'kg',
            'recipe': 'recipe_part_a'
        })

        write_yaml(temp_kb / "items" / "parts" / "part_b.yaml", {
            'id': 'part_b',
            'kind': 'part',
            'mass': 10.0,
            'unit': 'kg',
            'recipe': 'recipe_part_b'
        })

        # Recipe A requires B
        write_yaml(temp_kb / "recipes" / "recipe_part_a.yaml", {
            'id': 'recipe_part_a',
            'kind': 'recipe',
            'target_item_id': 'part_a',
            'inputs': [
                {'item_id': 'part_b', 'qty': 1.0, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'part_a', 'qty': 1.0, 'unit': 'kg'}
            ],
            'steps': []
        })

        # Recipe B requires A (circular!)
        write_yaml(temp_kb / "recipes" / "recipe_part_b.yaml", {
            'id': 'recipe_part_b',
            'kind': 'recipe',
            'target_item_id': 'part_b',
            'inputs': [
                {'item_id': 'part_a', 'qty': 1.0, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'part_b', 'qty': 1.0, 'unit': 'kg'}
            ],
            'steps': []
        })

        # Create machine requiring part_a
        write_yaml(temp_kb / "items" / "machines" / "circular_machine.yaml", {
            'id': 'circular_machine',
            'kind': 'machine',
            'name': 'Circular Machine',
            'mass': 100.0,
            'unit': 'kg',
            'bom': 'circular_machine'
        })

        write_yaml(temp_kb / "boms" / "circular_machine.yaml", {
            'machine_id': 'circular_machine',
            'components': [
                {'item_id': 'part_a', 'qty': 1.0, 'unit': 'count'}
            ]
        })

        # Load and analyze
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        result = analyzer.analyze_machine('circular_machine')

        # Should detect circular dependency and treat as import
        assert len(result['imported_items']) > 0
        assert any('circular' in err.lower() for err in result['errors'])


class TestUnresolvedItems:
    """Test unresolved item detection."""

    def test_missing_item_definition(self, temp_kb):
        """Should mark missing items as unresolved."""
        # Create machine referencing non-existent part
        write_yaml(temp_kb / "items" / "machines" / "broken_machine.yaml", {
            'id': 'broken_machine',
            'kind': 'machine',
            'name': 'Broken Machine',
            'mass': 100.0,
            'unit': 'kg',
            'bom': 'broken_machine'
        })

        write_yaml(temp_kb / "boms" / "broken_machine.yaml", {
            'machine_id': 'broken_machine',
            'components': [
                {'item_id': 'nonexistent_part', 'qty': 1.0, 'unit': 'count'}
            ]
        })

        # Load and analyze
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        result = analyzer.analyze_machine('broken_machine')

        # Should have unresolved item
        assert 'nonexistent_part' in result['unresolved_items']
        assert any('not found' in err for err in result['errors'])

    def test_item_without_recipe_not_raw(self, temp_kb):
        """Should mark items without recipe (and not raw) as unresolved."""
        # Create part without recipe
        write_yaml(temp_kb / "items" / "parts" / "no_recipe_part.yaml", {
            'id': 'no_recipe_part',
            'kind': 'part',
            'mass': 5.0,
            'unit': 'kg'
            # No recipe field, not a raw material
        })

        # Create machine
        write_yaml(temp_kb / "items" / "machines" / "incomplete_machine.yaml", {
            'id': 'incomplete_machine',
            'kind': 'machine',
            'name': 'Incomplete Machine',
            'mass': 100.0,
            'unit': 'kg',
            'bom': 'incomplete_machine'
        })

        write_yaml(temp_kb / "boms" / "incomplete_machine.yaml", {
            'machine_id': 'incomplete_machine',
            'components': [
                {'item_id': 'no_recipe_part', 'qty': 1.0, 'unit': 'count'}
            ]
        })

        # Load and analyze
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        result = analyzer.analyze_machine('incomplete_machine')

        # Should be unresolved
        assert 'no_recipe_part' in result['unresolved_items']
        assert any('no recipe' in err for err in result['errors'])


class TestFormatting:
    """Test report formatting."""

    def test_format_closure_report(self, temp_kb):
        """Should format report correctly."""
        result = {
            'machine_id': 'test_machine',
            'machine_name': 'Test Machine',
            'total_mass': 100.0,
            'raw_materials': {
                'steel_raw': {'qty': 10.0, 'unit': 'kg', 'mass_kg': 10.0}
            },
            'imported_items': {
                'import_chip': {'qty': 2.0, 'unit': 'count', 'mass_kg': 0.5}
            },
            'unresolved_items': {},
            'isru_mass': 10.0,
            'imported_mass': 0.5,
            'unresolved_mass': 0.0,
            'isru_percent': 95.2,
            'imported_percent': 4.8,
            'unresolved_percent': 0.0,
            'errors': []
        }

        report = format_closure_report(result)

        # Should contain key sections
        assert 'Test Machine' in report
        assert 'MATERIAL BREAKDOWN' in report
        assert 'RAW MATERIALS' in report
        assert 'IMPORTED ITEMS' in report
        assert 'steel_raw' in report
        assert 'import_chip' in report
        assert '95.2%' in report
        assert '4.8%' in report


class TestCaching:
    """Test expansion caching."""

    def test_caching_prevents_redundant_expansion(self, temp_kb):
        """Should cache expansion results and reuse them."""
        # Create raw material
        write_yaml(temp_kb / "items" / "materials" / "metal.yaml", {
            'id': 'metal',
            'kind': 'material',
            'mass': 1.0,
            'unit': 'kg',
            'is_raw_material': True
        })

        # Create part with recipe
        write_yaml(temp_kb / "items" / "parts" / "bolt.yaml", {
            'id': 'bolt',
            'kind': 'part',
            'mass': 0.1,
            'unit': 'kg',
            'recipe': 'recipe_bolt'
        })

        write_yaml(temp_kb / "recipes" / "recipe_bolt.yaml", {
            'id': 'recipe_bolt',
            'kind': 'recipe',
            'target_item_id': 'bolt',
            'inputs': [
                {'item_id': 'metal', 'qty': 0.1, 'unit': 'kg'}
            ],
            'outputs': [
                {'item_id': 'bolt', 'qty': 1.0, 'unit': 'count'}
            ],
            'steps': []
        })

        # Create machine using bolts multiple times
        write_yaml(temp_kb / "items" / "machines" / "cached_machine.yaml", {
            'id': 'cached_machine',
            'kind': 'machine',
            'mass': 100.0,
            'unit': 'kg',
            'bom': 'cached_machine'
        })

        write_yaml(temp_kb / "boms" / "cached_machine.yaml", {
            'machine_id': 'cached_machine',
            'components': [
                {'item_id': 'bolt', 'qty': 10.0, 'unit': 'count'},
                {'item_id': 'bolt', 'qty': 5.0, 'unit': 'count'}
            ]
        })

        # Load and analyze
        kb = KBLoader(temp_kb, use_validated_models=False)
        kb.load_all()

        analyzer = ClosureAnalyzer(kb)
        result = analyzer.analyze_machine('cached_machine')

        # Should have accumulated metal correctly (15 bolts * 0.1 kg each)
        assert 'metal' in result['raw_materials']
        assert result['raw_materials']['metal']['qty'] == pytest.approx(1.5, rel=1e-2)

        # Should have cache entries
        assert len(analyzer.expansion_cache) > 0
