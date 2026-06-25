---
row_identity:
  item: 2AC3
  cad_file: 2AC3_part_3
  source_row_number: 37
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: Bottom-axis supported bearing block for the reAM250 lower axis bearing assembly; it supports a 16 mm shaft/ballscrew end radially while matching the axis height of the paired HIWIN SFA/GFD support hardware.
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0037_2AC3__views_2x2.png; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "BOM row 37 names item 2AC3/2AC3_part_3 as 'axis bearing bottom'. The manifest maps it to bottom-axis-bearing assembly context 2AC0_bottom_axis_bearing_SLA10. The rendered context shows a pillow-block-like bearing support with a central bearing bore and mounting ears. HIWIN identifies SLA10 as a supported bearing, shaft nominal diameter 16 mm, with dimensions L 86 mm, B 24 mm, H 58 mm and bearing type 6200.2RS; those dimensions match the FreeCAD context bbox 86.00 x 24.00 x 58.00 mm."
    evidence_basis: independent_vendor_spec
  assumptions:
    - The row label 2AC3_part_3 imports with zero solids, so the matching SLA10 assembly context is treated as the row-level geometry/function proxy.
  uncertainty_notes:
    - The exact 2AC3 subpart cannot be isolated from the supplied CAD; function could represent one instance/subcomponent within the bottom-axis bearing assembly rather than a separately modeled commercial unit.
mass:
  value_kg: 0.53
  basis: "FreeCAD measured the available SLA10 assembly context volume as 67013.783 mm3. Treating that whole context as a steel-family metal volume gives 67013.783 mm3 x 1e-9 m3/mm3 x 7850 kg/m3 = 0.526 kg, rounded to 0.53 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/2AC0_bottom_axis_bearing_SLA10.step; kb/materials/properties.yaml; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "FreeCAD measured 6 solids, volume 67013.783 mm3, area 20516.186 mm2, bbox 86.00 x 24.00 x 58.00 mm for the assembly context. The local density table gives generic steel density as 7850 kg/m3. HIWIN SLA10 dimensions match the CAD context, but no row-level catalog mass was found. targeted_web_search: tried 'SLA10 bottom axis bearing material SLA10 bearing housing', 'HIWIN SLA supported bearing material SLA10 housing steel', and 'HIWIN SLA10 mass weight'; results identified function/dimensions but did not provide a row-specific mass."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The available assembly context volume is used as the row-level volume because the manifest says the specific 2AC3 label imported with zero solids.
    - A steel-family effective density is used as a conservative first estimate for the metal bearing support unit.
  uncertainty_notes:
    - If the isolated 2AC3 part is only one housing half, spacer, or other subcomponent of the SLA10 context, the row mass may be materially lower than 0.53 kg.
    - If the housing is aluminum, zinc alloy, cast iron, or a mixed metal/rubber bearing assembly, the all-steel-density estimate could be off by more than a factor of two.
material:
  primary_material: unknown metal/alloy bearing support unit with rolling bearing and seal elements
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "Local STEP material extraction for 2AC3_part_3 returned only Generic with density 1000.0, which is placeholder metadata. HIWIN identifies the matching SLA10 as a supported bearing using bearing type 6200.2RS, but the checked product page did not state housing or bearing material. targeted_web_search: tried 'HIWIN SLA supported bearing material SLA10 housing steel', 'HIWIN SFA SLA bearing units material housing', and 'HIWIN ballscrew supports SLA10 material datasheet'; no row-matched material grade/specification was found."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The functional item is modeled broadly as a metal/alloy bearing support rather than assigning an unsupported steel, cast iron, or aluminum grade.
  uncertainty_notes:
    - Material grade is unresolved at the level needed for manufacturing; later KB work should split housing, bearing, circlip, and seal materials if a catalog drawing or teardown source is found.
how_to_make:
  summary: "Fabricate the support housing, Manufacture a 6200.2RS bearing, add the circlip/seals, and assemble/inspect the bearing block"
  manufacturing_steps:
    - For local manufacture, machine or cast the bearing housing to the 86 mm x 24 mm x 58 mm envelope with mounting features and a bearing seat.
    - Install a 6200.2RS bearing and circlip, then check bore alignment, shaft fit, and radial support function in the bottom-axis assembly.
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0037_2AC3__views_2x2.png; https://www.hiwin.de/en/Products/Bearings/Bearings-SFA-SLA/SLA/SLA10/p/18-000127"
    cited_fact_or_basis: "The vendor page identifies a ready-made SLA10 supported bearing with dimensions and 6200.2RS bearing type. The preview shows a compact bearing block with central bore and mounting ears. The detailed machining/casting and assembly route is inferred from geometry and standard bearing-block construction rather than stated by a source. targeted_web_search: tried 'HIWIN SLA10 manufacturing housing material', 'HIWIN SLA10 datasheet material', and 'SLA10 bearing block material'; results did not provide a row-specific manufacturing process."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The inferred Manufacturing route assumes conventional bearing-block construction: machined/cast housing plus installed rolling bearing and retainer hardware.
  uncertainty_notes:
    - Without a manufacturer drawing or teardown, local manufacturing details such as heat treatment, fits/tolerances, housing alloy, seal material, and bearing preload are not resolved.
kb_implications:
  - "item_granularity: complex_module - Model this row as a functional SLA10-class supported bearing block for this pass; split into housing, 6200.2RS bearing, circlip/seal, and assembly operations only when a sub-BOM or material drawing is available."
---

