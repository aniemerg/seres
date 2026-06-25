---
row_identity:
  item: "1B43"
  cad_file: "1B43_frame"
  source_row_number: 14
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Custom thin rectangular external adapter frame in the reAM250 optical/flow-rectifier area; CAD shows a large open-center frame with perimeter holes and chamfered or relieved corner features, associated with the BOM's SM2A53 adapter interface."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B43_frame.step; research/ream250_bom/ream250_bom_row_0014_1B43__views_2x2.png"
    cited_fact_or_basis: "BOM row 14 states item 1B43, quantity 1, CAD file 1B43_frame, and description SM2A53 Adapter: External. The manifest maps this row to gold_export/parts/1B43_frame.step as a matched_existing part export. FreeCAD measured one solid with bounding box 335.00 x 12.80 x 248.00 mm. The rendered contact sheet shows a thin rectangular open frame with perimeter holes and corner relief/chamfer features."
    evidence_basis: "bom_provided"
  assumptions:
    - "The frame is interpreted as the custom machine-side external adapter/support frame for the neighboring SM2A53 optical-thread adapter hardware, rather than the small round Thorlabs SM2A53 adapter itself."
  uncertainty_notes:
    - "The row evidence identifies the frame geometry and adapter association, but not the exact mating surfaces, fastener pattern purpose, or optical/vacuum alignment requirements."
mass:
  value_kg: 0.725
  basis: "Per-unit mass for quantity 1. FreeCAD volume 268573.650 mm^3 equals 0.00026857365 m^3. Nominal value uses aluminum density 2700 kg/m^3 from kb/materials/properties.yaml, giving 0.725 kg for one 1B43 frame. If the same CAD volume were generic steel at 7850 kg/m^3, mass would be about 2.11 kg; stainless steel at 8000 kg/m^3 would be about 2.15 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B43_frame.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 268573.650 mm^3, area 79646.659 mm^2, and bounding box 335.00 x 12.80 x 248.00 mm. The local density table lists aluminum density 2700 kg/m^3, steel density 7850 kg/m^3, and stainless_steel density 8000 kg/m^3. targeted_web_search: searched \"1B43_frame\", \"1B43 reAM250 frame\", \"reAM250 1B43 SM2A53 Adapter External material\", and \"SM2A53 Adapter External frame material\"; results found duplicate BOM/product-context text and SM2A53 adapter pages, but no row-specific mass, drawing, or material source for the 1B43 frame."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one manufactured frame."
    - "Aluminum is used as the nominal scenario because the row is a large thin custom optical/mechanical adapter frame where machined aluminum plate is plausible and keeps mass consistent with similar lightened machine frames."
  uncertainty_notes:
    - "Mass depends directly on unresolved material; use 0.725 kg as an aluminum-scenario estimate, with steel or stainless construction near 2.1 kg."
material:
  primary_material: "unknown structural metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B43_frame.step; research/ream250_bom/ream250_bom_row_0014_1B43__views_2x2.png"
    cited_fact_or_basis: "BOM row 14 has blank material fields and no manufacturer or link URL. The assembly STEP material extractor matched 1B43_frame but returned material Generic and density 1000.0, which the task workflow treats as placeholder rather than resolved material evidence. CAD geometry is a bolted rectangular mechanical frame. targeted_web_search: searched \"1B43_frame\", \"1B43 reAM250 frame\", \"reAM250 1B43 SM2A53 Adapter External material\", and \"SM2A53 Adapter External frame material\"; no row-specific material callout was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A structural metal/alloy family is inferred from the thin bolted frame geometry and its role as an adapter/support part in a machine assembly."
  uncertainty_notes:
    - "The specific alloy or grade is not identified; aluminum alloy is plausible for a custom optical/mechanical adapter frame, while steel or stainless steel remain possible if stiffness, thermal, or vacuum-interface requirements dominate."
how_to_make:
  summary: "Fabricate as a custom machined metal adapter frame from plate stock in the resolved alloy, cutting the rectangular outline, open center, perimeter holes, and corner relief features to the CAD geometry."
  manufacturing_steps:
    - "Select structural metal plate stock in the resolved alloy, sized for the 335 x 248 mm footprint and about 12.8 mm final thickness."
    - "CNC mill, waterjet, or laser/profile-cut the outside rectangular perimeter and large center opening, leaving allowance for finish machining where precision is needed."
    - "Drill, counterbore, countersink, or tap the perimeter holes according to the mating hardware requirements."
    - "Finish-machine the adapter faces and corner relief/chamfer features, deburr all edges, and inspect flatness, hole position, outside dimensions, and opening size."
    - "Apply anodizing, passivation, blackening, or cleaning only after the alloy and service environment are resolved."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B43_frame.step; research/ream250_bom/ream250_bom_row_0014_1B43__views_2x2.png"
    cited_fact_or_basis: "CAD and preview show one thin 335.00 x 12.80 x 248.00 mm rectangular open-frame solid with perimeter holes and corner relief/chamfer features. targeted_web_search: searched \"1B43_frame manufacturing\", \"1B43 reAM250 frame drawing\", \"reAM250 1B43 SM2A53 Adapter External material\", and \"SM2A53 Adapter External frame drawing\" no row-specific manufacturing drawing, material callout, or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is treated as a custom simple part because the row has no manufacturer or link URL and the CAD name is a machine-specific frame"
    - "Subtractive machining or profile cutting from plate stock is assumed from the flat thin frame geometry and expected need for accurate mounting-hole locations."
  uncertainty_notes:
    - "The CAD/BOM evidence does not specify tolerances, surface finish, coating, or whether this adapter frame has optical alignment, vacuum, or thermal constraints."
kb_implications:
  - "item_granularity: simple_part - model as one custom machined structural adapter frame, with material grade unresolved until a drawing or designer note identifies it."
---

Research result for reAM250 BOM row 14.
