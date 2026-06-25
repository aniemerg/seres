---
row_identity:
  item: "91B"
  cad_file: "91B_square_profile_DIN_EN_10219-2_80x80x5_700"
  source_row_number: 287
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Cut 80 x 80 x 5 mm square hollow structural tube section, 700 mm nominal length, used as a straight frame or spacer member in the reAM250 structure."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91B_square_profile_DIN_EN_10219-2_80x80x5_700.step; research/ream250_bom/ream250_bom_row_0287_91B__views_2x2.png"
    cited_fact_or_basis: "BOM row 287 lists item 91B, quantity 1, description square hollow section, and CAD file 91B_square_profile_DIN_EN_10219-2_80x80x5_700. The manifest maps row 287 to a matched part STEP. FreeCAD measured one solid with volume 1004933.622 mm^3 and bounding box 80.00 x 150.00 x 701.98 mm. The rendered contact sheet shows a long straight square hollow profile with open ends."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as a structural frame member because the BOM description, CAD filename, and preview identify a square hollow section rather than a calibrated module."
  uncertainty_notes:
    - "The row evidence does not identify the exact frame location, mating joints, or why the CAD bounding box includes a 150 mm transverse extent despite the 80 x 80 profile designation."
mass:
  value_kg: 7.89
  basis: "FreeCAD volume 1004933.622 mm^3 equals 0.001004934 m^3. Using the local assembly STEP material density 7850 kg/m^3 for Steel, Mild gives 7.89 kg per cut section. Quantity is 1, so the row total is also about 7.89 kg. As a reasonableness check, a sharp-corner 80 x 80 x 5 mm hollow square over 0.700 m has about 0.00105 m^3 of steel before corner-radius effects, giving about 8.24 kg at 7850 kg/m^3."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91B_square_profile_DIN_EN_10219-2_80x80x5_700.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1004933.622 mm^3, area 405847.222 mm^2, and bounding box 80.00 x 150.00 x 701.98 mm. The local assembly STEP material extractor reports material Steel, Mild with density 7850.0 for this product. The local density table lists steel density as 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one cut section."
    - "The single BOM unit is represented by the one CAD-defined solid."
  uncertainty_notes:
    - "The CAD-derived mass depends on the exported solid volume, including its modeled corner radii or profile details; the simple sharp-corner hand check is a few percent higher."
material:
  primary_material: "mild steel square hollow structural section"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91B_square_profile_DIN_EN_10219-2_80x80x5_700.step; https://knowledge.bsigroup.com/products/cold-formed-welded-steel-structural-hollow-sections-tolerances-dimensions-and-sectional-properties"
    cited_fact_or_basis: "The local assembly STEP material extractor reports material Steel, Mild and density 7850.0 for 91B_square_profile_DIN_EN_10219-2_80x80x5_700. BSI's BS EN 10219-2 listing describes the standard as cold formed welded steel structural hollow sections and says it covers square hollow sections, matching the CAD filename's DIN_EN_10219-2 designation."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific STEP material metadata is used as the material authority; the EN 10219-2 designation is treated as a consistency check for steel hollow-section stock."
  uncertainty_notes:
    - "The exact EN structural steel grade, such as S235, S275, or S355, is not specified by the BOM row or local material metadata."
how_to_make:
  summary: "Procure or produce DIN EN 10219-style mild-steel square hollow section stock, then cut one piece to the row length and deburr/finish the ends for assembly."
  manufacturing_steps:
    - "Produce square hollow section stock from non-alloy structural steel by cold forming and longitudinal welding, or procure equivalent DIN EN 10219 square hollow section stock."
    - "Select 80 x 80 x 5 mm stock and cut one piece to the approximately 700 mm finished length shown by the CAD model."
    - "Deburr and square the cut ends; add holes, weld preparation, or attachment features only if required by the downstream frame assembly."
    - "Apply corrosion protection or paint after the downstream frame joining and interface requirements are known."
  source:
    url_or_path: "https://knowledge.bsigroup.com/products/cold-formed-welded-steel-structural-hollow-sections-tolerances-dimensions-and-sectional-properties; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/91B_square_profile_DIN_EN_10219-2_80x80x5_700.step; research/ream250_bom/ream250_bom_row_0287_91B__views_2x2.png"
    cited_fact_or_basis: "BSI's BS EN 10219-2 listing states that the standard covers cold-formed welded steel circular, square, rectangular, and elliptical structural hollow sections and their tolerances, dimensions, and sectional properties. CAD and preview show one straight square hollow section with no visible holes, brackets, or welded-on fittings. targeted_web_search: searched \"DIN EN 10219-2 square hollow section cold formed welded structural steel\", \"EN 10219-2 square hollow section dimensions tolerances\", and \"80x80x5 square hollow section weight kg per metre steel\"; found standard/product-family evidence for cold-formed welded steel hollow sections but no row-specific fabrication drawing beyond the supplied CAD."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Cut-to-length, deburring, and later coating are inferred from the CAD-defined member geometry and normal use of structural tube stock."
    - "No special machining is assumed because the row CAD preview shows a plain tube section rather than a part with holes, slots, brackets, or machined interfaces."
  uncertainty_notes:
    - "The row does not specify end tolerances, cut angle, weld-joint preparation, coating, or whether later assembly operations add connection details."
kb_implications:
  - "item_granularity: simple_part - model as reusable 80x80x5 mild-steel square hollow section stock with recipe/BOM variants for cut lengths rather than as a machine-specific purchased module."
---

Research result for reAM250 BOM row 287.
