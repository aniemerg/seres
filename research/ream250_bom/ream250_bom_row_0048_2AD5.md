---
row_identity:
  item: "2AD5"
  cad_file: "2AD5_part_5"
  source_row_number: 48
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small spherical rolling element for the top axis bearing group; likely one ball in a top-axis bearing or ball-transfer/guide contact set."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD5_part_5.step; research/ream250_bom/ream250_bom_row_0048_2AD5__views_2x2.png"
    cited_fact_or_basis: "BOM row 48 names item 2AD5 / 2AD5_part_5 as 'axis bearing top' with quantity 1. FreeCAD measured one solid with volume 63.506 mm^3 and a 4.95 x 4.95 x 4.95 mm bounding box. The rendered CAD preview shows a plain sphere."
    evidence_basis: "bom_provided"
  assumptions:
    - "The repeated adjacent BOM rows 2AD1 through 2ADB with the same description are treated as separate bearing balls in the same top-axis bearing group, not unique assemblies."
  uncertainty_notes:
    - "The local BOM does not identify the mating race, cage, or exact bearing standard, so the specific bearing arrangement remains inferred from the row name and spherical CAD shape."
mass:
  value_kg: 0.000499
  basis: "Per-unit estimate for one 4.95 mm diameter ball. CAD volume is 63.506 mm^3 = 6.3506e-8 m^3; using the local steel density constant 7850 kg/m^3 gives 0.000499 kg. BOM quantity is 1, so row total is also about 0.000499 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD5_part_5.step; kb/materials/properties.yaml; https://hartfordtechnologies.com/precision-balls/chrome-steel-balls/"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 63.506 mm^3, area 76.977 mm^2, and bounding box 4.95 x 4.95 x 4.95 mm. kb/materials/properties.yaml lists steel density as 7850 kg/m^3. Hartford Technologies states chrome steel balls use 52100 / 100Cr6 / SUJ2 / GCr15 material and are available from 1 mm to 50.8 mm. targeted_web_search: searched '5 mm bearing ball material chrome steel 100Cr6 standard', 'axis bearing top 2AD5 part 5 reAM250', and '2AD5_part_5 axis bearing top material'; found the duplicate/public BOM row and generic bearing-ball material sources, but no row-specific catalog mass or material metadata."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP sphere is treated as the physical item volume with no hidden cage, race, or fastener included in this row."
    - "Generic steel density is used as a close local calculation constant for a likely bearing-steel ball."
  uncertainty_notes:
    - "Assembly STEP material extraction returned only placeholder material 'Generic' with density 1000.0, so the mass depends on the bearing-steel material inference rather than row-specific material metadata."
material:
  primary_material: "bearing steel / chrome steel family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0048_2AD5__views_2x2.png; https://www.rolling-components.com/chrome-steel-1-3505-100cr6/; https://hartfordtechnologies.com/precision-balls/chrome-steel-balls/"
    cited_fact_or_basis: "The BOM identifies the row as 'axis bearing top' and the preview shows a 4.95 mm sphere. TIS describes 1.3505 / 100Cr6 as the typical rolling-bearing steel for balls, cylindrical rollers, and needle rollers. Hartford Technologies identifies chrome steel precision balls as 52100 / 100Cr6 / SUJ2 / GCr15 and lists sizes from 1 mm to 50.8 mm. targeted_web_search: searched '5 mm bearing ball material chrome steel 100Cr6 standard', '2AD5_part_5 axis bearing top material', and 'reAM250 2AD5 axis bearing top material'; no row-specific material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because the row is a small spherical bearing element, standard bearing/chrome steel is the most plausible material family."
  uncertainty_notes:
    - "The exact grade and heat treatment are not proven for this row; stainless or ceramic bearing balls would change the material model, but no row-specific evidence supports those alternatives."
how_to_make:
  summary: "Prepare as a standard precision bearing ball; form bearing-steel wire into a ball blank, harden it, then grind and lap to diameter and surface finish"
  manufacturing_steps:
    - "Start from bearing-steel wire or rod stock sized near the finished 4.95 mm ball diameter."
    - "Cold-head or otherwise form a near-spherical blank."
    - "Heat treat/harden if using chrome bearing steel."
    - "Grind, lap, clean, and inspect for diameter, roundness, and surface finish."
  source:
    url_or_path: "https://resources.hartfordtechnologies.com/blog/high-quality-precision-ball-manufacturing-a-process-overview; https://www.globalspec.com/article/4523/how-ball-bearings-are-manufactured; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD5_part_5.step"
    cited_fact_or_basis: "Hartford describes precision ball manufacturing steps including heading, flashing, heat treating, grinding, and lapping. GlobalSpec describes ball-bearing manufacture as involving machining, heat treating, grinding, honing, lapping, and assembly. The local STEP/preview identifies this row as a single small spherical bearing element. targeted_web_search: searched 'bearing balls manufacturing process chrome steel grinding lapping', '5 mm bearing ball manufacturing process', and '2AD5_part_5 axis bearing top manufacturing'; found generic precision-ball manufacturing routes but no row-specific factory process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route follows common precision bearing-ball practice because no row-specific production drawing is available."
  uncertainty_notes:
    - "Required grade, tolerance class, surface finish, and hardness are not specified by the BOM row."
kb_implications:
  - "item_granularity: simple_part - Model as reusable standard small bearing-ball hardware rather than a reAM250-specific custom part; capture diameter and probable bearing-steel material in notes."
---
