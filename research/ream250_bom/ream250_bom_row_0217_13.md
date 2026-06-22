---
row_identity:
  item: "13"
  cad_file: "13_flat_seal_side"
  source_row_number: 217
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
function:
  summary: "Cured-in-place flat side perimeter seal for a rectangular machine interface, using Liqui Moly 6185 black silicone sealing compound to form an elastic gasket between mating surfaces."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/13_flat_seal_side.step; research/ream250_bom/ream250_bom_row_0217_13__views_2x2.png; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "BOM row 217 names item 13 as 13_flat_seal_side, quantity 2, product 6185 black silicone sealant from Liqui Moly. CAD preview shows a thin rectangular perimeter seal, and FreeCAD measured a 3.00 x 520.00 x 400.00 mm bounding box. The Liqui Moly page describes the product as a silicone-based sealing compound that remains permanently elastic and is used for sealing metal, plastic, and glass parts."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD side perimeter represents the cured seal geometry after application, not the full 200 ml aerosol package."
  uncertainty_notes:
    - "Exact mating surfaces in the parent assembly were not resolved from this row alone, so the function is stated at the interface-seal level."
mass:
  value_kg: 0.0639
  basis: "Per-unit estimate for one side seal. FreeCAD measured volume 53227.433 mm^3, equal to 5.3227433e-5 m^3; using the local silicone_rubber density constant of 1200 kg/m^3 gives 0.06387 kg. BOM quantity is 2, so row total is about 0.128 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/13_flat_seal_side.step; kb/materials/properties.yaml; https://pim.liqui-moly.de/article/6177?language=en"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 53227.433 mm^3 and bounding box 3.00 x 520.00 x 400.00 mm. kb/materials/properties.yaml lists silicone_rubber density as 1200 kg/m^3. The Liqui Moly product information route for the same product identifies it as Silicone Sealing Compound, black and gives a historical density range of 0.95-1.28 g/cm3 for this product family in indexed product information. official_alternate_route_check: the BOM URL is the official liqui-moly.com product page for article 6185; pim.liqui-moly.de is the official Liqui Moly product-information/download route linked from the same product page, and it matches the same manufacturer, product family, and article/product identity."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the cured sealant volume for one physical side seal."
    - "The local silicone_rubber density is an appropriate planning constant for cured black silicone sealant and falls inside the Liqui Moly product-information density range found for this row's product family."
  uncertainty_notes:
    - "Sealant cure shrinkage, bead compression, and actual dispensed fill may shift mass modestly from the CAD-volume estimate."
material:
  primary_material: "black silicone sealing compound / cured silicone rubber, Liqui Moly 6185"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; https://pim.liqui-moly.de/article/6177?language=en"
    cited_fact_or_basis: "BOM row 217 calls the row product 6185: black silicone sealant from Liqui Moly. The official Liqui Moly page for article 6185 describes a silicone-based black sealing compound; the product information route describes a heat-resistant, single-component sealant that vulcanizes under air humidity and cures into a permanently elastic mass. official_alternate_route_check: the BOM URL is the official liqui-moly.com product page for article 6185; pim.liqui-moly.de is the official Liqui Moly product-information/download route linked from the same product page, and it matches the same manufacturer, product family, and article/product identity."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The row STEP material extractor returned only Generic material metadata, so the material conclusion depends on the BOM product identity and official Liqui Moly route rather than embedded CAD material."
how_to_make:
  summary: "Procure Liqui Moly 6185 or an equivalent one-component black RTV silicone sealant, clean and degrease the mating surfaces, dispense an even rectangular perimeter bead matching the CAD seal path, immediately assemble the parts, and allow moisture cure into an elastic gasket."
  manufacturing_steps:
    - "Procure or locally formulate a one-component black silicone sealing compound compatible with the target substrates."
    - "Clean the side interface surfaces so they are dry and free of oil and grease."
    - "Dispense a continuous perimeter bead following the rectangular side-seal geometry."
    - "Join the mating parts without flash-off time, then allow the sealant to vulcanize under ambient moisture."
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/13_flat_seal_side.step"
    cited_fact_or_basis: "The Liqui Moly page states that surfaces must be clean, oil-free, grease-free, and dry; material is applied evenly and parts are joined immediately without flash-off time. The product information route states the material vulcanizes under air humidity. CAD geometry provides the rectangular side-seal path."
    evidence_basis: "bom_provided"
  assumptions:
    - "For KB planning, the row is best modeled as applied sealant consumed into a cured gasket rather than as a separately molded reusable part."
  uncertainty_notes:
    - "Local self-manufacture of the silicone polymer and curing package is not decomposed here; this result only identifies the row-level application/procurement route."
kb_implications:
  - "item_granularity: consumable - Model as a consumed silicone sealant/cured gasket row, likely reusable across the other reAM250 flat seal rows that reference Liqui Moly 6185 rather than as a unique machined part."
---
