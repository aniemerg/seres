---
row_identity:
  item: "24"
  cad_file: "24_seal_left_right"
  source_row_number: 247
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
function:
  summary: "Long, thin left/right side seal strip formed from black silicone sealing compound; it fills the joint between mating machine panels or cover surfaces to prevent leakage and tolerate vibration."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/24_seal_left_right.step; research/ream250_bom/ream250_bom_row_0247_24__views_2x2.png; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "BOM row 247 names item 24 as quantity 2, CAD file 24_seal_left_right, product 6185 black silicone sealant from Liqui Moly. FreeCAD measured a 3.0 x 355.0 x 917.0 mm solid, and the rendered contact sheet shows a flat rectangular seal strip. The Liqui Moly BOM URL describes the product as a silicone-based sealing compound that remains elastic, resists chemicals/oils, and is used for sealing mating housings and covers."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid represents the applied/cured seal geometry for one left or right side seal, not the full 200 ml aerosol container."
  uncertainty_notes:
    - "The STEP file gives the seal envelope but not its installation preload, compression state, or exact sealed interface."
mass:
  value_kg: 0.0891
  basis: "Per physical seal strip. FreeCAD volume is 74218.672 mm^3 = 0.000074218672 m^3. Using the local silicone_rubber representative density of 1200 kg/m^3 gives 0.000074218672 * 1200 = 0.089062 kg per strip. BOM quantity is 2, so row total is about 0.178 kg; the two modeled strips occupy about 148.4 ml, within one 200 ml product container."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/24_seal_left_right.step; kb/materials/properties.yaml; https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 74218.672 mm^3 and bounding box 3.0 x 355.0 x 917.0 mm. BOM/vendor evidence identifies the material as black silicone sealing compound. kb/materials/properties.yaml lists silicone_rubber density as 1200 kg/m^3. The Liqui Moly BOM URL lists article 6185 as a 200 ml container."
    evidence_basis: "bom_provided"
  assumptions:
    - "Representative silicone rubber density is suitable for the applied/cured sealant volume for coarse BOM modeling."
  uncertainty_notes:
    - "Actual mass may vary with bead squeeze-out, voids, cure chemistry, and the density of the specific uncured Liqui Moly 6185 formulation."
material:
  primary_material: "black silicone-based sealing compound / cured silicone elastomer"
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "BOM row 247 gives description 6185: black silicone sealant and manufacturer Liqui Moly. The BOM-provided Liqui Moly page describes Silikondichtmasse schwarz as a silicone-based sealing compound and lists article 6185."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Assembly STEP material metadata returned only Generic with density 1000, so it was not used as material evidence."
    - "The public product page supports silicone-based sealant but does not expose a complete cured elastomer formulation or filler package."
how_to_make:
  summary: "Procure Liqui Moly 6185 black silicone sealing compound or an equivalent silicone gasket compound, clean and degrease the mating faces, dispense an even 3 mm-thick seal path matching the CAD strip, and join the mating parts immediately so the compound cures in place."
  manufacturing_steps:
    - "Procure 200 ml Liqui Moly 6185 black silicone sealing compound or equivalent silicone gasket compound."
    - "Clean the sealing faces so they are dry and free of oil and grease."
    - "Apply a continuous bead/strip following the left or right side seal path represented by the CAD geometry."
    - "Assemble the mating parts immediately, without a waiting/flash-off period, and allow the sealant to cure in place."
  source:
    url_or_path: "https://www.liqui-moly.com/de/de/silikondichtmasse-schwarz-p001435.html#6185; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/24_seal_left_right.step"
    cited_fact_or_basis: "The BOM-provided Liqui Moly page identifies article 6185 as a 200 ml black silicone sealing compound and states that surfaces should be clean, oil-free, grease-free, and dry; material is applied evenly and parts are joined immediately without flash-off time. The STEP file gives the long, flat seal geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "For KB modeling, procurement plus application is the appropriate route for this row because the BOM identifies a commercial sealant rather than a machined or molded discrete part."
  uncertainty_notes:
    - "The exact dispensing tool, cure time, and applied bead tolerance are not specified in the row evidence."
kb_implications:
  - "item_granularity: simple_part - Model as applied silicone sealant/seal material consumed during assembly rather than as a reusable machine part or purchased module."
---
