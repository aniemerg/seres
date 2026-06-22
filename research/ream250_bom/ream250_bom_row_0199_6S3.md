---
row_identity:
  item: "6S3"
  cad_file: "6S3_bent_part"
  source_row_number: 199
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Bent steel motor-mount bracket for the reAM250 motor mount group; it provides a vertical support flange and a horizontal motor face/mounting plate with central shaft or boss clearance and smaller fastener holes."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6S3_bent_part.step; research/ream250_bom/ream250_bom_row_0199_6S3__views_2x2.png"
    cited_fact_or_basis: "BOM row 199 lists item 6S3, quantity 1, CAD file 6S3_bent_part, description motor mount. Manifest row 199 maps the row to a matched part STEP. FreeCAD measured one solid with bounding box 69.03 x 65.45 x 68.41 mm, and the rendered preview shows an L-shaped bent bracket with one large circular opening and smaller mounting holes."
    evidence_basis: "bom_provided"
  assumptions:
    - "The large circular opening is interpreted as motor shaft, boss, or pulley clearance; the smaller holes are interpreted as fastener holes for the motor or mating mount."
  uncertainty_notes:
    - "The BOM and CAD do not expose assembly constraints, so the exact motor face, handedness, and mating fastener pattern are inferred from row name and geometry."
mass:
  value_kg: 0.171
  basis: "Per unit. BOM quantity is 1, so row total is also about 0.171 kg. FreeCAD volume 21765.427 mm^3 = 0.000021765427 m^3; assembly STEP metadata reports Steel density 7850 kg/m^3; computed mass = 0.000021765427 m^3 * 7850 kg/m^3 = 0.1709586 kg, rounded to 0.171 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6S3_bent_part.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 21765.427 mm^3, area 16192.837 mm^2, and bounding box 69.03 x 65.45 x 68.41 mm. The local assembly STEP material extractor matched 6S3_bent_part to material Steel with density 7850.0. The local density table lists steel density_kg_per_m3: 7850."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the finished physical volume for one 6S3 bracket."
    - "The assembly STEP steel density is interpreted as kg/m^3-like density, consistent with the local extractor note for this reAM250 export."
  uncertainty_notes:
    - "Mass excludes separate screws, spacers, motor, and adjacent mount parts that are represented by other BOM rows."
material:
  primary_material: "generic steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 6S3_bent_part to material Steel with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The local material metadata gives a steel family but not a specific alloy grade, coating, heat treatment, or surface finish."
how_to_make:
  summary: "Make as a custom bent steel motor bracket: cut the flat profile and hole pattern from steel sheet or plate, bend the vertical flange on a press brake or fixture, deburr, finish, and inspect the motor-hole pattern and bracket angle."
  manufacturing_steps:
    - "Start from steel sheet or plate stock sized for a roughly 69 x 65 x 68 mm bent bracket envelope."
    - "Laser cut, waterjet cut, punch, or mill the flat blank with the central circular opening and smaller mounting holes."
    - "Form the bracket bend with a press brake or equivalent fixture to create the vertical flange and horizontal motor plate."
    - "Deburr hole edges and bend edges; apply a corrosion-protective finish if the machine environment requires it."
    - "Inspect the bend angle, central clearance opening, hole positions, and fit to the adjacent motor mount components."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6S3_bent_part.step; research/ream250_bom/ream250_bom_row_0199_6S3__views_2x2.png"
    cited_fact_or_basis: "The STEP/contact sheet shows one steel L-shaped bent bracket with a vertical flange, horizontal plate, central circular opening, smaller holes, and a measured 69.03 x 65.45 x 68.41 mm bounding box. targeted_web_search: searched \"6S3_bent_part motor mount\", \"reAM250 6S3 motor mount\", \"reAM250 6S3_bent_part\", and \"sheet metal motor mount bracket bending steel mounting plate\"; results found duplicate reAM250 BOM text and general bent motor-bracket examples, but no row-specific fabrication drawing, tolerance callout, or manufacturing process source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the bent bracket geometry and steel material metadata rather than from a row-specific drawing."
    - "Cut-and-bend sheet or plate fabrication is preferred over casting or additive manufacturing because the CAD shape is a thin bent bracket with pierced holes."
  uncertainty_notes:
    - "The CAD does not specify stock thickness, bend radius, tolerances, coating, or whether the original was made by bending one blank versus welding or machining an L-shaped bracket."
kb_implications:
  - "item_granularity: simple_part - model as one custom steel bent motor-mount bracket made from sheet or plate stock with cutting, bending, deburring, and inspection."
---

Research result for reAM250 BOM row 199.
