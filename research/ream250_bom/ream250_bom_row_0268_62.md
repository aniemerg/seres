---
row_identity:
  item: "62"
  cad_file: "62_bearing_DIN 625 SKF - SKF 61800"
  source_row_number: 268
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.skf.com/de/products/rolling-bearings/ball-bearings/deep-groove-ball-bearings/productid-61800"
function:
  summary: "Thin single-row deep-groove ball bearing used to support a small rotating shaft with low-friction radial guidance; SKF 61800 is a 10 mm bore, 19 mm outside diameter, 5 mm wide bearing."
  source:
    url_or_path: "https://www.skf.com/products/rolling-bearings/ball-bearings/deep-groove-ball-bearings/productid-61800?failover=true; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/62_bearing_DIN 625 SKF - SKF 61800.step; research/ream250_bom/ream250_bom_row_0268_62__views_2x2.png"
    cited_fact_or_basis: "BOM row identifies manufacturer SKF and product 61800. SKF product route identifies product 61800 as a deep groove ball bearing with 10 mm bore, 19 mm outside diameter, and 5 mm width. FreeCAD measured one solid with volume 660.683 mm^3 and bounding box about 20.57 x 20.57 x 5.00 mm; rendered preview shows inner/outer rings, balls, and cage."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row item is the open SKF 61800 family member named in the BOM, not a sealed or shielded suffix variant."
  uncertainty_notes:
    - "The CAD measurement slightly overstates the visual-triage outer diameter because tessellation/geometry bounds include fine edge detail, but the preview and SKF dimensions agree on the thin bearing form."
mass:
  value_kg: 0.0052
  basis: "Per-unit mass estimate for one bearing: 660.683 mm^3 = 6.60683e-7 m^3, multiplied by local STEP material density 7850 kg/m^3 gives 0.00519 kg. BOM quantity is 2, so row total is about 0.0104 kg. SKF's public product snippet reports net weight about 0.01 lb, consistent as a rounded catalog value."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/62_bearing_DIN 625 SKF - SKF 61800.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.skf.com/us/products/rolling-bearings/ball-bearings/deep-groove-ball-bearings/productid-61800"
    cited_fact_or_basis: "FreeCAD measured the row STEP volume as 660.683 mm^3. Local assembly STEP material extraction for product 62_bearing_DIN 625 SKF - SKF 61800 returned material Steel, Mild with density 7850 kg/m^3. SKF product route for 61800 reports dimensions and a rounded net weight of about 0.01 lb."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume represents one complete bearing, including rings, balls, and cage."
    - "The STEP density is used as the calculation constant for this row-specific steel model."
  uncertainty_notes:
    - "Catalog net weight is rounded coarsely, so the CAD-volume calculation is the preferred per-unit mass for KB planning."
material:
  primary_material: "Steel bearing assembly; local STEP metadata says Steel, Mild, while matching vendor/distributor evidence for SKF 61800 states steel bearing and steel cage."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.purvisindustries.com/skf-61800"
    cited_fact_or_basis: "Local assembly STEP material extraction returned Steel, Mild for the row product. A matching SKF 61800 distributor listing states Bearing Material: Steel and Steel Cage. bom_url_route_check: the BOM-provided SKF URL was checked first and resolved product identity, dimensions, load/speed class, and weight, but did not expose a specific material field in the accessible page text; the different-domain source was used only to resolve material wording for the same SKF 61800 row identity."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "For downstream KB modeling, treat this as a generic steel precision bearing unless a later SKF engineering drawing specifies a bearing-steel grade."
  uncertainty_notes:
    - "The exact bearing steel grade, heat treatment, lubricant, and cage stamping alloy are not resolved by the BOM-side evidence."
how_to_make:
  summary: "Procure as a standard SKF 61800 deep-groove ball bearing; for local closure, model later as a precision steel bearing assembly rather than a custom reAM250-machined part."
  manufacturing_steps:
    - "Buy or inventory SKF 61800 / DIN 625 thin-section deep-groove ball bearing matching 10 mm bore, 19 mm outside diameter, and 5 mm width."
    - "Incoming inspection should verify bearing designation, open bearing style, dimensions, free rotation, and absence of contamination or brinelling."
    - "Install into the mating bearing seat/shaft interface as a reusable precision component."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.skf.com/de/products/rolling-bearings/ball-bearings/deep-groove-ball-bearings/productid-61800; research/ream250_bom/ream250_bom_row_0268_62__views_2x2.png"
    cited_fact_or_basis: "BOM row gives SKF and product 61800 with SKF product URL. SKF route identifies the row as a deep-groove ball bearing. CAD preview confirms the row is a complete bearing geometry rather than raw stock or a custom machined placeholder."
    evidence_basis: "bom_provided"
  assumptions:
    - "Near-term KB modeling should use procurement/import for this precision purchased component until a bearing sub-BOM and precision bearing manufacturing workflow are intentionally modeled."
  uncertainty_notes:
    - "A self-manufacturing route would require additional modeling for hardened races, balls, cage, grinding/lapping, lubrication, cleaning, and bearing-grade inspection."
kb_implications:
  - "item_granularity: purchased_module - Treat row 62 as a standard SKF precision bearing component for now; later consolidation should map it to a reusable bearing item family rather than a reAM250-specific custom part."
---
