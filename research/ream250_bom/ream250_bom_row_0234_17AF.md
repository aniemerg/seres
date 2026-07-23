---
row_identity:
  item: "17AF"
  cad_file: "17AF_handle"
  source_row_number: 234
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.ganternorm.com/de/produkte/1.2-Bedienen-mit-Maschinen-und-Geraetegriffen/Buegelgriffe/GN-328.5-Edelstahl-Buegelgriffe#l1%3Dc(120)%3BForm%3Du(5e72aa81-7282-4de6-aa3f-99d6b8e98e5d)%3BOberfl%C3%A4che%3Du(5ac173de-c979-4e10-ab22-480f0ce07560)"
function:
  summary: "Cabinet U-handle / bridge handle for manually gripping and opening or positioning a machine cover, door, or panel on the reAM250 assembly."
  source:
    url_or_path: "https://www.ganternorm.com/en/products/1.2-Operating-by-using-machine-anddevicehandles/Cabinet-U-handles/GN-328.5-Cabinet-U-Handles-Stainless-Steel; research/ream250_bom/ream250_bom_row_0234_17AF__views_2x2.png"
    cited_fact_or_basis: "Ganter identifies GN 328.5 as cabinet U-handles with stable ergonomic design and finger recesses; the CAD preview shows a U-shaped handle with two end mounting pads."
    evidence_basis: "bom_provided"
  assumptions:
    - "The reAM250 BOM item 17AF uses the standard handle in its normal machine-panel gripping role."
  uncertainty_notes: []
mass:
  value_kg: 0.523
  basis: "Per unit for quantity 1. D&D Barry's row-matched table lists GN 328.5-140-B-GS with weight 523 g. Local FreeCAD measured the supplied STEP as one solid with volume 69983.609 mm^3 and bounding box 166.50 x 60.03 x 28.00 mm; using the local stainless_steel density constant of 8000 kg/m^3 would give about 0.560 kg, close enough to support the catalog mass scale."
  source:
    url_or_path: "https://www.ddbarry.com.au/product/gn-328-5/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AF_handle.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "independent web search found D&D Barry table row GN 328.5-140-B-GS with weight 523 g. FreeCAD measured 69983.609 mm^3 for 17AF_handle.step. bom_url_route_check: the BOM-provided Ganter URL was checked first; it resolves product family, material, and dimensions, but the visible selected-part weight on that page is not locked to the BOM's 140-B variant, so the row-matched D&D Barry table was used for mass."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The D&D Barry table weight is interpreted as grams per one handle."
    - "The STEP volume is treated only as a sanity check, not as the primary mass value."
  uncertainty_notes:
    - "The supplied assembly STEP material metadata reports PC/ABS Plastic with an implausible density for this stainless handle, so that metadata was rejected for mass."
material:
  primary_material: "AISI 316 stainless steel precision casting with matte shot-blasted GS finish."
  source:
    url_or_path: "https://www.ganternorm.com/en/products/1.2-Operating-by-using-machine-anddevicehandles/Cabinet-U-handles/GN-328.5-Cabinet-U-Handles-Stainless-Steel"
    cited_fact_or_basis: "Ganter specifies GN 328.5 as stainless steel precision casting AISI 316 with matte shot-blasted finish GS."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The German Ganter page names stainless cast material 1.4408 for the same GN 328.5 family; this is compatible with the AISI 316 stainless family but should be normalized later if the KB needs exact grade semantics."
    - "The local STEP material extractor returned PC/ABS Plastic, conflicting with the row-matched vendor material, so the CAD metadata should not be used as material authority for this row."
how_to_make:
  summary: "Make a stainless precision-cast handle, apply matte shot-blasted finish, and provide the Type B front-mounting holes"
  manufacturing_steps:
    - "For local manufacture, precision-cast the U-handle body in AISI 316-family stainless steel."
    - "Finish to GS matte shot-blasted surface and verify the 140 mm grip length / 166.5 mm overall size family."
    - "Provide Type B operator-side mounting geometry and inspect fit against the panel fasteners."
  source:
    url_or_path: "https://www.ganternorm.com/en/products/1.2-Operating-by-using-machine-anddevicehandles/Cabinet-U-handles/GN-328.5-Cabinet-U-Handles-Stainless-Steel; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AF_handle.step"
    cited_fact_or_basis: "Ganter states GN 328.5 is stainless steel precision casting with GS matte shot-blasted finish and has Type B mounting from the operator side; the BOM product ID fixes the 140-B-GS variant."
    evidence_basis: "bom_provided"
  assumptions:
    - "The manufacturing route keeps only the vendor-stated process family and final geometry; it does not model foundry tooling or detailed finishing fixtures."
  uncertainty_notes:
    - "The exact casting tooling, post-cast machining allowance, and inspection tolerances are not provided by the BOM or vendor page."
kb_implications:
  - "item_granularity: simple_part - Model as reusable standard stainless cabinet U-handle hardware rather than a machine-specific module."
---
