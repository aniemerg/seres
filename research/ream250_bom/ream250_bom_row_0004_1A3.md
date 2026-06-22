---
row_identity:
  item: "1A3"
  cad_file: "1A3_mounting_plate_flow_rectifier"
  source_row_number: 4
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom mounting plate or narrow bridge for the reAM250 flow-rectifier / external SM2A53 adapter interface; CAD shows a long, thin mechanical plate with end features rather than the ring-shaped SM2A53 adapter itself."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A3_mounting_plate_flow_rectifier.step; research/ream250_bom/ream250_bom_row_0004_1A3__views_2x2.png; https://www.thorlabs.com/item/SM2A53"
    cited_fact_or_basis: "BOM row 4 states item 1A3, quantity 1, CAD file 1A3_mounting_plate_flow_rectifier, and description SM2A53 Adapter: External. The manifest maps the row to gold_export/parts/1A3_mounting_plate_flow_rectifier.step as a matched part export. FreeCAD measured one solid with bounding box 278.00 x 35.30 x 5.00 mm. The rendered contact sheet shows a long narrow plate with small end features. The official Thorlabs SM2A53 route identifies SM2A53 as an adapter with external M52 x 0.75 threads and internal SM2 threads."
    evidence_basis: "bom_provided"
  assumptions:
    - "The local CAD part is interpreted as the custom machine-side plate associated with mounting or locating the external SM2A53 adapter near the flow-rectifier assembly, not as the commercial threaded adapter ring."
  uncertainty_notes:
    - "The BOM/CAD evidence does not show the neighboring flow rectifier or mating fasteners, so the exact load path and whether the plate clamps, spaces, or locates the adapter remains unresolved."
mass:
  value_kg: 0.047
  basis: "FreeCAD volume 17342.598 mm^3 equals 0.000017343 m^3. Nominal value uses aluminum density 2700 kg/m^3 from kb/materials/properties.yaml, giving 0.0468 kg. If the same CAD volume were generic steel at 7850 kg/m^3, mass would be about 0.136 kg; stainless steel at 8000 kg/m^3 would be about 0.139 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A3_mounting_plate_flow_rectifier.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 17342.598 mm^3, area 13085.675 mm^2, and bounding box 278.00 x 35.30 x 5.00 mm. The local density table lists aluminum density 2700 kg/m^3, steel density 7850 kg/m^3, and stainless_steel density 8000 kg/m^3. targeted_web_search: searched \"1A3_mounting_plate_flow_rectifier material\", \"1A3 mounting plate flow rectifier mass\", \"reAM250 1A3 flow rectifier mounting plate\", \"SM2A53 adapter external material weight\", and \"SM2A53 anodized aluminum 0.02 kg\"; found SM2A53 adapter material/weight evidence but no row-specific mass source for the custom 1A3 mounting plate."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured plate."
    - "Aluminum is used as the nominal scenario because nearby optical adapter parts are aluminum and the row is a light, thin custom mounting plate rather than a pressure vessel or heavy structural element."
  uncertainty_notes:
    - "Mass depends directly on unresolved material; use 0.047 kg as an aluminum-scenario estimate, with steel or stainless construction near 0.14 kg."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A3_mounting_plate_flow_rectifier.step; https://www.thorlabs.com/item/SM2A53; https://www.oxxius.ru/upload/iblock/dbe/j38qr4oay7zb9p73yap8tcsa50z0acsq/24386_E0W.pdf"
    cited_fact_or_basis: "BOM row 4 has blank material fields. The assembly STEP material extractor matched 1A3_mounting_plate_flow_rectifier but returned material Generic and density 1000.0, which the task workflow treats as placeholder rather than resolved material evidence. CAD geometry is a thin bolted/custom mechanical plate. Web search found a Thorlabs SM2A53 drawing mirror stating anodized aluminum for the commercial adapter, while the official Thorlabs item route confirms the SM2A53 adapter identity. targeted_web_search: searched \"1A3_mounting_plate_flow_rectifier material\", \"1A3 mounting plate flow rectifier mass\", \"reAM250 1A3 flow rectifier mounting plate\", \"SM2A53 adapter external material weight\", and \"SM2A53 anodized aluminum 0.02 kg\"; found no source that directly assigns a material to the custom 1A3 plate."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal/alloy family is inferred from the long thin plate geometry, machine mounting role, and association with an optical/threaded adapter interface."
  uncertainty_notes:
    - "The specific alloy or grade is not identified. Aluminum alloy is plausible by context, but steel or stainless steel remain possible if stiffness, thermal stability, or vacuum/cleaning requirements dominate."
how_to_make:
  summary: "Fabricate as a simple machined or profile-cut metal mounting plate from the resolved alloy, then drill/machine end details and finish/deburr for assembly with the flow-rectifier / SM2A53 adapter interface."
  manufacturing_steps:
    - "Select structural metal flat bar or plate stock about 5 mm thick in the resolved alloy."
    - "CNC mill, waterjet, laser-cut, or saw/profile the long narrow plate outline to the CAD geometry."
    - "Machine the end features, holes, notches, or reliefs visible in the CAD, using drilling and milling as needed."
    - "Deburr all edges and inspect length, hole/end-feature positions, flatness, and fit to the mating flow-rectifier or adapter hardware."
    - "Apply anodizing, passivation, blackening, or cleaning only if later design evidence requires a specific surface finish."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1A3_mounting_plate_flow_rectifier.step; research/ream250_bom/ream250_bom_row_0004_1A3__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one 278.00 x 35.30 x 5.00 mm solid: a long, thin plate with small end features. targeted_web_search: searched \"1A3_mounting_plate_flow_rectifier material\", \"1A3 mounting plate flow rectifier mass\", \"reAM250 1A3 flow rectifier mounting plate\", \"SM2A53 adapter external material weight\", and \"SM2A53 anodized aluminum 0.02 kg\"; no row-specific manufacturing drawing, material callout, tolerance note, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom simple part rather than a purchased module because the BOM row has no manufacturer or link and the CAD file name is a custom assembly-specific mounting plate."
    - "Subtractive plate fabrication is assumed from the flat 5 mm-thick geometry and expected need for accurate mounting features."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify tolerances, surface finish, coating, or whether any end features are clearance, locating, or fastening features."
kb_implications:
  - "item_granularity: simple_part - custom flow-rectifier mounting plate likely modeled as one machined or profile-cut metal plate, with material grade unresolved until a drawing or designer note identifies it."
---

Research result for reAM250 BOM row 4.
