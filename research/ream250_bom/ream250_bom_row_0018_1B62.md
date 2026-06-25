---
row_identity:
  item: "1B62"
  cad_file: "1B62_cover"
  source_row_number: 18
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Horizontal side-mount toggle clamp used as door/cover hold-down hardware on the reAM250 schlieren imaging door/cover area; the BOM text identifies a GN 820.2 Type MFC U-bar clamp with spindle assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.elesa-ganter.com/en/www/Toggle-power-and-hook-clamps--Horizontal-acting-toggle-clamps--GN8202"
    cited_fact_or_basis: "BOM row 18 names item 1B62/1B62_cover and describes it as 'GN 820.2-Toggle clamps, Type MFC, U-bar version, with two'. The manifest maps the row to parent assembly 1B50_schlieren_imaging_door and reports assembly_only CAD export. The full assembly STEP contains product 1C0_clamp_GN 820_2-230-MFC with the GN 820.2 Type MFC clamp description. Elesa+Ganter states GN 820.2 clamps work by the toggle principle and that Type MFC is the U-bar version with GN 708.1 spindle assembly."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Treat the BOM description and matching full-assembly 1C0 standard clamp as the intended physical item for row 18, while preserving the leased row identity as 1B62."
  uncertainty_notes:
    - "CAD evidence is limited: the row export is assembly_only and the rendered contact sheet at research/ream250_bom/ream250_bom_row_0018_1B62__views_2x2.png shows a ring/cover feature, not the toggle clamp."
mass:
  value_kg: 0.42
  basis: "Per-unit mass for one physical clamp. The official Elesa+Ganter SKU data for GN 820.2-230-MFC lists logoweight 420 g; BOM quantity is 1, so row total is also about 0.42 kg. The row's available parent STEP measured 1 solid, 2573.818 mm^3 volume, 3560.408 mm^2 area, and 55.88 x 39.87 x 45.80 mm bounding box, but that ring-like geometry is not used for clamp mass. The matching 1C0 clamp STEP measured 7 solids, 72479.263 mm^3 volume, 37940.166 mm^2 area, and 196.59 x 121.00 x 43.00 mm bounding box, consistent with a larger clamp assembly but still lacking material metadata."
  source:
    url_or_path: "https://www.elesa-ganter.com/static/products/ganter/skus/GN%20820.2.en.js?dc=202606180906444; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/1B50_schlieren_imaging_door.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1C0_clamp_GN 820_2-230-MFC.step"
    cited_fact_or_basis: "The official SKU table row for GN 820.2-230-MFC gives Size 230, Type MFC, steel material code, 1700 N holding force, M8 spindle thread, and logoweight 420 g. FreeCAD measurements show the leased row CAD path is a small ring-like parent feature rather than the clamp."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Use the vendor SKU weight directly because it matches the BOM product family and the full-assembly clamp product name better than the collapsed row CAD."
  uncertainty_notes:
    - "The BOM row text is truncated before the exact size suffix; size 230 is resolved from the full assembly product name 1C0_clamp_GN 820_2-230-MFC, not from a row-specific 1B62 solid."
material:
  primary_material: "Case-hardened C10 steel clamp body/linkage with zinc-plated, blue-passivated finish; tempered bearing pins; zinc-plated steel GN 708.1 spindle assembly with 85 Shore A rubber tip; oil-resistant red plastic hand grip; lubricated moving parts."
  source:
    url_or_path: "https://www.elesa-ganter.com/en/www/Toggle-power-and-hook-clamps--Horizontal-acting-toggle-clamps--GN8202; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Elesa+Ganter's GN 820.2 steel specification lists case-hardened C10 steel with zinc-plated blue-passivated finish, tempered bearing pins, special grease on moving parts, oil-resistant red plastic hand grip, and GN 708.1 Type A steel spindle assembly with rubber tip 85 Shore A. Local STEP material extraction for 1B62_cover returned no matches; extraction for 1C0_clamp_GN 820_2-230-MFC found the product definition but no material or density property."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Use the steel GN 820.2 material set because the matched SKU is GN 820.2-230-MFC with steel material code, not the GN 820.2-NI stainless variant."
  uncertainty_notes:
    - "No row-specific non-placeholder STEP material metadata resolved this item; material is based on the row-matched official product family and full-assembly product identity."
how_to_make:
  summary: "Treat as a configured standard mechanical toggle clamp for row-level modeling: procure or fabricate the GN 820.2-230-MFC style clamp, then install and adjust it on the schlieren imaging door/cover interface."
  manufacturing_steps:
    - "Fabricate the clamp base, U-bar/linkage, lever, washers, and pins from steel stock by stamping, cutting, forming, machining, drilling, deburring, and heat treatment where required."
    - "Apply zinc plating and blue passivation to the steel clamp parts; lubricate moving joints with suitable grease."
    - "Make or source the GN 708.1 M8 spindle assembly with steel threaded screw and bonded rubber pressure tip, plus the oil-resistant plastic hand grip."
    - "Assemble pivots, rivets/pins, lever, U-bar, flanged washers, spindle, and grip; function-test toggle locking motion and holding force."
    - "Install the clamp on the door/cover structure and adjust spindle contact against the mating latch surface."
  source:
    url_or_path: "https://www.elesa-ganter.com/en/www/Toggle-power-and-hook-clamps--Horizontal-acting-toggle-clamps--GN8202; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The official product page identifies Type MFC as the U-bar version with GN 708.1 spindle assembly and lists the component material/finish set. The full assembly STEP provides the matching configured product name GN 820.2-230-MFC. targeted_web_search: searched 'GN 820.2-230-MFC manufacturing process' and 'GN 820.2 toggle clamp datasheet manufacturing' and found product specifications/catalog data, not a row-specific factory process plan."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Use standard metal clamp fabrication steps inferred from the vendor's component materials and finish because no first-party process plan was found."
    - "For near-term KB modeling, procurement plus installation is the practical route; local manufacture would be a later sub-BOM decomposition."
  uncertainty_notes:
    - "A future local-manufacturing model should decompose the clamp internals, heat treatment, plating, rubber pad, plastic grip, lubrication, assembly, and inspection rather than treating all steps as one opaque operation."
kb_implications:
  - "item_granularity: simple_part - Model as reusable standard mechanical toggle-clamp hardware for this row, not as the misleading 1B62_cover ring CAD export; decompose into clamp subparts only if local toggle-clamp manufacture becomes important."
---
