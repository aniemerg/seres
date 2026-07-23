---
row_identity:
  item: 3S47
  cad_file: 3S47_part_7
  source_row_number: 158
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: >
    Thin formed panel for the gas outlet subassembly, likely acting as one
    segment of an outlet duct, guide vane, or baffle surface that helps shape
    inert-gas flow leaving the outlet region.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S47_part_7.step; research/ream250_bom/ream250_bom_row_0158_3S47__views_2x2.png
    cited_fact_or_basis: >
      BOM row 158 identifies item 3S47, quantity 1, as "gas outlet: part 7";
      the manifest maps it to 3S47_part_7.step. FreeCAD measured one solid with
      bounding box about 8.00 x 50.00 x 90.71 mm, and the rendered preview shows
      a thin folded sheet-like panel with lips/creases.
    evidence_basis: bom_provided
  assumptions:
    - The row belongs to the multi-part gas outlet group represented by adjacent BOM rows 3S41 through 3S48.
  uncertainty_notes:
    - The exact installed orientation and flow-interface role are not stated in the BOM or STEP metadata.
mass:
  value_kg: 0.0359
  basis: >
    Per-unit estimate for quantity 1. FreeCAD volume is 4487.058 mm^3, equal to
    4.487058e-6 m^3. Using an 8000 kg/m^3 stainless-steel-density proxy from
    kb/materials/properties.yaml gives 0.035896 kg, rounded to 0.0359 kg.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S47_part_7.step; kb/materials/properties.yaml
    cited_fact_or_basis: >
      FreeCAD measured one solid, volume 4487.058 mm^3, surface area
      9264.743 mm^2, and bounding box about 8.00 x 50.00 x 90.71 mm.
      kb/materials/properties.yaml lists stainless_steel density as
      8000 kg/m^3. targeted_web_search: queries tried "reAM250 gas outlet part
      3S47 material", "Renishaw reAM250 gas outlet material", and "reAM250
      additive manufacturing machine gas outlet stainless steel"; results
      confirmed the reAM250/AM250 context as metal powder-bed-fusion equipment
      but did not provide a row-specific material or mass.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The CAD solid volume is a usable proxy for one physical item in this BOM row.
    - Stainless-steel density is used as a conservative proxy for a thin metal gas-flow panel in a powder-bed-fusion machine.
  uncertainty_notes:
    - If the actual part is aluminum or another lighter alloy, mass could be roughly 3x lower.
    - The STEP assembly material extractor returned only Generic with density 1000.0, so it does not resolve physical material.
material:
  primary_material: unknown corrosion-resistant sheet metal/alloy
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S47_part_7.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; https://davidwenzler.github.io/reAM250/
    cited_fact_or_basis: >
      CAD geometry shows a thin folded panel in the gas outlet group. The local
      assembly STEP material extractor matched 3S47_part_7 but reported only
      Generic and density 1000.0, which is placeholder metadata. The reAM250
      project page describes the machine as a powder bed fusion of metals
      research platform. targeted_web_search: queries tried "reAM250 gas outlet
      part 3S47 material", "Renishaw reAM250 gas outlet material", and
      "reAM250 additive manufacturing machine gas outlet stainless steel";
      no row-specific usable material source was found.
    evidence_basis: engineering_hypothesis
  assumptions:
    - A gas outlet panel inside or near an inert-gas flow path is more likely to be metal sheet than polymer because of heat, spatter, powder, and cleaning exposure.
  uncertainty_notes:
    - No source identified a specific grade, so later KB modeling should keep this broad unless the original CAD or drawings provide material callouts.
how_to_make:
  summary: >
    Plausible route is sheet-metal fabrication: cut a flat blank from
    Corrosion-resistant metal sheet, form the lips/creases with a press brake or
    Simple forming fixture, deburr, clean, and inspect fit in the gas outlet
    Assembly.
  manufacturing_steps:
    - Cut the blank profile from thin corrosion-resistant sheet stock by laser, waterjet, shear, or CNC routing.
    - Form the long lip and angled crease features with a press brake or matched fixture.
    - Deburr edges and clean surfaces for powder-bed-fusion machine service.
    - Inspect envelope and fit against the neighboring gas outlet parts.
  source:
    url_or_path: design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/3S47_part_7.step; research/ream250_bom/ream250_bom_row_0158_3S47__views_2x2.png; https://github.com/DavidWenzler/reAM250
    cited_fact_or_basis: >
      CAD and preview show a thin folded panel with simple planar faces and no
      Complex machined pockets. The reAM250 repository identifies the platform
      As a metal laser powder-bed-fusion research machine. targeted_web_search:
      Queries tried "reAM250 gas outlet part 3S47 material", "Renishaw reAM250
      Gas outlet material", and "reAM250 additive manufacturing machine gas
      Outlet stainless steel" no row-specific manufacturing drawing or vendor
      Process note was found.
    evidence_basis: engineering_hypothesis
  assumptions:
    - The visible folds are intentional formed sheet features rather than a thick machined solid.
    - Prioritize common sheet-metal operations over machining from billet.
  uncertainty_notes:
    - Without an assembly drawing, bend sequence, bend radii, and tolerances are unknown.
kb_implications:
  - "item_granularity: simple_part - Model later as a reusable formed sheet-metal baffle/panel for gas-flow ducting rather than as a purchased calibrated module."
---
## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0158_3S47.md
source_research_sha256: "017eba88d9e40d4f11dee687da81eeed7dc0f0cee9790b4080b96a2d9c8b4b36"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed gas-outlet panel function, stainless-density planning mass, unresolved corrosion-resistant sheet-metal evidence, cut/form/deburr route, and preview showing a folded panel with lips and creases."
decomposition:
  decision: simple_part
  rationale: "The row is one formed sheet panel in a multi-part gas outlet group; neighboring 3S41 through 3S48 rows define the larger outlet assembly."
  proposed_subparts: []
process_abstraction:
  original_process_family: formed_sheet_metal_gas_outlet_panel
  primary_process_bucket: sheet_plate_cutting_drilling
  supporting_processes:
    - stock_preparation
    - cutting
    - forming
    - deburring
    - cleaning
    - joining
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: sheet_metal_cutting_v0
      fit: partial
      reason: "Covers cutting the flat blank for the thin gas outlet panel."
    - process_id: sheet_metal_bending_and_forming_v0
      fit: direct
      reason: "Covers the lips and crease features visible in the CAD preview."
    - process_id: finishing_deburring_v0
      fit: supporting
      reason: "Covers edge cleanup before installation into the gas outlet assembly."
    - process_id: welding_brazing_basic_v0
      fit: supporting
      reason: "Relevant if this panel is joined into a sealed metal outlet assembly."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers bend geometry, envelope, and fit checks against neighboring outlet parts."
  abstraction_decision: keep_original_family
  rationale: "The source route is sheet-metal cutting and forming, matching the sheet/plate bucket with assembly-level joining support."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: review
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: shape gas flow as a segment of the outlet assembly
  material: unresolved_corrosion_resistant_metal
  scale_or_capacity:
    mass_kg: 0.0359
    bom_quantity: 1
    row_total_mass_kg: 0.0359
    scale_class: small
  geometry_form: thin_formed_sheet_baffle_panel_with_lips_and_creases
merge_pool:
  eligible: true
  functional_purpose_key: gas_flow_routing
  precision_guardrails:
    - bend_geometry
    - mating_edge_fit
    - gas_path_cleanliness
    - assembly_sealing
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - sheet_plate_cutting_drilling
  import_risk_factors:
    - "Material grade is unresolved and may affect corrosion, heat, spatter, and cleaning compatibility."
    - "Fit and sealing requirements depend on the complete gas outlet assembly."
  post_merge_decision_notes: "Final import/local decision is deferred until merge review groups gas outlet sheet segments and resolves material plus assembly joining."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic formed gas-routing panel if adjacent outlet rows converge."
assumptions:
  - "Stainless-density mass is retained as a conservative planning estimate while material remains unresolved corrosion-resistant metal."
  - "The visible folds are treated as intentional formed sheet features."
unresolved:
  - "Specific alloy, bend radius, bend sequence, tolerances, and installed orientation are not specified."
  - "The complete gas outlet assembly sealing and joining strategy remains unresolved."
```
