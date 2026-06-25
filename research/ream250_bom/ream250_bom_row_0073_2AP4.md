---
row_identity:
  item: 2AP4
  cad_file: "2AP4_bolt_DIN 7991 - M3x8"
  source_row_number: 73
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: "M3 x 8 DIN 7991 countersunk hex-socket screw used as flush-head fastening hardware in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP4_bolt_DIN 7991 - M3x8.step; research/ream250_bom/ream250_bom_row_0073_2AP4__views_2x2.png"
    cited_fact_or_basis: "BOM row 73 names item 2AP4 as quantity 8 of '2AP4_bolt_DIN 7991 - M3x8' with description 'countersunk screw'; CAD preview shows a countersunk head, cylindrical threaded shank, and internal hex socket."
    evidence_basis: bom_provided
  assumptions:
    - "DIN 7991 M3x8 designation is treated as the row's fastener interface identity."
  uncertainty_notes: []
mass:
  value_kg: 0.000559
  basis: "Per-unit mass from FreeCAD STEP volume 71.217 mm^3 converted with assembly STEP material density 7850 kg/m^3 for Steel, Mild: 71.21694957592831e-9 m^3 * 7850 kg/m^3 = 0.000559 kg. BOM quantity is 8, so row total is about 0.00447 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP4_bolt_DIN 7991 - M3x8.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 71.21694957592831 mm^3 and bounding box 8.00 x 5.54 x 5.54 mm; local STEP material extraction matched this product to Steel, Mild with density 7850.0 kg/m^3."
    evidence_basis: bom_provided
  assumptions:
    - "The exported single CAD solid represents one physical screw from the BOM row."
  uncertainty_notes:
    - "Mass excludes any coating contribution not separately represented in the STEP material metadata."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local STEP material extractor matched product '2AP4_bolt_DIN 7991 - M3x8' to material 'Steel, Mild' with density 7850.0 kg/m^3."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - "No surface finish or fastener property class is specified by the BOM row or local material metadata."
how_to_make:
  summary: "Treat as standard DIN 7991 M3x8 countersunk screw hardware: prepare as a commodity fastener , or manufacture from mild-steel wire/rod by screw-heading, socket forming, thread rolling, and finishing"
  manufacturing_steps:
    - "Cut mild-steel wire or small rod blank to screw length allowance."
    - "Form the countersunk head and hex socket by cold heading or equivalent small-fastener forming."
    - "Roll or machine the M3 external thread to the DIN 7991 M3x8 interface."
    - "Deburr, finish or coat as required by the assembly environment, and inspect head geometry, socket fit, and thread gauge."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://accu-components.com/us/countersunk-socket-head-screws/495094-SSK-M3-8-10-9-Z; https://www.fasteners.eu/standards/din/7991/"
    cited_fact_or_basis: "BOM identifies a DIN 7991 M3x8 countersunk screw; vendor/standard-family searches show DIN 7991 socket countersunk screws are commodity fasteners available in steel variants. targeted_web_search: queries tried 'DIN 7991 M3x8 countersunk screw material steel dimensions' and 'DIN 7991 socket countersunk head cap screw M3 x 8 steel'; results confirmed row-matched commodity DIN 7991 M3x8 steel screw families but did not provide row-specific manufacturing process details."
    evidence_basis: engineering_hypothesis
  assumptions:
    - "Fastener manufacturing route is inferred from standard screw production practice and the CAD geometry, not from a row-specific process plan."
  uncertainty_notes:
    - "Final Manufacturing route may vary between cold forming, thread rolling, and machining depending on available small-fastener tooling."
kb_implications:
  - "item_granularity: simple_part - Standard DIN 7991 screw hardware should map to a reusable fastener item rather than a machine-specific module."
---
