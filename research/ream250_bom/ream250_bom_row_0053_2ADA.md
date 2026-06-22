---
row_identity:
  item: "2ADA"
  cad_file: "2ADA_part_A"
  source_row_number: 53
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small spherical rolling element for the top axis-bearing group."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADA_part_A.step; research/ream250_bom/ream250_bom_row_0053_2ADA__views_2x2.png"
    cited_fact_or_basis: "BOM row 53 identifies item 2ADA, quantity 1, CAD file 2ADA_part_A, description 'axis bearing top'; FreeCAD measured one solid with a 4.95 mm x 4.95 mm x 4.95 mm bounding box; the rendered contact sheet shows a round ball-like part."
    evidence_basis: "bom_provided"
  assumptions:
    - "The repeated 2AD1-2ADB 'axis bearing top' rows are treated as separate rolling elements in the same bearing group rather than complete bearing cartridges."
  uncertainty_notes:
    - "The BOM description does not state the exact bearing type or race geometry, so the function is limited to the visible spherical rolling-element role."
mass:
  value_kg: 0.00050
  basis: "FreeCAD STEP volume 63.505921 mm^3 = 6.3505921e-8 m^3; multiplied by local generic steel density 7850 kg/m^3 from kb/materials/properties.yaml gives 0.0004985 kg, rounded to 0.00050 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADA_part_A.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured volume 63.505921 mm^3 and bounding box about 4.95 mm per side; kb/materials/properties.yaml lists steel density 7850 kg/m^3."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Generic steel density is used as the calculation constant for the hypothesized bearing-steel family."
    - "The STEP solid volume is used as the physical volume of one BOM item."
  uncertainty_notes:
    - "targeted_web_search: searched \"2ADA_part_A axis bearing top material\", \"2ADA axis bearing top reAM250 material\", and \"reAM250 axis bearing top bearing ball material\"; found duplicate BOM text and generic bearing-material pages only, with no row-specific material or catalog mass."
    - "If the ball is ceramic, stainless, or another alloy instead of generic steel, the mass should remain close in order of magnitude but the exact value would change."
material:
  primary_material: "hardened steel bearing-ball material family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADA_part_A.step"
    cited_fact_or_basis: "BOM row 53 describes the part as 'axis bearing top'; FreeCAD measured a single near-spherical 4.95 mm part; assembly STEP material extraction for 2ADA_part_A returned only placeholder material 'Generic' with density 1000.0."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A small spherical element in an axis-bearing group is modeled as a bearing ball, and the broad bearing-steel family is used rather than claiming a specific grade."
  uncertainty_notes:
    - "targeted_web_search: searched \"2ADA_part_A axis bearing top material\", \"2ADA axis bearing top reAM250 material\", and \"reAM250 axis bearing top bearing ball material\"; found duplicate BOM text and generic bearing-material pages only, with no row-specific vendor/material source."
    - "No BOM field, CAD metadata, vendor link, or standard designation resolves the exact grade."
how_to_make:
  summary: "Manufacture as a precision bearing ball from hardened steel stock, then finish-grind/lap and inspect diameter and surface finish."
  manufacturing_steps:
    - "Cut or cold-head small steel blanks near the required ball diameter."
    - "Rough form the blanks into spheres."
    - "Heat treat to bearing-ball hardness."
    - "Precision grind, lap, and polish to final diameter and surface finish."
    - "Clean and inspect diameter, roundness, and surface defects before installation in the axis-bearing assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2ADA_part_A.step"
    cited_fact_or_basis: "The STEP file measures one near-spherical solid about 4.95 mm in diameter for a BOM row described as 'axis bearing top'."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is a bearing ball rather than a spacer or decorative spherical feature."
    - "A conventional precision bearing-ball manufacturing route is used because the CAD shape and BOM context imply a rolling contact component."
  uncertainty_notes:
    - "targeted_web_search: searched \"2ADA_part_A axis bearing top material\", \"2ADA axis bearing top reAM250 material\", and \"reAM250 axis bearing top bearing ball material\"; found no row-specific manufacturing drawing or process specification."
    - "The required tolerance grade and surface-finish class are not specified by the BOM or CAD export."
kb_implications:
  - "item_granularity: simple_part - model as one small rolling bearing element; later KB work can reuse a generic bearing_ball_5mm-style part rather than creating row-specific 2AD variants."
---
