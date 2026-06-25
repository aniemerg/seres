---
row_identity:
  item: "2AV5"
  cad_file: "2AV5_DIN 912 - M8x1,25x50x28"
  source_row_number: 104
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "DIN 912 / ISO 4762-style M8 socket head cap screw used as reusable machine fastening hardware; the BOM row quantity is 18."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV5_DIN 912 - M8x1,25x50x28.step; research/ream250_bom/ream250_bom_row_0104_2AV5__views_2x2.png; https://www.metricmcc.com/socket-head-cap-screws"
    cited_fact_or_basis: "BOM and manifest row 104 identify item 2AV5 as quantity 18 of '2AV5_DIN 912 - M8x1,25x50x28' with description 'cylinder head cap screw'. FreeCAD measured one solid, and the rendered contact sheet shows a socket-head screw with cylindrical head, hex socket, and shank. Metric & Multistandard describes socket head cap screws as threaded fasteners with cylindrical heads and recessed hexagon drives."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN 912 file designation is treated as the row's standard fastener family, and the CAD shape confirms the BOM description."
  uncertainty_notes: []
mass:
  value_kg: 0.0268
  basis: "Per-unit mass estimate for one screw. FreeCAD volume is 3414.492 mm^3, equal to 3.414492e-6 m^3. Assembly STEP material metadata gives Steel, Mild with density 7850 kg/m^3, so 3.414492e-6 m^3 * 7850 kg/m^3 = 0.0268 kg. BOM quantity is 18, so the row total is about 0.482 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV5_DIN 912 - M8x1,25x50x28.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 3414.492 mm^3, area 1909.842 mm^2, and bounding box about 58.00 x 14.07 x 14.07 mm. Local assembly STEP material extraction for product 2AV5_DIN 912 - M8x1,25x50x28 returned material 'Steel, Mild' and density 7850.0. kb/materials/properties.yaml lists steel density 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP solid is treated as the physical solid volume of one screw."
    - "The local steel density constant is used directly for the STEP material's mild-steel density."
  uncertainty_notes:
    - "The estimate depends on the CAD solid retaining the real screw volume, including the socket recess and thread representation, rather than a simplified envelope."
material:
  primary_material: "mild steel fastener"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://www.intafast.com/wp-content/uploads/2019/09/Din912_ISO_4762_Socket_cap_screws-1.pdf"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 2AV5_DIN 912 - M8x1,25x50x28 returned material 'Steel, Mild'. The Intafast DIN 912 / ISO 4762 socket cap screw data sheet lists material as steel for Grade 12.9 screws; this is a standards-family cross-check, not the primary row-specific material source."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The row does not state property class, coating, or exact steel grade; downstream KB modeling should avoid assuming 8.8, 10.9, 12.9, black oxide, or zinc plating unless a purchase record or drawing confirms it."
how_to_make:
  summary: "Treat as standard finished steel socket-head cap screw hardware: prepare as DIN 912 / ISO 4762 M8 x 50-like fastener, or locally manufacture from steel wire/rod by heading the cylindrical socket head, forming the hex socket, rolling the thread, heat treating or finishing as required, and inspecting thread and drive geometry"
  manufacturing_steps:
    - "Start with steel wire or rod stock sized for an M8 socket-head screw blank."
    - "Cold-head or otherwise form the cylindrical cap head and shank blank."
    - "Broach or form the internal hex socket in the head."
    - "Roll the external metric thread on the shank."
    - "Apply any required heat treatment, coating, cleaning, and dimensional inspection for the specified property class and finish."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0104_2AV5__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV5_DIN 912 - M8x1,25x50x28.step; https://www.rotaloc.com/processes-capabilites/metal-molding-forming-processing/cold-heading-thread-rolling-tapping; https://www.metricmcc.com/socket-head-cap-screws"
    cited_fact_or_basis: "The CAD preview shows a one-piece socket-head screw with hex socket and shank. Rotaloc describes cold heading as commonly used for screw heads and thread rolling as forming helical threads by rolling rather than cutting. Metric & Multistandard identifies DIN 912 socket head cap screws as stocked standard threaded fasteners. targeted_web_search: tried 'DIN 912 socket head cap screw M8x50 material steel class 8.8 12.9' and 'socket head cap screw manufacturing cold heading thread rolling heat treatment'; results provided standard-part and generic fastener-manufacturing evidence, but no row-specific manufacturing process for item 2AV5."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the row's standard socket-head screw identity and visible one-piece screw geometry."
  uncertainty_notes:
    - "The row evidence does not resolve property class, coating, actual heat treatment, or whether the production route used cold heading versus machining for this specific screw."
kb_implications:
  - "item_granularity: simple_part - Model later as reusable standard M8 steel socket-head cap screw hardware or a fastener-kit member, not as raw stock or a purchased functional module."
---

Research result for the leased reAM250 BOM row.
