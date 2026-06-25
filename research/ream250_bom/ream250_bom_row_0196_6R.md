---
row_identity:
  item: "6R"
  cad_file: "6R_belt"
  source_row_number: 196
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small closed-loop rubber belt, likely a drive or timing belt used with the neighboring belt pulley rows in the reAM250 row-6 motion assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0196_6R__views_2x2.png"
    cited_fact_or_basis: "BOM row 196 lists item 6R, quantity 3, CAD file 6R_belt. Manifest row 196 maps 6R_belt to gold_export/parts/6R_belt.step with matched_existing part status. The rendered CAD preview shows a thin closed loop; nearby BOM rows list GT2 belt pulleys and pulley mounts."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name, closed-loop CAD shape, and adjacent pulley rows are interpreted together as a motion-transmission belt rather than a static seal."
  uncertainty_notes:
    - "The exact belt standard, pitch, tooth profile, and intended pulley pairing are not stated in row 196."
mass:
  value_kg: 0.00402
  basis: "FreeCAD measured volume 4323.217 mm^3. Assembly STEP material metadata reports Rubber with density 930 kg/m^3. Computed mass: 4323.217 mm^3 x 1e-9 m^3/mm^3 x 930 kg/m^3 = 0.00402 kg per belt."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6R_belt.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 4323.217 mm^3, area 9383.064 mm^2, and bounding box 77.00 x 130.43 x 10.00 mm. Local STEP material extraction for product 6R_belt found material Rubber and density 930.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP volume is treated as the physical belt volume and the assembly material density is applied uniformly to the part."
  uncertainty_notes:
    - "Any embedded cords, fabric reinforcement, or tooth-detail volume not represented distinctly in the STEP would change the true purchased belt mass."
material:
  primary_material: "rubber"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extraction for product 6R_belt found material Rubber with density 930.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local metadata gives only a broad Rubber material name, not a specific compound such as neoprene, polyurethane, nitrile rubber, silicone rubber, or a reinforcement material."
how_to_make:
  summary: "Model as a external or cut-to-length rubber belt stock item unless later KB work needs detailed belt manufacturing; form a reinforced rubber belt loop by extrusion or calendaring, curing, and joining/molding to final loop geometry"
  manufacturing_steps:
    - "Select rubber belt stock or compound compatible with the pulley geometry and operating environment."
    - "Form a strip by extrusion, calendaring, or molding; include cord or fabric reinforcement if required by the drive load."
    - "Cure/vulcanize the rubber and join or mold the strip into the closed loop."
    - "Trim and inspect loop width, thickness, length, and fit against the pulley set."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6R_belt.step; research/ream250_bom/ream250_bom_row_0196_6R__views_2x2.png"
    cited_fact_or_basis: "The CAD part is a single thin closed-loop rubber belt with measured bounding box 77.00 x 130.43 x 10.00 mm. targeted_web_search: searched \"6R_belt reAM250\", \"6R_belt reAM250 rubber belt\", \"6R_belt CAD belt\", \"6R_belt GT2\", and \"reAM250 6R_belt GT2\" results only duplicated BOM text or unrelated belt pages and did not provide a row-specific vendor or manufacturing specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The route is inferred from the belt geometry and broad rubber material metadata, not from a row-specific vendor drawing."
    - "For near-term KB modeling, this should be treated as a external belt or stock belt part because the exact profile and compound are unspecified"
  uncertainty_notes:
    - "Without a belt designation or vendor page, the manufacturing route cannot specify tooth pitch, reinforcement, compound, splice method, or curing parameters."
kb_implications:
  - "item_granularity: simple_part - This is a replaceable rubber belt-like motion component; model as a purchased/stock belt unless later work resolves the exact standard and compound."
---

Research result for reAM250 BOM row 196, item 6R.
