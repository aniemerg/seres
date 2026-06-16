---
row_identity:
  item: "3R2"
  cad_file: "3R2_seal_ISO_K_DN63_311ZRA063"
  source_row_number: 144
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/311ZRA063"
function:
  summary: "DN 63 ISO-K centering-ring seal with an outer ring and O-ring, used to center and seal an ISO-K vacuum flange joint."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3R2_seal_ISO_K_DN63_311ZRA063.step; research/ream250_bom/ream250_bom_row_0144_3R2__views_2x2.png; https://www.shop.buschgroup.com/global/en/products/311ZRA063/"
    cited_fact_or_basis: "BOM row 144 lists item 3R2, quantity 1, CAD file 3R2_seal_ISO_K_DN63_311ZRA063, product ID 311ZRA063, manufacturer Pfeiffer Vacuum, and the provided product URL; the manifest maps row 144 to the matched STEP file; FreeCAD measured one annular solid with an 85.993 x 85.996 x 8.00 mm bounding box; the rendered contact sheet shows a thin ring-like component with stepped side features; the official Busch canonical page for legacy number 311ZRA063 identifies the product as a centering ring with outer ring, aluminum, NBR, DN 63 ISO-K."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM/CAD ISO_K_DN63 designation, annular geometry, and row-matched product page are interpreted as the flange-interface sealing and centering role for this row."
  uncertainty_notes: []
mass:
  value_kg: 0.011
  basis: "FreeCAD measured the row STEP as one solid with volume 5586.124 mm^3, surface area 6239.540 mm^2, and bounding box 85.993 x 85.996 x 8.00 mm. With local density constants of 2700 kg/m^3 for aluminum and 1100 kg/m^3 for NBR, the all-aluminum and all-NBR bounds are about 0.015 kg and 0.006 kg. A midpoint effective-density estimate gives about 0.011 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3R2_seal_ISO_K_DN63_311ZRA063.step; research/ream250_bom/ream250_bom_row_0144_3R2__views_2x2.png; kb/materials/properties.yaml; https://www.shop.buschgroup.com/global/en/products/311ZRA063/"
    cited_fact_or_basis: "FreeCAD measured 5586.124 mm^3 for one solid; the rendered contact sheet shows a thin annular ring; the official Busch canonical page for legacy number 311ZRA063 identifies the product as aluminum and NBR; the local density table lists aluminum at 2700 kg/m^3 and NBR at 1100 kg/m^3."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The single-solid STEP volume is used as a coarse combined material-volume proxy because the CAD does not expose separate aluminum and NBR regions."
    - "The midpoint between the all-aluminum and all-NBR mass bounds is used as the representative BOM mass estimate."
  uncertainty_notes:
    - "The aluminum-to-NBR volume fraction is not measured separately, so the mass remains an effective-density estimate."
material:
  primary_material: "aluminum outer ring with NBR O-ring"
  source:
    url_or_path: "https://www.shop.buschgroup.com/global/en/products/311ZRA063/"
    cited_fact_or_basis: "The official Busch canonical page for legacy number 311ZRA063 identifies the product as a centering ring with outer ring, aluminum, NBR, DN 63 ISO-K; page data also lists materials in contact with media as aluminum and O-ring material as NBR."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
how_to_make:
  summary: "Model as a purchased standard DN 63 ISO-K centering-ring seal. A local manufacturing route would machine or form the aluminum centering/outer ring, make or source the NBR O-ring, assemble the seal, and inspect the flange-interface dimensions."
  manufacturing_steps:
    - "Turn, machine, or form the aluminum centering/outer ring to the DN 63 ISO-K geometry."
    - "Mold or procure the matching NBR O-ring for the sealing interface."
    - "Install the O-ring onto the aluminum ring without cuts, twist, or contamination."
    - "Clean and inspect annular dimensions, O-ring seating, and sealing surfaces before vacuum use."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0144_3R2__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3R2_seal_ISO_K_DN63_311ZRA063.step; https://www.shop.buschgroup.com/global/en/products/311ZRA063/"
    cited_fact_or_basis: "The rendered CAD preview shows a thin annular ring with stepped side features; FreeCAD measured one ring-like solid about 86 mm across and 8 mm thick; the official Busch canonical page identifies the product as a DN 63 ISO-K centering ring with outer ring made from aluminum and NBR."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB purposes, this standard purchased seal can be represented as aluminum ring fabrication plus elastomer O-ring production and assembly."
  uncertainty_notes:
    - "Exact groove geometry, sealing tolerances, and surface finish should come from the vendor drawing or applicable ISO-K seal specification before precision manufacturing."
kb_implications:
  - "Represent this as a reusable DN 63 ISO-K centering-ring seal rather than a reAM250-specific custom part."
  - "If modeled as an assembly, use aluminum plus NBR/elastomer material classes and keep the mass estimate coarse unless catalog mass or split-volume CAD becomes available."
---

Research result for reAM250 BOM row 144, item 3R2.
