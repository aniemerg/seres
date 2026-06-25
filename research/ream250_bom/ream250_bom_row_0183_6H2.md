---
row_identity:
  item: 6H2
  cad_file: 6H2_seal_top
  source_row_number: 183
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
  link_url: https://www.lisema.eu/
function:
  summary: Thin rectangular top seal/gasket, likely used to close a long rectangular interface on the reAM250 machine by compressing silicone rubber between mating surfaces.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6H2_seal_top.step; research/ream250_bom/ream250_bom_row_0183_6H2__views_2x2.png
    cited_fact_or_basis: "BOM row 183 names item 6H2 as 6H2_seal_top from Lisema; FreeCAD measured one solid with bounding box 352.00 x 80.00 x 2.00 mm; rendered top/iso views show a flat rectangular frame/window seal."
    evidence_basis: bom_provided
  assumptions:
    - The suffix "seal_top" and flat frame geometry indicate a compressive gasket function rather than a structural plate.
  uncertainty_notes:
    - The exact mating interface and sealing medium are not identified by the row-level CAD file.
mass:
  value_kg: 0.0294
  basis: "Per unit. Quantity in BOM row is 1, so row total is also about 0.0294 kg. FreeCAD volume is 23492.708 mm^3 = 2.3492708e-5 m^3; assembly STEP material metadata reports silicone rubber density 1250 kg/m^3; computed mass is 2.3492708e-5 m^3 x 1250 kg/m^3 = 0.02937 kg."
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6H2_seal_top.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: "FreeCAD measured one solid, volume 23492.708 mm^3, area 27030.903 mm^2, bounding box 352.00 x 80.00 x 2.00 mm. Local assembly material extractor matched 6H2_seal_top to material Rubber, Silicone with density 1250 kg/m^3."
    evidence_basis: bom_provided
  assumptions:
    - The STEP solid volume represents one physical seal for this BOM row.
    - The assembly STEP density is interpreted as kg/m^3, consistent with the extractor note for reAM250 material densities.
  uncertainty_notes:
    - CAD volume may omit compression set, manufacturing flash, or small bevel details, but those are unlikely to change mass by more than a few grams for this flat elastomer seal.
material:
  primary_material: Silicone rubber
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step
    cited_fact_or_basis: "Local STEP material extraction for product 6H2_seal_top reports material Rubber, Silicone and density 1250 kg/m^3."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - The material metadata gives the family but not durometer, cure system, filler package, color, or exact silicone grade.
how_to_make:
  summary: Procure as a Lisema/vendor silicone seal or manufacture locally as a flat silicone gasket cut from sheet stock, with waterjet/digital knife/die cutting suitable for the rectangular window profile; molded silicone is a fallback if the seal has controlled edge features not captured in the simplified route.
  manufacturing_steps:
    - Select silicone rubber sheet around 2 mm thick with compatible temperature, vacuum, and compression-set requirements.
    - Cut the outer rectangle and inner window profile from sheet using waterjet, digital knife, or steel-rule die tooling.
    - Deburr/clean the elastomer edges, inspect profile dimensions against the CAD outline, and install by compression between the mating top surfaces.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6H2_seal_top.step; https://www.stockwell.com/custom-gaskets/
    cited_fact_or_basis: "CAD evidence shows a 352.00 x 80.00 x 2.00 mm flat rectangular window seal. Stockwell Elastomerics describes custom silicone gaskets made by waterjet cutting, die cutting, molding, and cutting to supplied CAD/drawing geometries. targeted_web_search: tried 'Lisema 6H2 seal top silicone rubber seal', 'Lisema 6H2 seal_top', and 'Lisema reAM250 6H2 seal top'; no row-specific Lisema product or drawing was found beyond the BOM/CAD evidence."
    evidence_basis: engineering_hypothesis
  assumptions:
    - The seal is a flat gasket without embedded reinforcement, adhesive backing, or molded lips that would require a different process.
    - Local fabrication prioritizes low-volume sheet cutting because the visible part is a simple 2 mm thick frame.
  uncertainty_notes:
    - Without Lisema's drawing, the exact durometer, surface finish, and acceptance criteria remain unspecified.
kb_implications:
  - "item_granularity: simple_part - Model as a replaceable silicone seal/gasket rather than a machine-specific assembly; later KB work can reuse a generic flat silicone gasket process with row-specific dimensions."
---
