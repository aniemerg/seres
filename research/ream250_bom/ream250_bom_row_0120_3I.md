---
row_identity:
  item: "3I"
  cad_file: "3I_pipe_ISO_K_DN63_320RZS063-176"
  source_row_number: 120
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063"
function:
  summary: "Straight DN 63 ISO-K vacuum full nipple/spool that provides a rigid 176 mm stainless pipe section between ISO-K vacuum flanges in the reAM250 vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3I_pipe_ISO_K_DN63_320RZS063-176.step; research/ream250_bom/ream250_bom_row_0120_3I__views_2x2.png; https://www.vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063176/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 120 identifies item 3I, quantity 7, product family 320RZS063, manufacturer Pfeiffer Vacuum, and CAD file 3I_pipe_ISO_K_DN63_320RZS063-176. The manifest maps the row to the same STEP file. FreeCAD measured one solid with 176.00 mm length and the rendered contact sheet shows a straight cylindrical tube with ISO-K flange lips at both ends. The Pfeiffer Vacuum Online Shop page identifies 320RZS063-176 as a full nipple with DN 63 ISO-K connection flange, length A = 176 mm, and B = 70 mm. official_alternate_route_check: the BOM link is Pfeiffer Vacuum https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches the row-specific 320RZS063-176 product, Global-No. 2000042733, and DN 63 ISO-K full-nipple family."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row-specific CAD suffix -176 selects the 176 mm variant in the 320RZS063 product family."
  uncertainty_notes: []
mass:
  value_kg: 1.401
  basis: "Per-unit mass for one physical full nipple. FreeCAD measured CAD solid volume 174498.270 mm^3, equal to 1.74498270e-4 m^3; using stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml gives 1.401 kg per nipple. BOM quantity is 7, so the row total is about 9.81 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3I_pipe_ISO_K_DN63_320RZS063-176.step; kb/materials/properties.yaml; https://www.vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063176/full-nipple-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD read one solid from the row STEP and measured volume 174498.270 mm^3, surface area 100682.245 mm^2, and bounding box 176.00 mm x 105.13 mm x 105.13 mm. The row-matched Pfeiffer Vacuum Online Shop page identifies 320RZS063-176 as stainless steel 1.4301/304, and kb/materials/properties.yaml gives stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: the BOM link is Pfeiffer Vacuum https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches product 320RZS063-176 and Global-No. 2000042733."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents one physical row item and includes the flanged tube geometry needed for mass estimation."
    - "Pfeiffer's 1.4301/304 material designation maps to the local stainless_steel_304 density constant."
  uncertainty_notes:
    - "Mass is CAD-derived rather than a catalog net-weight value; small deviations are possible if the supplied STEP omits weld details, wall-thickness refinements, or final surface finish."
material:
  primary_material: "Stainless steel 1.4301 / AISI 304."
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063176/full-nipple-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row-matched Pfeiffer Vacuum Online Shop page for 320RZS063-176 states the product category as stainless steel 1.4301/304 and lists materials in contact with media as stainless steel 1.4301 (AISI 304). Local assembly STEP material extraction for 3I_pipe_ISO_K_DN63_320RZS063-176 returned only Generic with density 1000.0, which is placeholder metadata and was not used to resolve material. official_alternate_route_check: the BOM link is Pfeiffer Vacuum https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063; the accessible vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop and matches the row-specific product 320RZS063-176."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Prepare as Pfeiffer Vacuum 320RZS063-176 full nipple, or locally fabricate an equivalent DN 63 ISO-K stainless spool from 304-series tube and ISO-K flange geometry, then clean, inspect, and leak-test before installation"
  manufacturing_steps:
    - "Receiving route: verify DN 63 ISO-K interfaces, 176 mm length, clean sealing faces, bore clearance, and absence of flange or tube damage."
    - "Manufacturing route: fabricate from stainless 304 tube and ISO-K flange profiles or preformed ISO flanges, welding or machining the straight spool geometry shown by the CAD."
    - "Finish route: deburr, clean/passivate for vacuum service, inspect sealing faces and dimensions, and helium leak-test before installation with the separate centering ring/seal and clamp hardware."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0120_3I__views_2x2.png; https://www.vacuum-shop.com/shop/en_US/category/2073062/product/320rzs063176/full-nipple-stainless-steel-1-4301-304.html; https://www.lesker.com/newweb/flanges/fittings_iso_nipples.cfm?pgid=full"
    cited_fact_or_basis: "BOM row 120 provides the Pfeiffer Vacuum product route and the CAD preview shows a one-piece straight flanged pipe. The Pfeiffer Vacuum Online Shop identifies the row-matched DN 63 ISO-K stainless full-nipple product and dimensions. A separate ISO nipple vendor describes ISO nipples/spools as fabricated from 304L stainless steel tubing and ISO flanges. bom_url_route_check: the BOM-provided Pfeiffer route and official shop route resolve product identity, dimensions, and material but do not state a local manufacturing process; the independent ISO-nipple source was used only to sanity-check the inferred tube-plus-flange fabrication route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Cleaning/passivation, dimensional inspection, and leak testing are included as necessary vacuum-service controls but are not specified on the row-matched product page."
  uncertainty_notes:
    - "Targeted_web_search: searched 'ISO-K full nipple stainless steel manufacturing tube flange welding' and 'vacuum flange nipple stainless steel manufacturing welded tube flanges'; results found general ISO nipple fabrication evidence but no Pfeiffer row-specific manufacturing process."
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable standard DN 63 ISO-K stainless vacuum nipple/spool; preserve the 176 mm length as a variant parameter or BOM note rather than creating a machine-specific custom assembly."
---
