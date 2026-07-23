---
row_identity:
  item: "3Q4"
  cad_file: "3Q4_clamp_ISO_K_DN100_320BKL250"
  source_row_number: 141
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320BKL250"
function:
  summary: "Pfeiffer Vacuum 320BKL250 ISO-K double-claw bracket screw used to fasten DN 63 to DN 250 ISO-K vacuum flange joints; the BOM row quantity is 8."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://vacuum-shop.com/shop/en_US/category/2073019/product/320bkl250/bracket-screw-stainless-steel-1-4401-316.html"
    cited_fact_or_basis: "The BOM and manifest identify row 141 item 3Q4 as quantity 8 of 3Q4_clamp_ISO_K_DN100_320BKL250, product 320BKL250, manufacturer Pfeiffer Vacuum. The Pfeiffer Vacuum Online Shop page identifies 320BKL250 as a bracket screw in the ISO-K double claw clamp category, with connection flange DN 63-DN 250 ISO-K and torque 12-16 Nm. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320BKL250 returned a Pfeiffer wrapper page; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum navigation/product data, links the same 320BKL250 data sheet and STEP file, and matches the row manufacturer and product ID."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.0676
  basis: "FreeCAD measured CAD volume 8445.202 mm^3 for one row part. Using stainless_steel density 8000 kg/m^3 from kb/materials/properties.yaml gives 8445.202 mm^3 * 1e-9 m^3/mm^3 * 8000 kg/m^3 = 0.06756 kg, rounded to 0.0676 kg per unit. BOM quantity is 8, so the row total is about 0.541 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q4_clamp_ISO_K_DN100_320BKL250.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073019/product/320bkl250/bracket-screw-stainless-steel-1-4401-316.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 8445.202 mm^3, area 3167.313 mm^2, and bounding box 61.50 x 23.06 x 14.95 mm. The Pfeiffer Vacuum Online Shop page identifies 320BKL250 as stainless steel 1.4401/316 with media-contact material stainless steel 1.4404/AISI 316L. The local material density table lists stainless_steel density 8000 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320BKL250 returned a Pfeiffer wrapper page; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, links the same 320BKL250 data sheet and STEP file, and matches the row manufacturer and product ID."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical solid volume of one bracket screw/clamp."
    - "The local stainless_steel density value is used as the calculation constant for the 1.4401/316 and 1.4404/316L stainless family."
  uncertainty_notes:
    - "No catalog weight was needed for the estimate, but the result depends on the supplied CAD solid matching the purchased part without omitted small features or simplifications."
material:
  primary_material: "stainless steel 1.4401/316 bracket screw; media-contact material stainless steel 1.4404/AISI 316L"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073019/product/320bkl250/bracket-screw-stainless-steel-1-4401-316.html"
    cited_fact_or_basis: "The Pfeiffer Vacuum Online Shop page title names the product as a bracket screw, stainless steel 1.4401/316, and its technical table lists materials in contact with media as stainless steel 1.4404 (AISI 316L). official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320BKL250 returned a Pfeiffer wrapper page; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, links the same 320BKL250 data sheet and STEP file, and matches the row manufacturer and product ID."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The vendor page distinguishes the title material 1.4401/316 from the media-contact material 1.4404/316L; downstream KB modeling can usually use the stainless steel/316-family unless grade-specific corrosion behavior matters."
how_to_make:
  summary: "Model as a small stainless ISO-K vacuum fastening clamp/bracket screw: prepare as standard Pfeiffer vacuum hardware, or locally manufacture from stainless stock by machining the claw block, forming/threading the M10 screw feature, deburring/passivating, and inspecting torque-bearing and flange-contact surfaces"
  manufacturing_steps:
    - "Cut stainless steel bar or near-net stock for the clamp body and screw-form geometry."
    - "CNC mill the claw faces, shoulders, and stepped clamp block visible in the CAD preview."
    - "Turn and thread the cylindrical M10 screw feature identified by the vendor table."
    - "Deburr, clean, and passivate for vacuum-compatible stainless hardware."
    - "Inspect flange-contact geometry and torque-bearing surfaces for DN 63-DN 250 ISO-K use."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0141_3Q4__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q4_clamp_ISO_K_DN100_320BKL250.step; https://vacuum-shop.com/shop/en_US/category/2073019/product/320bkl250/bracket-screw-stainless-steel-1-4401-316.html"
    cited_fact_or_basis: "The rendered CAD contact sheet shows a compact claw-like clamp block with a cylindrical screw/shaft feature. FreeCAD measured bounding box 61.50 x 23.06 x 14.95 mm. The Pfeiffer Vacuum Online Shop page lists M10, torque 12-16 Nm, DN 63-DN 250 ISO-K use, and stainless steel material. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320BKL250 returned a Pfeiffer wrapper page; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, links the same 320BKL250 data sheet and STEP file, and matches the row manufacturer and product ID."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from stainless material, the vendor-listed M10 fastening interface, and the visible machined clamp geometry."
    - "Vacuum service requires clean, burr-free stainless bearing and threaded surfaces."
  uncertainty_notes:
    - "The row evidence resolves product identity, geometry, material, and interface, but not Pfeiffer's actual production process, heat treatment, or surface finish specification."
    - "Targeted_web_search: checked the BOM-provided Pfeiffer URL, the row-matched Pfeiffer Vacuum Online Shop page for 320BKL250, and searched local/page text for 320BKL250 manufacturing, datasheet, material, M10, and ISO-K clamp facts; found row-matched product/material/interface facts but no row-specific manufacturing process specification."
kb_implications:
  - "item_granularity: simple_part - standard ISO-K stainless vacuum fastening hardware with one main clamp/screw geometry; later KB modeling should map it to reusable stainless ISO-K clamp/fastener hardware rather than a machine-specific purchased module."
---

# reAM250 BOM Row 141 - 3Q4

Research result for the leased reAM250 BOM row.
