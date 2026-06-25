---
row_identity:
  item: "35"
  cad_file: "35_clamping_ring_ISO_KF_DN50_120BSR050"
  source_row_number: 251
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR050"
function:
  summary: "DN 50 ISO-KF clamping ring used to fasten an ISO-KF vacuum flange joint around an elastomer seal in the reAM250 gas/vacuum plumbing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/35_clamping_ring_ISO_KF_DN50_120BSR050.step; research/ream250_bom/ream250_bom_row_0251_35__views_2x2.png; https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR050; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr050/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "BOM row 251 identifies item 35 as product 120BSR050 by Pfeiffer Vacuum, quantity 4, and maps it to 35_clamping_ring_ISO_KF_DN50_120BSR050.step. The rendered CAD preview shows a hinged/segmented clamp ring with a wingnut screw feature. The Pfeiffer online-shop route identifies 120BSR050 as a clamping ring for elastomer seals with DN 50 ISO-KF connection flange. official_alternate_route_check: the original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR050; search/opening the row product resolves to the Pfeiffer Vacuum Online Shop page on vacuum-shop.com for the same order number 120BSR050 and global number 2000048700."
    evidence_basis: "bom_provided"
  assumptions:
    - "The clamping ring is used with the neighboring ISO-KF DN50 seal/flange components in the same reAM250 subsystem rather than as a standalone load-bearing clamp."
  uncertainty_notes: []
mass:
  value_kg: 0.185
  basis: "FreeCAD volume 23047.640 mm^3 equals 0.0000230476 m^3. Using stainless_steel_304 density 8030 kg/m^3 from kb/materials/properties.yaml gives 0.185 kg per clamping ring. BOM quantity is 4, so the row total is about 0.740 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/35_clamping_ring_ISO_KF_DN50_120BSR050.step; kb/materials/properties.yaml; https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr050/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 23047.640 mm^3, surface area 11116.609 mm^2, and bounding box 115.35 x 48.78 x 19.00 mm. The Pfeiffer online-shop route states material stainless steel 1.4301/304 and DN 50 ISO-KF dimensions A 115 mm, B 90 mm, C 19 mm, consistent with the CAD envelope. The local density table lists stainless_steel_304 density 8030 kg/m^3. official_alternate_route_check: the original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR050; the vacuum-shop.com Pfeiffer online-shop page matches order number 120BSR050 and global number 2000048700."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP solid is treated as the physical-volume proxy for one purchased clamping ring."
    - "Local stainless_steel_304 density is used as the calculation constant for the sourced 1.4301/304 material."
  uncertainty_notes:
    - "The STEP assembly metadata itself reports only placeholder material Generic, so mass depends on the row-matched vendor material and CAD volume rather than embedded material metadata."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr050/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Pfeiffer online-shop route for order number 120BSR050 states material stainless steel 1.4301/304. Local assembly STEP material extraction for the row returned Generic with density 1000.0, which is placeholder-only and not used as material evidence. official_alternate_route_check: the original BOM URL is https://www.pfeiffer-vacuum.com/global/de/shop/products/120BSR050; the vacuum-shop.com Pfeiffer online-shop page matches the same product number 120BSR050 and global number 2000048700."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Fabricate the stainless clamp halves and screw/wingnut hardware as a simple vacuum fastener"
  manufacturing_steps:
    - "For local fabrication, machine or precision-cast the two curved stainless clamp halves to the ISO-KF DN50 profile, including hinge/lug and screw-bearing features."
    - "Drill, deburr, and finish the hinge and tightening-lug interfaces; passivate or clean the stainless surfaces for vacuum service."
    - "Assemble the hinge pin, tightening screw, and wingnut or equivalent fastener, then verify fit on DN50 ISO-KF flanges with an elastomer seal at the specified 2 Nm wingnut torque."
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2072892/product/120bsr050/clamping-ring-for-elastomer-seals-stainless-steel-1-4301-304.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/35_clamping_ring_ISO_KF_DN50_120BSR050.step; research/ream250_bom/ream250_bom_row_0251_35__views_2x2.png"
    cited_fact_or_basis: "The Pfeiffer online-shop route identifies 120BSR050 as a DN 50 ISO-KF stainless 1.4301/304 clamping ring for elastomer seals and states 2 Nm wingnut torque. CAD and preview show the curved clamp body and wingnut/screw feature. targeted_web_search: searched \"Pfeiffer Vacuum 120BSR050 clamping ring ISO-KF DN50 material weight\" and \"site:pfeiffer-vacuum.com 120BSR050 clamping ring\" results resolved product identity, material, dimensions, and procurement route but did not provide a manufacturing process drawing."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the CAD geometry and standard clamp function"
    - "The screw/wingnut hardware is treated as part of the external clamp row because the CAD and vendor product identify one complete clamping ring item"
  uncertainty_notes:
    - "No row-specific tolerance, heat-treatment, surface-finish, or hinge/screw subcomponent specification was found, so local manufacturing details remain approximate."
kb_implications:
  - "item_granularity: simple_part - model as reusable ISO-KF DN50 stainless clamping-ring hardware, not as raw stock or a calibrated purchased module; the BOM quantity should instantiate four units."
---

Research result for reAM250 BOM row 251.
