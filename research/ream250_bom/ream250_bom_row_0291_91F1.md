---
row_identity:
  item: "91F1"
  cad_file: "91F1_square_profile_DIN_EN_10219-2_80x80x5_150"
  source_row_number: 291
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Short 80 x 80 x 5 mm square hollow structural section, 150 mm long, used as a compact frame/spacer member in the reAM250 mechanical structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0291_91F1__views_2x2.png"
    cited_fact_or_basis: "BOM row 291 identifies item 91F1 as quantity 1, CAD file 91F1_square_profile_DIN_EN_10219-2_80x80x5_150, description square hollow section; the manifest maps the same row to a matched part STEP; the preview shows an open-ended square tube with rounded corners and no added holes or brackets."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as a structural spacer/frame member because the BOM description and CAD geometry are a square hollow section, but the exact mounting location is not named in the row."
  uncertainty_notes:
    - "No parent assembly name or installation notes were provided, so the exact load path or mating parts remain unresolved."
mass:
  value_kg: 1.690
  basis: "FreeCAD measured one solid with volume 215342.917 mm^3 and bounding box 80.00 x 80.00 x 150.00 mm. The assembly STEP material metadata reports Steel, Mild with density 7850 kg/m^3. Per-unit mass = 215342.917 mm^3 * 1e-9 m^3/mm^3 * 7850 kg/m^3 = 1.690 kg. BOM quantity is 1, so row total is also about 1.690 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91F1_square_profile_DIN_EN_10219-2_80x80x5_150.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 215342.917 mm^3, area 89008.406 mm^2, and bounding box 80.00 x 80.00 x 150.00 mm; local assembly STEP material extraction for 91F1_square_profile_DIN_EN_10219-2_80x80x5_150 reports material Steel, Mild and density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP part volume is treated as the physical volume of one BOM-row item."
    - "The assembly STEP density is interpreted as kg/m^3, consistent with the reAM250 material extractor note."
  uncertainty_notes:
    - "The CAD volume includes modeled corner radii and any STEP simplifications; it should be preferred over a sharp-corner tube hand calculation for this row, but remains CAD-derived rather than weighed."
material:
  primary_material: "mild steel structural square hollow section"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://knowledge.bsigroup.com/products/cold-formed-welded-steel-structural-hollow-sections-tolerances-dimensions-and-sectional-properties"
    cited_fact_or_basis: "Local assembly STEP material extraction for this product reports Steel, Mild with density 7850.0; BSI describes BS EN 10219-2 as covering cold-formed welded steel structural hollow sections, including square sections."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN EN 10219-2 designation is used as corroboration that this row is a steel structural hollow section, while the row-specific STEP metadata resolves the material family as mild steel."
  uncertainty_notes:
    - "The exact EN steel grade, such as S235 or S355, is not specified by the BOM row, filename, or extracted STEP metadata."
how_to_make:
  summary: "Produce EN 10219-2-compatible mild-steel square hollow section stock and cut it to the 150 mm finished length; form steel strip into a square tube, longitudinally weld it, size it to 80 x 80 x 5 mm, then saw/cut and deburr the short section"
  manufacturing_steps:
    - "Start from mild-steel strip/coil or structural tube stock suitable for square hollow sections."
    - "For local tube production, cold-form the strip into an 80 x 80 mm square hollow profile and longitudinally weld the seam."
    - "Size/calibrate the profile to the required 5 mm wall and square-section tolerance class."
    - "Cut one 150 mm length from the tube stock."
    - "Deburr and inspect length, squareness, and open-end condition before assembly."
  source:
    url_or_path: "https://knowledge.bsigroup.com/products/cold-formed-welded-steel-structural-hollow-sections-tolerances-dimensions-and-sectional-properties; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91F1_square_profile_DIN_EN_10219-2_80x80x5_150.step"
    cited_fact_or_basis: "BSI identifies EN 10219-2 as a standard for cold-formed welded steel structural hollow sections and says it covers square sections and dimensions/tolerances; the row CAD measures an 80.00 x 80.00 x 150.00 mm open square tube. targeted_web_search: searched \"EN 10219-2 square hollow section cold formed welded structural steel tubes standard title\" and \"DIN EN 10219-2 square hollow section 80x80x5 steel tube\" found standard/catalog evidence for the stock family but no row-specific factory routing for item 91F1."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Cutting from standard EN 10219-2 square hollow section stock is the most plausible route for this simple structural row."
    - "The cold-forming and welding steps describe local tube-stock production"
  uncertainty_notes:
    - "Cut, cut in-house, or fabricated from strip"
kb_implications:
  - "item_granularity: simple_part - model as a reusable mild-steel square hollow structural section/cut tube length rather than a machine-specific assembly."
---

Research result for reAM250 BOM row 291.
