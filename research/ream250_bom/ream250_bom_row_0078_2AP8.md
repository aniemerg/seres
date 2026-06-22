---
row_identity:
  item: "2AP8"
  cad_file: "2AP8_bolt_DIN EN ISO 4016 - M6x40"
  source_row_number: 78
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "M6 x 40 product-grade-C hexagon-head bolt used as one of four mechanical fasteners in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP8_bolt_DIN EN ISO 4016 - M6x40.step; research/ream250_bom/ream250_bom_row_0078_2AP8__views_2x2.png"
    cited_fact_or_basis: "BOM row 78 lists item 2AP8, quantity 4, CAD file '2AP8_bolt_DIN EN ISO 4016 - M6x40', and description 'grade C'. FreeCAD measured one solid with a bounding box about 11.55 x 11.55 x 44.00 mm; the rendered preview shows a hex head and cylindrical shank."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN EN ISO 4016 M6x40 designation is interpreted as a metric M6 bolt with nominal 40 mm length."
  uncertainty_notes: []
mass:
  value_kg: 0.01157
  basis: "Per unit: FreeCAD STEP volume 1474.330 mm^3 = 1.474330e-6 m^3; multiplied by the assembly STEP steel density 7850 kg/m^3 gives 0.01157 kg per bolt. BOM quantity is 4, so the row total is about 0.0463 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP8_bolt_DIN EN ISO 4016 - M6x40.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, 1474.330 mm^3 volume, 1053.851 mm^2 area, and about 11.55 x 11.55 x 44.00 mm bounding box. The local assembly STEP material extractor matched this product to material 'Steel' with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP volume represents one physical bolt closely enough for BOM mass estimation."
  uncertainty_notes:
    - "Thread-detail fidelity, chamfers, and any surface coating are not independently resolved, so use this as a CAD-derived planning mass rather than a catalog weight."
material:
  primary_material: "steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product '2AP8_bolt_DIN EN ISO 4016 - M6x40' to material 'Steel' and density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The exact steel property class, alloy, and finish or coating are not specified by the BOM fields or local STEP material metadata."
how_to_make:
  summary: "Procure as a standard ISO 4016 steel hexagon-head bolt, or manufacture from steel wire/bar stock by heading the hex head, forming the shank, rolling or cutting the M6 thread, finishing, and inspection."
  manufacturing_steps:
    - "Start from steel wire or bar stock sized for an M6 bolt blank."
    - "Cold-head or forge the hex head and shank blank; machining is a low-volume fallback."
    - "Roll or cut the M6 thread and trim to the M6x40 bolt length convention."
    - "Deburr, clean, optionally apply a protective finish, and inspect thread fit, head geometry, and length."
  source:
    url_or_path: "https://www.iso.org/standard/72580.html; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP8_bolt_DIN EN ISO 4016 - M6x40.step"
    cited_fact_or_basis: "ISO 4016:2022 identifies this standard family as steel hexagon-head bolts with metric coarse pitch threads M5 to M64 and product grade C. The row CAD is a one-solid hex-head bolt geometry. targeted_web_search: searched 'DIN EN ISO 4016 M6x40 grade C hexagon head bolt material' and 'ISO 4016 hexagon head bolts product grade C'; found standard/vendor pages confirming steel ISO 4016 hex-head bolt identity but no row-specific manufacturing process sheet."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Cold heading plus thread rolling is the representative scalable process route for standard steel bolts; machining is acceptable for low-volume local fabrication."
    - "The BOM row does not require a machine-specific custom part beyond a standard fastener."
  uncertainty_notes:
    - "The exact production route, heat treatment, property class, and coating are not specified for this row."
kb_implications:
  - "item_granularity: simple_part - Treat as reusable standard M6x40 ISO 4016 hex-head fastener or fastener-kit member, not as a unique custom part or raw stock."
---
