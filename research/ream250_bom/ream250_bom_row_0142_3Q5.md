---
row_identity:
  item: "3Q5"
  cad_file: "3Q5_clamp_ISO_K_DN100_350BPD100"
  source_row_number: 142
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100"
function:
  summary: "Pfeiffer Vacuum 350BPD100 ISO-K single claw clamp for fastening a DN 63 to DN 100 ISO-K flange to a base plate with an O-ring groove; BOM quantity is 4."
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "The row identifies product 350BPD100 from Pfeiffer Vacuum. The official shop page names it a claw clamp for base plate with sealing groove, says it installs an ISO-K flange on a base plate with O-ring groove, lists connection flange DN 63-DN 100 ISO-K, and notes use with metal and elastomer seals. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 350BPD100."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.0323
  basis: "FreeCAD measured CAD volume 4119.697 mm^3 for one clamp. Using generic steel density 7850 kg/m^3 from kb/materials/properties.yaml gives 0.03234 kg per clamp, rounded to 0.0323 kg. BOM quantity is 4, so the row total is about 0.129 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q5_clamp_ISO_K_DN100_350BPD100.step; kb/materials/properties.yaml; https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 4119.697 mm^3, area 2345.582 mm^2, and bounding box 24.00 x 18.60 x 15.00 mm. The official shop page identifies zinc-plated steel material for 350BPD100. The local material density table lists steel density 7850 kg/m^3. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 350BPD100."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical solid volume for one purchased clamp."
    - "The thin zinc plating is included in the steel-volume approximation because its mass contribution is small at this scale."
  uncertainty_notes:
    - "No row-specific catalog weight was found on the checked product route or targeted searches, so this is a CAD-derived mass estimate rather than a vendor-stated weight."
material:
  primary_material: "zinc-plated steel"
  source:
    url_or_path: "https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "The official shop page title and technical data identify the 350BPD100 claw clamp material as zinc-plated steel and list temperature range 0-200 C. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 350BPD100."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The assembly STEP metadata returned only Generic material with density 1000.0, so material is taken from the row-matched official shop route rather than local STEP metadata."
how_to_make:
  summary: "Model as a standard zinc-plated steel ISO-K vacuum fastening claw clamp. Plausible machine or forge a small steel clamp blank, tap/thread the M8 interface, finish bearing faces, zinc plate, and inspect fit; near-term KB modeling should reuse a standard vacuum fastener part."
  manufacturing_steps:
    - "Cut or forge a small steel blank for the claw clamp body."
    - "Machine the stepped claw faces and central threaded M8 feature indicated by the vendor dimensions and CAD preview."
    - "Deburr and clean the bearing surfaces and thread."
    - "Apply zinc plating and inspect ISO-K flange fit and thread dimensions."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0142_3Q5__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3Q5_clamp_ISO_K_DN100_350BPD100.step; https://www.vacuum-shop.com/shop/en_US/category/2073029/product/350bpd100/claw-clamp-for-base-plate-with-sealing-groove-zinc-plated-steel.html"
    cited_fact_or_basis: "The rendered contact sheet shows a compact claw clamp block with a central cylindrical/threaded feature and stepped gripping faces. FreeCAD measured bounding box 24.00 x 18.60 x 15.00 mm. The official shop page lists dimension parameters A 30 mm, B M8, C 19 mm, D 10.1 mm, DN 63-DN 100 ISO-K use, and zinc-plated steel material. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/350BPD100 was checked; the used vacuum-shop.com page is branded as Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details and Pfeiffer copyright, and matches row product ID 350BPD100."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from zinc-plated steel material, M8 fastening function, and the visible machined clamp geometry."
    - "Vacuum service requires clean, burr-free clamp bearing faces even though the exact vendor finishing process is not stated."
  uncertainty_notes:
    - "The vendor/CAD evidence resolves function, material, envelope, and interface dimensions but not the actual production process, plating thickness, or inspection standard."
    - "Targeted_web_search: searched \"350BPD100 Weight\", \"350BPD100 Mass\", \"Datasheet_350BPD100_en.pdf weight\", and \"350BPD100 Pfeiffer Vacuum ISO-K DN100 clamp weight material\" found row-matched material, dimensions, and function facts but no row-specific manufacturing process or catalog weight."
kb_implications:
  - "item_granularity: simple_part - standard ISO-K zinc-plated steel vacuum claw clamp/fastener; later KB work should prefer a reusable standard hardware item rather than a machine-specific 3Q5-only item."
---

# reAM250 BOM Row 142 - 3Q5

Research result for the leased reAM250 BOM row.
