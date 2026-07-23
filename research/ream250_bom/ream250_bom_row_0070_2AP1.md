---
row_identity:
  item: "2AP1"
  cad_file: "2AP1_spring_plate"
  source_row_number: 70
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "One formed square spring plate in the reAM250 2AP assembly, likely providing a compliant preload, clamping, or locating interface around the central opening."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP1_spring_plate.step; research/ream250_bom/ream250_bom_row_0070_2AP1__views_2x2.png"
    cited_fact_or_basis: "BOM row 70 identifies item 2AP1, quantity 1, CAD file 2AP1_spring_plate. The manifest maps the row to gold_export/parts/2AP1_spring_plate.step with matched_existing part status. FreeCAD measured one solid with volume 502304.095 mm^3 and bounding box 250.00 x 20.00 x 250.00 mm; the rendered contact sheet shows a thin square frame-like plate with a large central opening, diagonal formed ribs, side lips, and small mounting holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the single physical item for BOM row 70."
    - "The item name 'spring_plate' is interpreted as a compliant formed plate, not as a coil spring or separate spring stack."
  uncertainty_notes:
    - "The BOM row and CAD do not show the complete 2AP assembly context, so the exact preload/clamping interface remains inferred from the part name and geometry."
mass:
  value_kg: 3.94
  basis: "Per-unit planning estimate for quantity 1. FreeCAD volume is 502304.095 mm^3, equal to 5.02304095e-4 m^3. Using the local generic steel density constant of 7850 kg/m^3 gives 3.943 kg, rounded to 3.94 kg. If the same CAD volume were aluminum at 2700 kg/m^3, it would be about 1.36 kg; the steel estimate is used because the BOM name and spring-plate function point to a steel-family spring material."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP1_spring_plate.step; kb/materials/properties.yaml; https://www.metalsupermarkets.com/what-is-spring-steel/; https://www.alleima.com/en/products/strip-steel/spring-steel/"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 502304.095 mm^3 and bounding box 250.00 x 20.00 x 250.00 mm. kb/materials/properties.yaml lists steel density 7850 kg/m^3 and aluminum density 2700 kg/m^3. Metal Supermarkets describes spring steel as steel engineered for high yield strength, elasticity, hardness, and resilience; Alleima describes spring steels as combining strength, elasticity, and corrosion resistance. targeted_web_search: tried '\"2AP1_spring_plate\"', '\"2AP1\" \"spring plate\" reAM250', '\"spring plate\" additive manufacturing machine steel', and 'spring plate material spring steel manufacturing'; results found duplicate BOM/reAM250 identity and general spring-steel material guidance, but no row-specific catalog weight or material grade."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A steel-family density is used as the single-value planning estimate because the row name says spring plate and the geometry is a formed compliant plate."
    - "The CAD solid volume is treated as the physical solid volume without hidden fasteners, inserts, or omitted cutouts."
  uncertainty_notes:
    - "Assembly STEP material extraction for 2AP1_spring_plate returned only placeholder material 'Generic' with density 1000.0, so the mass depends on the spring-steel material inference rather than row-specific material metadata."
    - "If the actual part is aluminum or a lighter alloy rather than steel, the per-unit mass would be materially lower."
material:
  primary_material: "unknown spring steel/steel alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.metalsupermarkets.com/what-is-spring-steel/; https://www.alleima.com/en/products/strip-steel/spring-steel/"
    cited_fact_or_basis: "BOM row 70 gives no manufacturer, product ID, material hint, or link URL beyond the CAD name 2AP1_spring_plate. Assembly STEP material extraction for product 2AP1_spring_plate returned material 'Generic' with density 1000.0, which is placeholder metadata. Metal Supermarkets describes spring steel as steel engineered for elasticity, hardness, resilience, and high yield strength; Alleima describes spring steels as stainless and nickel-based alloys for spring applications. targeted_web_search: tried '\"2AP1_spring_plate\"', '\"2AP1\" \"spring plate\" reAM250', '\"spring plate\" additive manufacturing machine steel', and 'spring plate material spring steel manufacturing'; no row-specific usable material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is modeled as a steel-family spring plate because the BOM/CAD name explicitly uses spring_plate and the geometry shows a formed compliant plate."
  uncertainty_notes:
    - "The exact grade, heat treatment, surface finish, and corrosion-resistance requirement are not resolved by the BOM, CAD material metadata, or web search."
how_to_make:
  summary: "Fabricate as a one-piece formed spring-steel plate"
  manufacturing_steps:
    - "Cut the square frame blank and central opening from spring-steel sheet or plate stock by laser, waterjet, or CNC profiling."
    - "Form the diagonal ribs, lips, and shallow offsets visible in the CAD geometry using a press brake, forming die, or matched tooling."
    - "Drill, punch, or finish the small mounting holes and deburr all edges."
    - "Heat treat, temper, or stress-relieve as required for spring behavior, then clean and apply any required corrosion-protection finish."
    - "Inspect flatness, hole locations, formed height, and fit against the mating 2AP assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP1_spring_plate.step; research/ream250_bom/ream250_bom_row_0070_2AP1__views_2x2.png; https://www.metalsupermarkets.com/what-is-spring-steel/"
    cited_fact_or_basis: "CAD preview shows a one-piece formed plate with a square frame, central opening, diagonal ribbed faces, and small mounting holes. FreeCAD measured one solid with 250.00 x 20.00 x 250.00 mm bounding box. Metal Supermarkets describes spring steel hardening via heat treatment or work hardening, including rolling to produce spring steel sheets, strips, rods, and bars. targeted_web_search: tried '\"2AP1_spring_plate\" manufacturing', '\"2AP1\" \"spring plate\" reAM250 manufacturing', 'formed spring steel plate manufacturing', and 'spring plate material spring steel manufacturing'; no row-specific manufacturing drawing or supplier process was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The visible CAD geometry is manufacturable as cut and formed sheet/plate rather than casting or machining from a thick block."
    - "Spring behavior requires appropriate steel temper or work-hardening control after forming."
  uncertainty_notes:
    - "The route is a plausible manufacturing plan only; the CAD/BOM does not specify bend radii, forming sequence, heat-treatment condition, flatness tolerance, or surface coating."
kb_implications:
  - "item_granularity: simple_part - Model later as a one-piece formed spring-steel plate, not a purchased module or raw stock; share with other formed spring plates only if geometry/function remain within the repo's reuse tolerance."
---

Result generated for the leased reAM250 BOM row only.
