---
row_identity:
  item: "3E"
  cad_file: "3E_seal_with_filter_ISO_KF_DN40_122ZRS040"
  source_row_number: 116
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/122ZRS040"
function:
  summary: "DN 40 ISO-KF centering-ring seal with an integrated sintered metal filter; it centers and seals a KF flange joint while adding a fine particulate/contamination filter in the vacuum line."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/122ZRS040 ; https://www.shop.buschgroup.com/global/en/products/122ZRS040/ ; research/ream250_bom/ream250_bom_row_0116_3E__views_2x2.png"
    cited_fact_or_basis: "BOM row 116 identifies item 3E as Pfeiffer Vacuum order 122ZRS040, quantity 2. The BOM-provided product route redirects to the Busch/Pfeiffer shop page for order number 122ZRS040, titled centering ring with sintered metal filter, stainless steel, FKM, DN 40 ISO-KF, with sintered metal filter and FKM O-ring. The rendered CAD preview shows a shallow round centering-ring/filter disk geometry. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/122ZRS040 redirects to https://www.shop.buschgroup.com/global/en/products/122ZRS040/, a Busch Group page carrying the Pfeiffer Vacuum logo and exact order number 122ZRS040; the same product family is also mirrored on the Pfeiffer Vacuum Online Shop page for 122ZRS040."
    evidence_basis: "bom_provided"
  assumptions:
    - "The installed row role follows the vendor component identity because the manifest maps this BOM row to the matching vendor STEP file."
  uncertainty_notes: []
mass:
  value_kg: 0.041
  basis: "Per unit. FreeCAD measured one solid with volume 5239.703 mm^3, surface area 4696.527 mm^2, and bounding box about 48.11 x 48.11 x 8.00 mm. The compact renderer reported a visual mesh envelope about 44.0 x 44.0 x 8.0 mm. Using an engineering effective density of 7800 kg/m^3 for the mixed stainless-steel/sintered-bronze/FKM component gives 5239.703e-9 m^3 * 7800 kg/m^3 = 0.0409 kg, rounded to 0.041 kg per centering ring/filter. BOM quantity is 2, so the row total is about 0.082 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3E_seal_with_filter_ISO_KF_DN40_122ZRS040.step ; kb/materials/properties.yaml ; https://www.pfeiffer-vacuum.com/global/de/shop/products/122ZRS040 ; https://vacuum-shop.com/shop/en_US/category/2072858/product/122zrs040/centering-ring-with-sintered-metal-filter-stainless-steel-1-4301-304.html"
    cited_fact_or_basis: "FreeCAD measured the row STEP as one solid with volume 5239.703 mm^3. The BOM-provided product route identifies stainless steel, sintered bronze filter, and FKM O-ring construction; the local density table lists stainless_steel_304 at 8030 kg/m^3, brass at 8500 kg/m^3 as the nearest local bronze-like copper alloy, and FKM at 1800 kg/m^3. targeted_web_search: queries tried: '122ZRS040 Pfeiffer weight', '122ZRS040 datasheet centering ring sintered metal filter DN 40 ISO-KF weight', and 'Pfeiffer 122ZRS040 PDF'; result: row-matched product and datasheet routes were found, but no accessible row-specific mass or material volume split was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD solid volume is treated as the per-unit solid material envelope for one physical centering-ring/filter item."
    - "A 7800 kg/m^3 effective density approximates a mostly stainless/bronze part with a smaller FKM O-ring contribution."
  uncertainty_notes:
    - "Mass is limited by the single-solid CAD export and lack of catalog weight or split volumes for the stainless ring, sintered bronze filter, and FKM O-ring."
material:
  primary_material: "stainless steel 1.4301/304 ring, sintered bronze filter, and FKM O-ring"
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/122ZRS040 ; https://www.shop.buschgroup.com/global/en/products/122ZRS040/ ; https://vacuum-shop.com/shop/en_US/category/2072858/product/122zrs040/centering-ring-with-sintered-metal-filter-stainless-steel-1-4301-304.html ; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The BOM-provided product route for 122ZRS040 states stainless steel, FKM, DN 40 ISO-KF, with sintered metal filter made of sintered bronze, mesh size about 0.02 mm, and FKM O-ring. The Pfeiffer Vacuum Online Shop page for the same order number states material ring stainless steel 1.4301/304, filter sintered bronze, and O-ring material FKM. Local assembly STEP material extraction returned only Generic with density 1000.0, so it was treated as placeholder metadata. official_alternate_route_check: original BOM URL https://www.pfeiffer-vacuum.com/global/de/shop/products/122ZRS040 redirects to a Busch Group shop page with Pfeiffer branding and exact order number 122ZRS040; the alternate vacuum-shop.com page is branded Pfeiffer Vacuum Online Shop, lists Pfeiffer Vacuum Components & Solutions GmbH contact details, and matches exact product ID 122ZRS040."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Best modeled as a purchased Pfeiffer ISO-KF seal/filter consumable. A plausible local route would form or machine the stainless centering ring, produce or buy the sintered bronze filter disk, mold or procure the FKM O-ring, clean for vacuum service, and assemble the ring/filter/O-ring stack."
  manufacturing_steps:
    - "Machine or form the stainless 1.4301/304 centering ring to DN 40 ISO-KF dimensions."
    - "Press and sinter bronze powder into the filter disk or procure a sintered bronze disk with about 0.02 mm average pore size."
    - "Mold, cure, and inspect the FKM O-ring, or procure a standard compatible O-ring."
    - "Clean parts for vacuum compatibility and assemble the filter disk and O-ring into the centering ring."
    - "Inspect fit, sealing surfaces, and filter integrity before installation."
  source:
    url_or_path: "https://www.pfeiffer-vacuum.com/global/de/shop/products/122ZRS040 ; https://vacuum-shop.com/shop/en_US/category/2072858/product/122zrs040/centering-ring-with-sintered-metal-filter-stainless-steel-1-4301-304.html ; research/ream250_bom/ream250_bom_row_0116_3E__views_2x2.png"
    cited_fact_or_basis: "Vendor pages identify the row as a DN 40 ISO-KF centering ring with stainless ring, sintered bronze filter, and FKM O-ring; the rendered CAD preview shows a shallow annular ring/filter geometry. targeted_web_search: queries tried: '122ZRS040 Pfeiffer weight', '122ZRS040 datasheet centering ring sintered metal filter DN 40 ISO-KF weight', 'Pfeiffer 122ZRS040 PDF', and 'ISO-KF centering ring sintered bronze filter manufacturing'; results resolved product identity, materials, dimensions, and pore size but did not provide a row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Manufacturing route is inferred from the component material stack and visible geometry, not directly specified by Pfeiffer for this exact row."
  uncertainty_notes:
    - "Filter porosity control and vacuum-cleanliness requirements may dominate real manufacturing quality beyond the coarse KB route."
kb_implications:
  - "item_granularity: consumable - Treat as a replaceable ISO-KF DN40 seal/filter consumable with component material notes, not as a reAM250-specific machine subsystem."
---

