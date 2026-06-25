---
row_identity:
  item: "2A2"
  cad_file: "2A2_back_plate"
  source_row_number: 25
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom back plate for the reAM250 2A motion/structural subassembly; CAD shows a long thick rectangular plate with relief or stiffening geometry, likely serving as a rear structural mounting plate for adjacent linear-guide and axis-support components."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A2_back_plate.step; research/ream250_bom/ream250_bom_row_0025_2A2__views_2x2.png"
    cited_fact_or_basis: "BOM row 25 states item 2A2, quantity 1, CAD file 2A2_back_plate. The manifest maps the row to gold_export/parts/2A2_back_plate.step as a matched part export. FreeCAD measured one solid with bounding box 280.00 x 30.00 x 680.00 mm. The rendered contact sheet shows a long, narrow, thick back-plate-like solid with internal relief or diagonal web geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The file name back_plate and the adjacent BOM rows for bottom plate, linear guide slide/rail parts, side plates, distance pieces, and support plates are interpreted as a 2A-axis structural mounting context."
  uncertainty_notes:
    - "The BOM/CAD evidence identifies the part as a back plate but does not identify the exact mating rails, fasteners, datum faces, or whether it carries static frame loads or moving-axis loads."
mass:
  value_kg: 14.5
  basis: "FreeCAD volume 5372903.441 mm^3 equals 0.005372903 m^3. Nominal value uses aluminum density 2700 kg/m^3 from kb/materials/properties.yaml, giving 14.51 kg. If the same CAD volume were generic steel at 7850 kg/m^3, mass would be about 42.17 kg; stainless steel at 8000 kg/m^3 would be about 42.98 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A2_back_plate.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 5372903.441 mm^3, area 459031.597 mm^2, and bounding box 280.00 x 30.00 x 680.00 mm. The local density table lists aluminum density 2700 kg/m^3, steel density 7850 kg/m^3, and stainless_steel density 8000 kg/m^3. targeted_web_search: searched \"2A2_back_plate material reAM250\", \"reAM250 2A2 back plate\", \"reAM250 2A2_back_plate\", and \"2A2 back plate reAM250\"; found duplicate BOM/project pages but no row-specific mass or material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured part."
    - "Aluminum is used as the nominal scenario because large custom machine plates and axis-support plates in this size range are commonly machined from aluminum tooling plate when no vacuum, heat, or high-wear material requirement is stated."
  uncertainty_notes:
    - "Mass depends directly on unresolved material; use 14.5 kg as an aluminum-scenario estimate, with steel or stainless construction near 42-43 kg."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A2_back_plate.step; research/ream250_bom/ream250_bom_row_0025_2A2__views_2x2.png"
    cited_fact_or_basis: "BOM row 25 has blank material fields. The assembly STEP material extractor matched 2A2_back_plate but returned material Generic and density 1000.0, which the task workflow treats as placeholder rather than resolved material evidence. CAD geometry is a large plate-like structural part. targeted_web_search: searched \"2A2_back_plate material reAM250\", \"reAM250 2A2 back plate\", \"reAM250 2A2_back_plate\", and \"2A2 back plate reAM250\"; found duplicate BOM/project pages but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal/alloy family is inferred from the plate role, 680 mm length, 30 mm thickness, relief geometry, and neighboring linear-guide/axis-support BOM context."
  uncertainty_notes:
    - "The specific alloy or grade is not identified; aluminum alloy is plausible for a custom machined machine plate, while steel or stainless steel remain possible if stiffness, wear, or vacuum-chamber integration requirements dominate."
how_to_make:
  summary: "Fabricate as a custom machined structural back plate from the resolved alloy, most likely by CNC machining a thick plate blank to the CAD outline, relief geometry, mounting features, and datum faces."
  manufacturing_steps:
    - "Select structural metal plate stock in the resolved alloy, nominally about 30 mm thick before finish machining."
    - "Saw or rough profile the 280 x 680 mm blank, leaving machining allowance."
    - "CNC mill the outer profile, internal relief or diagonal web features, pockets, and any rail or support mounting faces visible in the CAD."
    - "Drill, tap, counterbore, or countersink mounting holes as required by the mating linear-guide, side-plate, distance-piece, and support-plate interfaces."
    - "Finish-machine datum and mating faces for flatness and alignment, then deburr, clean, and inspect hole positions, flatness, and plate straightness."
    - "Apply anodizing, passivation, blackening, or other surface treatment only if later drawing evidence identifies a required finish."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2A2_back_plate.step; research/ream250_bom/ream250_bom_row_0025_2A2__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one 280.00 x 30.00 x 680.00 mm solid with a long back-plate form and relief or diagonal web geometry. targeted_web_search: searched \"2A2_back_plate material reAM250\", \"reAM250 2A2 back plate\", \"reAM250 2A2_back_plate\", and \"2A2 back plate reAM250\" no row-specific manufacturing drawing, material callout, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom simple part because the BOM row has no manufacturer, product ID, or link URL and the CAD name is a custom assembly-specific back plate"
    - "Subtractive machining from plate stock is assumed from the thick plate geometry, lightening/relief features, and expected need for accurate rail or structural mounting interfaces."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify tolerances, flatness requirements, surface finish, heat treatment, coating, or whether the relief geometry is functional lightening, stiffness tuning, or clearance."
kb_implications:
  - "item_granularity: simple_part - custom structural back plate likely modeled as one machined metal plate, with material grade unresolved until a drawing or designer note identifies it."
---

Research result for reAM250 BOM row 25.
