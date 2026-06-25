---
row_identity:
  item: "3P6"
  cad_file: "3P6_powder_container_2_liter"
  source_row_number: 136
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.amproved.com/amproved-produkte1/powder-container-2l.html"
function:
  summary: "Two-liter powder storage and handling bottle/container for additive-manufacturing powder, with an ISO KF DN40 connection for sealed storage, transfer, and machine interface use."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0136_3P6__views_2x2.png; https://www.amproved.com/amproved-produkte1/powder-container-2l.html"
    cited_fact_or_basis: "BOM row 136 and the manifest identify item 3P6 as AMPROVED CAD file 3P6_powder_container_2_liter, quantity 1. The AMPROVED product route identifies Powder Container - 2L, manufacturer AMproved GmbH, 2 L capacity, ISO KF DN40 connection, powder storage and handling, dust-free powder handling, protective-gas storage, and resealability. The rendered row CAD contact sheet shows a cylindrical bottle body with shoulder, neck, and top connection geometry."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM-linked AMPROVED product page is the row-matched product route for this 3P6 vendor component."
  uncertainty_notes:
    - "The row STEP is a single visible container-body solid; hidden closure, gasket, valve, or pipe-connection details are not separately resolved by this CAD file."
mass:
  value_kg: 2.104
  basis: "Per-unit mass for BOM quantity 1. FreeCAD measured volume 268060.147 mm^3, equal to 0.000268060147 m^3. The assembly STEP material metadata reports Steel AISI 1144 at density 7850 kg/m^3 for this product, so 0.000268060147 m^3 * 7850 kg/m^3 = 2.104 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P6_powder_container_2_liter.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 268060.147 mm^3, surface area 182070.108 mm^2, and bounding box about 147.21 x 147.21 x 210.50 mm. The local assembly STEP material extractor reports material Steel AISI 1144 and density 7850 kg/m^3 for 3P6_powder_container_2_liter. The local density table lists generic steel at 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single measured STEP solid is the physical item represented by this BOM row."
  uncertainty_notes:
    - "If the delivered AMPROVED product includes separate closure, gasket, valve, or pipe-connection pieces not represented in this single CAD solid, those extras are outside this CAD-derived per-unit mass."
material:
  primary_material: "Steel AISI 1144 in the row-specific CAD metadata; AMPROVED product route describes a stainless-steel powder container."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.amproved.com/amproved-produkte1/powder-container-2l.html"
    cited_fact_or_basis: "The local assembly STEP material extractor reports material Steel AISI 1144 and density 7850 kg/m^3 for 3P6_powder_container_2_liter. The AMPROVED Powder Container - 2L product route describes the product as a stainless-steel bottle/container for powder storage and handling."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "There is a material naming mismatch between the CAD package metadata and the vendor wording; preserve both until a drawing or datasheet resolves the exact delivered alloy grade."
how_to_make:
  summary: "Use the AMPROVED Powder Container - 2L as the supported procurement route; a plausible local route is to form or fabricate the steel bottle body, add the ISO KF DN40 neck/interface, finish for powder compatibility, and verify sealing and cleanliness."
  manufacturing_steps:
    - "Procure or quote the AMPROVED Powder Container - 2L through the BOM-linked AMPROVED product route when matching the original reAM250 BOM."
    - "For a later local-manufacturing model, fabricate the bottle-like steel body from suitable steel or stainless steel by forming, spinning, drawing, or welded fabrication consistent with the CAD envelope."
    - "Machine or attach the ISO KF DN40 neck/interface, then finish, clean, and passivate or otherwise protect the powder-contacting surfaces."
    - "Inspect capacity, envelope, ISO KF DN40 fit, resealability, and powder-cleanliness behavior before assembly into the powder-handling system."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P6_powder_container_2_liter.step; research/ream250_bom/ream250_bom_row_0136_3P6__views_2x2.png; https://www.amproved.com/amproved-produkte1/powder-container-2l.html"
    cited_fact_or_basis: "BOM row 136 identifies manufacturer AMPROVED and links to the Powder Container - 2L product route. The AMPROVED page identifies a purchasable 2 L powder container with ISO KF DN40 connection and downloadable CAD. The row CAD geometry and preview show a one-piece bottle-like container body with shoulder, neck, and top connection. targeted_web_search: queried 'AMPROVED Powder Container 2L manufacturing process material drawing' and 'AMPROVED powder container 2L datasheet stainless ISO KF DN40'; results resolved product function, material family, interface, and CAD downloads but did not state a detailed fabrication process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The local route is inferred from the bottle-like CAD geometry, steel material evidence, and ISO KF DN40 interface rather than from a vendor-stated process plan."
  uncertainty_notes:
    - "The actual vendor process, surface finish, cleanliness specification, and pressure or protective-atmosphere qualification are not stated by the available row evidence."
kb_implications:
  - "item_granularity: simple_part - Model as one powder-container hardware item for this pass, with 2 L capacity, steel/stainless material evidence, ISO KF DN40 interface, sealing, cleaning, and verification captured as item notes or process requirements rather than decomposing hidden closure details from this single-row CAD file."
---
