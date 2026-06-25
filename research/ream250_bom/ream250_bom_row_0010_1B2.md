---
row_identity:
  item: "1B2"
  cad_file: "1B2_handle"
  source_row_number: 10
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Edelstahl-Buegelgriffe#l1%3Dc(120)%3BForm%3Du(5e72aa81-7282-4de6-aa3f-99d6b8e98e5d)%3BOberfl%C3%A4che%3Du(5ac173de-c979-4e10-ab22-480f0ce07560)"
function:
  summary: "Stainless steel U-shaped machine/device bow handle used as a manually gripped pull or carry handle on the reAM250 assembly, with two mounting ends and underside finger recesses for ergonomic grip."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B2_handle.step; research/ream250_bom/ream250_bom_row_0010_1B2__views_2x2.png; https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Buegelgriffe-Edelstahl"
    cited_fact_or_basis: "BOM row 10 identifies item 1B2, quantity 1, CAD file 1B2_handle, product GN 328.5-140-B-GS, manufacturer GanterNorm. The manifest maps row 10 to gold_export/parts/1B2_handle.step as a matched_existing vendor_component. FreeCAD measured one solid with bounding box 166.50 x 60.03 x 28.00 mm; the rendered contact sheet shows a U-shaped handle with two mounting ends and finger recesses. The Ganter BOM URL canonical route identifies GN 328.5 as stainless steel precision-cast bow handles and states that the handles are stable, ergonomic, and have finger recesses on the underside."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row is interpreted as a pull/carry handle because the BOM name is handle, the supplier product family is a bow-handle family, and the CAD preview shows the matching U-handle geometry."
  uncertainty_notes:
    - "The local evidence does not identify the exact panel, cover, or door face that this specific handle mounts to."
mass:
  value_kg: 0.56
  basis: "FreeCAD volume 69,983.609 mm^3 equals 0.000069983609 m^3. Using the local stainless_steel density constant of 8000 kg/m^3 gives 0.560 kg per handle. BOM quantity is 1, so the row total is also about 0.56 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B2_handle.step; kb/materials/properties.yaml; https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Buegelgriffe-Edelstahl"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 69,983.609 mm^3, area 18,157.086 mm^2, and bounding box 166.50 x 60.03 x 28.00 mm. The Ganter BOM URL canonical route identifies the part family as stainless steel precision casting 1.4408. kb/materials/properties.yaml lists stainless_steel density as 8000 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "Generic stainless_steel density is used as the density constant for stainless precision-cast 1.4408 because the local density table has stainless steel but no separate 1.4408 entry."
    - "The isolated STEP solid volume is used as the physical-volume proxy for one purchased handle."
  uncertainty_notes:
    - "The assembly STEP material extractor returned only placeholder material Generic with density 1000.0, so it was not used for mass."
    - "The Ganter/Hanser page HTML exposed a displayed weight of 0.318 kg while also showing a default selected article number for a 120-A variant; because this row and CAD geometry are GN 328.5-140-B-GS with a 166.5 mm envelope, the CAD-volume estimate is used for this row."
material:
  primary_material: "Stainless steel precision casting 1.4408, matte blasted GS finish"
  source:
    url_or_path: "https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Buegelgriffe-Edelstahl"
    cited_fact_or_basis: "The Ganter BOM URL canonical route identifies GN 328.5 as stainless steel precision-cast bow handles and lists execution as Edelstahl-Feinguss 1.4408 with matt blasted GS finish."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The row-specific assembly STEP material metadata was placeholder Generic, so material is taken from the BOM-provided manufacturer route rather than STEP material metadata."
how_to_make:
  summary: "Procure as the standard GanterNorm GN 328.5-140-B-GS stainless steel bow handle; if modeled locally later, treat it as a stainless precision-cast handle with finish machining of the mounting features and matte blasting."
  manufacturing_steps:
    - "Specify and procure GanterNorm GN 328.5-140-B-GS, matching l1 140, Form B, and GS matte blasted finish."
    - "Receive and inspect the handle against the CAD envelope and mounting-end geometry."
    - "For a local manufacturing approximation, investment-cast stainless steel 1.4408 to the U-handle shape, finish-machine or drill the mounting holes/counterbores for the Form B interface, deburr, and matte blast the surface."
    - "Install with the mating fasteners or mounting hardware required by the reAM250 panel or door assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B2_handle.step; research/ream250_bom/ream250_bom_row_0010_1B2__views_2x2.png; https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Buegelgriffe-Edelstahl"
    cited_fact_or_basis: "BOM row 10 gives product GN 328.5-140-B-GS and manufacturer GanterNorm. The Ganter BOM URL canonical route identifies GN 328.5 as stainless steel precision-cast bow handles, material 1.4408, finish GS matte blasted, and includes Form B in the product-family variants. The CAD preview shows a single U-shaped handle with two mounting ends."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Procurement is preferred for KB modeling because this is an identified catalog standard component with manufacturer and product number."
    - "The local manufacturing approximation is inferred from the sourced precision-cast material description and visible mounting geometry; the source does not provide a full process plan."
  uncertainty_notes:
    - "targeted_web_search: BOM-provided Ganter URL and canonical Ganter page were checked first; no separate drawing or process plan was needed for the procurement route, and the detailed local casting/machining sequence remains an inferred approximation."
kb_implications:
  - "item_granularity: simple_part - model later as one catalog stainless steel bow handle GN 328.5-140-B-GS; do not split into raw casting, finish, and mounting features unless this handle becomes a major import-mass contributor."
---

Research result for reAM250 BOM row 10.
