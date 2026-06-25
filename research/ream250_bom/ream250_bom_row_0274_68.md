---
row_identity:
  item: "68"
  cad_file: "68_convex_crowned_shaft"
  source_row_number: 274
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "One long convex-crowned stainless shaft or roller element, likely providing a rotating/support contact surface with smaller end journals for mounting in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/68_convex_crowned_shaft.step; research/ream250_bom/ream250_bom_row_0274_68__views_2x2.png"
    cited_fact_or_basis: "BOM row 274 lists item 68, quantity 1, description '68_convex_crowned_shaft'. The manifest maps the row to gold_export/parts/68_convex_crowned_shaft.step. FreeCAD measured one solid with bounding box about 313.80 x 26.00 x 26.00 mm, and the rendered contact sheet shows a long crowned cylinder with smaller end journals."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP solid represents one physical shaft/roller item for this BOM row."
  uncertainty_notes:
    - "The BOM and manifest do not identify the parent subsystem, bearing interfaces, drive coupling, or whether the crowned surface contacts a belt, a guide, or another moving part."
mass:
  value_kg: 1.056
  basis: "Per-unit estimate for BOM quantity 1. FreeCAD volume is 131977.817 mm^3, equal to 0.000131977817 m^3. Assembly STEP material metadata gives stainless steel density 8000 kg/m^3, so 0.000131977817 m^3 * 8000 kg/m^3 = 1.0558 kg, rounded to 1.056 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/68_convex_crowned_shaft.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 131977.817 mm^3, area 23027.077 mm^2, and bounding box 313.80 x 26.00 x 26.00 mm. Local assembly STEP material extraction for product 68_convex_crowned_shaft returned material 'Stainless Steel' with density 8000.0, and kb/materials/properties.yaml lists stainless_steel density 8000 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical solid volume of one shaft."
    - "The extracted stainless steel density is used directly as the mass calculation constant."
  uncertainty_notes:
    - "The estimate depends on the supplied STEP solid including all material volume and not being a simplified visual envelope."
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 68_convex_crowned_shaft returned row-specific material 'Stainless Steel' with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata resolves the material family but not a specific stainless grade, heat treatment, shaft tolerance, or surface finish."
how_to_make:
  summary: "Machine from stainless round bar as a one-piece crowned shaft: rough turn the journals and body, generate the shallow convex crown, finish-turn or grind the contact surface, deburr, clean, and inspect concentricity and crown profile."
  manufacturing_steps:
    - "Cut stainless round bar stock slightly longer than the 313.8 mm finished length."
    - "Turn between centers or in a CNC lathe to form the smaller end journals and the larger cylindrical body."
    - "Generate the convex crown on the central contact surface by CNC turning/profile turning or cylindrical grinding."
    - "Deburr and clean the shaft, then inspect overall length, journal diameters, runout, surface finish, and crown profile."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/68_convex_crowned_shaft.step; research/ream250_bom/ream250_bom_row_0274_68__views_2x2.png; https://www.rollerco.com/crowning/"
    cited_fact_or_basis: "CAD evidence shows one long axisymmetric crowned shaft/roller with end journals. AELM Roller Company describes crowned roller services that grind and shape convex, concave, cylindrical, straight-taper, and other roller profiles. targeted_web_search: tried 'convex crowned shaft manufacturing turning grinding crowned shaft' and 'crowned roller shaft machining crowned shaft lathe grinding'; results supported crowning/grinding as a plausible roller profile route but did not provide a row-specific reAM250 manufacturing drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because the part is a one-piece stainless axisymmetric shaft, turning plus profile grinding/finishing is the most plausible Manufacturing route."
    - "The crowned surface is functionally important enough to require inspection rather than treating the part as plain cut round stock."
  uncertainty_notes:
    - "No row-specific drawing states tolerances, crown height, bearing fits, heat treatment, or required surface roughness."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable one-piece machined stainless crowned shaft/roller, not as raw bar stock or a purchased calibrated module."
---

Research result for the leased reAM250 BOM row.
