---
row_identity:
  item: "2AV8"
  cad_file: "2AV8_DIN 912 - M8x1x25x22,5"
  source_row_number: 107
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "DIN 912 socket head cap screw used as reusable threaded fastening hardware in the reAM250 assembly; the row is an M8 x 1 x 25 mm screw with a cylindrical socket head and internal hex drive."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV8_DIN 912 - M8x1x25x22,5.step; research/ream250_bom/ream250_bom_row_0107_2AV8__views_2x2.png"
    cited_fact_or_basis: "BOM row 107 states item 2AV8, quantity 16, CAD file 2AV8_DIN 912 - M8x1x25x22,5, and description cylinder head cap screw. The manifest maps the same row to a matched part STEP export. FreeCAD measured one solid with bounding box 33.00 x 14.07 x 14.07 mm; the rendered contact sheet shows a threaded screw with cylindrical head and internal hex socket."
    evidence_basis: "bom_provided"
  assumptions:
    - "The English BOM description cylinder head cap screw is interpreted as a socket head cap screw, consistent with DIN 912 naming and the visible internal hex drive."
  uncertainty_notes:
    - "The BOM/CAD evidence does not identify the exact mating holes or which reAM250 subassembly these 16 screws fasten."
mass:
  value_kg: 0.01696
  basis: "FreeCAD volume 2160.284 mm^3 equals 0.000002160284 m^3. The assembly STEP material extractor reports Steel, Mild with density 7850 kg/m^3, giving 0.01696 kg per screw. BOM quantity is 16, so the row total is about 0.271 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV8_DIN 912 - M8x1x25x22,5.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 2160.284 mm^3, surface area 1284.057 mm^2, and bounding box 33.00 x 14.07 x 14.07 mm. The assembly STEP material extractor matched this product name and reported material Steel, Mild with density 7850.0. The local density table lists steel density 7850 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The single STEP solid volume is used as the physical-volume proxy for one screw represented by the BOM row."
    - "The assembly STEP density and local steel density are treated as equivalent for this calculation."
  uncertainty_notes:
    - "Mass may differ slightly for a real purchased DIN 912 screw if the exported thread geometry, socket detail, chamfers, or coating differ from the physical part."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product 2AV8_DIN 912 - M8x1x25x22,5 and returned material Steel, Mild with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The BOM row does not state a DIN/ISO property class, coating, or corrosion-resistant grade; mild steel should not be treated as a verified strength class for later structural calculations."
how_to_make:
  summary: "Use as a standard DIN 912 socket head cap screw"
  manufacturing_steps:
    - "Select mild steel or later-resolved cap-screw steel stock sized for an M8 socket head screw blank."
    - "Cold-head or machine the cylindrical head and shank blank."
    - "Broach, punch, or machine the internal hex socket in the head."
    - "Roll or cut the M8 x 1 external thread to the required length, preserving the approximately 25 mm nominal screw length from the row name."
    - "Apply any required heat treatment, coating, or cleaning only after a later source resolves property class and finish."
    - "Inspect thread fit, head diameter and height, socket drive size, overall length, and visual thread quality."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV8_DIN 912 - M8x1x25x22,5.step; research/ream250_bom/ream250_bom_row_0107_2AV8__views_2x2.png; https://accu-components.com/us/metric-cap-head-screws/386837-SSCF-M8-25-12-9-Z; https://www.metricmcc.com/socket-head-cap-screws"
    cited_fact_or_basis: "BOM/CAD identify the row as a DIN 912 M8 x 1 x 25 socket head cap screw and show the threaded shank plus hex socket. targeted_web_search: queries tried were \"DIN 912 socket head cap screw M8 material property class manufacturing thread rolling\" and \"DIN 912 cylinder head cap screw socket head cap screw standard material property class\" results found standard fastener pages for DIN 912/socket head cap screws and material/property-class families, but no row-specific 2AV8 manufacturing drawing or process route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row is treated as standard reusable fastener hardware rather than a custom machined reAM250 part."
    - "The inferred from the screw geometry and common socket-head screw production practice"
  uncertainty_notes:
    - "Property class, heat treatment, surface finish, and coating are unresolved; those choices affect whether the manufacturing route needs high-strength alloy steel and controlled heat treatment rather than generic mild-steel screw production."
kb_implications:
  - "item_granularity: simple_part - standard DIN 912 socket head cap screw hardware should later map to a reusable fastener item or kit parameterized by thread, length, material, and property class rather than a reAM250-specific custom part."
---

Research result for reAM250 BOM row 107.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0107_2AV8.md
source_research_sha256: "a10d4e8281af9d2e0fa6c7482ab98bc44d84d57848532782589f797de915fbf9"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the threaded-fastening function, CAD-derived per-unit and row-total mass, mild steel material metadata, standard socket-head screw route, KB implications, and CAD preview showing an M8 socket-head cap screw."
decomposition:
  decision: simple_part
  rationale: "The row is standard steel threaded hardware with no internal closure dependencies beyond fastener manufacture."
  proposed_subparts: []
process_abstraction:
  original_process_family: standard_fastener_forming_threading
  primary_process_bucket: fastener_forming_thread_rolling
  supporting_processes:
    - forming
    - thread_forming
    - precision_machining
    - heat_treatment
    - deburring
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: fastener_kit_medium_production_v0
      fit: partial
      reason: "Aggregates M6-M12 fastener production and kitting, matching this M8 row at closure level."
    - process_id: fastener_kit_small_fabrication_v0
      fit: poor_fit
      reason: "Useful as a small-fastener analogy but sized below this M8 screw family."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Can cover fallback small-batch machined screw features if heading and thread rolling are not separately represented."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers thread, length, socket, head, and material checks."
  abstraction_decision: keep_original_family
  rationale: "The source evidence identifies standard DIN 912 screw hardware. The fastener forming and thread rolling bucket is the correct closure handle before fastener merge review."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: not_applicable
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "removable threaded fastening"
  material: mild_steel
  scale_or_capacity:
    mass_kg: 0.01696
    bom_quantity: 16
    row_total_mass_kg: 0.271
    scale_class: small
  geometry_form: din_912_m8_socket_head_cap_screw
merge_pool:
  eligible: true
  functional_purpose_key: threaded_fastening
  precision_guardrails:
    - thread_size
    - socket_fit
    - fastener_property_class
    - coating
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - fastener_forming_thread_rolling
  import_risk_factors:
    - "Fastener property class, coating, exact steel grade, and heat treatment are unresolved."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review decides whether individual M8 sizing matters beyond medium fastener kit modeling."
kb_staging:
  proposed_item_id: null
  notes: "Wait for fastener merge review; quantity 16 and 0.271 kg row total should be preserved in staging."
assumptions:
  - "Mild steel STEP metadata is accepted for row-level classification."
  - "The DIN 912 M8 designation is standard enough to merge with other threaded fastener rows under guardrails."
unresolved:
  - "Installed joint duty, property class, coating, exact grade, supplier tolerance, and final kit-level abstraction are not specified."
```
