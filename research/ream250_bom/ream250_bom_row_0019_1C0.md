---
row_identity:
  item: "1C0"
  cad_file: "1C0_clamp_GN 820_2-230-MFC"
  source_row_number: 19
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.ganternorm.com/de/produkte/2.4-Spannen-mit-Spannmechanik/Schnellspanner/GN-853-Edelstahl-Verschlussspanner-mit-Verriegelung#Gr%C3%B6%C3%9Fe%3Di(160)%3BForm%3Du(bec5acdb-2fc0-4cf4-9459-a053043062c1)%3BWerkstoff%3Du(4ffaa763-f739-4917-9edb-5c7ca96d4057)"
function:
  summary: "Ganter/Elesa+Ganter GN 820.2-230-MFC horizontal acting toggle clamp with side/vertical mounting base, forked clamping arm, two flanged washers, and GN 708.1 spindle assembly; BOM quantity is 2."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1C0_clamp_GN 820_2-230-MFC.step; https://www.ganternorm.com/en/products/2.4-Tensioning-with-clamping-mechanisms/Toggle-clamps/GN-820.2-Stainless-Steel-Toggle-clamps-operating-lever-horizontal-with-side-mounting"
    cited_fact_or_basis: "BOM row 19 names item 1C0, quantity 2, CAD file 1C0_clamp_GN 820_2-230-MFC, manufacturer GanterNorm, and description 'flanged washers and GN spindle assembly'. Manifest row 19 maps the row to a matched vendor-component STEP. FreeCAD measured 7 solids with bounding box 196.59 x 121.00 x 43.00 mm, matching the GN 820.2 size-230 envelope; the contact sheet shows a toggle clamp with side mounting base, forked arm, handle, and clamping screw. Ganter describes GN 820.2 as a horizontal acting toggle clamp, says type MFC includes two flanged washers and clamping screw GN 708.1, and lists size 230 with holding capacity 1700 N. official_alternate_route_check: the original BOM Link URL was checked, but it points to Ganter GN 853 rather than the row's GN 820.2 CAD/product identity; the row-matched Ganter GN 820.2 page on the same official manufacturer domain was used instead because it matches the BOM/CAD product family and filename."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The original BOM Link URL appears to be a row-linking error because it identifies GN 853 while the BOM text, CAD filename, manifest, and geometry identify GN 820.2-230-MFC."
mass:
  value_kg: 0.42
  basis: "Per unit. BOM quantity is 2, so the row total is about 0.84 kg. D&D Barry's Elesa+Ganter GN 820.2 table lists the exact steel SKU GN 820.2-230-MFC with weight 420 g. Local CAD volume is 72479.263 mm^3 and bounding box is 196.59 x 121.00 x 43.00 mm; this supports size/shape identity but is not used for density-derived mass because the row is a multi-solid, multi-material assembly."
  source:
    url_or_path: "https://www.ddbarry.com.au/product/gn-820-2/; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1C0_clamp_GN 820_2-230-MFC.step"
    cited_fact_or_basis: "D&D Barry's GN 820.2 listing includes SKU GN 820.2-230-MFC with dimensions matching size 230 and weight 420 g. FreeCAD measured the row STEP as 7 solids, volume 72479.263 mm^3, area 37940.166 mm^2, and bounding box 196.59 x 121.00 x 43.00 mm. bom_url_route_check: the original BOM Link URL points to GN 853 and did not resolve the exact GN 820.2-230-MFC mass; the row-matched Elesa+Ganter distributor table was used for mass."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The row's CAD filename omits the NI stainless suffix, so the non-NI steel GN 820.2-230-MFC catalog row is treated as the BOM item."
  uncertainty_notes:
    - "The Ganter page reached from the row-matched search exposes a selected-part weight field, but browser state did not reliably prove that field was configured to GN 820.2-230-MFC; the exact SKU table weight is therefore preferred."
    - "The assembly STEP material extractor found the product but no material or density metadata for this row."
material:
  primary_material: "case-hardened steel C10 clamp body with zinc-plated blue-passivated finish, tempered bearing pins, lubricated moving parts, oil-resistant red plastic hand grip, and GN 708.1 spindle assembly with steel or stainless spindle and rubber tip"
  source:
    url_or_path: "https://static.globalindustrial.com/products/pdf/45554-jw-winco-inc/B2958413.pdf; https://www.ganternorm.com/en/products/2.4-Tensioning-with-clamping-mechanisms/Toggle-clamps/GN-820.2-Stainless-Steel-Toggle-clamps-operating-lever-horizontal-with-side-mounting"
    cited_fact_or_basis: "The JW Winco/Ganter GN 820.2 standard sheet states the steel toggle clamp material as case-hardened steel C10 with zinc-plated blue-passivated finish, tempered bearing pins, moving parts lubricated with special grease, oil-resistant red plastic hand grip, and GN 708.1 spindle assembly with rubber tip. The Ganter GN 820.2 page identifies type MFC as the forked clamping arm with two flanged washers and clamping screw GN 708.1. agent-initiated independent search route: searched exact row product 'GN 820.2-230-MFC' after finding the original BOM Link URL pointed to GN 853; the row-matched GN 820.2 catalog/source facts were used for material."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "Because the BOM/CAD row names GN 820.2-230-MFC without the NI suffix, the steel material option is used rather than the stainless GN 820.2-230-MFC-NI option."
  uncertainty_notes:
    - "If the BOM Link URL was intended to indicate a stainless replacement despite the CAD filename, the material would shift toward AISI 304 stainless components; the current row identity evidence favors the non-NI steel SKU."
how_to_make:
  summary: "Manufacturing route would be a small mechanical assembly made from stamped or machined steel clamp links/base, bearing pins/rivets, a formed or molded plastic handle, and a threaded clamping spindle with rubber thrust pad"
  manufacturing_steps:
    - "Manufacturing route: cut, form, or machine C10 steel sheet/plate pieces for the side mounting base, forked clamping arm, and linkage plates, then zinc plate or otherwise protect the steel surfaces."
    - "Make or source pins/rivets, flanged washers, the GN 708.1-style threaded spindle, plastic handle, and rubber tip; lubricate moving joints."
    - "Assemble the linkage and spindle, then inspect clamp travel, over-center locking action, mounting-hole geometry, and approximate holding-capacity suitability."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0019_1C0__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/1C0_clamp_GN 820_2-230-MFC.step; https://www.ganternorm.com/en/products/2.4-Tensioning-with-clamping-mechanisms/Toggle-clamps/GN-820.2-Stainless-Steel-Toggle-clamps-operating-lever-horizontal-with-side-mounting; https://static.globalindustrial.com/products/pdf/45554-jw-winco-inc/B2958413.pdf"
    cited_fact_or_basis: "The CAD preview shows a multi-link toggle clamp assembly with base, forked arm, pins, handle, and threaded clamping screw. FreeCAD measured a 196.59 x 121.00 x 43.00 mm envelope. The Ganter page identifies the GN 820.2 toggle-clamp function and MFC clamping screw; the JW Winco/Ganter sheet identifies steel, pins, plastic handle, lubrication, and spindle/rubber tip component materials. The detailed fabrication sequence is inferred from component geometry and material stack rather than stated by the cited sources. targeted_web_search: queries tried included 'GN 820.2-230-MFC manufacturing process', 'GN 820.2 toggle clamp material C10 pins handle', and 'GN 820.2-230-MFC weight material'; results resolved row-matched product, material, dimensions, and mass but did not provide a row-specific manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The clamp is best represented initially as a external standard module because it combines several small precision linkage, handle, spindle, and rubber-pad parts"
    - "The manufacturing route assumes conventional sheet/plate forming or machining plus pin/rivet assembly, consistent with standard toggle clamp construction."
  uncertainty_notes:
    - "No row-specific drawing was found for tolerances, pin fits, heat treatment depth, plating specification, lubrication type, or production tooling."
kb_implications:
  - "item_granularity: simple_part - Treat as a reusable standard toggle-clamp hardware item for near-term KB modeling; split into steel links/base, pins, handle, spindle, washers, and rubber pad only if clamp manufacturing becomes a detailed target."
---

# reAM250 BOM Row 19 - 1C0

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0019_1C0.md
source_research_sha256: "be5b16b94a677c0fd1f6b630985f1f2af850c2a9c3d4c94ad89b3e92e0aba9ed"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read function, mass basis, material stack, inferred manufacturing route, KB implications, and CAD preview before conversion."
decomposition:
  decision: complex_module
  rationale: "The row is a reusable toggle-clamp hardware assembly with steel links and base, pins, spindle, washers, plastic grip, rubber tip, lubrication, and surface treatment. Phase 1 can stage it as one clamping module, while later closure may split the material families if clamp manufacture becomes important."
  proposed_subparts:
    - steel_toggle_links_and_base
    - bearing_pins_and_rivets
    - threaded_clamping_spindle_and_washers
    - plastic_hand_grip
    - rubber_thrust_tip
process_abstraction:
  original_process_family: stamped_formed_machined_steel_toggle_clamp_assembly
  primary_process_bucket: manual_assembly_with_general_tools
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - drilling
    - thread_forming
    - heat_treatment
    - coating
    - assembly
    - calibration
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: assembly_basic_v0
      fit: partial
      reason: "Covers assembling the clamp linkage, spindle, washers, grip, and pad into one hardware module; detailed over-center adjustment remains a guardrail."
    - process_id: sheet_metal_forming_v0
      fit: supporting
      reason: "Relevant to forming the steel base, forked arm, and linkage plates from sheet and plate stock."
    - process_id: machining_basic_v0
      fit: supporting
      reason: "Covers drilled holes, spindle interfaces, and local cleanup on the clamp body and linkage features."
    - process_id: fastener_kit_medium_production_v0
      fit: supporting
      reason: "Anchors threaded spindle, washers, pins, and small steel hardware fabrication as a reusable fastener-family process."
    - process_id: additive_manufacturing_polymer_v0
      fit: poor_fit
      reason: "Only relevant for a substitute plastic grip; it does not cover the main steel clamp assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers travel, mounting-hole, clamping action, and fit checks before staging selects final recipe details."
  abstraction_decision: substitute_process_family
  rationale: "The source is a vendor toggle clamp with mixed component manufacture. For closure analysis, the row maps best to a general manual assembly module, with steel forming, machining, fastener production, coating, and inspection carried as support tags."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: provide over-center clamping force for access, fixture, and closure interfaces
  material: mixed_steel_polymer_elastomer
  scale_or_capacity:
    mass_kg: 0.42
    bom_quantity: 2
    row_total_mass_kg: 0.84
    scale_class: small
  geometry_form: horizontal_toggle_clamp_with_side_mount_base_forked_arm_spindle_and_grip
merge_pool:
  eligible: true
  functional_purpose_key: mechanical_clamping
  precision_guardrails:
    - holding_capacity
    - over_center_locking_action
    - mounting_hole_pattern
    - spindle_adjustment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - manual_assembly_with_general_tools
  import_risk_factors:
    - "Commercial toggle clamp has multiple small materials, plated steel, heat-treated pins, lubrication, adjusted linkage action, and rubber contact pad."
    - "If later review needs exact 1700 N holding capacity with catalog repeatability, this may stay an import candidate."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares this row against other clamping hardware and decides whether a generic local toggle clamp is acceptable."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely reusable mechanical clamping hardware rather than a row-specific Ganter SKU."
assumptions:
  - "The non-NI steel GN 820.2-230-MFC identity is retained because the CAD filename and matched product evidence support it."
  - "The 0.42 kg unit mass and BOM quantity 2 are sufficient for Phase 2 scale grouping."
  - "A generic toggle-clamp closure item may substitute for the exact commercial part if holding capacity and mounting pattern remain guardrails."
unresolved:
  - "Exact pin fits, heat treatment depth, plating specification, lubrication, and rubber tip composition are not available from the row evidence."
  - "Need merge review to decide whether this stays one closure item, becomes a decomposed small assembly, versus remains a commercial import."
```
