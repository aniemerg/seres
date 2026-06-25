---
row_identity:
  item: "3R1"
  cad_file: "3R1_clamp_ISO_K_DN63_350BPD100"
  source_row_number: 143
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100"
function:
  summary: "Pfeiffer Vacuum 350BPD100 ISO-K single claw clamp for fastening a DN 63 to DN 100 ISO-K flange to a base plate with an O-ring groove; the BOM row quantity is 4."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "The BOM and manifest identify row 143 item 3R1 as quantity 4 of 3R1_clamp_ISO_K_DN63_350BPD100, product 350BPD100, manufacturer Pfeiffer Vacuum. The Pfeiffer Vacuum Online Shop page identifies 350BPD100 as a claw clamp for a base plate with sealing groove, suitable for metal and elastomer seals, for installing an ISO-K flange on a base plate with O-ring groove, with connection flange DN 63-DN 100 ISO-K. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 led to the Pfeiffer-branded vacuum-shop.com product page; that page carries Pfeiffer Vacuum Online Shop branding, lists the same product ID 350BPD100, links a 350BPD100 data sheet and STEP file, and matches the row manufacturer/product."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.0323
  basis: "FreeCAD measured CAD volume 4119.697 mm^3 for one row part. Using steel density 7850 kg/m^3 from kb/materials/properties.yaml gives 4119.697 mm^3 * 1e-9 m^3/mm^3 * 7850 kg/m^3 = 0.03234 kg, rounded to 0.0323 kg per unit. BOM quantity is 4, so the row total is about 0.129 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3R1_clamp_ISO_K_DN63_350BPD100.step; kb/materials/properties.yaml; https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 4119.697 mm^3, area 2345.582 mm^2, and bounding box 24.00 x 18.60 x 15.00 mm. The Pfeiffer Vacuum Online Shop page identifies the material as zinc-plated steel. The local material density table lists steel density 7850 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 led to the Pfeiffer-branded vacuum-shop.com product page; that page carries Pfeiffer Vacuum Online Shop branding, lists the same product ID 350BPD100, links a 350BPD100 data sheet and STEP file, and matches the row manufacturer/product."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical solid volume of one claw clamp."
    - "The thin zinc plating is neglected in the density calculation because the vendor identifies the base material as steel and the plating mass is negligible at this planning precision."
  uncertainty_notes:
    - "No catalog weight was found or needed for this estimate, but the result depends on the supplied CAD solid matching the purchased clamp without omitted small features or simplifications."
material:
  primary_material: "zinc-plated steel"
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "The Pfeiffer Vacuum Online Shop page title and technical table identify 350BPD100 as a claw clamp made from zinc-plated steel. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 led to the Pfeiffer-branded vacuum-shop.com product page; that page carries Pfeiffer Vacuum Online Shop branding, lists the same product ID 350BPD100, links a 350BPD100 data sheet and STEP file, and matches the row manufacturer/product."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The assembly STEP material extractor returned only Generic material at 1000 kg/m^3, so the vendor material is the useful row-specific material evidence."
how_to_make:
  summary: "Model as standard Pfeiffer ISO-K zinc-plated steel vacuum fastening hardware: prepare the finished 350BPD100 claw clamp, or manufacture locally only if the reusable standard hardware path is later modeled"
  manufacturing_steps:
    - "If local substitution is needed later, make a small steel clamp blank matching the CAD claw geometry and M8 interface."
    - "Machine the bearing faces, central clearance/hole feature, side reliefs, and clamp shoulders visible in the CAD preview."
    - "Deburr, zinc plate, and inspect the DN 63-DN 100 ISO-K flange-contact geometry."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0143_3R1__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3R1_clamp_ISO_K_DN63_350BPD100.step; https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "The rendered CAD contact sheet shows a compact claw clamp block with a central round clearance/hole feature, stepped side faces, and wedge-like clamp shoulders. FreeCAD measured bounding box 24.00 x 18.60 x 15.00 mm. The Pfeiffer Vacuum Online Shop page identifies 350BPD100 as a zinc-plated steel claw clamp, lists M8 and DN 63-DN 100 ISO-K dimensions, and offers the finished part and its STEP download. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 led to the Pfeiffer-branded vacuum-shop.com product page; that page carries Pfeiffer Vacuum Online Shop branding, lists the same product ID 350BPD100, links a 350BPD100 data sheet and STEP file, and matches the row manufacturer/product."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Vacuum flange fastening requires clean, burr-free bearing faces and dimensionally consistent clamp shoulders."
  uncertainty_notes:
    - "The row evidence resolves product identity, geometry, material, and interface, but not Pfeiffer's actual production method, coating specification, or tolerances."
    - "targeted_web_search: checked the BOM-provided Pfeiffer URL, the row-matched Pfeiffer Vacuum Online Shop page for 350BPD100, and searched for 350BPD100 manufacturing, material, datasheet, M8, DN 63 DN 100 ISO-K claw clamp, and zinc-plated steel facts; found row-matched product/material/interface facts but no row-specific production-process specification."
kb_implications:
  - "item_granularity: simple_part - standard ISO-K zinc-plated steel vacuum claw clamp hardware; later KB modeling should map it to reusable standard clamp/fastener hardware rather than a reAM250-specific purchased module."
---

# reAM250 BOM Row 143 - 3R1

Research result for the leased reAM250 BOM row.
