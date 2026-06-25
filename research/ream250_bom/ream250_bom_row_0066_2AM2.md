---
row_identity:
  item: "2AM2"
  cad_file: "2AM2_part_2"
  source_row_number: 66
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.ganternorm.com/de/produkte/3.6-Bewegen-Uebertragen-mit-Wellen-und-Gelenken/Wellenkupplungen/GN-2240-Elastomer-Klauenkupplungen-mit-Klemmnabe#Werkstoff%3Du(b8c35298-9aba-4143-ba51-0f6786b9aaa3)%3BBohrungskennzeichnung%3Du(3f3cf7dd-6770-422d-ad18-23ffeeca0972)%3BH%C3%A4rte%3Du(a3830bd0-c2bd-4c30-ae0a-b3680627ad9a)%3Bd2%3Dc(3)%3Bd3%3Dc(3)%3Bd1%3Dc(14)"
function:
  summary: "Aluminum clamping-hub half of a Ganternorm GN 2240-30-B8-14-AL-WS-1 elastomer jaw coupling; it provides the 14 mm shaft-side hub/jaw interface that clamps to a shaft and mates through the elastomer spider to transmit torque while tolerating small shaft misalignment."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.ganternorm.com/de/produkte/3.6-Bewegen-Uebertragen-mit-Gelenken-Kupplungen-und-Getrieben/Wellenkupplungen/GN-2240-Elastomer-Klauenkupplungen-mit-Klemmnabe; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AM2_part_2.step; research/ream250_bom/ream250_bom_row_0066_2AM2__views_2x2.png"
    cited_fact_or_basis: "BOM row 66 identifies item 2AM2 as Ganternorm product 30-B8-14-AL-WS-1. The Ganter GN 2240 page describes elastomer jaw couplings with clamping hubs as torque/power transmission couplings that compensate shaft offsets and runout, and the selected product family includes d1 30, bore code B without keyway, AL aluminum, and WS 92 Shore A. The row STEP/contact sheet shows one cylindrical jaw-coupling hub with a central bore, jaw teeth, clamp slot, and screw feature."
    evidence_basis: "bom_provided"
  assumptions:
    - "The 2AM2_part_2 STEP is interpreted as the second clamping hub body from the configured 8 mm / 14 mm GN 2240 coupling, because it is a single hub-like solid and sibling row 65 carries the same coupling product ID for the matching side."
  uncertainty_notes:
    - "The row CAD does not include the mating hub, elastomer spider, or separate screw bodies, so this row is treated as the hub-half represented by 2AM2_part_2 rather than the complete catalog coupling assembly."
mass:
  value_kg: 0.0192
  basis: "FreeCAD measured one solid with volume 7096.697 mm^3 = 7.096697e-6 m^3. Using the local aluminum density of 2700 kg/m^3 gives 0.01916 kg, rounded to 0.0192 kg per 2AM2 hub body. BOM quantity is 1, so the row total is also about 0.0192 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AM2_part_2.step; kb/materials/properties.yaml; https://www.ganternorm.com/de/produkte/3.6-Bewegen-Uebertragen-mit-Gelenken-Kupplungen-und-Getrieben/Wellenkupplungen/GN-2240-Elastomer-Klauenkupplungen-mit-Klemmnabe"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 7096.697 mm^3, surface area 3905.047 mm^2, and bounding box 22.50 x 30.00 x 29.99 mm. The local density table lists aluminum at 2700 kg/m^3. The Ganter page states the GN 2240 hub material as aluminum AL, natural anodized."
    evidence_basis: "bom_provided"
  assumptions:
    - "The STEP solid volume is treated as the physical material volume for the row's one hub body."
    - "The row-specific body is modeled as aluminum throughout; the full catalog coupling's TPU spider and steel screws are represented outside this CAD body or by sibling/assembly context."
  uncertainty_notes:
    - "This is a CAD-volume calculation for the row body, not a vendor catalog mass for the complete GN 2240 coupling assembly."
material:
  primary_material: "Aluminum AL, natural-anodized hub body; the complete GN 2240 coupling product family also uses a TPU coupling spider and blackened steel socket cap screws, but those are not visible as separate bodies in this row STEP."
  source:
    url_or_path: "https://www.ganternorm.com/de/produkte/3.6-Bewegen-Uebertragen-mit-Gelenken-Kupplungen-und-Getrieben/Wellenkupplungen/GN-2240-Elastomer-Klauenkupplungen-mit-Klemmnabe; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The BOM-provided Ganter GN 2240 route states the hub is aluminum AL, natural anodized; the coupling spider is thermoplastic polyurethane with selectable hardness including WS 92 Shore A white; and the socket cap screws are blackened steel. Local assembly STEP material extraction for 2AM2_part_2 returned only placeholder material Generic with density 1000.0, so the material value uses the row-matched vendor route."
    evidence_basis: "bom_provided"
  assumptions:
    - "For this row's solid body, the vendor-stated hub material is more specific than the placeholder STEP material metadata."
  uncertainty_notes:
    - "The source resolves the hub material family and surface state, but not the exact aluminum alloy or anodizing specification."
how_to_make:
  summary: "A plausible Manufacturing route for the 2AM2 hub body is precision machining an aluminum clamping hub from round stock or near-net blank, anodizing it, then assembling it with the coupling spider, mating hub, and clamp screw in the coupling"
  manufacturing_steps:
    - "Local hub route: cut aluminum round stock or use a near-net aluminum blank sized for the roughly 22.50 x 30.00 x 29.99 mm hub envelope."
    - "CNC turn/mill the outside diameter, central shaft bore, jaw teeth, clamp slot, and transverse screw feature visible in the CAD preview."
    - "Deburr and natural-anodize the hub, then assemble with the TPU coupling spider, mating hub, and blackened steel socket cap screw."
    - "Inspect shaft bore fit, clamp action, jaw engagement, concentricity/runout, and installed coupling spacing."
  source:
    url_or_path: "https://www.ganternorm.com/de/produkte/3.6-Bewegen-Uebertragen-mit-Gelenken-Kupplungen-und-Getrieben/Wellenkupplungen/GN-2240-Elastomer-Klauenkupplungen-mit-Klemmnabe; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AM2_part_2.step; research/ream250_bom/ream250_bom_row_0066_2AM2__views_2x2.png"
    cited_fact_or_basis: "The Ganter page identifies GN 2240 as an aluminum clamping-hub elastomer jaw coupling with TPU spider and blackened steel socket cap screws. FreeCAD measured a 22.50 x 30.00 x 29.99 mm envelope, and the rendered preview shows a one-piece hub body with bore, jaw teeth, clamp slot, and screw feature. The detailed local fabrication sequence is inferred from material and geometry rather than stated by the vendor. targeted_web_search: searched \"Ganternorm GN 2240 30-B8-14-AL-WS-1 manufacturing\", \"GN 2240 elastomer jaw coupling datasheet manufacturing\", and \"GN 2240 AL WS material weight\" results resolved product construction and technical data but not the factory manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Subtractive machining is the planning route because the row body is a small precision aluminum shaft-coupling hub with bore, clamp, and jaw features."
    - "Near-term KB use should prefer a external configured coupling or hub abstraction until precision coupling manufacture, anodizing, elastomer spider production, and inspection are modeled"
  uncertainty_notes:
    - "Vendor/CAD evidence does not state the exact production process, tolerances, balance class, bore finishing method, screw grade, or anodizing standard."
kb_implications:
  - "item_granularity: simple_part - model this row as one aluminum clamping-hub body from a standard jaw-coupling family; keep the full coupling or purchased module as a higher-level abstraction if sibling hub, spider, screws, and performance selection are modeled together later."
---

# reAM250 BOM Row 66 - 2AM2

Research result for the leased reAM250 BOM row.
