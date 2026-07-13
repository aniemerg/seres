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
  summary: "Steel wire/bar stock, cold heading or machining of the cylindrical head and shank, hex-socket forming, thread rolling or cutting, and inspection"
  manufacturing_steps:
    - "Manufacturing route: start from mild-steel wire or bar stock, form the cylindrical head and shank, create the internal hex socket, roll or cut the M8 thread, deburr, and inspect fit."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0111_2AVC__views_2x2.png; https://accu-components.com/us/metric-cap-head-screws/3903-SSCF-M10-30-A2; https://www.holo-krome.com/custom-fasteners.html"
    cited_fact_or_basis: "BOM and CAD identify a DIN 912 M8 socket head cap screw. Accu confirms this product family is manufactured to DIN 912 / ISO 4762 and available as socket cap screws. HOLO-KROME describes custom fasteners and cold-headed parts as part of socket fastener manufacturing capability. targeted_web_search: queries tried: 'DIN 912 M8 socket head cap screw cylinder head cap screw hex socket function' and 'socket head cap screw manufacturing cold heading thread rolling hex socket'; results supported standard DIN 912 procurement and cold-heading relevance but did not provide a row-specific manufacturing traveler."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB planning, standard screw manufacture can be approximated from generic socket-cap-screw production practice."
  uncertainty_notes:
    - "The process-plausible but not a row-specific vendor process specification."
kb_implications:
  - "item_granularity: simple_part - Finished standard DIN 912 socket head cap screw; later KB work should reuse or create generic standard fastener hardware rather than model this as raw stock or a purchased module."
---

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0111_2AVC.md
source_research_sha256: "00a9671da3f0887e982bde72814f9697899fe37e2bd8ddce09d807c41bc1770a"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read removable fastener function, CAD/STEP material mass basis, mild-steel material evidence, socket-cap-screw manufacturing route, KB implication, and preview of the threaded socket-head screw."
decomposition:
  decision: simple_part
  rationale: "The row is one finished standard screw with no useful internal decomposition at KB closure scale."
  proposed_subparts: []
process_abstraction:
  original_process_family: cold_headed_threaded_socket_cap_screw
  primary_process_bucket: fastener_forming_thread_rolling
  supporting_processes:
    - forming
    - thread_forming
    - precision_machining
    - deburring
    - heat_treatment
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: fastener_kit_medium_production_v0
      fit: direct
      reason: "Covers M6-M12 style fastener production with forged blanks, machined details, and cut/tapped threads at kit level."
    - process_id: metal_forming_basic_v0
      fit: supporting
      reason: "Covers basic forming operations relevant to headed screw blank production."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers socket, shank, and thread cleanup when thread rolling is not separately modeled."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional and thread-fit checks before kitting/use."
  abstraction_decision: keep_original_family
  rationale: "The source route is standard screw forming and threading, which maps directly to the fastener-forming/thread-rolling closure bucket."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: removable threaded fastener clamping mechanical joints
  material: mild_steel
  scale_or_capacity:
    mass_kg: 0.01497
    bom_quantity: 4
    row_total_mass_kg: 0.0599
    scale_class: tiny
  geometry_form: din912_m8_socket_head_cap_screw
merge_pool:
  eligible: true
  functional_purpose_key: threaded_fastening
  precision_guardrails:
    - thread_standard_fit
    - socket_drive_fit
    - strength_class
    - coating_finish
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - fastener_forming_thread_rolling
  import_risk_factors:
    - "Strength class, heat treatment, and coating are unresolved."
    - "At closure scale this may be better represented inside a medium fastener kit."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until after merge review with other DIN/ISO screw rows and fastener-kit abstractions."
kb_staging:
  proposed_item_id: null
  notes: "Leave final closure item ID open; likely merge into standard fastener hardware instead of a row-specific screw."
assumptions:
  - "Use STEP-derived mild steel density and CAD volume for the mass estimate."
  - "Treat the item as standard DIN 912 / ISO 4762 style cap screw hardware."
  - "Use fastener kit production as a likely coarse closure route."
unresolved:
  - "Strength class, exact steel grade, heat treatment, and coating."
  - "Whether later staging should model individual M8 socket screws versus fold them into a medium fastener kit."
```
