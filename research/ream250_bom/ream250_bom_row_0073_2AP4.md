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

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0073_2AP4.md
source_research_sha256: "3010d3e90e22d1808735564dcd7e811dcfacc3445702ec01bb4d32915ff090f6"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read function, quantity, CAD-derived mass, mild-steel material evidence, standard screw manufacturing route, kb implications, and preview showing a countersunk hex-socket M3 screw."
decomposition:
  decision: simple_part
  rationale: "The row is one standard fastener geometry repeated eight times. It has no meaningful internal closure subparts at this scale."
  proposed_subparts: []
process_abstraction:
  original_process_family: cold_heading_socket_forming_and_thread_rolling
  primary_process_bucket: fastener_forming_thread_rolling
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - thread_forming
    - surface_finishing
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: fastener_kit_small_fabrication_v0
      fit: partial
      reason: "Best existing small-fastener production anchor, though it aggregates many small fasteners instead of representing one DIN 7991 screw."
    - process_id: fastener_kit_medium_production_v0
      fit: supporting
      reason: "Documents forging, machining/threading, finishing, sorting, and kitting steps for steel fasteners."
    - process_id: metal_forming_basic_v0
      fit: supporting
      reason: "Relevant to head forming at coarse closure level."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Relevant for thread gauge, socket fit, and head geometry checks."
  abstraction_decision: keep_original_family
  rationale: "The source route already belongs to standard fastener forming and thread production. Later KB staging should likely merge it into a small fastener kit instead of creating one item per screw size."
  process_guardrails:
    tolerance: standard_thread_review
    surface_finish: coating_finish_review
    sealing_quality: not_applicable
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: flush head threaded fastening
  material: mild_steel
  scale_or_capacity:
    mass_kg: 0.000559
    bom_quantity: 8
    row_total_mass_kg: 0.00447
    scale_class: small
  geometry_form: din_7991_m3x8_countersunk_hex_socket_screw
merge_pool:
  eligible: true
  functional_purpose_key: fastening_hardware
  precision_guardrails:
    - m3_thread
    - countersunk_head
    - hex_socket_fit
    - coating_unspecified
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - fastener_forming_thread_rolling
  import_risk_factors:
    - "Property class, coating, and corrosion requirements are unresolved."
    - "Small screw production may be better modeled through reusable fastener kits than individual screw recipes."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups small steel fasteners and decides kit-level reuse."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review before assigning an item ID; likely candidate family is small steel fastener hardware."
assumptions:
  - "BOM quantity is 8, so row total mass is about 0.00447 kg from the 0.000559 kg per-unit CAD estimate."
  - "DIN 7991 M3x8 designation is sufficient to preserve interface identity during merge review."
  - "The row can likely merge into a small fastener kit unless exact screw geometry becomes simulation-relevant."
unresolved:
  - "Fastener property class and coating."
  - "Whether local closure should model this exact screw size separately from a generic small fastener kit."
```
