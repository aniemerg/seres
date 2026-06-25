---
row_identity:
  item: "2AF1"
  cad_file: "2AF1_track"
  source_row_number: 57
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/"
function:
  summary: "Track/body of a K+C linear optical glass measuring scale for the reAM250 axis, providing a protected precision position reference over a 520 mm measuring range."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/"
    cited_fact_or_basis: "BOM row 57 identifies item 2AF1 as K+C 'measuring range 520 mm: track'. The manifest maps it to 2AF1_track.step. K+C describes the product family as a linear optical measuring system based on a glass scale read by a read head and used for machine and plant engineering."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM word 'track' is treated as the installed linear scale track/body rather than the separate display electronics."
  uncertainty_notes:
    - "The row CAD contains the long scale body only; the complete commercial scale may also include read head, cable, mounting hardware, and protective angle hardware."
mass:
  value_kg: 0.99
  basis: "Per-unit estimate for quantity 1. FreeCAD measured one solid with volume 365696.325 mm^3 and bounding box about 20.00 x 28.50 x 644.00 mm. Using the local aluminum density constant 2700 kg/m^3 gives 365696.325 mm^3 * 1e-9 m^3/mm^3 * 2700 kg/m^3 = 0.987 kg, rounded to 0.99 kg. The row total is also about 0.99 kg. A row-matched distributor page lists 3.1 kg shipping weight for K+C M5/0500, treated only as a packaged upper-bound sanity check."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AF1_track.step; kb/materials/properties.yaml; https://www.top-maschinen.de/k-c-glasmassstab-m5-500-mm-5-m-verfahrweg-520-mm-810012.html"
    cited_fact_or_basis: "FreeCAD measured CAD volume 365696.325 mm^3 and bbox 20.00 x 28.50 x 644.00 mm. kb/materials/properties.yaml lists aluminum density 2700 kg/m^3. The distributor product page for K+C M5 500 mm / travel 520 mm lists shipping weight 3.1 kg and dimensions near the CAD length. bom_url_route_check: original BOM URL https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/ confirms product family/materials but did not expose a net item mass; a different-domain distributor was used only for row-match and shipping-weight sanity check. targeted_web_search: tried 'site:kuc-maschinen.de K+C Glasmassstaebe Gewicht M5 520 mm', 'K+C Glasmassstaebe Gewicht 520', and 'linear glass scale aluminum housing weight 520 mm K+C M5'; no row-specific net mass source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid volume is treated as a usable per-unit volume proxy for the row item."
    - "The aluminum housing dominates the modeled CAD volume; small glass, seal, cable, and reader components are not split into separate volume fractions."
  uncertainty_notes:
    - "STEP material metadata for this row is only Generic, and no net catalog weight was found; the estimate may miss internal glass/electronics/cable mass or CAD simplification differences."
material:
  primary_material: "aluminum housing with glass scale, elastomer sealing lips, read-head hardware/electronics, cable, metal protective sleeve, and connector"
  source:
    url_or_path: "https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "K+C states the system is based on a glass scale with optical scaling, protected in a robust aluminum housing with sealing lips. Local assembly STEP material extraction for 2AF1_track returned only Generic with density 1000.0, so it does not resolve material."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Exact aluminum grade, glass composition, seal elastomer, connector metal, and cable jacket material are not specified by the BOM-side evidence."
how_to_make:
  summary: "Best current route is procurement as a calibrated K+C M5/0500-style linear glass scale module; a plausible local route would fabricate the aluminum scale housing/profile, install the glass scale, read-head carriage, seals, cable, connector, and protective sleeve, then laser-measure/calibrate the assembly."
  manufacturing_steps:
    - "Procure row-matched K+C M5 500 mm / 520 mm travel linear glass scale where available."
    - "For local manufacture, extrude or machine the long aluminum housing/profile and cut it to the required scale length."
    - "Install the optical glass scale, read-head carriage or interface hardware, sealing lips, cable, DIN-style connector, and protective sleeve."
    - "Perform precision alignment, laser measurement/calibration, sealing, electrical testing, and functional verification before installation."
  source:
    url_or_path: "https://www.kuc-maschinen.de/produkt/linear-glasmassstaebe/; https://www.top-maschinen.de/k-c-glasmassstab-m5-500-mm-5-m-verfahrweg-520-mm-810012.html; research/ream250_bom/ream250_bom_row_0057_2AF1__views_2x2.png"
    cited_fact_or_basis: "K+C describes glass scale optical measurement, aluminum housing, sealing lips, laser measurement/calibration, read-head carriage, 3 m data cable, and connector. The row-matched distributor identifies MPN M5/0500, 500 mm nominal length, 520 mm travel, and a ready-wired scale. CAD preview shows a long narrow profiled rail/scale body. bom_url_route_check: the original BOM URL resolved product-family construction and calibration facts but not the exact MPN; the distributor page was used for the exact 520 mm product identity. targeted_web_search: tried 'K+C Glasmassstab M5 manufacturing aluminum housing glass scale' and found product/construction descriptions, not a detailed factory process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Local manufacturing would require precision metrology and calibration comparable to commercial linear encoder production."
    - "The CAD track profile can be produced by extrusion plus finish machining or by direct machining at low quantity."
  uncertainty_notes:
    - "No source found gives K+C's detailed manufacturing process or calibration fixture design, so the local route is a high-level engineering plan rather than a sourced process recipe."
kb_implications:
  - "item_granularity: complex_module - Treat as a calibrated functional linear encoder/scale complex module for this pass; later KB work should only decompose it after modeling optical scale fabrication, read-head electronics, sealing, cabling, and calibration."
---

