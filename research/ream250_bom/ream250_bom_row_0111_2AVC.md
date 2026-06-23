---
row_identity:
  item: "2AVC"
  cad_file: "2AVC_DIN 912 - M8x1,25x20x16,875"
  source_row_number: 111
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Metric DIN 912 M8 cylinder/socket head cap screw used as a removable threaded fastener in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0111_2AVC__views_2x2.png; https://accu-components.com/us/metric-cap-head-screws/3903-SSCF-M10-30-A2"
    cited_fact_or_basis: "BOM row 111 names item 2AVC, quantity 4, description 'cylinder head cap screw'; CAD preview shows a socket-head screw with external threads and internal hex drive; Accu states metric socket cap head screws use an internal socket drive for a hex key and are manufactured to DIN 912 / ISO 4762."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The exact installed joint location is not identified by the row context, so the function is limited to fastener role rather than a subsystem-specific joint."
mass:
  value_kg: 0.01497
  basis: "Per-unit mass from FreeCAD volume 1906.527 mm^3 = 1.906527e-6 m^3 multiplied by row-specific STEP material density 7850 kg/m^3 for Steel, Mild. BOM quantity is 4, so row total is about 0.0599 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AVC_DIN 912 - M8x1,25x20x16,875.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 1906.527 mm^3, area 1155.859 mm^2, bounding box about 28.00 x 14.07 x 14.07 mm. Assembly STEP material extraction for this product reports Steel, Mild with density 7850.0 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single exported STEP solid represents one physical screw from the BOM row."
  uncertainty_notes:
    - "CAD tessellation/solid volume may omit very small thread-root detail, but the error is minor for planning-scale mass."
material:
  primary_material: "Steel, Mild"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction matched product '2AVC_DIN 912 - M8x1,25x20x16,875' to non-placeholder material 'Steel, Mild' with density 7850.0 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "No strength class, coating, or heat-treatment grade is provided by the BOM row or STEP material metadata."
how_to_make:
  summary: "Best treated as a standard DIN 912 M8 socket head cap screw for procurement; a plausible local route is steel wire/bar stock, cold heading or machining of the cylindrical head and shank, hex-socket forming, thread rolling or cutting, and inspection."
  manufacturing_steps:
    - "Procurement route: source as a standard DIN 912 / ISO 4762 M8 socket head cap screw matching the row dimensions."
    - "Local manufacturing route: start from mild-steel wire or bar stock, form the cylindrical head and shank, create the internal hex socket, roll or cut the M8 thread, deburr, and inspect fit."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0111_2AVC__views_2x2.png; https://accu-components.com/us/metric-cap-head-screws/3903-SSCF-M10-30-A2; https://www.holo-krome.com/custom-fasteners.html"
    cited_fact_or_basis: "BOM and CAD identify a DIN 912 M8 socket head cap screw. Accu confirms this product family is manufactured to DIN 912 / ISO 4762 and available as socket cap screws. HOLO-KROME describes custom fasteners and cold-headed parts as part of socket fastener manufacturing capability. targeted_web_search: queries tried: 'DIN 912 M8 socket head cap screw cylinder head cap screw hex socket function' and 'socket head cap screw manufacturing cold heading thread rolling hex socket'; results supported standard DIN 912 procurement and cold-heading relevance but did not provide a row-specific manufacturing traveler."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB planning, standard screw manufacture can be approximated from generic socket-cap-screw production practice."
  uncertainty_notes:
    - "The local manufacturing route is process-plausible but not a row-specific vendor process specification."
kb_implications:
  - "item_granularity: simple_part - Finished standard DIN 912 socket head cap screw; later KB work should reuse or create generic standard fastener hardware rather than model this as raw stock or a purchased module."
---
