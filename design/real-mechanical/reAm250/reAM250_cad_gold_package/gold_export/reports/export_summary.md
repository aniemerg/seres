# Gold CAD Export Summary

- BOM rows processed: `401`
- Exported as canonical part files: `0`
- Matched to existing exact part files: `389`
- Assembly-only rows: `9`
- Missing rows: `1`
- Ambiguous rows: `2`
- Canonical paths populated: `398`

## Known Limitations

- Canonical part files are copied from the completed FreeCAD noisy export, not re-exported from raw STEP one row at a time.
- FreeCAD does not expose some raw STEP product labels as exportable solid objects, notably the 41A/41D/419 pulley labels.
- Some raw STEP products import as zero-solid FreeCAD objects, notably 2AC1, 2AC2, and 2AC3.
- Ambiguous similar profiles 17AG/17AH are not silently substituted with item 96/94 profile files.

## Recommended Follow-Up

- Use a stable Open Cascade XCAF pipeline if exact raw STEP product-label extraction is required for 41A, 41D, 419, or zero-solid labels.
- Manually inspect assembly-only rows before creating downstream research tasks that require standalone geometry.

## Assembly-Only Rows

- `1B52` `1B52_flange_schlieren_imaging` -> `1B50_schlieren_imaging_door`
- `1B61` `1B61_seal` -> `1B50_schlieren_imaging_door`
- `1B62` `1B62_cover` -> `1B50_schlieren_imaging_door`
- `2AC1` `2AC1_part_1` -> `2AC0_bottom_axis_bearing_SLA10`
- `2AC2` `2AC2_part_2` -> `2AC0_bottom_axis_bearing_SLA10`
- `2AC3` `2AC3_part_3` -> `2AC0_bottom_axis_bearing_SLA10`
- `41A` `41A_belt_pulley_D12-575390` -> `410_powder_inlet`
- `41D` `41D_belt_pulley_D7-575457` -> `410_powder_inlet`
- `419` `419_belt_pulley_D14-575388` -> `410_powder_inlet`

## Missing Rows

- `2AP6` `2AP6_outer_seal`

## Ambiguous Rows

- `17AG` `17AG_profile_60x60_300` alternatives: `gold_export/instances/17AG_profile_60x60_300__96_profile_60x60_300.step | gold_export/instances/17AG_profile_60x60_300__96_profile_60x60_301.step`
- `17AH` `17AH_profile_60x60_350` alternatives: `gold_export/instances/17AH_profile_60x60_350__94_profile_60x60_350.step | gold_export/instances/17AH_profile_60x60_350__94_profile_60x60_351.step`