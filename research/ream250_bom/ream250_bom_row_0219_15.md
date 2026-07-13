---
row_identity:
  item: "15"
  cad_file: "15_seal_door"
  source_row_number: 219
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.lisema.eu/Moosgummiprofile_Halbrund"
function:
  summary: "Compressible rectangular door seal for the reAM250 enclosure or chamber door; CAD shows one continuous rectangular gasket loop made from a narrow half-round/bulb sponge-rubber profile."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/manifest.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/15_seal_door.step; research/ream250_bom/ream250_bom_row_0219_15__views_2x2.png; https://lisema.eu/Moosgummiprofile_Halbrund"
    cited_fact_or_basis: "BOM row 219 states item 15, quantity 1, CAD file 15_seal_door, manufacturer Lisema, and the Lisema half-round sponge-profile URL. The manifest maps the row to gold_export/parts/15_seal_door.step as a matched vendor-component export. FreeCAD measured 1 solid with bounding box about 844.94 x 20.00 x 404.94 mm; the rendered contact sheet shows a thin rectangular gasket loop. The Lisema page is for NEOSOFT EPDM sponge half-round and hollow chamber standard profiles and lists 20 x 20 mm black half-round-profile stock matching the CAD profile thickness."
    evidence_basis: "bom_provided"
  assumptions:
    - "The filename seal_door and rectangular compressible-loop geometry are interpreted as a door perimeter seal rather than a structural frame."
  uncertainty_notes:
    - "The CAD/BOM evidence identifies the seal role and approximate envelope, but not the exact mating groove, compression percentage, adhesive layout, or required leak-rate specification."
mass:
  value_kg: 0.23
  basis: "FreeCAD volume 453695.042 mm^3 equals 453.695 cm^3 or 0.000453695 m^3 for one seal. Using a representative apparent density of 0.5 g/cm^3 (500 kg/m^3) for EPDM sponge rubber profiles gives 0.000453695 m^3 * 500 kg/m^3 = 0.2268 kg, rounded to 0.23 kg per unit. BOM quantity is 1, so the row total is also about 0.23 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/15_seal_door.step; https://lisema.eu/Moosgummiprofile_Halbrund; https://kremer-tec.de/en/products/rubber-profiles/epdm-profiles.html"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 453695.042 mm^3, area 133536.424 mm^2, and bounding box about 844.94 x 20.00 x 404.94 mm. The Lisema BOM route identifies the material family as EPDM sponge profile but does not state mass or density. Independent web search found Kremer's EPDM profile page, which states that EPDM sponge rubber cords and sponge rubber profiles commonly have density about 0.5 g/cm^3, lower than solid EPDM profiles due to cellular structure. bom_url_route_check: the BOM-provided Lisema URL was checked first and resolved material/profile dimensions but not row-specific density or weight, so the different-domain Kremer profile source was used only for the density constant."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The STEP solid volume is used as the apparent-volume proxy for one physical gasket loop."
    - "The independent EPDM sponge-profile density is treated as representative for the Lisema NEOSOFT EPDM sponge profile because Lisema does not publish row-specific density or weight on the BOM-provided page."
  uncertainty_notes:
    - "The mass is sensitive to foam density and profile hollowness; lower-density closed-cell EPDM sponge grades could make the real mass materially lower, while denser sponge grades could make it higher."
material:
  primary_material: "black EPDM sponge rubber profile with mixed open/closed cellular structure and closed outer skin"
  source:
    url_or_path: "https://lisema.eu/Moosgummiprofile_Halbrund; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Lisema BOM-provided route identifies NEOSOFT sponge-rubber half-round and hollow-chamber standard profiles made from black EPDM. The same page describes mixed cells with both closed and open pores and a protective closed outer skin, and gives hardness about 15-20 Shore A. The local assembly STEP material extractor matched 15_seal_door but returned only Generic material and density 1000.0, so STEP metadata did not resolve material."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "Lisema identifies the material family and hardness range, but not the exact EPDM compound, filler package, density, adhesive backing, or batch-specific datasheet."
how_to_make:
  summary: "Locally fabricate as a cut-to-length EPDM sponge half-round profile formed into a rectangular frame seal, with corners joined by adhesive bonding or vulcanized joining and the finished loop fitted to the door perimeter"
  manufacturing_steps:
    - "Select black EPDM sponge half-round or hollow-chamber profile stock matching the CAD cross section, approximately 20 mm profile thickness."
    - "Cut four profile lengths to the door perimeter dimensions with mitered or square ends as required by the corner-joint design."
    - "Join the corners by suitable rubber-profile adhesive bonding or vulcanized corner joining, then allow the joint to cure."
    - "Trim flash or excess adhesive and inspect continuity, corner alignment, and compression surface quality."
    - "Install on the door or mating groove with the specified adhesive or mechanical retention and verify uniform compression around the rectangular loop."
  source:
    url_or_path: "https://lisema.eu/Moosgummiprofile_Halbrund; https://kremer-tec.de/en/products/rubber-profiles/epdm-profiles.html; research/ream250_bom/ream250_bom_row_0219_15__views_2x2.png"
    cited_fact_or_basis: "Lisema identifies the BOM route as EPDM sponge half-round/hollow-chamber profiles and states bonding guidance for these profiles. Independent web search found Kremer's EPDM profile page, which states EPDM profiles can be supplied by the metre, as profile sections, bonded or impact-vulcanized rings, and corner-vulcanized frame seals. The CAD contact sheet shows the row-specific part as a rectangular loop seal. bom_url_route_check: the BOM-provided Lisema URL was checked first and resolved the product family and bonding note, but did not state whether this row was supplied as a cut profile, bonded loop, or vulcanized frame, so the different-domain Kremer source was used for the frame-seal delivery/manufacturing route."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The reAM250 row is treated as a finished gasket loop made from profile stock rather than a raw 5 m vendor coil, because the CAD export is a closed rectangular loop sized to the machine door."
    - "Local fabrication would reuse general rubber-profile cutting, bonding, and inspection tooling rather than requiring a dedicated special-purpose machine."
  uncertainty_notes:
    - "The sources support the profile and frame-seal route, but the row does not state whether Lisema supplied this exact seal as a bonded loop, a loose profile length cut during assembly, or a corner-vulcanized custom frame."
kb_implications:
  - "item_granularity: simple_part - door gasket/seal should later map to a reusable elastomer seal/profile replaceable or applied part rather than a machine-specific structural part; model size and material as variants of generic EPDM sponge seal stock where possible."
---

Research result for reAM250 BOM row 219.

## KB Conversion

```yaml
conversion_status: row_reviewed
source_research_file: research/ream250_bom/ream250_bom_row_0219_15.md
source_research_sha256: "5659a21bbef93397b8f1f7a2fa56e20833f3543869644061aa61de261c161c64"
evidence_reviewed:
  original_research_sections:
    - function
    - mass
    - material
    - how_to_make
    - kb_implications
  geometry_evidence_used: true
  notes: "Reviewed the original seal function, 0.23 kg mass estimate, EPDM sponge material evidence, local profile-cutting and corner-joining route, KB implication, and CAD contact sheet showing a thin rectangular gasket loop."
decomposition:
  decision: simple_part
  rationale: "The row is one continuous compressible door gasket loop made from sponge-rubber profile stock; it has no internal modules worth decomposing for closure analysis."
  proposed_subparts: []
process_abstraction:
  original_process_family: rubber_profile_cutting_bonding_vulcanized_joining
  primary_process_bucket: polymer_elastomer_forming_dispensing
  supporting_processes:
    - elastomer_forming
    - cutting
    - joining
    - curing
    - cleaning
    - dimensional_inspection
    - leak_testing
    - assembly
  candidate_existing_processes:
    - process_id: elastomer_molding_basic_v0
      fit: partial
      reason: "Captures generic elastomer forming with a molding press, but does not specifically model extruded sponge-profile stock plus corner-frame joining."
    - process_id: molding_basic_v0
      fit: partial
      reason: "Relevant fallback for producing rubber/plastic intermediate shapes before profile cutting; material and profile-cell structure would need recipe binding."
    - process_id: gasket_sheet_cut_to_part_v0
      fit: supporting
      reason: "Anchors simple gasket cutting operations, though this row is a half-round profile loop rather than a flat gasket sheet."
    - process_id: seal_installation_v0
      fit: supporting
      reason: "Covers installation of seals and gaskets into components after the loop has been fabricated."
    - process_id: leak_testing_v0
      fit: supporting
      reason: "Relevant if merge review keeps a chamber-door sealing requirement with verified compression plus leak performance."
    - process_id: inspection_basic_v0
      fit: supporting
      reason: "Covers visual and dimensional checks of the finished gasket loop."
  abstraction_decision: substitute_process_family
  rationale: "The source route is a vendor EPDM profile/frame seal, but the closure model should represent it as a reusable elastomer-forming, profile-cutting, joining, curing, and inspection path rather than a row-specific purchased profile."
  process_guardrails:
    tolerance: low_to_moderate
    surface_finish: compression_skin_quality_review
    sealing_quality: review
    alignment_accuracy: low
    blocked_by_precision: false
identity_for_merge:
  functional_purpose: "compressible perimeter seal for a machine enclosure chamber door"
  material: epdm_sponge_rubber
  scale_or_capacity:
    mass_kg: 0.23
    bom_quantity: 1
    row_total_mass_kg: 0.23
    scale_class: small
  geometry_form: rectangular_half_round_profile_gasket_loop
merge_pool:
  eligible: true
  functional_purpose_key: environment_barrier
  precision_guardrails:
    - sealing_quality
    - compression_set
    - corner_joint_continuity
    - profile_cross_section
downstream_decision_inputs:
  local_manufacturing_paths_considered:
    - polymer_elastomer_forming_dispensing
  import_risk_factors:
    - "Exact EPDM sponge compound, cellular structure, closed outer skin, and long-term compression set may be difficult to reproduce locally."
    - "Leak-rate and chamber atmosphere requirement are not specified; high sealing performance could shift the part toward import plus specialized elastomer processing."
  post_merge_decision_notes: "Final import/local decision is deferred until after merge review compares this gasket with other enclosure, chamber, and door sealing rows."
kb_staging:
  proposed_item_id: null
  notes: "Wait for merge review; likely candidate for a generic EPDM sponge door gasket/profile seal rather than a row-specific item."
assumptions:
  - "BOM quantity is 1 and row total mass is treated as 0.23 kg from the source research."
  - "The CAD preview confirms a rectangular loop with a narrow roughly 20 mm profile, so geometry evidence was used for merge identity."
  - "Local closure path assumes profile stock can be formed, then substituted by a compatible elastomer profile, cut, and joined into a loop."
unresolved:
  - "Exact adhesive, vulcanized corner method, mating groove geometry, compression percentage, and leak-rate requirement are not specified."
  - "The exact EPDM sponge density, compound, filler package, and aging/compression-set performance remain unresolved."
```
