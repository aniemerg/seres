---
row_identity:
  item: "2AD3"
  cad_file: "2AD3_part_3"
  source_row_number: 46
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small spherical rolling element for the reAM250 top axis bearing group."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD3_part_3.step; research/ream250_bom/ream250_bom_row_0046_2AD3__views_2x2.png"
    cited_fact_or_basis: "BOM row 46 identifies item 2AD3, quantity 1, CAD file 2AD3_part_3, description 'axis bearing top'. The manifest maps row 46 to gold_export/parts/2AD3_part_3.step with matched_existing part status. FreeCAD measured one solid with volume 63.506 mm^3 and bounding box about 4.95 x 4.95 x 4.95 mm; the rendered contact sheet shows a plain near-spherical part."
    evidence_basis: "bom_provided"
  assumptions:
    - "The repeated adjacent BOM rows 2AD1 through 2ADB with the same 'axis bearing top' description are treated as individual rolling elements in the same top-axis bearing group rather than separate bearing cartridges."
  uncertainty_notes:
    - "The BOM does not identify the mating race, preload method, cage, or complete bearing standard, so the exact role inside the top-axis bearing assembly remains inferred from row context and spherical geometry."
mass:
  value_kg: 0.000499
  basis: "Per-unit estimate for one physical BOM row 2AD3 item. CAD volume is 63.506 mm^3 = 6.3506e-8 m^3; multiplying by the local generic steel density constant of 7850 kg/m^3 gives 0.000499 kg. BOM quantity is 1, so the row total is also about 0.000499 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD3_part_3.step; kb/materials/properties.yaml; https://hartfordtechnologies.com/precision-balls/chrome-steel-balls/"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 63.506 mm^3, area 76.977 mm^2, and bounding box about 4.95 x 4.95 x 4.95 mm. kb/materials/properties.yaml lists steel density as 7850 kg/m^3. Hartford Technologies identifies chrome steel balls as 52100 / 100Cr6 / SUJ2 / GCr15 and lists sizes from 1 mm to 50.8 mm. targeted_web_search: searched '2AD3_part_3 axis bearing top material', '2AD3 axis bearing top reAM250 material', 'axis bearing top 2AD3 bearing ball', and '5 mm bearing ball material chrome steel 100Cr6'; found duplicate BOM-style row text and generic bearing-ball material sources, but no row-specific material metadata or catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP sphere is treated as the complete physical item volume for one BOM row 2AD3 part, with no hidden cage, race, or fastener included."
    - "Generic steel density is used as a local calculation constant for a likely bearing-steel ball."
  uncertainty_notes:
    - "Assembly STEP material extraction returned only placeholder material 'Generic' with density 1000.0, so the mass depends on the bearing-steel material inference rather than row-specific material metadata."
material:
  primary_material: "bearing steel / chrome steel family"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD3_part_3.step; research/ream250_bom/ream250_bom_row_0046_2AD3__views_2x2.png; https://www.rolling-components.com/chrome-steel-1-3505-100cr6/; https://hartfordtechnologies.com/precision-balls/chrome-steel-balls/"
    cited_fact_or_basis: "The BOM identifies the row as 'axis bearing top' and the CAD/contact sheet shows a 4.95 mm sphere. TIS describes 1.3505 / 100Cr6 as the typical standard rolling-bearing steel for balls, cylindrical rollers, and needle rollers. Hartford Technologies identifies chrome steel balls as 52100 / 100Cr6 / SUJ2 / GCr15. targeted_web_search: searched '2AD3_part_3 axis bearing top material', '2AD3 axis bearing top reAM250 material', 'reAM250 axis bearing top ball material', and 'chrome steel 1.3505 100Cr6 bearing balls'; found no row-specific vendor/material source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because the row is a small spherical bearing element, standard bearing/chrome steel is the most plausible material family."
  uncertainty_notes:
    - "The exact grade, heat treatment, and tolerance class are not proven for this row; stainless or ceramic bearing balls would change the material model, but no row-specific evidence supports those alternatives."
how_to_make:
  summary: "Prepare as a standard precision bearing ball; form bearing-steel wire into a ball blank, harden it, then grind and lap to final diameter and surface finish"
  manufacturing_steps:
    - "Start from bearing-steel wire or rod stock sized near the finished 4.95 mm ball diameter."
    - "Cold-head or otherwise form a near-spherical blank."
    - "Remove flash and deburr the blank."
    - "Heat treat or through-harden if using chrome bearing steel."
    - "Grind, lap, clean, and inspect for diameter, roundness, surface finish, and visible defects."
  source:
    url_or_path: "https://resources.hartfordtechnologies.com/blog/high-quality-precision-ball-manufacturing-a-process-overview; https://resources.hartfordtechnologies.com/blog/the-precision-ball-manufacturing-process; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AD3_part_3.step"
    cited_fact_or_basis: "Hartford describes precision ball manufacturing steps including raw-material inspection, cold heading, flashing, heat treatment, grinding, lapping, cleaning, and visual inspection. The local STEP/preview identifies this row as a single small spherical bearing element. targeted_web_search: searched '2AD3_part_3 axis bearing top manufacturing', 'bearing balls manufacturing process cold heading flashing heat treatment grinding lapping', and '5 mm bearing ball manufacturing process'; found generic precision-ball manufacturing routes but no row-specific factory process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route follows common precision bearing-ball practice because no row-specific production drawing is available."
  uncertainty_notes:
    - "The BOM row gives no tolerance grade, hardness, surface finish, or inspection class, so this is a plausible route rather than a complete manufacturing specification."
kb_implications:
  - "item_granularity: simple_part - Model as reusable standard small bearing-ball hardware rather than a reAM250-specific custom part; capture approximate diameter and probable bearing-steel material in notes."
---

Research result for reAM250 BOM row 46.
