---
row_identity:
  item: "3S45"
  cad_file: "3S45_part_5"
  source_row_number: 156
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom gas outlet segment, part 5 of the 3S41-3S48 gas outlet group; the CAD shows a small thin bent sheet or wall segment used as one piece of the larger gas outlet path."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S45_part_5.step; research/ream250_bom/ream250_bom_row_0156_3S45__views_2x2.png"
    cited_fact_or_basis: "BOM row 156 lists item 3S45, quantity 1, CAD file 3S45_part_5, description 'gas outlet: part 5'. The manifest maps row 156 to one matched_existing part STEP. FreeCAD measured one solid with volume 4745.527 mm^3 and a 21.00 x 50.00 x 90.71 mm bounding box; the rendered preview shows a thin folded panel-like outlet segment."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted within neighboring BOM rows 3S41 through 3S48, which are sequential 'gas outlet' parts, so this is one custom segment of the larger outlet rather than a standalone fitting."
  uncertainty_notes:
    - "The CAD/BOM evidence identifies the gas outlet role and segment geometry, but not exact flow direction, mating interface, or sealing method."
mass:
  value_kg: 0.0373
  basis: "Per-unit estimate for quantity 1. FreeCAD measured CAD solid volume 4745.527 mm^3, or 0.000004745527 m^3. Using the local steel density constant 7850 kg/m^3 gives 0.03725 kg, rounded to 0.0373 kg for one physical 3S45 part."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S45_part_5.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 4745.527 mm^3, area 9792.452 mm^2, and bounding box 21.00 x 50.00 x 90.71 mm. Local assembly STEP material extraction for 3S45_part_5 returned only placeholder material 'Generic' with density 1000.0. The local density table lists steel density_kg_per_m3: 7850 and stainless_steel density_kg_per_m3: 8000. targeted_web_search: searched '3S45_part_5 gas outlet reAM250 material', '3S45 gas outlet reAM250', 'reAM250 gas outlet material', and 'Renishaw AM250 gas outlet material'; results provided only general reAM250/gas-flow context and duplicate BOM-like references, not row-specific material or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume for one gas outlet segment."
    - "Steel density is used as a representative sheet-metal density because the actual alloy or material family is not supplied by the BOM, STEP metadata, or targeted search."
  uncertainty_notes:
    - "If this panel is aluminum, mass would be about 0.0128 kg; if stainless steel, about 0.0380 kg. The reported value should be treated as a steel-equivalent planning mass until material evidence is available."
material:
  primary_material: "unknown metal/alloy sheet"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0156_3S45__views_2x2.png; web targeted search"
    cited_fact_or_basis: "BOM row 156 identifies the part as 'gas outlet: part 5' but provides no material, manufacturer, product ID, or link URL. Local assembly STEP material extraction for 3S45_part_5 returned only placeholder material 'Generic' with density 1000.0. The rendered preview shows a rigid thin folded panel-like gas outlet segment. targeted_web_search: searched '3S45_part_5 gas outlet reAM250 material', '3S45 gas outlet reAM250', 'reAM250 gas outlet material', and 'Renishaw AM250 gas outlet material'; results did not resolve row-specific material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A gas outlet segment in this machine is modeled as sheet metal because the CAD geometry is thin, folded, and part of the gas outlet assembly."
  uncertainty_notes:
    - "No source resolves whether the alloy is stainless steel, generic steel, aluminum, or another sheet material, so downstream KB modeling should preserve the broad metal/alloy family."
how_to_make:
  summary: "Fabricate as a small custom sheet-metal outlet segment, then clean and fit it into the larger gas outlet assembly."
  manufacturing_steps:
    - "Cut a flat metal sheet blank sized for the 21.00 x 50.00 x 90.71 mm folded geometry."
    - "Bend or brake-form the sheet to the angled outlet-panel profile shown in the CAD preview."
    - "Trim, deburr, and clean the formed edges before assembly."
    - "Join or seal this segment to neighboring gas outlet parts according to the final outlet assembly design."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S45_part_5.step; research/ream250_bom/ream250_bom_row_0156_3S45__views_2x2.png; web targeted search"
    cited_fact_or_basis: "FreeCAD measured a one-solid part with 21.00 x 50.00 x 90.71 mm bounding box. The rendered preview shows a thin folded panel-like geometry without visible standard fitting, shaft, electronics, or calibrated module features. targeted_web_search: searched '3S45_part_5 gas outlet reAM250 manufacturing', '3S45_part_5 drawing', '3S45 gas outlet reAM250 material', and 'Renishaw AM250 gas outlet material'; results did not provide a row-specific fabrication drawing or process note."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Sheet cutting and brake forming are the plausible route because the row geometry is thin and folded rather than machined from a thick block."
    - "Final sealing and joining are handled at the larger gas outlet assembly level because this row is only part 5 of the outlet group."
  uncertainty_notes:
    - "The CAD preview does not show the full gas outlet assembly, so exact edge preparation, fastening, welding, or sealing details remain unresolved."
kb_implications:
  - "item_granularity: simple_part - Model as one custom fabricated sheet-metal gas outlet segment, with assembly-level joining handled by the larger 3S outlet group."
---

