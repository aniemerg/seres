---
row_identity:
  item: "91A"
  cad_file: "91A_square_profile_DIN_EN_10219-2_80x80x5_670"
  source_row_number: 286
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Cut 80 x 80 x 5 mm square hollow structural tube section, 670 mm long, used as a straight frame or spacer member in the reAM250 structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91A_square_profile_DIN_EN_10219-2_80x80x5_670.step; research/ream250_bom/ream250_bom_row_0286_91A__views_2x2.png"
    cited_fact_or_basis: "BOM row 286 lists item 91A, quantity 8, description square hollow section, and CAD file 91A_square_profile_DIN_EN_10219-2_80x80x5_670. The manifest maps row 286 to a matched part STEP. FreeCAD measured one solid with bounding box 80.00 x 80.00 x 670.00 mm. The rendered contact sheet shows a long straight square hollow profile."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as a structural frame member because the BOM description, CAD filename, and preview all identify a square hollow section rather than a calibrated module."
  uncertainty_notes:
    - "The available row evidence does not identify the exact frame location or mating joints for these eight identical members."
mass:
  value_kg: 7.55
  basis: "FreeCAD volume 961865.031 mm^3 equals 0.000961865 m^3. Using the local assembly STEP material density 7850 kg/m^3 for Steel, Mild gives 7.55 kg per cut section. Quantity is 8, so the row total is about 60.4 kg. As a cross-check, a published 80 x 80 x 5.0 square hollow section table gives 11.6 kg/m, which would give about 7.77 kg for 0.670 m."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91A_square_profile_DIN_EN_10219-2_80x80x5_670.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; https://irp-cdn.multiscreensite.com/cf413761/files/uploaded/Square%20Hollow%20Section.pdf"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 961865.031 mm^3, area 387617.251 mm^2, and bounding box 80.00 x 80.00 x 670.00 mm. The local assembly STEP material extractor reports material Steel, Mild with density 7850.0 for this product. The local density table lists steel density as 7850 kg/m^3. The Square Hollow Section table lists 80 x 80 x 5.0 SHS mass as 11.6 kg/m."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one cut section."
    - "The eight BOM units are identical copies of this one CAD-defined cut length."
  uncertainty_notes:
    - "CAD-derived mass is slightly below the tabulated 11.6 kg/m cross-check, likely due to corner radii or profile-definition differences; either value is within a few percent for KB planning."
material:
  primary_material: "mild steel square hollow structural section"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91A_square_profile_DIN_EN_10219-2_80x80x5_670.step; https://webstore.ansi.org/standards/din/dinen102192006-1162594"
    cited_fact_or_basis: "The local assembly STEP material extractor reports material Steel, Mild and density 7850.0 for 91A_square_profile_DIN_EN_10219-2_80x80x5_670. ANSI's DIN EN 10219-2 listing describes the standard as cold formed welded structural hollow sections of non-alloy and fine grain steels, matching the CAD filename's DIN_EN_10219-2 designation."
    evidence_basis: "bom_provided"
  assumptions:
    - "The material metadata is taken as the row-specific material authority, while the DIN EN 10219-2 designation is used as a consistency check for steel structural hollow section stock."
  uncertainty_notes:
    - "The exact EN steel grade, such as S235, S275, or S355, is not specified by the BOM row or local material metadata."
how_to_make:
  summary: "Produce DIN EN 10219-style mild-steel square hollow section stock, then cut to the 670 mm row length and deburr/finish the ends for assembly"
  manufacturing_steps:
    - "Produce square hollow section stock from non-alloy structural steel by cold forming and longitudinal welding"
    - "Select 80 x 80 x 5 mm stock and cut one piece to the 670 mm finished length shown by the CAD model."
    - "Deburr and square the cut ends; drill or weld attachment features only if required by the downstream frame assembly."
    - "Apply the final corrosion-protection or paint system after the downstream frame joining requirements are known."
  source:
    url_or_path: "https://webstore.ansi.org/standards/din/dinen102192006-1162594; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91A_square_profile_DIN_EN_10219-2_80x80x5_670.step; research/ream250_bom/ream250_bom_row_0286_91A__views_2x2.png"
    cited_fact_or_basis: "ANSI's DIN EN 10219-2 listing states that the standard covers cold formed welded circular, square, and rectangular structural hollow sections and gives dimensions and sectional properties for standard sizes. CAD and preview show one 80.00 x 80.00 x 670.00 mm straight square hollow section. targeted_web_search: searched \"DIN EN 10219-2 cold formed welded structural hollow sections\", \"80x80x5 square hollow section mass per metre steel\", and \"DIN EN 10219 square hollow section cold formed welded\" found standard/product-family evidence for cold-formed welded steel hollow sections but no row-specific fabrication drawing beyond the supplied CAD."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Cut-to-length, deburring, and later coating are inferred from the CAD-defined 670 mm member length and normal use of structural tube stock."
    - "No special machining is assumed because the row CAD shows a plain tube section with no holes, brackets, or welded attachments."
  uncertainty_notes:
    - "The row does not specify end tolerances, weld-joint preparation, coating, or whether later assembly operations add holes or welded connection details."
kb_implications:
  - "item_granularity: simple_part - model as reusable 80x80x5 mild-steel square hollow section stock with recipe/BOM variants for cut lengths rather than as a machine-specific purchased module."
---

Research result for reAM250 BOM row 286.
