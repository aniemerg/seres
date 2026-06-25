---
row_identity:
  item: "12"
  cad_file: "12_flat_seal_back"
  source_row_number: 216
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
function:
  summary: "Applied rear flat seal bead/gasket for the reAM250 assembly, made from Liqui Moly 6185 black silicone sealant and forming a long rectangular perimeter seal."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/12_flat_seal_back.step; research/ream250_bom/ream250_bom_row_0216_12__views_2x2.png; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "BOM row 216 identifies item 12, quantity 1, CAD file 12_flat_seal_back, product 6185 black silicone sealant, manufacturer Liqui Moly, and a Liqui Moly product URL. The manifest maps the row to one matched vendor-component STEP. FreeCAD measured one solid with bounding box 840.00 x 3.00 x 400.00 mm, and the contact sheet shows a thin rectangular perimeter seal. The Liqui Moly page describes 6185 as a silicone-based sealing compound for sealing assemblies."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP file represents the cured or applied seal geometry for the single physical BOM row item, not the full 200 ml retail container."
  uncertainty_notes:
    - "The row evidence identifies this as the back flat seal but does not show the mating faces or compression condition in the final machine assembly."
mass:
  value_kg: 0.0869
  basis: "Per-unit estimate for quantity 1. FreeCAD measured volume 72427.433 mm^3 = 0.000072427433 m^3 for the applied seal geometry. Using the local silicone_rubber density constant of 1200 kg/m^3 gives 0.086913 kg, rounded to 0.0869 kg. The row total is the same because the BOM quantity is 1."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/12_flat_seal_back.step; kb/materials/properties.yaml; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 72427.433 mm^3, area 62770.442 mm^2, and bounding box 840.00 x 3.00 x 400.00 mm. The Liqui Moly page identifies product 6185 as a silicone-based sealing compound. kb/materials/properties.yaml lists silicone_rubber density_kg_per_m3: 1200."
    evidence_basis: "bom_provided"
  assumptions:
    - "The cured/applied seal density is approximated by the local silicone_rubber density constant."
    - "The CAD volume is treated as the physical volume of one applied back seal bead/gasket."
  uncertainty_notes:
    - "Actual cured sealant density and final compressed volume may differ from the local representative silicone-rubber constant and the uncompressed CAD export."
material:
  primary_material: "black silicone-based sealing compound / cured silicone elastomer"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "BOM row 216 names product 6185 as black silicone sealant from Liqui Moly. The Liqui Moly product page describes it as a silicone-based sealing compound and lists article 6185 as a 200 ml aerosol can variant."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The product page resolves the material family but not the exact cured formulation, filler package, pigment composition, or durometer."
how_to_make:
  summary: "Procure Liqui Moly 6185 black silicone sealant, clean and dry the mating surfaces, dispense the sealant uniformly along the CAD-defined rear perimeter, then assemble the parts immediately so the bead cures as the back flat seal."
  manufacturing_steps:
    - "Procure Liqui Moly 6185 black silicone sealant or a functionally equivalent silicone sealing compound."
    - "Clean the rear sealing surfaces so they are dry and free of oil and grease."
    - "Apply the sealant uniformly along the back perimeter matching the 12_flat_seal_back CAD path."
    - "Join the mating parts immediately after application and allow the sealant to cure in place."
    - "Inspect for continuous coverage and absence of gaps, smears into functional openings, or obvious underfilled sections."
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/12_flat_seal_back.step; research/ream250_bom/ream250_bom_row_0216_12__views_2x2.png"
    cited_fact_or_basis: "The Liqui Moly page states that 6185 is supplied in an automatic cartridge/aerosol can, identifies article 6185 as 200 ml, and instructs users to clean/dry/degrease sealing surfaces, apply material evenly, and assemble parts immediately. The STEP/contact sheet provides the rear rectangular perimeter path and 3 mm thickness for this row's applied seal geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "Inspection is modeled as a basic assembly-quality check because the cited product page gives application guidance but not reAM250-specific quality-control criteria."
  uncertainty_notes:
    - "The product route and CAD path resolve procurement and application, but not the exact bead dispensing tolerance, cure time under the machine's assembly conditions, or acceptance test for leak tightness."
kb_implications:
  - "item_granularity: simple_part - Model as an applied silicone sealant/gasket replaceable or applied part tied to a CAD-defined bead path, not as a reusable machine part or purchased module."
---

Research result for the leased reAM250 BOM row only.
