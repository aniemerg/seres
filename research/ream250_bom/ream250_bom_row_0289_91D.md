---
row_identity:
  item: "91D"
  cad_file: "91D_angle_profile_DIN_59370_50x5_810"
  source_row_number: 289
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Sharp-edged mild-steel L-profile used as a straight structural angle member in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91D_angle_profile_DIN_59370_50x5_810.step; research/ream250_bom/ream250_bom_row_0289_91D__views_2x2.png"
    cited_fact_or_basis: "BOM row 289 identifies item 91D as 'sharp-edged L-profile' with quantity 8; CAD filename encodes DIN_59370_50x5_810; FreeCAD measured one solid with 50.00 x 50.00 x 810.00 mm bounding box; rendered preview shows an L-shaped angle section."
    evidence_basis: "bom_provided"
  assumptions:
    - "The L-profile functions as structural angle stock or a bracket rail rather than a calibrated purchased module."
  uncertainty_notes:
    - "The BOM row and isolated CAD do not identify the exact mounting location or load case in the full machine."
mass:
  value_kg: 3.0217
  basis: "Per-unit mass from CAD volume 384923.827 mm^3 = 0.000384923827 m^3 times row-specific STEP density 7850 kg/m^3, giving 3.02165 kg per angle. BOM quantity is 8, so the row total is about 24.17 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91D_angle_profile_DIN_59370_50x5_810.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 384923.827 mm^3. Local assembly STEP material extractor returned material 'Steel, Mild' with density 7850.0 for product 91D_angle_profile_DIN_59370_50x5_810; kb/materials/properties.yaml also lists generic steel density as 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The per-part STEP solid volume represents one physical 91D profile."
    - "The STEP density is interpreted as kg/m^3, matching the reAM250 extractor note and local steel density table."
  uncertainty_notes: []
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extractor returned material 'Steel, Mild' for product 91D_angle_profile_DIN_59370_50x5_810."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata gives material family only; it does not name a specific steel grade such as S235."
how_to_make:
  summary: "Locally make as mild-steel equal angle stock, cut to 810 mm length, deburr sharp edges as required, and inspect the 50 x 50 x 5 mm L-section dimensions"
  manufacturing_steps:
    - "Start from mild-steel angle stock matching the 50 x 50 x 5 mm DIN 59370-style L-profile geometry."
    - "Cut the profile to 810 mm length."
    - "Deburr or lightly finish cut ends while preserving the specified sharp-edged profile geometry."
    - "Inspect length, leg dimensions, and straightness before installation."
  source:
    url_or_path: "https://www.heco.de/en/stainless-steel/installation-supplies/steel-bars/angles-bars/unequal/bright-din-59370.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91D_angle_profile_DIN_59370_50x5_810.step"
    cited_fact_or_basis: "CAD/BOM define a DIN 59370-style 50 x 5 x 810 L-profile. targeted_web_search: queries tried: 'DIN 59370 sharp edged L profile steel angle bar manufacturing hot rolled cold drawn' and 'DIN 59370 L profile sharp edged steel angle 50x5'; search found DIN 59370 angle-profile vendor references and cold-drawn/sharp-edged angle-stock examples, but no row-specific manufacturing route for item 91D."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB planning, this row can be treated as cut-to-length structural angle stock rather than a custom machined part."
    - "Use standard bar/profile forming or external angle stock plus cutting, not a reAM250-specific fabrication process"
  uncertainty_notes:
    - "The exact industrial route for the source profile, such as hot rolling, cold drawing, or welded profile production, is not specified by the BOM-side evidence."
kb_implications:
  - "item_granularity: simple_part - Model later as reusable mild-steel angle/profile stock with cut length variants; the BOM row is a cut-to-length stock form rather than a finished module."
---
