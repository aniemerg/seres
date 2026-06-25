---
row_identity:
  item: 2AVA
  cad_file: "2AVA_DIN 912 - M4x0,7x20x18,25"
  source_row_number: 109
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Socket-head cylinder cap screw used as M4 threaded fastening hardware in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AVA_DIN 912 - M4x0,7x20x18,25.step; research/ream250_bom/ream250_bom_row_0109_2AVA__views_2x2.png"
    cited_fact_or_basis: "BOM row 109 identifies item 2AVA, quantity 20, CAD file '2AVA_DIN 912 - M4x0,7x20x18,25', description 'cylinder head cap screw'. The rendered CAD preview shows an externally threaded screw with cylindrical socket head and internal hex drive."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.00302
  basis: "Per screw. FreeCAD measured volume 384.920 mm^3 for one solid; assembly STEP material metadata gives Steel, Mild density 7850 kg/m^3. Calculation: 384.920e-9 m^3 * 7850 kg/m^3 = 0.0030216 kg per screw. BOM quantity is 20, so row total is about 0.0604 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AVA_DIN 912 - M4x0,7x20x18,25.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measurement: 1 solid, volume 384.920331 mm^3, area 430.857616 mm^2, bounding box 24.00 x 7.58 x 7.58 mm. Local assembly STEP material extractor matched product name to material 'Steel, Mild' with density 7850 kg/m^3; kb/materials/properties.yaml lists generic steel density 7850 kg/m^3."
    evidence_basis: bom_provided
  assumptions:
    - "The CAD solid represents one physical screw for the BOM row."
    - "The STEP density is interpreted as kg/m^3, consistent with the extractor note and local steel density table."
  uncertainty_notes:
    - "Thread and socket geometry are taken from the exported CAD; any supplier-specific head tolerances or minor chamfer differences would only slightly change this mass."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product '2AVA_DIN 912 - M4x0,7x20x18,25' returned material 'Steel, Mild' and density 7850 kg/m^3."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - "No coating, property class, or heat-treatment grade is specified by the BOM-side evidence."
how_to_make:
  summary: "Treat as standard M4 DIN 912 socket-head cap screw hardware.7 thread and 20 mm nominal length, or model later as a generic steel socket-head screw if local fastener production is expanded"
  manufacturing_steps:
    - "Verify thread, head diameter, socket drive, length, and quantity before installation."
    - "For later local manufacturing detail, split into steel wire/rod preparation, head forming, socket forming, thread rolling or cutting, finishing, and inspection."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0109_2AVA__views_2x2.png"
    cited_fact_or_basis: "BOM and manifest identify a cylinder head cap screw with CAD filename parameters DIN 912, M4x0.7, and 20 mm length; the rendered preview confirms socket-head screw geometry."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - "The BOM-side evidence does not specify a supplier part number, strength class, coating, or acceptance standard beyond the DIN 912-style designation in the CAD filename."
kb_implications:
  - "item_granularity: simple_part - Standard M4 socket-head cap screw hardware should map to a reusable fastener item rather than a reAM250-specific purchased module."
---
