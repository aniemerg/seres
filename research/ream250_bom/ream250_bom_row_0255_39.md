---
row_identity:
  item: "39"
  cad_file: "39_pipe_ISO_K_DN63"
  source_row_number: 255
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS063"
function:
  summary: "Straight DN 63 ISO-K vacuum piping nipple used to bridge two ISO-K vacuum components while preserving a sealable high-vacuum flow path."
  source:
    url_or_path: "https://www.shop.buschgroup.com/products/320RZS063; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/39_pipe_ISO_K_DN63.step; research/ream250_bom/ream250_bom_row_0255_39__views_2x2.png"
    cited_fact_or_basis: "official_alternate_route_check: the BOM Link URL is the Pfeiffer product path for 320RZS063; direct fetch of that domain was blocked, but the official Busch Group shop route for the same product code resolves to 'Full nipple, stainless steel 304/1.4301, DN 63 ISO-K', category Piping components, connecting flange DN 63 ISO-K, and product-table name ISO-K Full Nipple. The row STEP and preview show a straight cylindrical pipe with ISO-K-style flanges at both ends."
    evidence_basis: "bom_provided"
  assumptions:
    - "Treat the BOM product code and supplied CAD as the same row identity even though the CAD length is longer than the official catalog dimension exposed by the shop route."
  uncertainty_notes:
    - "The official shop route lists length 88 mm, while the row CAD bounding box is about 214 mm long; function as a straight DN 63 ISO-K vacuum connector is still consistent, but exact variant length should be checked before detailed layout reuse."
mass:
  value_kg: 1.62
  basis: "Per unit for quantity 1. FreeCAD measured one solid with volume 202064.851 mm^3. Converted to 0.000202064851 m^3 and multiplied by the local stainless_steel_304 density constant 8030 kg/m^3 from kb/materials/properties.yaml, giving 1.623 kg, rounded to 1.62 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/39_pipe_ISO_K_DN63.step; kb/materials/properties.yaml; https://www.shop.buschgroup.com/products/320RZS063"
    cited_fact_or_basis: "FreeCAD measured the row STEP as 1 solid, volume 202064.851 mm^3, area 118096.093 mm^2, and bounding box about 214.00 x 105.13 x 105.13 mm. official_alternate_route_check: the BOM Link URL points to Pfeiffer product 320RZS063; direct fetch of that domain was blocked, but the official Busch Group shop route for the same product code resolves the row-matched product and identifies stainless steel 304/1.4301. kb/materials/properties.yaml lists stainless_steel_304 density 8030 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume represents one physical BOM-row item."
    - "Use the local stainless_steel_304 density as an adequate density constant for stainless steel 304/1.4301."
  uncertainty_notes:
    - "If the longer CAD geometry is a machine-specific stretched variant of the catalog full nipple, this CAD-derived mass is preferable for the reAM250 row but may not match the catalog part mass."
material:
  primary_material: "stainless steel 304/1.4301"
  source:
    url_or_path: "https://www.shop.buschgroup.com/products/320RZS063; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "official_alternate_route_check: the BOM Link URL points to Pfeiffer 320RZS063, and the official Busch Group shop route for the same product code names the product 'Full nipple, stainless steel 304/1.4301, DN 63 ISO-K' and lists media-contact material as Stainless steel 1.4301 (AISI 304). Local assembly STEP material extraction for 39_pipe_ISO_K_DN63 returned only material 'Generic' with density 1000.0, so it was not used as material evidence."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "No row-specific non-placeholder STEP material was available; material comes from the official product-code route rather than embedded CAD metadata."
how_to_make:
  summary: "Prepare as Pfeiffer/Busch product 320RZS063 or model locally as a stainless 304/1.4301 ISO-K full nipple made from tube and two ISO-K flange ends, followed by vacuum cleaning and leak/fit inspection"
  manufacturing_steps:
    - "Cut stainless 304/1.4301 tube to the required row length and prepare two ISO-K flange ends."
    - "Join the tube/flange geometry by welding or equivalent vacuum-compatible fabrication, then machine or finish the sealing and clamp-interface surfaces."
    - "Clean for vacuum service and verify dimensions, flange fit, and leak-tightness before installation."
  source:
    url_or_path: "https://www.shop.buschgroup.com/products/320RZS063; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/39_pipe_ISO_K_DN63.step"
    cited_fact_or_basis: "The official alternate route for BOM product 320RZS063 identifies a purchasable DN 63 ISO-K stainless full nipple. The supplied CAD shows a straight tube-like body with flanged ends. The local fabrication sequence is inferred from that geometry and material. targeted_web_search: searched 'Pfeiffer 320RZS063 manufacturing welded tube full nipple' and found product/spec pages but no row-specific manufacturing process disclosure."
    evidence_basis: "engineering_hypothesis"
  assumptions: []
  uncertainty_notes:
    - "Exact flange forming, weld prep, surface finish, and leak-test acceptance criteria are not specified by the row evidence."
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable ISO-K stainless vacuum pipe/full-nipple part with size and length variants rather than a calibrated purchased module."
---
