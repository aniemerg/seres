# Multi-Material 3D Printer Detailed Research Report

Date: 2026-03-04
Scope: `design/srm2_bom_research_results/10_multi_material_3d_printer.md`
Purpose: represent a modular multi-tool additive platform in KB without duplicating existing WAAM/EBAM machines.

## 1) Source extraction summary
Report 10 describes a modular platform with:
- shared motion/chamber/control base
- swappable material toolheads (wire/ceramic/binder)
- integrated finishing/assembly paths

## 2) Existing KB mapping
Reusable existing IDs:
- `resource_3d_printer_basic_v0`
- `wire_arc_additive_machine`
- `ebf3_wire_feed_machine_v0`
- `quick_change_tool_interface`
- `motion_gantry_basic`

Gap:
- no explicit multi-material printer variant machine
- no explicit modular toolhead parts for this variant
- no process representing multi-material build execution

## 3) Recommended KB updates
- machine: `resource_3d_printer_multi_material_v0`
- BOM + recipe for machine
- parts:
  - `toolhead_powder_deposition_v0`
  - `toolhead_wire_deposition_v0`
  - `toolhead_binder_dispense_v0`
- process: `multi_material_additive_manufacturing_v0`
- output material: `multi_material_fabricated_part_v0`

