---
row_identity:
  item: "3S46"
  cad_file: "3S46_part_6"
  source_row_number: 157
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Part 6 of the reAM250 gas outlet assembly; the CAD shape is a thin formed panel or vane that likely helps define, shield, or guide the outlet flow passage rather than acting as a round pipe fitting."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; research/ream250_bom/ream250_bom_row_0157_3S46__views_2x2.png"
    cited_fact_or_basis: "BOM row 157 lists item 3S46 quantity 1 as 'gas outlet: part 6'; manifest row 157 maps it to gold_export/parts/3S46_part_6.step with matched_existing part status; rendered CAD preview shows a thin bent panel/vane form."
    evidence_basis: "bom_provided"
  assumptions:
    - "The numbered gas outlet parts 3S41 through 3S48 are treated as sibling pieces of one outlet subassembly."
  uncertainty_notes:
    - "The BOM label does not state the exact sub-function, so guide/shield/vane wording is inferred from the row name plus CAD geometry."
mass:
  value_kg: 0.0362
  basis: "FreeCAD measured one solid with volume 4606.352 mm^3 and bounding box about 14.00 x 50.00 x 90.71 mm. Planning mass uses 4606.352 mm^3 = 4.606352e-6 m^3 times the local generic steel density constant 7850 kg/m^3, giving about 0.0362 kg per unit; BOM quantity is 1, so row total is also about 0.0362 kg. If the sheet is aluminum-density metal, the same CAD volume would be about 0.0124 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S46_part_6.step; kb/materials/properties.yaml; web search"
    cited_fact_or_basis: "FreeCAD measured volume 4606.351513941971 mm^3 for 3S46_part_6.step; local properties list generic steel density as 7850 kg/m^3. targeted_web_search: queries tried: \"3S46\" \"gas outlet\" reAM250; \"3S46_part_6\"; \"Renishaw AM250\" \"gas outlet\" material; \"reAM250\" \"gas outlet\". Result: public BOM mirrors and general AM250 gas-outlet context appeared, but no row-specific mass, material, or drawing for 3S46_part_6 was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The part is modeled as ferrous sheet metal for a conservative planning mass because the STEP material is only Generic and the gas outlet environment is inside a metal powder-bed-fusion machine."
  uncertainty_notes:
    - "The material is unresolved; mass could differ by roughly 3x if the part is aluminum rather than steel."
    - "The STEP volume includes the modeled solid only and does not account for coating, weld bead, or fasteners that may be present in the installed outlet assembly."
material:
  primary_material: "unknown sheet metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; web search"
    cited_fact_or_basis: "Assembly STEP material extraction for product 3S46_part_6 returned material 'Generic' with density 1000.0, which is placeholder metadata under the task criteria; BOM row 157 gives no material, manufacturer, product ID, or link URL. targeted_web_search: queries tried: \"3S46\" \"gas outlet\" reAM250; \"3S46_part_6\"; \"Renishaw AM250\" \"gas outlet\" material; \"reAM250\" \"gas outlet\". Result: no row-specific material specification was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The CAD form and outlet service suggest a formed metallic sheet rather than polymer, elastomer, or ceramic."
  uncertainty_notes:
    - "No grade or alloy is supported; downstream KB modeling should keep the material broad until a drawing, source model, or build note resolves it."
how_to_make:
  summary: "Plausible route: make as a small formed sheet-metal outlet insert/panel, then integrate it into the gas outlet assembly."
  manufacturing_steps:
    - "Cut the flat blank from thin metal sheet by laser cutting, waterjet cutting, or shearing."
    - "Form the bends/flanges to match the CAD profile."
    - "Deburr and clean the edges for installation in the gas outlet flow path."
    - "Attach or retain it in the larger gas outlet assembly by the assembly method used for the neighboring outlet parts."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S46_part_6.step; research/ream250_bom/ream250_bom_row_0157_3S46__views_2x2.png; web search"
    cited_fact_or_basis: "CAD preview and dimensions show a thin bent panel/vane with sheet-like proportions and no visible complex machined bores or standard hardware features. targeted_web_search: queries tried: \"3S46\" \"gas outlet\" reAM250; \"3S46_part_6\" \"Renishaw AM250\" \"gas outlet\" material; \"reAM250\" \"gas outlet\". Result: no row-specific manufacturing drawing or process note was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Sheet cutting plus bending is selected because it matches the thin folded geometry more closely than billet machining or additive manufacture."
    - "Final joining details are deferred to the gas outlet assembly because this single row does not show holes, fasteners, or weld callouts."
  uncertainty_notes:
    - "If the source CAD represents a cast or printed flow-guide part rather than sheet metal, the manufacturing route would change."
kb_implications:
  - "item_granularity: simple_part - Model 3S46 as a simple formed sheet-metal gas-outlet component unless later evidence shows it is inseparable from a larger outlet assembly."
---

Research result for reAM250 BOM row 157.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0157_3S46.md
source_research_sha256: "1588f7da6fb96e1fbebab7b18b5ca6d49f7c11c51db8e65ffc8740026f8dc608"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read the gas-outlet function, mass estimate and basis, unresolved sheet-metal evidence, forming route, KB implications, and CAD preview showing a thin bent panel/vane."
decomposition:
  decision: simple_part
  rationale: "The row is a single formed sheet-metal outlet component with no separable subparts visible in the evidence."
  proposed_subparts: []
process_abstraction:
  original_process_family: sheet_cutting_bending
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - deburring
    - cleaning
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: cutting_basic_v0
      fit: direct
      reason: "Covers cutting the thin metal blank from sheet stock."
    - process_id: metal_forming_basic_v0
      fit: supporting
      reason: "Covers bending and flange forming for the outlet-panel geometry."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers checks of formed profile, dimensions, edge quality, and fit in the outlet assembly."
    - process_id: cleaning_basic_v0
      fit: supporting
      reason: "Relevant because the row functions in a gas-flow path and should be clean before installation."
  abstraction_decision: keep_original_family
  rationale: "The source route is a thin sheet cutting and forming path. The primary closure bucket should remain sheet and plate cutting, with forming as a supporting step."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "guide and shield element for a gas outlet flow passage"
  material: unknown_sheet_metal_alloy
  scale_or_capacity:
    mass_kg: 0.0362
    bom_quantity: 1
    row_total_mass_kg: 0.0362
    scale_class: small
  geometry_form: formed_thin_sheet_vane_panel
merge_pool:
  eligible: true
  functional_purpose_key: gas_flow_guidance
  precision_guardrails:
    - formed_profile
    - edge_quality
    - outlet_fit
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Material is unresolved; steel and aluminum variants change mass and closure inputs."
    - "Attachment method and final outlet assembly fit are unresolved."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review compares the numbered gas-outlet sheet components."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review with sibling gas outlet parts before assigning a closure item."
assumptions:
  - "Steel-density planning mass is retained from the research row while material remains unresolved."
  - "The part is treated as formed sheet metal because the preview shows a thin bent panel with sheet-like proportions."
unresolved:
  - "Exact alloy, thickness callout, coating, attachment method, fit tolerance, and role within the full gas outlet assembly are not specified."
```
