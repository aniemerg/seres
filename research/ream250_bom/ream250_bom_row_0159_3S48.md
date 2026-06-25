---
row_identity:
  item: "3S48"
  cad_file: "3S48_part_8"
  source_row_number: 159
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom gas outlet segment, part 8 of the 3S41-3S48 gas outlet group; the CAD shows a very thin folded or stiffened panel used as one wall, baffle, or flow-guide piece in the outlet path."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S48_part_8.step; research/ream250_bom/ream250_bom_row_0159_3S48__views_2x2.png"
    cited_fact_or_basis: "BOM row 159 lists item 3S48, quantity 1, CAD file 3S48_part_8, description 'gas outlet: part 8'. The manifest maps row 159 to one matched_existing part STEP. FreeCAD measured one solid with volume 4040.000 mm^3 and a 1.00 x 50.00 x 84.00 mm bounding box; the rendered preview shows a very thin panel with diagonal crease/stiffener-like features."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted within neighboring BOM rows 3S41 through 3S48, which are sequential 'gas outlet' parts, so this is one custom segment of the larger outlet rather than a standalone fitting."
  uncertainty_notes:
    - "The isolated part CAD does not show how this thin panel mates into the complete outlet, so its exact role as wall, baffle, or cover segment remains approximate."
mass:
  value_kg: 0.0317
  basis: "FreeCAD volume 4040.000 mm^3 = 4.040e-6 m^3. Using the local generic steel density of 7850 kg/m^3 gives 0.0317 kg per part. Stainless steel at 8000 kg/m^3 would give about 0.0323 kg. BOM quantity is 1, so per-unit mass and row total are the same."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S48_part_8.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 4040.000 mm^3, area 8352.000 mm^2, and bounding box 1.00 x 50.00 x 84.00 mm. The local density table lists steel at 7850 kg/m^3 and stainless_steel at 8000 kg/m^3. targeted_web_search: searched \"3S48_part_8 gas outlet reAM250 material\", \"3S48 gas outlet reAM250\", \"reAM250 gas outlet material\", and \"3S48_part_8\"; results found public reAM250 pages and duplicate/general gas-outlet material results, but no row-specific material or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume for one gas-outlet segment."
    - "Generic steel density is used as a conservative metal outlet estimate because neither the BOM nor STEP metadata resolves the alloy."
  uncertainty_notes:
    - "Material is not directly specified; if this panel is aluminum, the same CAD volume would be about 0.0109 kg using the local aluminum density of 2700 kg/m^3."
material:
  primary_material: "unknown metal/alloy sheet"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0159_3S48__views_2x2.png; web targeted search"
    cited_fact_or_basis: "BOM row 159 identifies the part as 'gas outlet: part 8' but provides no material, manufacturer, product ID, or link URL. Local assembly STEP material extraction for 3S48_part_8 returned only placeholder material 'Generic' with density 1000.0. The rendered preview shows a rigid thin sheet-like outlet segment. targeted_web_search: searched \"3S48_part_8 gas outlet reAM250 material\", \"3S48 gas outlet reAM250 material\", \"reAM250 gas outlet material\", and \"3S48_part_8\"; results did not resolve row-specific material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A gas outlet segment in this machine is modeled as sheet metal because the CAD geometry is a rigid 1 mm thick panel and the row sits among other gas/vacuum outlet hardware."
  uncertainty_notes:
    - "No source resolves the exact material family or grade; later KB modeling should keep this as a broad metal/alloy sheet part unless a drawing or assembly material note identifies the alloy."
how_to_make:
  summary: "Make as a custom sheet-metal gas-outlet panel: cut the thin blank, form or emboss the diagonal stiffening/crease features, trim and finish the edges, then clean and inspect it for fit in the gas outlet assembly."
  manufacturing_steps:
    - "Cut the approximately 1 mm thick panel blank from metal sheet by laser, waterjet, punch, or CNC profile cutting."
    - "Form, press, or brake the diagonal crease/stiffener features visible in the CAD preview."
    - "Trim, deburr, and clean the edges and small edge features for assembly into the gas outlet."
    - "Inspect flatness, profile, and mating-edge fit before joining or fastening it with the neighboring gas outlet parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S48_part_8.step; research/ream250_bom/ream250_bom_row_0159_3S48__views_2x2.png; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid with a 1.00 x 50.00 x 84.00 mm bounding box. The preview shows a thin panel with diagonal crease/stiffener-like features and no visible standard fitting, shaft, or calibrated module features. targeted_web_search: searched \"3S48_part_8 gas outlet reAM250 manufacturing\", \"3S48 gas outlet reAM250 drawing\", \"reAM250 gas outlet material\", and \"3S48_part_8\" results did not provide a row-specific fabrication drawing or process note."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible 1 mm thin panel geometry is treated as sheet-metal cutting and forming rather than casting or billet machining."
    - "Final sealing and joining are handled at the larger gas outlet assembly level because this row is only part 8 of the outlet group."
  uncertainty_notes:
    - "The CAD and BOM do not state tolerances, bend allowances, surface finish, or gas-tightness requirements; those details determine the final forming and inspection process."
kb_implications:
  - "item_granularity: simple_part - Model as one custom fabricated sheet-metal gas outlet panel, with assembly-level joining handled by the larger 3S outlet group."
---

Research result for reAM250 BOM row 159.
