#!/usr/bin/env python3
"""
Phase 2c: Mark all 60 HIGH confidence template candidates.

Based on systematic review of all 843 processes, these 60 processes have:
- Generic placeholder inputs (wet_, rough_, bulk_, unfinished_, etc.)
- "or" patterns in input/output names
- Empty inputs/outputs (explicit templates)
- Notes explicitly saying "placeholder" or "generic"
- Generic plural terms (components, parts, assemblies, equipment)
"""

import yaml
from pathlib import Path
from typing import Dict, Any


PHASE_2C_TEMPLATE_CANDIDATES = {
    # Manufacturing Operations (14)
    'drying_basic_v0': {
        'generic_input': 'wet_material',
        'category': 'Manufacturing',
        'justification': 'Generic drying operation with wet_material placeholder'
    },
    'cleaning_basic_v0': {
        'generic_input': 'part_to_clean, cleaning_solvent_or_detergent',
        'category': 'Manufacturing',
        'justification': 'Generic cleaning with "or" pattern in solvent'
    },
    'grinding_basic_v0': {
        'generic_input': 'rough_part',
        'category': 'Manufacturing',
        'justification': 'Generic grinding with rough_part placeholder'
    },
    'heating_basic_v0': {
        'generic_input': 'bulk_material',
        'category': 'Manufacturing',
        'justification': 'Generic heating with bulk_material placeholder'
    },
    'drilling_basic_v0': {
        'generic_input': 'formed_metal_part',
        'category': 'Manufacturing',
        'justification': 'Generic drilling operation'
    },
    'welding_basic_v0': {
        'generic_input': 'steel_stock',
        'category': 'Manufacturing',
        'justification': 'Generic welding producing assemblies'
    },
    'crushing_basic_v0': {
        'generic_input': 'feedstock',
        'category': 'Manufacturing',
        'justification': 'Generic crushing for rock/mineral feedstock'
    },
    'casting_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Manufacturing',
        'justification': 'Empty template - notes say "placeholder parameters"'
    },
    'rolling_basic_v0': {
        'generic_input': 'metal_ingot',
        'category': 'Manufacturing',
        'justification': 'Generic metal rolling operation'
    },
    'extrusion_basic_v0': {
        'generic_input': 'polymer_feedstock',
        'category': 'Manufacturing',
        'justification': 'Generic extrusion with feedstock'
    },
    'molding_basic_v0': {
        'generic_input': 'plastic_pellets',
        'category': 'Manufacturing',
        'justification': 'Generic molding - notes say "Placeholder basic molding"'
    },
    'annealing_basic_v0': {
        'generic_input': 'material_unannealed',
        'category': 'Manufacturing',
        'justification': 'Generic unannealed/annealed pattern'
    },
    'finishing_basic_v0': {
        'generic_input': 'unfinished_part',
        'category': 'Manufacturing',
        'justification': 'Perfect generic unfinished/finished pattern'
    },
    'sawing_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Manufacturing',
        'justification': 'Empty template - notes say "placeholder parameters"'
    },

    # Material Processing (12)
    'filtration_basic_v0': {
        'generic_input': 'treated_cutting_fluid',
        'category': 'Material Processing',
        'justification': 'Generic filtration step'
    },
    'evaporation_basic_v0': {
        'generic_input': 'material',
        'category': 'Material Processing',
        'justification': 'Generic evaporation - notes say "Basic evaporation step"'
    },
    'screening_basic_v0': {
        'generic_input': 'powder_metal_or_ceramic',
        'category': 'Material Processing',
        'justification': 'Uses "or" pattern for generic powder screening'
    },
    'batching_and_mixing_basic_v0': {
        'generic_input': 'powder_components',
        'category': 'Material Processing',
        'justification': 'Generic powder batching with "components" plural'
    },
    'sintering_basic_v0': {
        'generic_input': 'powder_metal_or_ceramic',
        'category': 'Material Processing',
        'justification': 'Uses "or" pattern for generic sintering'
    },
    'melting_basic_v0': {
        'generic_input': 'metal_alloy_bulk',
        'category': 'Material Processing',
        'justification': 'Generic melting - notes say "Generic melting step"'
    },
    'alloying_basic_v0': {
        'generic_input': 'metal_feedstock',
        'category': 'Material Processing',
        'justification': 'Generic alloying with feedstock pattern'
    },
    'ceramic_forming_basic_v0': {
        'generic_input': 'ceramic_powder_mixture',
        'category': 'Material Processing',
        'justification': 'Generic ceramic forming with parts plural'
    },
    'ceramic_casting_basic_v0': {
        'generic_input': 'ceramic_material',
        'category': 'Material Processing',
        'justification': 'Generic ceramic casting - notes say "Placeholder values"'
    },
    'pressing_operations_basic_v0': {
        'generic_input': 'feedstock_material',
        'category': 'Material Processing',
        'justification': 'Perfect generic feedstock pattern'
    },
    'holding_and_pouring_basic_v0': {
        'generic_input': 'molten_material',
        'category': 'Material Processing',
        'justification': 'Generic holding/pouring operation'
    },
    'shakeout_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Material Processing',
        'justification': 'Empty template for casting cleanup'
    },

    # Assembly & Integration (14)
    'electrical_assembly_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Assembly',
        'justification': 'Empty template - notes say "Basic electrical assembly"'
    },
    'electrical_testing_basic_v0': {
        'generic_input': 'assembled_electrical_equipment',
        'category': 'Assembly',
        'justification': 'Generic assembled/tested pattern'
    },
    'coil_winding_basic_v0': {
        'generic_input': 'wire (aluminum or copper)',
        'category': 'Assembly',
        'justification': 'Generic coil winding operation'
    },
    'soldering_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Assembly',
        'justification': 'Empty template - notes say "placeholder pending detailed solder"'
    },
    'pcb_assembly_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Assembly',
        'justification': 'Empty template for PCB population'
    },
    'enclosure_assembly_basic_v0': {
        'generic_input': 'enclosure + equipment',
        'category': 'Assembly',
        'justification': 'Generic enclosure assembly'
    },
    'frame_fabrication_basic_v0': {
        'generic_input': 'steel_stock',
        'category': 'Assembly',
        'justification': 'Generic structural frame fabrication'
    },
    'metal_fabrication_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Assembly',
        'justification': 'Empty template - notes say "Generic metal fabrication"'
    },
    'machine_assembly_basic_v0': {
        'generic_input': 'frame + electronics',
        'category': 'Assembly',
        'justification': 'Generic machine assembly from components'
    },
    'assembly_process_general_v0': {
        'generic_input': 'assembly_components',
        'category': 'Assembly',
        'justification': 'Perfect generic components → equipment - notes say "Generic assembly"'
    },
    'fitting_assembly_basic_v0': {
        'generic_input': 'metal_fittings_raw',
        'category': 'Assembly',
        'justification': 'Generic fitting assembly'
    },
    'sealing_and_assembly_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Assembly',
        'justification': 'Empty template for sealing operations'
    },
    'crimping_and_soldering_basic_v0': {
        'generic_input': 'electrical_wire_and_connectors',
        'category': 'Assembly',
        'justification': 'Generic wire harness assembly'
    },
    'alignment_and_testing_basic_v0': {
        'generic_input': 'assembled_equipment',
        'category': 'Assembly',
        'justification': 'Generic assembled/tested pattern'
    },

    # Metalworking & Machining (10)
    'gear_cutting_basic_v0': {
        'generic_input': 'steel_stock_bar_or_billet',
        'category': 'Metalworking',
        'justification': 'Uses "or" pattern for generic gear cutting'
    },
    'wire_drawing_basic_v0': {
        'generic_input': 'metal_wire_feed',
        'category': 'Metalworking',
        'justification': 'Generic wire drawing operation'
    },
    'metal_cutting_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Metalworking',
        'justification': 'Empty template for cutting stock'
    },
    'welding_tig_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Metalworking',
        'justification': 'Empty template for TIG welding'
    },
    'welding_brazing_basic_v0': {
        'generic_input': 'cast_metal_parts',
        'category': 'Metalworking',
        'justification': 'Generic parts → assemblies - notes say "Joining anchor"'
    },
    'welded_fabrication_basic_v0': {
        'generic_input': 'steel_stock',
        'category': 'Metalworking',
        'justification': 'Generic stock → fabrications pattern'
    },
    'spur_gear_cutting_basic_v0': {
        'generic_input': 'gear_set',
        'category': 'Metalworking',
        'justification': 'Generic gear cutting - notes say "Placeholder time/energy"'
    },
    'helical_gear_cutting_basic_v0': {
        'generic_input': 'gear_set',
        'category': 'Metalworking',
        'justification': 'Generic gear cutting - notes say "Placeholder time/energy"'
    },
    'bevel_gear_cutting_basic_v0': {
        'generic_input': 'gear_set',
        'category': 'Metalworking',
        'justification': 'Generic gear cutting - notes say "Placeholder time/energy"'
    },
    'worm_gear_cutting_basic_v0': {
        'generic_input': 'gear_set',
        'category': 'Metalworking',
        'justification': 'Generic gear cutting operation'
    },

    # Heat Treatment & Finishing (6)
    'stress_relief_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Heat Treatment',
        'justification': 'Empty template for stress relief'
    },
    'firing_ceramic_basic_v0': {
        'generic_input': 'EMPTY',
        'category': 'Heat Treatment',
        'justification': 'Empty template for ceramic firing'
    },
    'bearing_installation_basic_v0': {
        'generic_input': 'bearing_set + rough_part',
        'category': 'Heat Treatment',
        'justification': 'Generic rough/finished pattern'
    },
    'calibration_and_test_basic_v0': {
        'generic_input': 'device_uncalibrated',
        'category': 'Heat Treatment',
        'justification': 'Perfect generic uncalibrated/calibrated pattern'
    },
    'balancing_dynamic_basic_v0': {
        'generic_input': 'machined_part_raw',
        'category': 'Heat Treatment',
        'justification': 'Generic dynamic balancing'
    },
    'lamination_basic_v0': {
        'generic_input': 'substrate + copper_plate_or_sheet',
        'category': 'Heat Treatment',
        'justification': 'Uses "or" pattern - notes say "Baseline lamination"'
    },

    # Non-basic but Generic (4)
    'microcontroller_ic_generic_fabrication_v0': {
        'generic_input': 'silicon wafer',
        'category': 'Generic Process',
        'justification': 'Name includes "generic" - notes say "Placeholder fabrication"'
    },
    'motor_assembly_standard_fabrication_v0': {
        'generic_input': 'steel_stock',
        'category': 'Generic Process',
        'justification': 'Name includes "standard" - generic motor assembly'
    },
    'casting_or_fabrication_machine_frame_v0': {
        'generic_input': 'raw_metal_block',
        'category': 'Generic Process',
        'justification': 'Name uses "or" pattern - notes say "placeholder"'
    },
    'plate_rolling_basic_v0': {
        'generic_input': 'steel_billet_or_slab',
        'category': 'Generic Process',
        'justification': 'Uses "or" pattern in both input and output'
    },
}


def mark_process_as_template(process_path: Path, process_id: str, info: Dict[str, Any]) -> bool:
    """Add is_template: true to a process definition."""
    if not process_path.exists():
        print(f'  ✗ File not found: {process_path}')
        return False

    try:
        with open(process_path, 'r', encoding='utf-8') as f:
            content = f.read()

        data = yaml.safe_load(content)
        if not data:
            print(f'  ✗ Empty or invalid YAML: {process_path}')
            return False

        # Check if already a template
        if data.get('is_template'):
            print(f'  ⊙ Already a template: {process_id}')
            return False

        # Add is_template field
        data['is_template'] = True

        # Write back
        with open(process_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        return True

    except Exception as e:
        print(f'  ✗ Error processing {process_path}: {e}')
        return False


def main():
    """Main entry point."""
    project_root = Path(__file__).parent.parent
    processes_dir = project_root / 'kb' / 'processes'

    print('='*70)
    print('PHASE 2C: MARKING 60 HIGH CONFIDENCE TEMPLATE CANDIDATES')
    print('='*70)
    print()
    print('Based on systematic review of all 843 processes.')
    print('These processes have generic placeholders, "or" patterns, empty inputs,')
    print('or explicit "placeholder"/"generic" notes.')
    print()

    modified_count = 0
    already_template_count = 0
    not_found_count = 0

    # Group by category for reporting
    by_category = {}
    for process_id, info in PHASE_2C_TEMPLATE_CANDIDATES.items():
        category = info['category']
        if category not in by_category:
            by_category[category] = []
        by_category[category].append((process_id, info))

    for category in sorted(by_category.keys()):
        print(f'\n{"="*70}')
        print(f'{category} ({len(by_category[category])} processes)')
        print('='*70)

        for process_id, info in by_category[category]:
            process_path = processes_dir / f'{process_id}.yaml'

            print(f'\n{process_id}:')
            print(f'  Generic input: {info["generic_input"]}')
            print(f'  Justification: {info["justification"]}')

            result = mark_process_as_template(process_path, process_id, info)

            if result:
                print(f'  ✓ Marked as template')
                modified_count += 1
            elif process_path.exists():
                already_template_count += 1
            else:
                not_found_count += 1

    print('\n' + '='*70)
    print('PHASE 2C SUMMARY:')
    print(f'  Processes marked as template: {modified_count}')
    print(f'  Already templates: {already_template_count}')
    print(f'  Not found: {not_found_count}')
    print(f'  Total processed: {len(PHASE_2C_TEMPLATE_CANDIDATES)}')
    print('='*70)
    print()
    print('Combined Phases 2 + 2b + 2c:')
    print(f'  Phase 2: 7 templates')
    print(f'  Phase 2b: 9 templates')
    print(f'  Phase 2c: {modified_count} templates')
    phase2_total = 7 + 9 + modified_count
    print(f'  Total new templates: {phase2_total}')
    print(f'  KB now has: {16 + phase2_total} templates (was 16)')
    print('='*70)
    print()
    print('Expected impact:')
    print(f'  Estimated errors eliminated: 700-1,000')
    print(f'  Remaining errors (estimated): ~1,100-1,400')
    print('='*70)


if __name__ == '__main__':
    main()
