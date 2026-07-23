---
row_identity:
  item: "1B51"
  cad_file: "1B51_SM2A53-Step"
  source_row_number: 15
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.thorlabs.com/thorproduct.cfm?partnumber=SM2A53"
function:
  summary: "Thorlabs SM2A53 optical thread adapter ring, adapting external M52 x 0.75 threads to internal SM2 2.035-40 threads for mounting SM2-threaded optics or tube components into an M52 interface."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.thorlabs.com/item/SM2A53; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B51_SM2A53-Step.step; research/ream250_bom/ream250_bom_row_0015_1B51__views_2x2.png"
    cited_fact_or_basis: "BOM row 15 identifies item 1B51 as Thorlabs SM2A53 with description 'M52x0,75; Internal SM2 Threads' and the BOM link redirects to the Thorlabs SM2A53 item page. FreeCAD measured one ring-shaped solid with volume 2573.818 mm^3 and a 55.88 x 55.88 x 7.37 mm bounding box, and the rendered preview shows a thin threaded adapter ring."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row represents one physical SM2A53 adapter ring, consistent with BOM quantity 1 and one matched CAD solid."
  uncertainty_notes: []
mass:
  value_kg: 0.02
  basis: "Per unit. BOM quantity is 1, so the row total is also about 0.02 kg. The row-matched SM2A53 drawing lists approximate weight 0.02 kg. FreeCAD measured 1 solid, volume 2573.818 mm^3, area 3560.408 mm^2, and bounding box 55.88 x 55.88 x 7.37 mm; using local aluminum density 2700 kg/m^3 on that CAD volume would give about 0.00695 kg, so the drawing weight is retained as the better product-level mass estimate."
  source:
    url_or_path: "https://www.oxxius.ru/upload/iblock/dbe/j38qr4oay7zb9p73yap8tcsa50z0acsq/24386_E0W.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B51_SM2A53-Step.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "The SM2A53 drawing names the item 'SM2 to M52 x 0.75 adapter' and lists approximate weight 0.02 kg. FreeCAD measured the row STEP as one solid with volume 2573.818 mm^3 and a 55.88 x 55.88 x 7.37 mm bounding box. The local density table lists aluminum density 2700 kg/m^3. bom_url_route_check: the BOM-provided Thorlabs SM2A53 route was checked and resolves row identity and package-weight context, but the accessible page text did not expose the drawing material/approx-weight fields used for this mass value; the cited drawing is row-matched to SM2A53 and carries Thorlabs drawing/title text."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The drawing approximate weight is treated as the best product-level per-item mass despite the simplified local CAD volume yielding a lower aluminum-density estimate."
  uncertainty_notes:
    - "The Thorlabs item page search snippet reports package weight 0.01 kg each while the drawing reports approximate item weight 0.02 kg; downstream mass rollups should treat 0.02 kg as a rounded catalog/drawing value, not a weighed measurement."
material:
  primary_material: "anodized aluminum"
  source:
    url_or_path: "https://www.oxxius.ru/upload/iblock/dbe/j38qr4oay7zb9p73yap8tcsa50z0acsq/24386_E0W.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row-matched SM2A53 drawing lists material as anodized aluminum. The local assembly STEP material extractor matched 1B51_SM2A53-Step but returned only Generic with density 1000.0, which is placeholder metadata under the task acceptance rules. bom_url_route_check: the BOM-provided Thorlabs SM2A53 route was checked and resolves product identity, but the accessible page text did not expose the material field; the cited drawing is row-matched to SM2A53 and carries Thorlabs drawing/title text."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "The source does not state the aluminum alloy grade or anodize type/thickness."
how_to_make:
  summary: "Machine an aluminum adapter ring, cut the external M52 x 0.75 and internal SM2 threads, knurl or texture the outside grip surface, anodize, and inspect thread fit and clear aperture"
  manufacturing_steps:
    - "Start from aluminum round bar or tube stock large enough for the 55.9 mm outside diameter."
    - "Turn the ring faces and bore on a lathe, leaving the approximately 7.4 mm axial thickness shown by the CAD and drawing."
    - "Cut the M52 x 0.75 external thread and internal SM2 2.035-40 thread; add the visible knurled or textured outer grip surface."
    - "Deburr and clean the optical-thread interfaces, anodize the aluminum, and inspect thread engagement, clear aperture, and overall thickness."
  source:
    url_or_path: "https://www.thorlabs.com/item/SM2A53; https://www.oxxius.ru/upload/iblock/dbe/j38qr4oay7zb9p73yap8tcsa50z0acsq/24386_E0W.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1B51_SM2A53-Step.step; research/ream250_bom/ream250_bom_row_0015_1B51__views_2x2.png"
    cited_fact_or_basis: "The BOM-linked Thorlabs route identifies SM2A53 as the row product. The SM2A53 drawing and CAD/preview show a thin adapter ring with external M52 x 0.75 threads, internal SM2 threads, anodized aluminum material, 55.9 mm outside diameter, 48.3 mm clear aperture, and about 7.4 mm thickness. targeted_web_search: searched 'SM2A53 Thorlabs material weight', 'SM2A53 M52x0.75 internal SM2 threads material', and 'Thorlabs SM2A53 drawing anodized aluminum'; results found row-matched product/drawing facts but no row-specific manufacturing-process specification."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The inferred from the ring geometry, aluminum material, standard optical thread forms, and visible textured grip surface."
    - "Anodizing is included because the row-matched drawing states anodized aluminum."
  uncertainty_notes:
    - "The sources do not state Thorlabs' actual production route, tooling, alloy, anodize class, thread tolerances, or inspection procedure."
kb_implications:
  - "item_granularity: simple_part - Model as one standard anodized aluminum optical thread adapter ring; reuse a generic threaded adapter or optomechanical ring part if later KB entries need similar SM2/M52 adapters."
---

# reAM250 BOM Row 15 - 1B51

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0015_1B51.md
source_research_sha256: "9ac466695dbee34dc292d268a5b6fb04008ce77625621f1641c6ff1affe4289a"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read optical thread-adapter function, catalog/drawing mass basis, anodized aluminum material evidence, machining/threading route, KB implication, and preview of the thin ring geometry."
decomposition:
  decision: simple_part
  rationale: "The row is one passive optomechanical adapter ring with no electronic, optical glass, actuator, and sealed subassembly content."
  proposed_subparts: []
process_abstraction:
  original_process_family: turned_threaded_anodized_aluminum_ring
  primary_process_bucket: general_subtractive_machining
  supporting_processes:
    - stock_preparation
    - precision_machining
    - thread_forming
    - deburring
    - surface_finishing
    - coating
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: machining_basic_v0
      fit: partial
      reason: "Covers turning the ring faces, bore, and outside diameter from aluminum stock."
    - process_id: machining_precision_v0
      fit: supporting
      reason: "Relevant for optical-thread fit, concentricity, and clear-aperture control."
    - process_id: surface_treatment_anodizing_v0
      fit: supporting
      reason: "Covers anodized aluminum finishing after machining."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers basic dimensional checks; thread gauges may be needed during later staging."
  abstraction_decision: keep_original_family
  rationale: "The source manufacturing route is a machined aluminum ring with cut threads and anodizing, which maps directly to subtractive machining with thread and coating support."
  process_guardrails:
    tolerance: high
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: optomechanical thread adapter joining two optical mounting thread standards
  material: anodized_aluminum
  scale_or_capacity:
    mass_kg: 0.02
    bom_quantity: 1
    row_total_mass_kg: 0.02
    scale_class: tiny
  geometry_form: thin_circular_threaded_adapter_ring_with_internal_and_external_threads
merge_pool:
  eligible: true
  functional_purpose_key: optical_mounting_adapter
  precision_guardrails:
    - thread_standard_fit
    - concentricity
    - clear_aperture
    - anodized_surface_condition
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - general_subtractive_machining
  import_risk_factors:
    - "Optical-thread standards may require gauges and tighter inspection than generic threaded hardware."
    - "Exact alloy, anodize class, and thread tolerance are unresolved."
  post_merge_decision_notes: "Final import/local manufacture decision is deferred until after merge review with other optomechanical adapter rings."
kb_staging:
  proposed_item_id: null
  notes: "Leave final closure item ID open for merge review across small optical mounting adapters."
assumptions:
  - "Use the drawing value of 0.02 kg as the planning mass despite the lower simplified CAD-volume estimate."
  - "Treat anodized aluminum as the resolved material family."
  - "Treat thread cutting/gauging as the main precision burden."
unresolved:
  - "Specific aluminum alloy and anodize specification."
  - "Internal SM2 and external M52 thread tolerance class."
  - "Whether lunarized staging can merge this with other optical adapter rings by function and scale."
```
