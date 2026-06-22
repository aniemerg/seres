---
row_identity:
  item: "2AC4"
  cad_file: "2AC4_part_4"
  source_row_number: 38
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Loose spherical rolling element for the bottom axis bearing stack; it provides point rolling contact between bearing races or seats so the bottom axis can rotate with lower friction."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC4_part_4.step; research/ream250_bom/ream250_bom_row_0038_2AC4__views_2x2.png"
    cited_fact_or_basis: "BOM row 38 names item 2AC4 / 2AC4_part_4 as 'axis bearing bottom'; FreeCAD measured one solid with a 5.40 mm by 5.40 mm by 5.40 mm bounding box, and the rendered contact sheet shows a smooth sphere."
    evidence_basis: "bom_provided"
  assumptions:
    - "The repeated neighboring 2AC rows with the same 'axis bearing bottom' description are separate rolling elements in the same bottom bearing assembly."
  uncertainty_notes: []
mass:
  value_kg: 0.000647
  basis: "Per-unit mass for one 5.4 mm diameter sphere. FreeCAD measured volume 82.448 mm^3; using the local generic steel density 7850 kg/m^3 gives 82.448e-9 m^3 * 7850 kg/m^3 = 0.000647 kg, about 0.647 g. BOM quantity is 1, so the row total is also about 0.000647 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC4_part_4.step; kb/materials/properties.yaml; https://www.redhillballs.com/product/bearing-steel-balls/bearing-chrome-steel-balls/"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 82.448 mm^3. The local material table gives generic steel density as 7850 kg/m^3. The independent bearing-ball vendor page describes chrome steel bearing balls as AISI 52100 high-carbon chromium alloy steel used for precision bearings."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD solid represents one physical bearing ball and has no hidden internal voids."
    - "Generic steel density is a close calculation constant for chrome bearing steel at this modeling precision."
  uncertainty_notes:
    - "The row STEP material metadata is only 'Generic' with density 1000 kg/m^3, so the steel material used for mass is independently inferred from bearing-ball practice rather than supplied by the BOM package."
material:
  primary_material: "chrome bearing steel / high-carbon chromium bearing steel"
  source:
    url_or_path: "https://www.redhillballs.com/product/bearing-steel-balls/bearing-chrome-steel-balls/"
    cited_fact_or_basis: "Targeted search for '5.4 mm bearing ball material chrome steel' found an independent bearing-ball supplier describing bearing chrome steel balls as AISI 52100 high-carbon chromium alloy steel for precision bearing applications."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's spherical CAD geometry and 'axis bearing bottom' BOM description identify this as a loose bearing ball, so common bearing-ball material practice is applicable."
  uncertainty_notes:
    - "No row-specific non-placeholder STEP material or BOM vendor link resolves the exact grade; stainless or ceramic bearing balls are possible alternatives, but the BOM package gives no evidence for those variants."
how_to_make:
  summary: "Treat as a standard precision loose bearing ball: procure as a finished chrome-steel bearing ball where possible; a local manufacturing route would form a steel blank, harden it, then grind, lap, polish, and inspect to bearing-ball roundness and surface-finish requirements."
  manufacturing_steps:
    - "Start from bearing-steel wire or rod sized for a roughly 5.4 mm ball blank."
    - "Cold-head or cut and upset the blank into a near-spherical ball, then remove flash."
    - "Through-harden and temper the ball for bearing service."
    - "Rough grind, lap, polish, clean, and grade-sort for diameter, roundness, and surface finish."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC4_part_4.step; https://hartfordtechnologies.com/precision-balls/chrome-steel-balls/"
    cited_fact_or_basis: "The row CAD is a smooth 5.4 mm sphere. The independent precision-ball supplier page describes chrome steel as bearing-grade alloy steel with high hardness, wear resistance, through-hardening, and precision surface characteristics. targeted_web_search: tried '5.4 mm bearing ball material chrome steel' and 'bearing balls chrome steel material 5.4 mm'; results found general bearing-ball material/spec pages but no row-specific manufacturing process for 2AC4."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Detailed forming, grinding, lapping, and inspection steps are inferred from common precision-ball manufacturing practice, because the BOM and supplier pages identify the item class but do not specify the actual production route for this row."
  uncertainty_notes:
    - "Local manufacture would require precision finishing and metrology capability; procurement is the more realistic near-term route unless the KB later models precision bearing-ball production."
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable loose precision bearing ball or small bearing-ball part, not as raw stock or a purchased functional module."
---
