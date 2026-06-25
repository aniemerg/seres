---
row_identity:
  item: "2AM1"
  cad_file: "2AM1_part_1"
  source_row_number: 65
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.ganternorm.com/de/produkte/3.6-Bewegen-Uebertragen-mit-Wellen-und-Gelenken/Wellenkupplungen/GN-2240-Elastomer-Klauenkupplungen-mit-Klemmnabe#Werkstoff%3Du(b8c35298-9aba-4143-ba51-0f6786b9aaa3)%3BBohrungskennzeichnung%3Du(3f3cf7dd-6770-422d-ad18-23ffeeca0972)%3BH%C3%A4rte%3Du(a3830bd0-c2bd-4c30-ae0a-b3680627ad9a)%3Bd2%3Dc(3)%3Bd3%3Dc(3)%3Bd1%3Dc(14)"
function:
  summary: "Ganternorm GN 2240-30-B8-14-AL-WS-1 elastomer jaw coupling with clamping hub; it transmits torque between two shafts while compensating limited shaft misalignment and runout in the reAM250 drive train."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; https://www.ganternorm.com/de/produkte/3.6-Bewegen-Uebertragen-mit-Gelenken-Kupplungen-und-Getrieben/Wellenkupplungen/GN-2240-Elastomer-Klauenkupplungen-mit-Klemmnabe; research/ream250_bom/ream250_bom_row_0065_2AM1__views_2x2.png"
    cited_fact_or_basis: "BOM row 65 identifies item 2AM1 as Ganternorm product 30-B8-14-AL-WS-1, elastomer jaw coupling GN 2240. The Ganter page describes GN 2240 elastomer jaw couplings with clamping hubs as torque/power transmission couplings that compensate shaft offsets/runout, and the selected parameters include d1 30, bore code B without keyway, d2 8, d3 14, AL aluminum, and WS 92 Shore A white. The CAD preview shows a compact cylindrical jaw coupling with clamp slots and screw bosses."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row's 2AM1_part_1 STEP represents one complete GN 2240 coupling, not a separate spider or one half-hub, because the BOM row quantity is 1 and the CAD preview shows both hub sides and the jaw-coupling form."
  uncertainty_notes: []
mass:
  value_kg: 0.0323
  basis: "FreeCAD measured one solid with volume 12909.276 mm^3, equivalent to 1.2909276e-5 m^3. The vendor resolves the material set as aluminum hubs, TPU spider, and blackened steel screws, but the CAD is a single solid without split volumes. Using an effective density of 2500 kg/m^3 for an aluminum-dominated coupling gives 0.03227 kg per coupling, rounded to 0.0323 kg for quantity 1."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AM1_part_1.step; kb/materials/properties.yaml; https://www.ganternorm.com/de/produkte/3.6-Bewegen-Uebertragen-mit-Gelenken-Kupplungen-und-Getrieben/Wellenkupplungen/GN-2240-Elastomer-Klauenkupplungen-mit-Klemmnabe"
    cited_fact_or_basis: "FreeCAD measured 1 solid, volume 12909.276 mm^3, area 5678.512 mm^2, and bounding box 24.00 x 30.00 x 29.99 mm. Local density table values include aluminum 2700 kg/m^3, NBR/elastomer-like densities near 1100 kg/m^3, and steel 7850 kg/m^3. The Ganter page states aluminum hub, TPU coupling spider, and blackened steel screws. targeted_web_search: searched \"Ganternorm GN 2240 30-B8-14-AL-WS-1 elastomer jaw coupling weight material\", \"GN 2240 30-B8-14-AL-WS-1 weight\", and \"GN 2240 elastomer jaw coupling AL WS 30 B8 14\"; found row-matched product/material/dimension data but no row-specific catalog mass."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The STEP volume is treated as the per-unit physical volume for the complete coupling."
    - "An effective density of 2500 kg/m^3 is used because the part is aluminum-dominated but includes a lower-density TPU spider and small higher-density steel screws."
  uncertainty_notes:
    - "Mass is not a catalog weight and depends on unresolved material volume fractions; a fully aluminum calculation would be about 0.0349 kg, while added steel screws and TPU spider could shift the true mass by several grams."
material:
  primary_material: "Aluminum AL natural-anodized hubs, thermoplastic polyurethane (TPU) coupling spider with WS 92 Shore A hardness, and blackened steel socket cap screws."
  source:
    url_or_path: "https://www.ganternorm.com/de/produkte/3.6-Bewegen-Uebertragen-mit-Gelenken-Kupplungen-und-Getrieben/Wellenkupplungen/GN-2240-Elastomer-Klauenkupplungen-mit-Klemmnabe"
    cited_fact_or_basis: "The BOM-provided Ganter GN 2240 route states hub material as aluminum AL, natural anodized; coupling spider as TPU with selectable hardness including WS 92 Shore A white; and DIN 912 socket cap screws as blackened steel. The product selector includes AL aluminum and WS 92 Shore A white for the row's selected product family."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The source resolves material families and surface state, but not the exact aluminum alloy, TPU formulation, or steel screw grade."
how_to_make:
  summary: "Machined/anodized aluminum clamp hubs, molded or cut TPU jaw spider, blackened steel screw manufacture, and final coupling assembly and bore/runout inspection"
  manufacturing_steps:
    - "Local-manufacturing route: machine two aluminum clamp hubs with jaws, clamp slots, shaft bores, and screw holes from round stock or near-net blanks."
    - "Produce"
    - "Mold or machine the TPU spider to the jaw profile at the required 92 Shore A hardness."
    - "Assemble the hubs and spider, install screws, then inspect bore fit, clamp function, jaw engagement, balance/runout, and torsional coupling fit."
  source:
    url_or_path: "https://www.ganternorm.com/de/produkte/3.6-Bewegen-Uebertragen-mit-Gelenken-Kupplungen-und-Getrieben/Wellenkupplungen/GN-2240-Elastomer-Klauenkupplungen-mit-Klemmnabe; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AM1_part_1.step; research/ream250_bom/ream250_bom_row_0065_2AM1__views_2x2.png"
    cited_fact_or_basis: "The Ganter page identifies GN 2240 as an aluminum clamping-hub elastomer jaw coupling with TPU spider and blackened steel socket cap screws; FreeCAD measured a 24.00 x 30.00 x 29.99 mm envelope; the rendered preview shows cylindrical clamp hubs, jaw teeth, clamp slots, and screw features. The detailed local fabrication sequence is inferred from material and geometry rather than stated by the vendor. targeted_web_search: searched \"Ganternorm GN 2240 30-B8-14-AL-WS-1 elastomer jaw coupling manufacturing\", \"GN 2240 elastomer jaw coupling datasheet\", and \"GN 2240 AL WS material weight\" results resolved product construction and technical data but not the factory manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The manufacturing route treats this as a precision coupling assembly where shaft-bore fit and concentricity matter more than bulk material availability."
    - "Manufacture and elastomer spider production are modeled"
  uncertainty_notes:
    - "The vendor/CAD evidence does not state manufacturing tolerances, balance class, exact bore process, anodizing specification, screw grade, or TPU molding details."
kb_implications:
  - "item_granularity: simple_part - Model as reusable standard jaw-coupling hardware with hubs, elastomer spider, and screws captured in the manufacturing notes; only create a detailed coupling sub-BOM if drive-coupling manufacture becomes a target."
---

# reAM250 BOM Row 65 - 2AM1

Research result for the leased reAM250 BOM row.
