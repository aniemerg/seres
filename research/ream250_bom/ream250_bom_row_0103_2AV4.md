---
row_identity:
  item: "2AV4"
  cad_file: "2AV4_DIN 912 - M5x0,8x8x6"
  source_row_number: 103
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "M5 x 0.8 x 8 mm DIN 912 socket-head cap screw used as a small reusable mechanical fastener in the reAM250 assembly; the BOM row quantity is 2."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV4_DIN 912 - M5x0,8x8x6.step; research/ream250_bom/ream250_bom_row_0103_2AV4__views_2x2.png"
    cited_fact_or_basis: "BOM row 103 and the manifest identify item 2AV4 as quantity 2 of '2AV4_DIN 912 - M5x0,8x8x6' with description 'cylinder head cap screw'. FreeCAD measured one solid and the rendered CAD contact sheet shows a socket-head screw with cylindrical head, hex socket, and short threaded shank."
    evidence_basis: "bom_provided"
  assumptions:
    - "The per-row STEP file represents one physical screw for this BOM row."
  uncertainty_notes:
    - "The BOM row does not state the exact mating component or fastening location within the reAM250 assembly."
mass:
  value_kg: 0.00311
  basis: "Per-unit estimate for one screw. FreeCAD volume is 395.896 mm^3, equal to 3.95896e-7 m^3. Assembly STEP material extraction gives Steel, Mild with density 7850 kg/m^3, so 3.95896e-7 m^3 * 7850 kg/m^3 = 0.003108 kg, rounded to 0.00311 kg per unit. BOM quantity is 2, so the row total is about 0.00622 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV4_DIN 912 - M5x0,8x8x6.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 395.896 mm^3, area 399.081 mm^2, and bounding box about 13.00 x 9.20 x 9.20 mm. Local assembly STEP material extraction for product '2AV4_DIN 912 - M5x0,8x8x6' returned material 'Steel, Mild' with density 7850.0. kb/materials/properties.yaml lists steel density 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical solid volume of one screw."
    - "The STEP material density and local steel density table are treated as the same generic steel density constant."
  uncertainty_notes:
    - "The result depends on the CAD solid including the thread/socket geometry at sufficient fidelity; no catalog weight was provided for cross-checking."
material:
  primary_material: "mild/generic steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product '2AV4_DIN 912 - M5x0,8x8x6' returned non-placeholder material 'Steel, Mild' with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata gives a steel family but not a property class, heat treatment, coating, or exact alloy grade for the DIN 912 screw."
how_to_make:
  summary: "Procure as a standard DIN 912 / ISO 4762 M5 x 8 socket-head cap screw, or locally make as small steel fastener hardware by forming or machining the head and shank, creating the hex socket, threading the shank, heat treating or finishing as required, and inspecting thread/socket fit."
  manufacturing_steps:
    - "Select steel wire, rod, or screw blank stock sized for an M5 socket-head cap screw."
    - "Form or machine the cylindrical head and short shank geometry."
    - "Broach or form the internal hex socket in the head."
    - "Roll or cut the M5 x 0.8 external thread to the required length."
    - "Apply any required heat treatment, coating, cleaning, and dimensional inspection for screw service."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0103_2AV4__views_2x2.png; https://www.fasteners.eu/standards/iso/4762/; https://www.intafast.com/wp-content/uploads/2019/09/Din912_ISO_4762_Socket_cap_screws-1.pdf"
    cited_fact_or_basis: "BOM row 103 identifies a DIN 912 M5x0.8x8 cylinder head cap screw and the CAD preview shows the expected socket-head screw geometry. Fasteners.eu lists ISO 4762 as hexagon socket head cap screws, current norm DIN EN ISO 4762, equivalent norm DIN 912, with M5 pitch 0.8 and steel property-class options. The Intafast DIN 912 / ISO 4762 sheet identifies the standard as hexagon socket head screws and lists material as steel for grade 12.9. The detailed local forming, broaching, threading, heat-treatment, and inspection route is inferred rather than stated for this row. targeted_web_search: tried 'DIN 912 M5 x 8 socket head cap screw steel cylinder head cap screw', 'ISO 4762 DIN 912 socket head cap screw steel material', and 'socket head cap screws manufacturing cold headed thread rolled'; results resolved standard identity/material conventions but did not provide a row-specific production process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For local KB planning, a standard screw-making route is sufficient because the row is a finished commodity fastener rather than a calibrated machine subsystem."
    - "Heat treatment and coating requirements should be chosen later from the required fastener property class and service environment."
  uncertainty_notes:
    - "The row evidence does not specify property class, coating, or actual manufacturing process used by the original supplier."
kb_implications:
  - "item_granularity: simple_part - finished standard DIN 912 / ISO 4762 M5 socket-head cap screw; later KB work should map it to reusable standard steel screw or fastener-kit hardware rather than raw stock or a purchased module."
---

# reAM250 BOM Row 103 - 2AV4

Research result for the leased reAM250 BOM row.
