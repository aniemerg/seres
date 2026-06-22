# Missing Or Suspicious CAD Items

This report covers BOM rows called out by the prior audit plus the `2AP6_outer_seal` special case.

## 1B52 - `1B52_flange_schlieren_imaging`

- CSV source row: `16`
- Status: `assembly_only`
- Export kind: `assembly`
- Raw STEP contains exact CAD product: `False`
- Canonical STEP path: `gold_export/assemblies/1B50_schlieren_imaging_door.step`
- Parent assembly: `1B50_schlieren_imaging_door`
- Alternate STEP paths: ``
- Notes: No 1B52-prefixed product was found in the raw STEP; BOM row appears collapsed into the 1B50 schlieren imaging door assembly.

## 1B61 - `1B61_seal`

- CSV source row: `17`
- Status: `assembly_only`
- Export kind: `assembly`
- Raw STEP contains exact CAD product: `False`
- Canonical STEP path: `gold_export/assemblies/1B50_schlieren_imaging_door.step`
- Parent assembly: `1B50_schlieren_imaging_door`
- Alternate STEP paths: ``
- Notes: No 1B61-prefixed product was found in the raw STEP; BOM row appears collapsed into the 1B50 schlieren imaging door assembly.

## 1B62 - `1B62_cover`

- CSV source row: `18`
- Status: `assembly_only`
- Export kind: `assembly`
- Raw STEP contains exact CAD product: `False`
- Canonical STEP path: `gold_export/assemblies/1B50_schlieren_imaging_door.step`
- Parent assembly: `1B50_schlieren_imaging_door`
- Alternate STEP paths: ``
- Notes: No 1B62-prefixed product was found in the raw STEP; BOM row appears collapsed into the 1B50 schlieren imaging door assembly.

## 2AC1 - `2AC1_part_1`

- CSV source row: `35`
- Status: `assembly_only`
- Export kind: `assembly`
- Raw STEP contains exact CAD product: `True`
- Canonical STEP path: `gold_export/assemblies/2AC0_bottom_axis_bearing_SLA10.step`
- Parent assembly: `2AC0_bottom_axis_bearing_SLA10`
- Alternate STEP paths: ``
- Notes: Raw STEP contains 2AC1_part_1, but FreeCAD imports that label with zero solids; retained larger 2AC0 bottom-axis-bearing assembly as context.

## 2AC2 - `2AC2_part_2`

- CSV source row: `36`
- Status: `assembly_only`
- Export kind: `assembly`
- Raw STEP contains exact CAD product: `True`
- Canonical STEP path: `gold_export/assemblies/2AC0_bottom_axis_bearing_SLA10.step`
- Parent assembly: `2AC0_bottom_axis_bearing_SLA10`
- Alternate STEP paths: ``
- Notes: Raw STEP contains 2AC2_part_2, but FreeCAD imports that label with zero solids; retained larger 2AC0 bottom-axis-bearing assembly as context.

## 2AC3 - `2AC3_part_3`

- CSV source row: `37`
- Status: `assembly_only`
- Export kind: `assembly`
- Raw STEP contains exact CAD product: `True`
- Canonical STEP path: `gold_export/assemblies/2AC0_bottom_axis_bearing_SLA10.step`
- Parent assembly: `2AC0_bottom_axis_bearing_SLA10`
- Alternate STEP paths: ``
- Notes: Raw STEP contains 2AC3_part_3, but FreeCAD imports that label with zero solids; retained larger 2AC0 bottom-axis-bearing assembly as context.

## 2AP6 - `2AP6_outer_seal`

- CSV source row: `75`
- Status: `missing_in_cad`
- Export kind: `unknown`
- Raw STEP contains exact CAD product: `False`
- Canonical STEP path: ``
- Parent assembly: ``
- Alternate STEP paths: ``
- Notes: No 2AP6_outer_seal product or exported file was found; 2AP6_inner_seal exists and is mapped separately.

## 17AG - `17AG_profile_60x60_300`

- CSV source row: `235`
- Status: `ambiguous`
- Export kind: `unknown`
- Raw STEP contains exact CAD product: `False`
- Canonical STEP path: ``
- Parent assembly: ``
- Alternate STEP paths: `gold_export/instances/17AG_profile_60x60_300__96_profile_60x60_300.step | gold_export/instances/17AG_profile_60x60_300__96_profile_60x60_301.step`
- Notes: No 17AG-prefixed product was found in the raw STEP. Similar 60x60x300 profiles exist as item 96, but were not substituted as the canonical BOM file.

## 17AH - `17AH_profile_60x60_350`

- CSV source row: `236`
- Status: `ambiguous`
- Export kind: `unknown`
- Raw STEP contains exact CAD product: `False`
- Canonical STEP path: ``
- Parent assembly: ``
- Alternate STEP paths: `gold_export/instances/17AH_profile_60x60_350__94_profile_60x60_350.step | gold_export/instances/17AH_profile_60x60_350__94_profile_60x60_351.step`
- Notes: No 17AH-prefixed product was found in the raw STEP. Similar 60x60x350 profiles exist as item 94, but were not substituted as the canonical BOM file.

## 41A - `41A_belt_pulley_D12-575390`

- CSV source row: `256`
- Status: `assembly_only`
- Export kind: `assembly`
- Raw STEP contains exact CAD product: `True`
- Canonical STEP path: `gold_export/assemblies/410_powder_inlet.step`
- Parent assembly: `410_powder_inlet`
- Alternate STEP paths: ``
- Notes: Raw STEP contains 41A_belt_pulley_D12-575390, but FreeCAD did not expose that label as an exportable object; retained 410 powder inlet assembly context.

## 41D - `41D_belt_pulley_D7-575457`

- CSV source row: `259`
- Status: `assembly_only`
- Export kind: `assembly`
- Raw STEP contains exact CAD product: `True`
- Canonical STEP path: `gold_export/assemblies/410_powder_inlet.step`
- Parent assembly: `410_powder_inlet`
- Alternate STEP paths: ``
- Notes: Raw STEP contains 41D_belt_pulley_D7-575457, but FreeCAD did not expose that label as an exportable object; retained 410 powder inlet assembly context.

## 419 - `419_belt_pulley_D14-575388`

- CSV source row: `333`
- Status: `assembly_only`
- Export kind: `assembly`
- Raw STEP contains exact CAD product: `True`
- Canonical STEP path: `gold_export/assemblies/410_powder_inlet.step`
- Parent assembly: `410_powder_inlet`
- Alternate STEP paths: ``
- Notes: Raw STEP contains 419_belt_pulley_D14-575388, but FreeCAD did not expose that label as an exportable object; retained 410 powder inlet assembly context.
