---
row_identity:
  item: "17AK"
  cad_file: "17AK_sheet_top"
  source_row_number: 239
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Flat top sheet/panel for the reAM250 enclosure or hood group; the CAD shows a simple rectangular sheet likely used as a cover or guard surface rather than a load-bearing machine axis component."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AK_sheet_top.step; research/ream250_bom/ream250_bom_row_0239_17AK__views_2x2.png"
    cited_fact_or_basis: "BOM row 239 lists item 17AK, quantity 1, CAD file 17AK_sheet_top. The manifest maps the row to one matched part STEP. FreeCAD measured one solid with a 474.00 x 2.00 x 304.00 mm bounding box, and the rendered preview shows a plain flat rectangular sheet."
    evidence_basis: "bom_provided"
  assumptions:
    - "The filename suffix sheet_top is interpreted as placement on the top of the local 17A enclosure/hood sheet group."
  uncertainty_notes:
    - "The CAD does not show mating hardware or assembly context, so the exact cover/guard interface is inferred only at broad panel-function level."
mass:
  value_kg: 2.26
  basis: "FreeCAD volume 288192.000 mm^3 equals 0.000288192 m^3. With representative generic steel density 7850 kg/m^3 from kb/materials/properties.yaml, the estimated per-unit mass is 2.262 kg; BOM quantity is 1, so row total is also about 2.26 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AK_sheet_top.step; kb/materials/properties.yaml; web search"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 288192.000 mm^3, area 291304.000 mm^2, and bounding box 474.00 x 2.00 x 304.00 mm. The local density table lists steel density_kg_per_m3: 7850. targeted_web_search: searched \"reAM250 17AK sheet_top material\", \"17AK_sheet_top\", and \"reAM250 sheet_top material\"; results found official/duplicate reAM250 BOM listings but no row-specific mass or material specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP solid volume is treated as the finished physical volume of one sheet."
    - "Generic steel density is used as a conservative planning density for an unspecified machine-cover sheet."
  uncertainty_notes:
    - "The STEP material metadata is only Generic at density 1000.0, so the actual material is unresolved; if the sheet is aluminum rather than steel, the per-unit mass would be about 0.78 kg."
material:
  primary_material: "unknown sheet metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; web search"
    cited_fact_or_basis: "The BOM row has no material-family or grade field populated. The local assembly STEP material extractor matched 17AK_sheet_top only to placeholder material Generic with density 1000.0. targeted_web_search: searched \"reAM250 17AK sheet_top material\", \"17AK_sheet_top\", and \"reAM250 sheet_top material\"; found duplicate BOM/project references but no row-specific material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The 2 mm flat-sheet geometry and sheet_top name indicate a sheet-metal panel rather than glass, elastomer, or a multi-part module."
  uncertainty_notes:
    - "The evidence supports only a broad sheet-metal/alloy family, not steel versus aluminum or a specific grade."
how_to_make:
  summary: "Make as a simple flat sheet-metal panel: cut a 474 x 304 mm rectangle from 2 mm sheet stock, deburr edges, and apply any coating or surface finish required by the enclosure environment."
  manufacturing_steps:
    - "Start from 2 mm sheet-metal stock in the selected enclosure-panel material."
    - "Cut the rectangular blank to approximately 474 x 304 mm by shear, laser cutting, waterjet cutting, or CNC routing."
    - "Deburr and inspect edge straightness, panel flatness, and thickness."
    - "Apply protective finish or cleaning if required by the final enclosure/hood environment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AK_sheet_top.step; research/ream250_bom/ream250_bom_row_0239_17AK__views_2x2.png; web search"
    cited_fact_or_basis: "The STEP geometry measures a simple 2.00 mm thick rectangular sheet with no visible holes, bends, or attached features in the rendered preview. targeted_web_search: searched \"reAM250 17AK sheet_top material\", \"17AK_sheet_top\", and \"reAM250 sheet_top material\" found no row-specific fabrication drawing or manufacturing source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A plain 2 mm rectangular sheet is best modeled as a cut sheet-metal part rather than a machined block or external calibrated module"
    - "Finishing is included as a conditional step because the unresolved material and enclosure location may require corrosion or powder-contact surface protection."
  uncertainty_notes:
    - "No row-specific drawing was found, so tolerances, finish, and whether any hidden post-CAD operations are required remain unresolved."
kb_implications:
  - "item_granularity: simple_part - model as one reusable flat sheet-metal panel/cover part, with material and finish kept as later notes rather than creating a purchased module."
---

Research result for reAM250 BOM row 239.
