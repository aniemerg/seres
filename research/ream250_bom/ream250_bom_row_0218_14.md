---
row_identity:
  item: "14"
  cad_file: "14_flat_seal_top_bottom"
  source_row_number: 218
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
function:
  summary: "Black silicone sealant dispensed as a thin rectangular perimeter seal for the top/bottom interface represented by the row CAD, providing an elastic sealing bead between mating reAM250 panels or housings."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/14_flat_seal_top_bottom.step; research/ream250_bom/ream250_bom_row_0218_14__views_2x2.png; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; https://pim.liqui-moly.de/article/6177?language=en"
    cited_fact_or_basis: "BOM row 218 lists item 14, quantity 2, CAD file 14_flat_seal_top_bottom, description/product ID 6185: black silicone sealant, manufacturer Liqui Moly, and the Liqui Moly product URL. Manifest row 218 maps it to a matched vendor-component STEP. FreeCAD measured one solid with a 840.00 x 520.00 x 3.00 mm bounding box, and the rendered top view shows a thin rectangular perimeter bead. The Liqui Moly product route identifies Silicone Sealing Compound, black as a heat-resistant one-component sealant used for sealing metal, plastic, glass, and similar materials. official_alternate_route_check: original BOM URL is the Liqui Moly product page on liqui-moly.com for p001435#6185; https://pim.liqui-moly.de/article/6177?language=en is a Liqui Moly PIM product-information PDF for the same Silicone Sealing Compound, black family and lists the 6185 200 ml can variant."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row name top_bottom and the rectangular perimeter CAD geometry are interpreted as a seal bead for a top or bottom plate/housing interface rather than a free-standing sheet gasket."
    - "The two BOM units represent two physically separate applications of this same perimeter seal geometry."
  uncertainty_notes:
    - "The CAD and BOM do not show the exact mating plates, compression state, or service environment, so the precise sealed volume and pressure duty remain unspecified."
mass:
  value_kg: 0.0956
  basis: "Per unit. BOM quantity is 2, so the row total is about 0.191 kg. FreeCAD volume 79627.433 mm^3 = 0.000079627433 m^3. Using the local silicone_rubber density constant 1200 kg/m^3 gives 0.000079627433 m^3 * 1200 kg/m^3 = 0.0955529 kg, rounded to 0.0956 kg per seal. Product-specific literature found during cross-check gives a broad 0.95-1.28 g/cm^3 sealant density range, which would bracket the same CAD volume at about 0.0756-0.102 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/14_flat_seal_top_bottom.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 79627.433 mm^3, area 69010.442 mm^2, and bounding box 840.00 x 520.00 x 3.00 mm. The BOM and Liqui Moly product route identify the row material as black silicone sealant. The local density table lists silicone_rubber density_kg_per_m3: 1200. Local assembly STEP material extraction returned only Generic with density 1000.0, which was not used as material evidence."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the cured sealant volume for one physical seal item."
    - "The local silicone_rubber density constant is a suitable planning density for cured silicone sealant."
  uncertainty_notes:
    - "Actual installed mass may vary with bead compression, trimming, over-application, and cure shrinkage; use the product-density bracket in the basis when a range is more appropriate than the single planning value."
material:
  primary_material: "black neutral-crosslinked silicone sealant, no-MEKO formulation"
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; https://pim.liqui-moly.de/article/6177?language=en; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "BOM row 218 describes the row as 6185 black silicone sealant from Liqui Moly. The Liqui Moly product page identifies Silikondichtmasse schwarz and article 6185 as a 200 ml aerosol can variant. The current Liqui Moly product-information PDF for Silicone Sealing Compound, black lists the base as neutral cross-linked and No MEKO/free of 2-butanone oxime, with black silicone sealing-compound product identity. official_alternate_route_check: original BOM URL is the Liqui Moly German product page for p001435#6185; the alternate https://pim.liqui-moly.de/article/6177?language=en is a Liqui Moly PIM product-information PDF linked through the same product/download route and lists the same Silicone Sealing Compound, black family and 6185 200 ml can variant."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The sources identify the sealant chemistry family and current formulation type but not a full filler/additive composition or cured rubber compound recipe."
how_to_make:
  summary: "Procure Liqui Moly 6185 black silicone sealing compound, clean and degrease the mating surfaces, dispense a uniform rectangular perimeter bead matching the CAD path, then join the parts immediately and allow humidity cure."
  manufacturing_steps:
    - "Procure or prepare a neutral-crosslinking black silicone sealing compound equivalent to Liqui Moly 6185."
    - "Clean the top/bottom mating surfaces so they are dry and free of oil and grease."
    - "Dispense the sealant as a continuous rectangular perimeter bead matching the 840 x 520 mm CAD envelope and about 3 mm bead height."
    - "Join the mating parts immediately without flash-off time, controlling squeeze-out so the bead remains continuous."
    - "Allow humidity cure before service; inspect for bead continuity, gaps, contamination, and excessive squeeze-out."
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; https://pim.liqui-moly.de/article/6177?language=en; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/14_flat_seal_top_bottom.step; research/ream250_bom/ream250_bom_row_0218_14__top.png"
    cited_fact_or_basis: "The Liqui Moly product route states that the sealant vulcanizes under air humidity, the surfaces to be sealed must be clean, dry, and free of oil and grease, material should be applied evenly, and parts should be joined immediately without flash-off time. The STEP geometry and rendered top view provide the rectangular perimeter bead path and 3 mm height used for the row-specific application. official_alternate_route_check: original BOM URL is the Liqui Moly product page on liqui-moly.com for p001435#6185; https://pim.liqui-moly.de/article/6177?language=en is a Liqui Moly PIM product-information PDF for the same Silicone Sealing Compound, black family and lists the 6185 200 ml can variant."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD bead is a target cured or installed bead shape, so dispensing controls should target a similar perimeter and approximate volume before compression."
    - "For KB modeling, procurement plus local dispensing/curing is the appropriate route unless a later task models silicone sealant synthesis and cartridge/can packaging in detail."
  uncertainty_notes:
    - "Exact fixture pressure, cure time before machine operation, and inspection acceptance criteria are not specified by the row evidence."
kb_implications:
  - "item_granularity: consumable - Model as a reusable silicone sealant/gasket consumable applied by dispensing and curing, not as a unique rigid custom part."
---

Research result for reAM250 BOM row 218.
