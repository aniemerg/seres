---
row_identity:
  item: "86"
  cad_file: "86_T_pipe_ISO_KF_DN40"
  source_row_number: 282
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/170RTS040"
function:
  summary: "DN 40 ISO-KF tee fitting that branches or joins three equal-size vacuum lines in the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.pfeiffer-vacuum.com/global/de/shop/products/170RTS040; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/86_T_pipe_ISO_KF_DN40.step; research/ream250_bom/ream250_bom_row_0282_86__views_2x2.png"
    cited_fact_or_basis: "BOM row 282 and the manifest identify item 86 as 86_T_pipe_ISO_KF_DN40, quantity 1, product 170RTS040, manufacturer Pfeiffer Vacuum. The BOM-provided Pfeiffer URL identifies article number 170RTS040 as a tee, stainless steel 1.4404/316L, DN 40 ISO-KF, under vacuum chamber piping components. FreeCAD measured one solid with bounding box about 130.00 x 94.77 x 59.53 mm; the rendered contact sheet shows a three-port fitting with ISO-KF flange lips."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.513
  basis: "Per-unit planning mass for one tee. BOM quantity is 1, so the row total is also about 0.513 kg. FreeCAD volume is about 64,114.012 mm3 = 0.000064114 m3; multiplying by the local stainless_steel density constant of 8000 kg/m3 gives about 0.5129 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/86_T_pipe_ISO_KF_DN40.step; https://www.pfeiffer-vacuum.com/global/de/shop/products/170RTS040; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume about 64,114.012 mm3, surface area about 49,670.033 mm2, and bounding box about 130.00 x 94.77 x 59.53 mm. The BOM-provided Pfeiffer product page identifies article number 170RTS040 as stainless steel 1.4404/316L. kb/materials/properties.yaml lists stainless_steel density as 8000 kg/m3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP solid volume represents the physical metal volume of one tee closely enough for row-level planning."
    - "The local generic stainless_steel density constant is used for 316L/1.4404 because the local density table has no separate 316L entry."
  uncertainty_notes:
    - "Small mass error is possible from CAD export simplification and from using a generic stainless density instead of an alloy-specific 316L density."
material:
  primary_material: "Stainless steel 316L / EN 1.4404."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.pfeiffer-vacuum.com/global/de/shop/products/170RTS040; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "BOM row 282 gives product 170RTS040 and manufacturer Pfeiffer Vacuum. The BOM-provided Pfeiffer product page identifies article number 170RTS040 as a tee made from stainless steel 1.4404/316L. Local assembly STEP material extraction for product 86_T_pipe_ISO_KF_DN40 returned only Generic material with density 1000.0, so it was not used as material evidence."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "For local manufacturing planning, make as a stainless ISO-KF tee: form or fabricate the three-port 316L tube body, add ISO-KF flange ends, finish the sealing faces, clean for vacuum service, and leak-test."
  manufacturing_steps:
    - "Cut or form 316L stainless tube sections for a DN 40 tee body, using pulled-port or fitted-branch geometry compatible with the CAD tee shape."
    - "Attach or form the three DN 40 ISO-KF flange lips and machine/finish the sealing faces and outside clamp features."
    - "Deburr, clean, passivate or otherwise finish for vacuum service, then dimensionally inspect and leak-test the tee before installation with separate centering rings, seals, and clamps."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/170RTS040; https://www.n-c.com/vacuum-flanges-fittings/tees/iso-kf-nw; research/ream250_bom/ream250_bom_row_0282_86__views_2x2.png"
    cited_fact_or_basis: "The BOM-provided Pfeiffer page identifies the row item as a finished DN 40 ISO-KF stainless 316L/1.4404 tee. The CAD contact sheet shows a three-flange tee fitting. targeted_web_search: queries tried were 'Pfeiffer 170RTS040 Tee stainless steel 316L DN 40 ISO-KF manufacturing welded tube flange' and 'ISO-KF stainless steel tee 316L welded tube flange vacuum fitting manufacturing'; a Pfeiffer Vacuum+Fab Solutions ISO-KF tee family page says ISO-KF tee fittings are produced from stainless pulled-port tubing and ISO-KF flanges, but it does not state the exact row-specific shop process for 170RTS040."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row represents the tee fitting only; ISO-KF clamps, centering rings, and elastomer or metal seals are separate hardware rows."
    - "A future local route can approximate the commercial fitting by fabricating a 316L stainless tee body and KF flange geometry, followed by vacuum-service cleaning and leak testing."
  uncertainty_notes:
    - "The precise commercial forming, welding, finishing, and inspection sequence for Pfeiffer article 170RTS040 is not specified by the BOM row or product page."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable ISO-KF stainless tee fitting; keep clamps, centering rings, and seals as separate hardware or consumable rows rather than folding them into this tee."
---
