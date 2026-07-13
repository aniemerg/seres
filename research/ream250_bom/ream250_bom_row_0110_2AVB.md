---
row_identity:
  item: "2AVB"
  cad_file: "2AVB_DIN 912 - M6x1x35x24"
  source_row_number: 110
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "DIN 912 M6 x 35 mm socket-head cap screw used as standard machine fastening hardware; the row quantity is 12 screws."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AVB_DIN 912 - M6x1x35x24.step; research/ream250_bom/ream250_bom_row_0110_2AVB__views_2x2.png; https://accu-components.com/us/metric-cap-head-screws/386814-SSC-M6-35-12-9-Z"
    cited_fact_or_basis: "BOM row 110 states item 2AVB, quantity 12, description cylinder head cap screw, and CAD file 2AVB_DIN 912 - M6x1x35x24. The manifest maps the row to gold_export/parts/2AVB_DIN 912 - M6x1x35x24.step as a matched part export. FreeCAD measured one solid with bounding box 41.00 x 10.82 x 10.82 mm; the rendered contact sheet shows a socket-head screw with cylindrical head, shank, threaded end, and hex socket. Accu's DIN 912 M6 x 35 product page identifies the same standard/size family as a metric cap-head screw with M6 thread, 35 mm length, 1 mm pitch, 5 mm socket, and DIN 912 manufacturing standard."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row represents twelve separate instances of the same standard screw; function is interpreted per one screw."
  uncertainty_notes:
    - "The BOM row does not identify the exact mating holes or clamped subassembly, so the local joint location within the reAM250 machine remains unspecified."
mass:
  value_kg: 0.0108
  basis: "FreeCAD volume 1376.334 mm^3 equals 0.000001376 m^3. Using the assembly STEP material density 7850 kg/m^3 gives 0.0108 kg per screw. The BOM quantity is 12, so the row total is about 0.130 kg. As a sanity check, an independent DIN 912 M6 x 35 steel vendor listing gives 910 g per 100 screws, or 0.0091 kg each, which is within about 20 percent of the CAD-derived value."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AVB_DIN 912 - M6x1x35x24.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; https://accu-components.com/us/metric-cap-head-screws/386814-SSC-M6-35-12-9-Z"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 1376.334 mm^3, area 1045.653 mm^2, and bounding box 41.00 x 10.82 x 10.82 mm. The assembly STEP material extractor matched 2AVB_DIN 912 - M6x1x35x24 and returned material Steel, Mild with density 7850.0. The local density table lists steel density 7850 kg/m^3. Accu's DIN 912 M6 x 35 steel listing gives weight per 100 units as 910 g."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is used as the physical-volume proxy for one screw."
    - "The assembly STEP material density is treated as kg/m^3-like, per the extractor note for this reAM250 export."
  uncertainty_notes:
    - "The CAD volume and catalog sanity-check mass are close but not identical; downstream mass accounting should treat 0.0108 kg as a CAD-derived estimate rather than a weighed part value."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AVB_DIN 912 - M6x1x35x24.step"
    cited_fact_or_basis: "The assembly STEP material extractor matched product 2AVB_DIN 912 - M6x1x35x24 and returned material Steel, Mild with density 7850.0. The part STEP and contact sheet show a one-piece screw geometry."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The CAD package resolves the material family but not fastener property class, coating, surface finish, or heat-treatment state; DIN 912 screws are commonly sold in higher-strength steel variants, so the mild-steel tag may be a CAD-material simplification."
how_to_make:
  summary: "Steel wire or rod cut to blank length, cold headed to form the cylindrical socket head, socket-punched, thread rolled to M6 x 1, heat treated or stress relieved as required by the selected fastener grade, finished, and inspected"
  manufacturing_steps:
    - "Manufacturing route: select steel wire or rod stock sized for an M6 socket-head screw blank."
    - "Cut blanks, cold-head/upset the cylindrical cap head, and form the internal hex socket."
    - "Roll the M6 x 1 external thread over the required threaded length rather than machining every thread for high-volume production."
    - "Apply heat treatment, coating or passivation if the final property class and corrosion requirement demand it; then inspect thread, socket, head height, and overall length."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AVB_DIN 912 - M6x1x35x24.step; research/ream250_bom/ream250_bom_row_0110_2AVB__views_2x2.png; https://accu-components.com/us/metric-cap-head-screws/386814-SSC-M6-35-12-9-Z; https://www.mwcomponents.com/uploads/Resource-Center/Fasteners-Overview-Presentation-v020724.pdf?srsltid=AfmBOooZ0rkO_yX3gRVqKd2nZw0ssAg9SNCcoiOjdL1U2Mkei4yXxHAF"
    cited_fact_or_basis: "CAD and preview show a one-piece socket-head screw with cylindrical head, internal hex socket, shank, and threaded end. Accu identifies the same standard/size family as a DIN 912 M6 x 35 cap-head screw. MW Components lists socket head cap screws among fastener products and lists production processes including cold heading/cold forming, thread rolling, trimming, heat treatment, hardening, and annealing. targeted_web_search: searched \"DIN 912 M6 x 35 socket head cap screw material steel dimensions\", \"DIN 912 M6x35 socket head cap screw weight steel\", \"DIN 912 cylinder head cap screw M6x35 material steel\", \"socket head cap screw manufacturing cold heading thread rolling heat treatment\", and \"how socket head cap screws are made cold heading thread rolling\" found matching standard-product and general fastener-manufacturing evidence, but no row-specific reAM250 manufacturing drawing or process sheet."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The generalized from standard screw geometry and fastener manufacturing practice; exact tooling, material grade, and heat treatment depend on the final property class."
  uncertainty_notes:
    - "The row lacks a property class or coating callout, so the route cannot yet specify final heat-treatment target, plating/passivation, or acceptance tests beyond generic dimensional inspection."
kb_implications:
  - "item_granularity: simple_part - model as reusable standard hardware, likely consolidated with other DIN/ISO socket-head cap screws by size/material rather than as a machine-specific purchased module."
---

Research result for reAM250 BOM row 110.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0110_2AVB.md
source_research_sha256: 39e3184d8aa27a88abbd0fd7c26209083d99a49a5a60080bd7a252709ccdde31
evidence_reviewed:
  original_research_sections:
  - function
  - mass
  - material
  - how_to_make
  - kb_implications
  geometry_evidence_used: true
  notes: Reviewed the row function, quantity, CAD-derived mass, mild-steel material evidence, standard fastener manufacturing
    route, KB implication, and CAD preview showing socket-head screw geometry.
decomposition:
  decision: simple_part
  rationale: This is a one-piece standard DIN 912 M6 socket-head cap screw used as reusable fastening hardware; no internal
    closure-relevant subassembly is present.
  proposed_subparts: []
process_abstraction:
  original_process_family: cold_heading_thread_rolling
  primary_process_bucket: fastener_forming_thread_rolling
  supporting_processes:
  - stock_preparation
  - forming
  - thread_forming
  - heat_treatment
  - coating
  - dimensional_inspection
  candidate_existing_processes:
  - process_id: fastener_kit_small_fabrication_v0
    fit: partial
    reason: Covers small fastener families as a reusable closure abstraction.
  - process_id: fastener_kit_medium_production_v0
    fit: partial
    reason: Covers medium fastener families as a reusable closure abstraction.
  - process_id: machining_process_drilling_v0
    fit: supporting
    reason: Covers drilled features when fastener geometry needs them.
  - process_id: heat_treat_basic_v0
    fit: supporting
    reason: Covers strength conditioning when fastener properties require it.
  - process_id: fastener_kit_small_fabrication_v0
    fit: supporting
    reason: Relevant when the row depends on thread geometry.
  - process_id: surface_treatment_basic_v0
    fit: supporting
    reason: Relevant when the row needs protective surface treatment.
  abstraction_decision: keep_original_family
  rationale: The source route already belongs to the shared fastener forming bucket. Cold heading and thread rolling should
    be shared across standard steel screws, then handled as a fastener family during merge review.
  process_guardrails:
    tolerance: review - M6 thread fit, head height, and socket dimensions must match standard hardware tolerance.
    surface_finish: review - thread and head bearing surfaces need usable finish after forming and rolling.
    sealing_quality: not_applicable
    alignment_accuracy: review - screw straightness and socket concentricity affect installation but are standard fastener
      requirements.
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: reusable threaded fastening hardware for clamping machine components
  material: mild_steel_fastener_steel
  scale_or_capacity:
    mass_kg: 0.0108
    bom_quantity: 12
    row_total_mass_kg: 0.13
    scale_class: small
  geometry_form: socket_head_cap_screw_m6x35
merge_pool:
  eligible: true
  functional_purpose_key: threaded_fastening_hardware
  precision_guardrails:
  - metric_thread_fit
  - socket_drive_geometry
  - fastener_strength_grade
  - head_bearing_surface
downstream_decision_inputs:
  local_manufacturing_paths_considered:
  - fastener_forming_thread_rolling
  import_risk_factors:
  - Unknown property class, coating, and heat-treatment state could make this an imported fastener if local fastener-grade
    steel and forming capability are out of scope.
  post_merge_decision_notes: Final import/local manufacture decision is deferred until merge review determines the condition
    that this row becomes a generic steel screw and fastener-kit closure item.
kb_staging:
  proposed_item_id: null
  notes: Do not create a row-specific item ID before merge review; likely candidate for consolidation with other M6 steel
    socket-head screws and a reusable fastener kit.
assumptions:
- Per-screw mass is 0.0108 kg from CAD volume and steel density; row total mass uses the BOM quantity of 12.
- Mild steel in the CAD material is treated as a steel fastener-family signal, with final grade and coating unresolved.
- The CAD preview is sufficient to identify socket-head cap screw form and does not indicate a custom machine-specific geometry.
unresolved:
- Exact fastener property class, heat treatment, coating, and mating joint are not specified in the source row.
- Merge review must decide the condition that to represent this as a discrete screw size and as part of a fastener kit abstraction.
```
