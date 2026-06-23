---
row_identity:
  item: "8C2"
  cad_file: "8C2_end_piece"
  source_row_number: 209
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0500"
function:
  summary: "One DN 40 ISO-KF stainless end piece/flange for the Pfeiffer flexible corrugated vacuum hose, providing the clamp and seal interface at a hose end."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8C2_end_piece.step; https://vacuum-shop.com/2074124/downloads/datasheets/Datasheet_120SWG040-0500_en.pdf; https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html"
    cited_fact_or_basis: "BOM row 209 identifies item 8C2 as quantity 2 of 8C2_end_piece for Pfeiffer Vacuum 120SWG040-0500 end piece, with 120SWG040-0250 flexible pipe also named in the row. FreeCAD measured one solid and the preview shows a short annular flanged end piece. The Pfeiffer shop/datasheet route identifies the product family as DN 40 ISO-KF corrugated flexible hose with flange connection length 15 mm, B dimension 41 mm, and C dimension 52 mm. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0500; the accessible alternate route https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html is branded/copyrighted Pfeiffer Vacuum and lists the same 120SWG040-0500 order number and DN 40 ISO-KF family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row's two instances represent the two physical hose end pieces rather than two complete hose assemblies."
  uncertainty_notes:
    - "The CAD is the end-piece geometry only, so hose bellows function is referenced only as the mating assembly context."
mass:
  value_kg: 0.063
  basis: "Per-unit mass for one end piece: FreeCAD volume 7852.167 mm^3 = 7.852167e-6 m^3 multiplied by local stainless_steel_1_4301 density 8030 kg/m^3 gives 0.0631 kg. BOM quantity is 2, so the row total is about 0.126 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8C2_end_piece.step; kb/materials/properties.yaml; https://vacuum-shop.com/2074124/downloads/datasheets/Datasheet_120SWG040-0500_en.pdf"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 7852.167 mm^3, area 8066.728 mm^2, and bounding box 18.75 x 59.53 x 59.53 mm for 8C2_end_piece. The Pfeiffer datasheet states the flange material is stainless steel 1.4301/304. kb/materials/properties.yaml lists stainless_steel_1_4301 density as 8030 kg/m^3. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0500; the vacuum-shop datasheet is a Pfeiffer Vacuum route for the same 120SWG040-0500 DN 40 ISO-KF product family and provides the flange material needed for the CAD-volume calculation."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents one physical end piece without omitted internal cavities or hidden subparts."
    - "Stainless steel 1.4301/304 density from the local material table is appropriate for the end-piece CAD solid."
  uncertainty_notes:
    - "Catalog mass for the separate end piece was not exposed, so the estimate depends on CAD volume fidelity."
material:
  primary_material: "stainless steel 1.4301/304 end piece/flange; mating hose family uses 316L stainless bellows"
  source:
    url_or_path: "https://vacuum-shop.com/2074124/downloads/datasheets/Datasheet_120SWG040-0500_en.pdf; https://vacuum-shop.com/2074220/downloads/datasheets/Datasheet_120SWG040-0250_en.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Pfeiffer datasheets for 120SWG040-0500 and 120SWG040-0250 state flange material as stainless steel 1.4301/304 and bellows material as 316L. Local assembly STEP material extraction for 8C2_end_piece returned only Generic with density 1000.0, which is placeholder and was not used as material evidence. official_alternate_route_check: original BOM URL was https://www.pfeiffer-vacuum.com/global/de/shop/products/120SWG040_0500; the vacuum-shop datasheet route is an official Pfeiffer Vacuum online-shop/download route matching the same 120SWG040-0500 row family and the related 120SWG040-0250 row text."
    evidence_basis: "bom_provided"
  assumptions:
    - "Because the row item is the visible end piece rather than the corrugated hose body, the flange/end-piece stainless 1.4301/304 material is the primary material."
  uncertainty_notes:
    - "The exact weld filler or surface finish is not specified in the accessible row evidence."
how_to_make:
  summary: "Near-term route is procurement as part of the Pfeiffer DN 40 ISO-KF corrugated hose family; a local route would fabricate a stainless ISO-KF end flange/end piece and weld it to the stainless bellows hose assembly."
  manufacturing_steps:
    - "Procure row-matched Pfeiffer 120SWG040 hose/end-piece component for the current BOM model."
    - "For local manufacture, cut/form or machine the 1.4301/304 stainless end-flange profile to the DN 40 ISO-KF interface geometry."
    - "Join the end piece to the 316L corrugated bellows by vacuum-compatible welding, then clean and leak-test the hose assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/8C2_end_piece.step; https://vacuum-shop.com/shop/en_US/category/2072984/iso-kf-corrugated-hose-flexible-annealed.html; https://www.pfeiffervacuum.com/global/en/products/components-accessories/vacuum-components/"
    cited_fact_or_basis: "The Pfeiffer shop route identifies this as a DN 40 ISO-KF corrugated hose family with stainless flange/bellows materials and pressure/temperature service data; the CAD preview shows a one-piece annular flanged end piece. Pfeiffer's vacuum-components page describes high-quality vacuum components, flange and piping parts, flexible vacuum hoses, and leak-tested vacuum components. targeted_web_search: searched 'Pfeiffer Vacuum 120SWG040-0500 end piece flexible pipe material weight', '120SWG040-0500 Pfeiffer flexible pipe end piece', and 'Pfeiffer 120SWG040-0250 flexible pipe end piece'; results resolved the row-matched product family/materials but did not state a factory process for the separate end piece, so the detailed local fabrication steps are inferred."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Local self-manufacture would use standard vacuum-hardware practice for stainless ISO-KF hose ends when vendor procurement is not allowed."
  uncertainty_notes:
    - "The source evidence does not provide the exact Pfeiffer factory process, tooling, weld specification, or acceptance leak-rate for this specific end piece."
kb_implications:
  - "item_granularity: simple_part - Model as one reusable DN 40 ISO-KF stainless hose end/flange component; keep the full flexible hose as a separate assembly or purchased hose row rather than decomposing this end piece into subparts."
---

Structured research result for reAM250 BOM row 209.
