---
row_identity:
  item: "3P6"
  cad_file: "3P6_powder_container_2_liter"
  source_row_number: 136
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.amproved.com/amproved-produkte1/powder-container-2l.html"
function:
  summary: "Two-liter powder storage and handling bottle/container for additive-manufacturing powder, with an ISO KF DN40 connection for dust-reduced handling and connection to compatible equipment."
  source:
    url_or_path: "https://www.amproved.com/powder-container-2l.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0136_3P6__views_2x2.png"
    cited_fact_or_basis: "The AMPROVED Powder Container - 2L page states a 2 L capacity, ISO KF DN40 connection, powder storage/handling use, dust-free powder handling, protective-gas storage, and resealability; the BOM row names item 3P6 as 3P6_powder_container_2_liter; the CAD preview shows a ribbed bottle with a narrow neck/connector."
    evidence_basis: "bom_provided"
  assumptions:
    - "The canonical AMPROVED product page on the same domain is the live route for the BOM-provided Link URL product family."
  uncertainty_notes:
    - "The CAD preview confirms the container shape but does not show any separate cap, valve, or gasket hardware as separate solids for this row."
mass:
  value_kg: 2.104
  basis: "Per-unit mass for quantity 1. FreeCAD measured one solid with volume 268060.147 mm^3, which is 0.000268060147 m^3. The assembly STEP material metadata reports density 7850 kg/m^3 for Steel AISI 1144, giving 0.000268060147 * 7850 = 2.104 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3P6_powder_container_2_liter.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 268060.147 mm^3, area 182070.108 mm^2, and bounding box about 147.21 x 147.21 x 210.50 mm. The assembly STEP material extractor matched this product to Steel AISI 1144 with density 7850 kg/m^3. The local density table lists generic steel density as 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume represents the physical metal container body for the BOM row."
  uncertainty_notes:
    - "If the purchased container includes separate closure, seal, or valve pieces not present in this single-solid row CAD, their mass is not included in this per-unit estimate."
material:
  primary_material: "Steel AISI 1144 container body; AMPROVED product-family page describes the 2 L powder container as stainless steel."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.amproved.com/powder-container-2l.html"
    cited_fact_or_basis: "The local assembly STEP material extractor reports Steel AISI 1144 and density 7850 kg/m^3 for 3P6_powder_container_2_liter. The AMPROVED product page describes the Powder Container - 2L as an Edelstahl bottle for powder storage and handling."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "There is a material naming mismatch between the CAD package metadata, which says Steel AISI 1144, and the vendor page wording Edelstahl/stainless steel; later KB modeling should preserve both until a drawing or datasheet resolves the exact grade."
how_to_make:
  summary: "Procure as an AMPROVED Powder Container - 2L purchased component and fit it through its ISO KF DN40 interface in the powder handling path."
  manufacturing_steps:
    - "Buy or quote the AMPROVED Powder Container - 2L from the BOM-provided AMPROVED product route."
    - "Verify ISO KF DN40 interface compatibility against adjacent powder handling hardware."
    - "Use the supplied STP/CAD geometry for installation clearance and envelope checks."
  source:
    url_or_path: "https://www.amproved.com/powder-container-2l.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
    cited_fact_or_basis: "The AMPROVED page identifies the purchasable Powder Container - 2L, manufacturer AMPROVED GmbH, ISO KF DN40 connection, and available CAD downloads in STP/Parasolid/STL formats; BOM row 136 points to the same AMPROVED powder-container route."
    evidence_basis: "bom_provided"
  assumptions:
    - "For this research row, procurement is the preferred route because the BOM points to a named vendor product rather than a drawing-controlled in-house fabricated vessel."
  uncertainty_notes:
    - "The vendor page does not provide a detailed fabrication process for the container body; local manufacturing steps such as forming, welding, or surface finishing were not asserted."
kb_implications:
  - "item_granularity: purchased_module - Model as one purchased powder-container module for now, with the 2 L capacity and ISO KF DN40 interface captured in notes rather than splitting cap/seal/valve subparts from this single-solid CAD row."
---

