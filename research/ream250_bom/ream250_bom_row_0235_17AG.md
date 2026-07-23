---
row_identity:
  item: "17AG"
  cad_file: "17AG_profile_60x60_300"
  source_row_number: 235
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Likely a cut length of 60 x 60 mm slotted aluminum strut profile used as a structural frame/support member in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/instances/17AG_profile_60x60_300__96_profile_60x60_300.step; research/ream250_bom/ream250_bom_row_0235_17AG__views_2x2.png; https://esd.equipment/en/bosch-rexroth-3842993033.html"
    cited_fact_or_basis: "BOM row 235 names item 17AG, quantity 2, cad_file 17AG_profile_60x60_300. Manifest row 235 marks CAD export ambiguous and says similar 60x60x300 profiles exist as item 96 but were not substituted as the canonical BOM file. The alternate STEP proxy measures one solid with a 240.00 x 60.00 x 60.00 mm bounding box, and the preview shows a slotted square extrusion. The row-96 BOM/manifest entry identifies the same profile family as a Bosch Rexroth AG strut profile. The vendor page describes a 60 x 60 mm slotted strut profile for structural frames, machine guards, modular workstations, and assembly systems. targeted_web_search: searched '17AG_profile_60x60_300', '17AG profile_60x60_300', and 'Bosch Rexroth 60x60 strut profile aluminum profile'; results found duplicate reAM250 BOM listings for 17AG and Bosch/Rexroth 60x60 strut-profile sources, but no independent row-specific 17AG source."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The ambiguous row-96 60x60 profile STEP instance is treated as the best available geometry proxy for row 235 because the canonical 17AG STEP path is empty."
    - "The row name's profile_60x60_300 token indicates the intended part family even though the measured proxy STEP length is 240 mm."
  uncertainty_notes:
    - "The row identity is not directly matched in CAD; downstream modeling should preserve a note that 17AG is inferred from a similar 60x60 profile export rather than a canonical 17AG part file."
mass:
  value_kg: 0.9369
  basis: "FreeCAD measured the ambiguous alternate STEP proxy volume as 346981.868 mm^3, or 0.000346981868 m^3. The row-96 assembly material extractor matched the same profile geometry as Aluminum with density 2700 kg/m^3, also matching kb/materials/properties.yaml. 0.000346981868 m^3 * 2700 kg/m^3 = 0.93685 kg per physical profile, rounded to 0.9369 kg. BOM quantity is 2, so the row total would be about 1.874 kg. Catalog cross-check: a Bosch Rexroth 60x60 8N profile page lists mass 2.6 kg/m; if the intended length is 300 mm this gives 0.78 kg, while the 240 mm proxy length gives 0.624 kg. The CAD-volume estimate is retained because it is row-package geometry, but it is likely high relative to catalog linear mass."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/instances/17AG_profile_60x60_300__96_profile_60x60_300.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml; https://esd.equipment/en/bosch-rexroth-3842993033.html"
    cited_fact_or_basis: "FreeCAD measured one solid, volume 346981.868 mm^3, area 219269.517 mm^2, and bounding box 240.00 x 60.00 x 60.00 mm for both ambiguous alternate STEP instances. The assembly material extractor found no 17AG material match, but matched 96_profile_60x60_300 to Aluminum with density 2700.0. The local density table lists aluminum density 2700 kg/m^3. The vendor page for Bosch Rexroth 60x60 8N lists mass 2.6 kg/m, material aluminum anodized, and dimensions 60 x 60 mm. targeted_web_search: searched '17AG_profile_60x60_300 mass', '17AG profile_60x60_300 material', and 'Bosch Rexroth 60x60 strut profile mass kg/m'; no row-specific 17AG mass was found, but the Bosch 60x60 family page supplied a catalog linear-mass cross-check."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The ambiguous row-96 STEP proxy is close enough to the row-235 physical item for a per-unit planning mass."
    - "The STEP volume includes the relevant voids/slots and can be multiplied by aluminum density as a coarse physical estimate."
  uncertainty_notes:
    - "The CAD proxy length is 240 mm while the row filename says 300 mm, and the CAD-volume mass is heavier than a Bosch 60x60 8N catalog linear-mass estimate; treat this value as a conservative planning estimate until a canonical 17AG CAD export or article number is resolved."
material:
  primary_material: "aluminum or anodized aluminum strut-profile extrusion"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; https://esd.equipment/en/bosch-rexroth-3842993033.html"
    cited_fact_or_basis: "The assembly STEP material extractor found no direct 17AG material match, but matched the same 60x60 profile geometry under 96_profile_60x60_300 to Aluminum with density 2700.0. Manifest row 235 says similar 60x60x300 profiles exist as item 96. The vendor page for Bosch Rexroth 60x60 8N lists material as aluminum, anodized. targeted_web_search: searched '17AG_profile_60x60_300 material', '17AG profile 60x60 aluminum', and 'Bosch Rexroth 60x60 8N material'; results did not resolve a direct 17AG source but did support aluminum/anodized aluminum for the matching 60x60 strut-profile family."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row-235 17AG profile uses the same material family as the row-96 matched 60x60 strut profile."
  uncertainty_notes:
    - "Exact article number, aluminum alloy, and surface treatment for 17AG are not directly stated by the row; use aluminum/anodized aluminum rather than a specific alloy grade."
how_to_make:
  summary: "Prepare as a cut-to-length 60 x 60 mm modular aluminum strut profile; aluminum extrusion through a slotted-profile die, anodizing, saw cutting, deburring, and any needed end finishing"
  manufacturing_steps:
    - "Cut it to the required BOM length"
    - "Manufacturing route: extrude aluminum alloy through a die forming the 60 x 60 mm slotted square profile cross-section."
    - "Straighten and age or stress-relieve the extrusion as needed for the alloy and dimensional tolerance."
    - "Anodize or otherwise finish the extrusion for corrosion resistance and slot-wear durability."
    - "Saw-cut to the resolved length, deburr, and add any row-specific end drilling or tapping if later drawings require it."
  source:
    url_or_path: "research/ream250_bom/ream250_bom_row_0235_17AG__views_2x2.png; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/instances/17AG_profile_60x60_300__96_profile_60x60_300.step; https://esd.equipment/en/bosch-rexroth-3842993033.html"
    cited_fact_or_basis: "The preview and STEP proxy show a slotted 60 x 60 mm square extrusion. The vendor page describes the 60x60 8N profile as variable length/cut to size, aluminum anodized, with T-slots for modular framing. The detailed extrusion, anodizing, cutting, and finishing route is inferred from the profile geometry and material rather than directly stated as the supplier's manufacturing process. targeted_web_search: searched 'Bosch Rexroth 60x60 strut profile manufacturing extrusion anodized', 'Bosch Rexroth 60x60 8N cut to length', and '17AG_profile_60x60_300 manufacturing'; results supported cut-to-length procurement and aluminum/anodized profile identity but no row-specific factory manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "For KB modeling, this should be treated as reusable strut-profile stock cut to length, not as a bespoke machined bar."
    - "Any end finishing is optional until a row-specific drawing, fastener interface, or canonical CAD file identifies it."
  uncertainty_notes:
    - "The exact intended length remains inconsistent between the row filename and ambiguous CAD proxy; later KB work should capture length as a BOM parameter rather than creating a unique item for each length."
kb_implications:
  - "item_granularity: simple_part - model as reusable cut-to-length 60x60 aluminum strut profile stock, with length/CAD ambiguity captured in BOM notes rather than creating a unique machine-specific item."
---

# reAM250 BOM Row 235 - 17AG

Research result for the leased reAM250 BOM row.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0235_17AG.md
source_research_sha256: "e8bb0026cda1fe8fc1f22491e0f0520fcafe4c817c0efcf1f572a38187a2a364"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Read function, mass basis, material evidence, manufacturing route, CAD proxy, image preview, and KB implications before conversion."
decomposition:
  decision: simple_part
  rationale: "Single cut length of slotted structural stock with no internal closure dependencies; length ambiguity belongs in later BOM notes."
  proposed_subparts: []
process_abstraction:
  original_process_family: aluminum_profile_extrusion_cut_to_length
  primary_process_bucket: structural_profile_stock_fabrication_cutting
  supporting_processes:
    - extrusion
    - heat_treatment
    - surface_finishing
    - cutting
    - deburring
    - drilling
    - dimensional_inspection
  candidate_existing_processes:
    - process_id: metal_extrusion_process_v0
      fit: partial
      reason: "Covers extrusion of metal stock, while the slotted die details and anodized finish remain staging guardrails."
    - process_id: cutting_basic_v0
      fit: supporting
      reason: "Covers cut-to-length work after stock fabrication."
    - process_id: surface_finishing_v0
      fit: supporting
      reason: "Covers finish control after extrusion and cutting when slot wear resistance matters."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers dimensional checks for length, square section, slot condition, and frame fit."
  abstraction_decision: keep_original_family
  rationale: "The source route is already stock extrusion with finishing and cut-to-length work; the bucket preserves that closure handle without creating row-specific profile items."
  process_guardrails:
    tolerance: review
    surface_finish: review
    sealing_quality: not_applicable
    alignment_accuracy: review
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: structural support member for machine framing
  material: anodized_aluminum_strut_stock
  scale_or_capacity:
    mass_kg: 0.9369
    bom_quantity: 2
    row_total_mass_kg: 1.8738
    scale_class: sub_1kg_each
  geometry_form: slotted_square_strut_length
merge_pool:
  eligible: true
  functional_purpose_key: structural_frame_support_member
  precision_guardrails:
    - length_accuracy
    - slot_geometry
    - squareness
    - frame_alignment
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - structural_profile_stock_fabrication_cutting
  import_risk_factors:
    - "Complex slotted die and anodized finish may be deferred if local profile stock capability is absent."
    - "Exact length and row identity use a proxy STEP file, so staging should preserve uncertainty."
  post_merge_decision_notes: "Final import and local manufacture decision is deferred until merge review compares matching frame support rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for shared structural strut stock with row-specific length captured in BOM notes."
assumptions:
  - "The row uses the same aluminum strut family as the matched proxy profile."
  - "Profile length variation can be represented through BOM quantity and notes rather than a unique closure item."
  - "End drilling and tapping are optional secondary steps pending later drawing evidence."
unresolved:
  - "Canonical 17AG STEP geometry is missing; current geometry comes from a similar proxy export."
  - "Filename length and proxy measured length disagree, so final staging must carry length uncertainty."
```
