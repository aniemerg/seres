---
row_identity:
  item: "3Q1"
  cad_file: "3Q1_pipe_ISO_K_DN100_320RZS100"
  source_row_number: 138
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS100"
function:
  summary: "Pfeiffer Vacuum 320RZS100 ISO-K full nipple, DN 100 ISO-K, used as a straight vacuum piping component between ISO-K flange connections."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html; research/ream250_bom/ream250_bom_row_0138_3Q1__views_2x2.png"
    cited_fact_or_basis: "The BOM row identifies Pfeiffer Vacuum product 320RZS100. The official shop route lists 320RZS100 under ISO-K Full Nipple, connection flange DN 100 ISO-K, dimensions A 108 mm and B 102 mm. The rendered CAD preview shows a straight cylindrical pipe/fitting with ISO-K flange lips at both ends. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS100 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 320RZS100."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 1.55
  basis: "FreeCAD measured CAD volume 192923.105 mm^3 for one full nipple. Converting to 0.000192923105 m^3 and multiplying by stainless_steel_1_4301 density 8030 kg/m^3 from kb/materials/properties.yaml gives 1.549 kg, rounded to 1.55 kg. BOM quantity is 1, so the row total is also about 1.55 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q1_pipe_ISO_K_DN100_320RZS100.step; kb/materials/properties.yaml; https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 192923.105 mm^3, area 100992.531 mm^2, and bounding box 108.00 x 143.02 x 143.02 mm. The official shop route identifies 320RZS100 as stainless steel 1.4301/304. The local material density table lists stainless_steel_1_4301 density 8030 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS100 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 320RZS100."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical solid volume for one purchased full nipple."
    - "The product's stated stainless steel 1.4301/304 material is mapped to the local stainless_steel_1_4301 density constant."
  uncertainty_notes:
    - "No row-specific catalog weight was found on the checked product route or targeted searches, so this is a CAD-derived mass estimate rather than a vendor-stated weight."
material:
  primary_material: "stainless steel 1.4301/304"
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html"
    cited_fact_or_basis: "The official shop route lists ISO-K Full Nipple subcategory/material as stainless steel 1.4301/304 and includes 320RZS100 in that material table. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/320RZS100 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 320RZS100."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The assembly STEP metadata returned only Generic material with density 1000.0, so material is taken from the row-matched official shop route rather than local STEP metadata."
how_to_make:
  summary: "Procure as a standard Pfeiffer Vacuum DN 100 ISO-K stainless full nipple. A plausible local route is to make it from 1.4301/304 stainless tube and ISO-K flange geometry, then weld, clean, and helium leak test it for vacuum service."
  manufacturing_steps:
    - "Cut stainless steel 1.4301/304 tube or rolled tube stock to the required 108 mm nominal length."
    - "Form or machine DN 100 ISO-K flange lips/rings with the required sealing interface at both ends."
    - "TIG weld or otherwise join the flange features to the tube body, then deburr and clean all vacuum-wetted surfaces."
    - "Inspect ISO-K interface dimensions and perform vacuum leak testing before installation."
  source:
    url_or_path: "https://vacuum-shop.com/shop/en_US/category/2073061/iso-k-full-nipple.html; https://www.pfeiffervacuum.com/global/en/products/components-accessories/vacuum-components/; research/ream250_bom/ream250_bom_row_0138_3Q1__views_2x2.png"
    cited_fact_or_basis: "The row-matched official shop route identifies 320RZS100 as a DN 100 ISO-K full nipple in stainless steel 1.4301/304 with A 108 mm and B 102 mm dimensions. Pfeiffer's vacuum components page states piping components provide stable secure pathways for volume flows, flanges join and seal vacuum-system parts, and components undergo helium leak testing. The rendered CAD contact sheet shows a straight cylindrical nipple with flange lips at both ends. targeted_web_search: searched \"320RZS100 weight\", \"320RZS100 mass\", \"320RZS100 datasheet manufacturing\", and \"Pfeiffer 320RZS100 full nipple material weight\"; found row-matched function, material, and dimensions but no row-specific manufacturing-process statement or catalog weight."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local manufacturing route is inferred from the stainless ISO-K full-nipple geometry and common vacuum piping fabrication practice."
    - "Helium leak testing is included because the row is a vacuum component and Pfeiffer describes leak testing as a general vacuum-component quality practice."
  uncertainty_notes:
    - "The vendor/CAD evidence resolves product family, material, and interface geometry, but not the actual Pfeiffer fabrication sequence, weld details, surface finish, or acceptance limit for this specific part number."
kb_implications:
  - "item_granularity: simple_part - standard DN 100 ISO-K stainless full nipple/vacuum pipe fitting; later KB work should model it as reusable vacuum plumbing hardware, not as a reAM250-specific custom machine part."
---

# reAM250 BOM Row 138 - 3Q1

Research result for the leased reAM250 BOM row.
