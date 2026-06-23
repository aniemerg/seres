---
row_identity:
  item: "3S33"
  cad_file: "3S33_part_3"
  source_row_number: 149
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Thin-wall gas outlet pipe segment, part 3 of the neighboring 3S31-3S35 gas outlet pipe group; the CAD shows a hollow square duct section used to route outlet/process gas through the machine gas path."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S33_part_3.step; research/ream250_bom/ream250_bom_row_0149_3S33__views_2x2.png"
    cited_fact_or_basis: "BOM row 149 lists item 3S33, quantity 1, CAD file 3S33_part_3, and description 'gas outlet pipe: part 3'. The manifest maps row 149 to one matched_existing part STEP. FreeCAD measured one solid with a 60.00 x 60.00 x 200.00 mm bounding box, and the rendered preview shows a hollow square duct/tube segment with angled transition faces."
    evidence_basis: "bom_provided"
  assumptions:
    - "The phrase 'gas outlet pipe: part 3' is interpreted as one segment in the adjacent 3S31-3S35 multi-piece gas outlet pipe sequence."
  uncertainty_notes:
    - "The CAD/BOM evidence identifies the gas outlet role and duct-like geometry, but not the exact mating interfaces, gas-flow direction, or assembly sealing method."
mass:
  value_kg: 0.574
  basis: "Per-unit estimate for quantity 1. FreeCAD volume is 73114.147 mm^3 = 7.3114147e-5 m^3. Using the local generic steel density of 7850 kg/m^3 gives 0.573946 kg per part, rounded to 0.574 kg. Stainless steel at 8000 kg/m^3 would give about 0.585 kg; aluminum at 2700 kg/m^3 would give about 0.197 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S33_part_3.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 73114.147 mm^3, area 74272.572 mm^2, and bounding box 60.00 x 60.00 x 200.00 mm. Local assembly STEP material extraction for 3S33_part_3 returned only placeholder material Generic with density 1000.0. The local density table lists steel at 7850 kg/m^3, stainless_steel at 8000 kg/m^3, and aluminum at 2700 kg/m^3. targeted_web_search: searched '3S33_part_3 gas outlet pipe material reAM250', '3S33 gas outlet pipe reAM250', 'Renishaw AM250 gas outlet pipe material', and 'reAM250 gas outlet pipe part 3 material'; results found reAM250/AM250 gas-flow context and duplicate-like references but no row-specific material, drawing, or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume for one duct segment."
    - "Generic steel density is used as a conservative planning constant for a rigid metal gas-outlet duct because neither the BOM nor STEP metadata resolves the alloy."
  uncertainty_notes:
    - "Mass depends directly on unresolved material; downstream use should keep the aluminum and stainless/steel alternatives in mind until a drawing, native CAD material, or physical weighing resolves the alloy."
material:
  primary_material: "unknown metal/alloy sheet or thin-wall duct material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; research/ream250_bom/ream250_bom_row_0149_3S33__views_2x2.png; web targeted search"
    cited_fact_or_basis: "BOM row 149 identifies the part as 'gas outlet pipe: part 3' but provides no material, manufacturer, product ID, or link URL. Local assembly STEP material extraction for 3S33_part_3 returned only placeholder material Generic with density 1000.0. The rendered preview shows a rigid thin-wall hollow square duct form. targeted_web_search: searched '3S33_part_3 gas outlet pipe material reAM250', '3S33 gas outlet pipe reAM250 material', 'Renishaw AM250 gas outlet pipe material', and 'reAM250 gas outlet pipe part 3 material'; results did not resolve row-specific material."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A gas outlet pipe segment in this machine is modeled as a metal/alloy duct part because the CAD geometry is a rigid hollow square section and the row sits among adjacent numbered gas outlet pipe segments."
  uncertainty_notes:
    - "No source resolves the exact material family or grade; later KB modeling should keep this as a broad metal/alloy sheet part unless a drawing or assembly material note identifies the alloy."
how_to_make:
  summary: "Make as a custom sheet-metal or square-tube duct segment: cut the blank or tube to the 200 mm envelope, form the angled transition geometry, join or seal seams as required, then deburr, clean, leak-check, and assemble into the gas outlet pipe run."
  manufacturing_steps:
    - "Select square metal tube or folded sheet stock close to the 60 mm outer section."
    - "Cut to the 200 mm envelope and create the angled transition faces shown in the CAD."
    - "If formed from sheet, bend/form the walls and join seams and corners by welding, brazing, or another gas-tight metal joining method."
    - "Deburr internal edges, clean the gas path, and inspect the square openings and mating edges."
    - "Leak-check or fit-check the segment before installing it with the neighboring gas outlet pipe parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S33_part_3.step; research/ream250_bom/ream250_bom_row_0149_3S33__views_2x2.png; web targeted search"
    cited_fact_or_basis: "FreeCAD measured one solid with a 60.00 x 60.00 x 200.00 mm bounding box. The preview shows a hollow square duct/tube segment with thin walls and angled transition faces. targeted_web_search: searched '3S33_part_3 gas outlet pipe manufacturing', '3S33 gas outlet pipe reAM250 drawing', 'Renishaw AM250 gas outlet pipe material', and 'reAM250 gas outlet pipe part 3 material'; results did not provide a row-specific fabrication drawing or process note."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD form represents a fabricated duct shell, so sheet cutting/forming plus seam joining or modification of square tube stock is the dominant planning route."
    - "Final sealing, fasteners, and alignment are handled at the larger gas outlet pipe assembly level."
  uncertainty_notes:
    - "The CAD and BOM do not state wall thickness callouts, tolerances, surface finish, alloy, or gas-tightness class; those details determine whether folded seams, welded seams, brazing, or another process is appropriate."
kb_implications:
  - "item_granularity: simple_part - Model as one custom fabricated sheet-metal gas outlet pipe segment, with material kept broad and assembly-level joining handled by the larger 3S outlet group."
---

Research result for reAM250 BOM row 149.
