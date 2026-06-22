---
row_identity:
  item: "61B"
  cad_file: "61B_countersunk_bolt_DIN 7991 - M5x30"
  source_row_number: 267
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "M5 x 30 DIN 7991 countersunk hex-socket screw used as a flush-head mechanical fastener."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/61B_countersunk_bolt_DIN 7991 - M5x30.step"
    cited_fact_or_basis: "BOM row 267 describes item 61B as 'countersunk screw'; the CAD filename states DIN 7991 - M5x30; FreeCAD measured one solid with a 30.00 mm length and 9.43 mm maximum head diameter; the rendered preview shows a countersunk head, cylindrical shank, and internal hex socket."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes: []
mass:
  value_kg: 0.00521
  basis: "FreeCAD volume 663.763 mm^3 converted to 6.63763e-7 m^3 and multiplied by the assembly STEP material density 7850 kg/m^3 for Steel, Mild. BOM quantity is 1, so the row total is also about 0.00521 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured the part STEP volume as 663.763 mm^3; the assembly STEP material extractor matched product '61B_countersunk_bolt_DIN 7991 - M5x30' to material 'Steel, Mild' with density 7850.0 kg/m^3; kb/materials/properties.yaml also lists generic steel density as 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single-solid CAD volume is treated as the solid steel volume of one screw."
  uncertainty_notes:
    - "Threads and socket details are represented by the exported CAD; any small modeling simplification directly affects this gram-scale mass estimate."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product '61B_countersunk_bolt_DIN 7991 - M5x30' to material 'Steel, Mild' with density 7850.0 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The CAD metadata does not specify a fastener property class, coating, or heat treatment."
how_to_make:
  summary: "Model as a standard steel countersunk socket screw made from steel fastener stock by heading, socket forming, thread rolling, and finishing."
  manufacturing_steps:
    - "Cut steel wire or rod blank sized for an M5 x 30 screw."
    - "Cold-head or forge the countersunk head."
    - "Form the internal hex socket by punch or broach operation."
    - "Roll the M5 external thread and apply any required heat treatment or finish."
    - "Inspect overall length, countersunk head geometry, socket fit, and thread fit before assembly use."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/61B_countersunk_bolt_DIN 7991 - M5x30.step; https://accu-components.com/us/countersunk-socket-head-screws/472035-SSK-M5-30-10-9; https://fastcoindustries.com/thread-rolling-service-cold-heading-fastener-manufacturers-usa/"
    cited_fact_or_basis: "BOM/CAD identity states DIN 7991 - M5x30 countersunk screw; CAD preview shows a countersunk head, cylindrical shank, and internal hex socket. Accu lists a DIN 7991 M5 x 30 steel countersunk socket screw with 30 mm overall length, 90 degree countersunk head, and 3 mm socket size. Fastco describes thread rolling as dies pressing against a cold-headed blank to form external screw threads. targeted_web_search: searched 'DIN 7991 M5 x 30 countersunk socket screw steel dimensions weight' and 'socket countersunk screws manufacturing process cold forming thread rolling'; found standard fastener catalog and screw-manufacturing references, but no row-specific supplier process route beyond standard fastener practice."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A standard fastener manufacturing route is used because the row is a commodity DIN 7991 screw rather than a custom machined reAM250 part."
  uncertainty_notes:
    - "The exact supplier process, property class, coating, and heat treatment are not resolved from the BOM/CAD evidence."
kb_implications:
  - "item_granularity: simple_part - finished commodity M5 x 30 DIN 7991 steel countersunk screw; later KB modeling should reuse or create generic standard fastener hardware rather than raw stock or a reAM250-specific part."
---
