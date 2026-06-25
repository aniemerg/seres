---
row_identity:
  item: "21"
  cad_file: "21_seal_top"
  source_row_number: 244
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
function:
  summary: "Top perimeter seal formed from Liqui Moly 6185 black silicone sealant; it seals a roughly 386 mm square interface as a thin cured bead or gasket."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0244_21__views_2x2.png; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html"
    cited_fact_or_basis: "The BOM row identifies item 21 as 21_seal_top, quantity 1, description 6185 black silicone sealant, manufacturer Liqui Moly; the CAD preview shows a thin square perimeter seal; the BOM-provided product page identifies article 6185 as black silicone sealing compound for sealing joined surfaces."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD perimeter body represents the cured sealant bead applied to the top interface, not a separately stocked molded gasket."
  uncertainty_notes: []
mass:
  value_kg: 0.043
  basis: "FreeCAD measured one solid with volume 35793.557 mm^3, surface area 32810.761 mm^2, and bounding box about 386.00 x 386.00 x 3.00 mm. Using the local silicone_rubber density constant of 1200 kg/m^3 gives 0.04295 kg for the cured sealant represented by the CAD solid. BOM quantity is 1, so the row total is also about 0.043 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/21_seal_top.step; kb/materials/properties.yaml; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html"
    cited_fact_or_basis: "FreeCAD measured volume 35793.557 mm^3 and bounding box 386.00 x 386.00 x 3.00 mm; the BOM-provided Liqui Moly page identifies article 6185 as silicone-based sealing compound; kb/materials/properties.yaml lists silicone_rubber density as 1200 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD volume is treated as cured silicone-rubber volume after application."
    - "The local silicone_rubber density is used as a representative calculation constant for cured silicone sealant."
  uncertainty_notes:
    - "Sealant cure shrinkage, bead compression, and any excess squeeze-out are not represented separately, so the mass is best treated as a CAD-derived installed-seal estimate."
material:
  primary_material: "black silicone sealant / cured silicone rubber"
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The BOM row specifies 6185 black silicone sealant from Liqui Moly; the BOM-provided Liqui Moly product page describes the product as silicone-based sealing compound; the assembly STEP material extractor for 21_seal_top returned only Generic material with density 1000.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "For KB material modeling, the installed bead is represented as cured silicone rubber rather than uncured aerosol/can contents."
  uncertainty_notes:
    - "The exact silicone formulation and fillers are not specified by the BOM row or product page, so the material should remain a broad silicone-sealant family rather than a precise compound."
how_to_make:
  summary: "Model as an applied consumable sealant: dispense black silicone sealant along the top perimeter, assemble the mating surfaces immediately, and let it cure into the thin square gasket-like bead."
  manufacturing_steps:
    - "Clean and dry the mating surfaces so they are free of oil and grease."
    - "Dispense Liqui Moly 6185 or equivalent black silicone sealant along the roughly 386 mm square perimeter path."
    - "Join the parts promptly so the bead compresses to the approximately 3 mm CAD thickness."
    - "Allow the sealant to cure, then inspect the perimeter for continuity, adhesion, and excess squeeze-out."
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html; research/ream250_bom/ream250_bom_row_0244_21__views_2x2.png"
    cited_fact_or_basis: "The BOM-provided Liqui Moly page states that the surfaces to be sealed should be clean, oil-free, grease-free, and dry, and that material is applied evenly before parts are joined immediately; the CAD preview shows a thin square perimeter bead."
    evidence_basis: "bom_provided"
  assumptions:
    - "The local manufacturing action is application and curing of a external sealant, not synthesis of silicone chemistry"
    - "The CAD preview is used only for the applied path and approximate installed shape."
  uncertainty_notes:
    - "The BOM evidence does not state the actual dispensing nozzle size, cure schedule, or compression target used in the reAM250 assembly."
kb_implications:
  - "item_granularity: simple_part - installed black silicone sealant bead; model as a replaceable or applied part/applied material rather than a reusable part or separate molded gasket."
---
