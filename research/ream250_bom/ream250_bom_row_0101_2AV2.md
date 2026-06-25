---
row_identity:
  item: "2AV2"
  cad_file: "2AV2_DIN 912 - M8x1,25x35x31,875"
  source_row_number: 101
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "M8 DIN 912 cylinder/socket head cap screw used as one of ten machine fasteners in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV2_DIN 912 - M8x1,25x35x31,875.step; research/ream250_bom/ream250_bom_row_0101_2AV2__views_2x2.png"
    cited_fact_or_basis: "BOM row 101 identifies item 2AV2, quantity 10, CAD file 2AV2_DIN 912 - M8x1,25x35x31,875, and description 'cylinder head cap screw'. The manifest maps the row to a matched part STEP. FreeCAD measured one solid with bounding box 43.00 x 14.07 x 14.07 mm; the rendered contact sheet shows a cylindrical socket-head screw with an internal hex drive and threaded shaft."
    evidence_basis: "bom_provided"
  assumptions:
    - "The supplied per-row STEP represents one physical screw for this BOM row."
  uncertainty_notes:
    - "The local row evidence identifies the screw standard/size family but not the exact mating joint or clamped reAM250 subassembly."
mass:
  value_kg: 0.0209
  basis: "Per-unit mass for one screw. FreeCAD volume is 2660.509 mm^3 = 2.660509e-6 m^3. Assembly STEP metadata gives density 7850 kg/m^3 for Steel, Mild, so 2.660509e-6 m^3 * 7850 kg/m^3 = 0.0209 kg per screw. BOM quantity is 10, so the row total is about 0.209 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV2_DIN 912 - M8x1,25x35x31,875.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 2660.509 mm^3, area 1532.851 mm^2, and bounding box 43.00 x 14.07 x 14.07 mm. Assembly STEP material extraction for product 2AV2_DIN 912 - M8x1,25x35x31,875 returned material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The CAD solid volume is treated as the physical solid volume of one screw, including the modeled socket recess and threads."
  uncertainty_notes:
    - "The estimate depends on the CAD thread/socket representation matching the real screw; catalog mass was not provided in the BOM row."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Assembly STEP material extraction for product 2AV2_DIN 912 - M8x1,25x35x31,875 returned material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "DIN 912 socket head cap screws are commonly sold in several steel grades and finishes, but this row's local STEP metadata resolves only the broad mild-steel material family, not a property class or coating."
how_to_make:
  summary: "Prepare as a standard DIN 912 M8x35 socket head cap screw; a Manufacturing route would form or machine a steel screw blank, create the cylindrical head and hex socket, roll or cut the M8 thread, apply heat treatment/coating if required, and inspect thread/head dimensions"
  manufacturing_steps:
    - "Start from steel wire, rod, or screw blank stock sized for an M8 socket head cap screw."
    - "Cold-head or machine the cylindrical cap head and shank."
    - "Broach or form the internal hex socket in the head."
    - "Roll or cut the M8 x 1.25 thread along the shaft length shown in the CAD."
    - "Apply any required heat treatment, coating, cleaning, and dimensional inspection for the DIN 912 interface."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0101_2AV2__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV2_DIN 912 - M8x1,25x35x31,875.step; https://accu-components.com/us/metric-cap-head-screws/386839-SSC-M8-35-12-9-Z; https://www.item24.com/en-de/hexagon-socket-head-cap-screw-din-912-m8x35-bright-zinc-plated-65515"
    cited_fact_or_basis: "The CAD preview shows a socket-head threaded screw geometry. The Accu M8 x 35 mm DIN 912 page identifies this size family as full-thread socket head cap screws and lists M8, 35 mm length, DIN 912 / ISO 4762, steel material, and zinc-plated finish for one common variant. The item24 page lists a DIN 912 M8x35 bright-zinc-plated hexagon socket head cap screw with cylindrical head. targeted_web_search: tried 'DIN 912 M8 x 35 socket head cap screw dimensions material steel' and 'DIN 912 M8 x 35 socket head cap screw bright zinc plated steel M8x35'; found matching standard-part/vendor identity and material examples, but no row-specific reAM250 manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route is inferred from the row's standard screw geometry and common fastener production methods, not from a reAM250 production drawing."
  uncertainty_notes:
    - "The row does not state property class, coating, or actual supplier process; those details matter for strength/corrosion modeling but not for coarse BOM mass closure."
kb_implications:
  - "item_granularity: simple_part - standard M8 DIN 912 socket head cap screw; later KB modeling should reuse a generic steel metric socket-head screw item rather than create a machine-specific part."
---

Research result for reAM250 BOM row 101.
