# 10 Multi-Material 3D Printer - KB Integration Plan

Detailed basis:
- `design/srm2_per_result_plans/10_multi_material_3d_printer_detailed_research_report.md`

## Scope in report
- Printer architecture supporting multiple feedstocks/toolheads.

## Current KB mapping
- Existing printer/motion assets:
  - `resource_3d_printer_basic_v0`
  - `wire_arc_additive_machine`
  - `motion_gantry_basic`, `quick_change_tool_interface`
- No explicit multi-material printer ID.

## Decision
- `variant` approach: base printer + toolhead modules.
- Avoid monolithic new machine where possible.

## Proposed KB deltas
- Add machine variant: `resource_3d_printer_multi_material_v0`
- Add parts:
  - `toolhead_powder_deposition_v0`
  - `toolhead_wire_deposition_v0`
  - `toolhead_binder_dispense_v0` (if report supports it)
- Add process:
  - `multi_material_additive_manufacturing_v0`
- Update recipe/BOM for printer to include modular toolhead interface.

## Machine requirements for new process
- `resource_3d_printer_multi_material_v0`
- Optional explicit dependencies:
  - feed prep equipment for powder/wire conditioning

## Key risks / open issues
- Ensure variants do not duplicate WAAM/EBM machine semantics.
- Inputs/outputs must remain explicit per recipe variant to satisfy validator behavior.
