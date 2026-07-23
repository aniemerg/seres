---
row_identity:
  item: "2AC6"
  cad_file: "2AC6_part_6"
  source_row_number: 40
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small spherical rolling element for the bottom axis bearing group; likely one ball in the lower SLA10-class bearing support or guide contact set."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC6_part_6.step; research/ream250_bom/ream250_bom_row_0040_2AC6__views_2x2.png"
    cited_fact_or_basis: "BOM row 40 identifies item 2AC6, quantity 1, CAD file 2AC6_part_6, description 'axis bearing bottom'. The manifest maps the same row to gold_export/parts/2AC6_part_6.step with matched_existing part status. FreeCAD measured one solid with volume 82.448 mm^3, area 91.609 mm^2, and bounding box about 5.40 x 5.40 x 5.40 mm; the rendered contact sheet shows a plain near-spherical part."
    evidence_basis: "bom_provided"
  assumptions:
    - "The repeated adjacent BOM rows 2AC4 through 2AC9 with the same bottom-axis-bearing description are treated as separate rolling elements or sibling bearing subparts in the same lower bearing group, not unique machine assemblies."
  uncertainty_notes:
    - "The local BOM does not identify the mating race, cage, preload method, or exact bearing standard, so the specific bearing arrangement remains inferred from the row name and spherical CAD shape."
mass:
  value_kg: 0.000647
  basis: "Per-unit estimate for one 5.40 mm diameter ball. CAD volume is 82.448 mm^3 = 8.2448e-8 m^3; using the local generic steel density constant 7850 kg/m^3 gives 0.000647 kg. BOM quantity is 1, so row total is also about 0.000647 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC6_part_6.step; kb/materials/properties.yaml; https://hartfordtechnologies.com/precision-balls/chrome-steel-balls/; https://bearing-king.co.uk/products/5-5mm-diameter-grade-100-52100-hardened-chrome-steel-balls"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 82.448 mm^3 and bounding box about 5.40 x 5.40 x 5.40 mm. kb/materials/properties.yaml lists generic steel density as 7850 kg/m^3. Hartford Technologies identifies chrome steel balls as 52100 / 100Cr6 / SUJ2 / GCr15 and sizes from 1 mm to 50.8 mm; Bearing King lists a 5.5 mm 52100 chrome-steel ball at 0.6786 g, consistent with the CAD-density estimate. targeted_web_search: searched '2AC6_part_6 axis bearing bottom material', 'reAM250 2AC6 axis bearing bottom', '5.5 mm chrome steel bearing ball AISI 52100 weight', and '5.4 mm bearing ball material'; found duplicate local/public BOM-style text and generic bearing-ball sources only, with no row-specific catalog mass or material metadata."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP sphere is treated as the complete physical volume for one BOM row 2AC6 item, with no hidden cage, race, retainer, or fastener included."
    - "Generic steel density is used as a close local calculation constant for a likely bearing-steel ball."
  uncertainty_notes:
    - "Assembly STEP material extraction returned only placeholder material 'Generic' with density 1000.0, so the mass depends on the bearing-steel material inference rather than row-specific material metadata."
material:
  primary_material: "hardened bearing steel / chrome steel bearing-ball material family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC6_part_6.step; research/ream250_bom/ream250_bom_row_0040_2AC6__views_2x2.png; https://hartfordtechnologies.com/precision-balls/chrome-steel-balls/; https://bearing-king.co.uk/products/5-5mm-diameter-grade-100-52100-hardened-chrome-steel-balls"
    cited_fact_or_basis: "The BOM identifies the row as 'axis bearing bottom' and the CAD/contact sheet shows a 5.40 mm sphere. Hartford Technologies identifies chrome steel precision balls as 52100 / 100Cr6 / SUJ2 / GCr15. Bearing King identifies comparable 5.5 mm balls as 52100 hardened chrome steel. targeted_web_search: searched '2AC6_part_6 axis bearing bottom material', 'reAM250 2AC6 axis bearing bottom material', 'SLA10 bearing ball material', and '5.5 mm bearing ball material chrome steel 52100'; no row-specific material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because the row is a small spherical element in an axis-bearing group, standard hardened bearing/chrome steel is the most plausible material family."
  uncertainty_notes:
    - "The exact grade and heat treatment are not proven for this row; stainless steel, ceramic, or another bearing-ball material would change the material model, but no row-specific evidence supports those alternatives."
how_to_make:
  summary: "Prepare as a standard approximately 5.4-5.5 mm precision bearing ball; form bearing-steel wire into a ball blank, harden it, then grind and lap to diameter and surface finish"
  manufacturing_steps:
    - "Start from bearing-steel wire or rod stock sized near the finished 5.40 mm ball diameter."
    - "Cold-head or otherwise form a near-spherical blank."
    - "Flash/deburr the blank to remove excess material."
    - "Heat treat/harden if using chrome bearing steel."
    - "Grind, lap, clean, and inspect for diameter, roundness, hardness, and surface finish."
  source:
    url_or_path: "https://resources.hartfordtechnologies.com/blog/high-quality-precision-ball-manufacturing-a-process-overview; https://insights.globalspec.com/article/12349/how-are-bearing-balls-made; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC6_part_6.step"
    cited_fact_or_basis: "Hartford describes precision ball production using wire/slug cutting, cold heading, flashing, heat treatment, grinding, lapping, and cleaning. GlobalSpec describes bearing-ball manufacturing steps including heading, flashing, soft grinding, heat treating, grinding, lapping, washing, and sizing. The local STEP/preview identifies this row as a single small spherical bearing element. targeted_web_search: searched 'bearing balls manufacturing process cold heading flashing grinding lapping', '5.5 mm bearing ball manufacturing process', and '2AC6_part_6 axis bearing bottom manufacturing'; found generic precision-ball manufacturing routes but no row-specific reAM250 production process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route follows common precision bearing-ball practice because no row-specific production drawing is available."
  uncertainty_notes:
    - "Required grade, tolerance class, surface finish, and hardness are not specified by the BOM row."
kb_implications:
  - "item_granularity: simple_part - Model as reusable standard small bearing-ball hardware rather than a reAM250-specific custom part; capture diameter and probable bearing-steel material in notes."
---
