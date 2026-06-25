---
row_identity:
  item: "31"
  cad_file: "31_circulation_pump"
  source_row_number: 249
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.becker-international.com/de/de/produkte/vakuumpumpen/seitenkanal-vakuumpumpen/sv201-einstufig.htm"
function:
  summary: "Becker SV 201/1 single-stage side-channel vacuum pump/blower module that provides oil-free, non-contact vacuum or low-pressure air flow for the reAM250 circulation/vacuum circuit."
  source:
    url_or_path: "https://www.becker-international.com/de/de/produkte/vakuumpumpen/seitenkanal-vakuumpumpen/sv201-einstufig.htm; design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/31_circulation_pump.step"
    cited_fact_or_basis: "BOM row 249 identifies item 31 as 31_circulation_pump, product G050508, Becker GmbH. The BOM-provided Becker page is for SV 201/1, a single-stage side-channel vacuum pump/blower with oil-free, non-contact operation, integrated inlet/discharge silencers, pedestal/vibration-isolator mounting, and 190 m3/h flow at 50 Hz. FreeCAD measured one CAD solid with bounding box about 462.74 x 708.08 x 546.18 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM product token G050508 corresponds to the linked Becker SV 201/1 pump row identity."
  uncertainty_notes:
    - "The CAD contact-sheet renderer was stopped after an extended FreeCAD run, so visible feature inspection is limited to the STEP geometry measurement and vendor product description."
mass:
  value_kg: 32.5
  basis: "Use the Becker SV 201/1 listed weight of 32.5 kg with motor as the per-unit BOM mass. BOM quantity is 1, so the row total is also about 32.5 kg. FreeCAD measured CAD volume about 22,590,938.655 mm3, area about 2,308,526.908 mm2, and bounding box about 462.74 x 708.08 x 546.18 mm; vendor mass supersedes CAD density estimation for this multi-material pump module."
  source:
    url_or_path: "https://www.becker-international.com/de/de/produkte/vakuumpumpen/seitenkanal-vakuumpumpen/sv201-einstufig.htm; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/31_circulation_pump.step"
    cited_fact_or_basis: "Becker SV 201/1 specifications list Gewicht 32,5 kg mit Motor. FreeCAD measured one solid, volume about 22,590,938.655 mm3, area about 2,308,526.908 mm2, and bounding box about 462.74 x 708.08 x 546.18 mm."
    evidence_basis: "bom_provided"
  assumptions:
    - "The listed Becker weight with motor is the relevant installed purchased-module mass for the CAD/BOM row."
  uncertainty_notes:
    - "The CAD export is a vendor component represented as one solid and does not expose separate motor, blower, filter, silencer, bearing, or fastener masses."
material:
  primary_material: "Unknown multi-material electromechanical pump module: metal/alloy blower structure and motor hardware, electrical conductor/insulation materials, plus elastomer or polymer mounting, filter, and seal materials."
  source:
    url_or_path: "https://www.becker-international.com/de/de/produkte/vakuumpumpen/seitenkanal-vakuumpumpen/sv201-einstufig.htm; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Becker page identifies a motorized side-channel pump with sealed bearings, integrated inlet/discharge silencers, optional internal inlet filter/safety valve, and pedestal or rubber-buffer mounting. Local assembly STEP material extraction for 31_circulation_pump returned only Generic with density 1000.0, which is placeholder metadata and was not used to resolve material. targeted_web_search: queries tried included 'Becker SV 201/1 material housing side channel blower aluminum cast iron' and 'Becker SV 201/1 datasheet weight material G050508'; results gave row-matched function, dimensions, and mass but no authoritative material breakdown."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Common side-channel blower construction is used only at broad material-family level because no row-matched source found a specific material grade or component material breakdown."
  uncertainty_notes:
    - "Material families should not be treated as a sourced Becker bill of materials; a future local-manufacturing model needs a Becker parts list or teardown-level source."
how_to_make:
  summary: "Current KB route should procure the Becker SV 201/1/G050508 as a calibrated purchased pump module; a later local-manufacture route would decompose it into cast or machined blower housing/impeller parts, an electric motor, sealed bearings, silencers/filter hardware, seals, vibration mounts, final assembly, and pump performance testing."
  manufacturing_steps:
    - "Procure Becker SV 201/1/G050508 pump module as a finished vendor component for near-term modeling."
    - "Install the pump on its pedestal or vibration isolators and connect the suction/discharge ports into the reAM250 circulation or vacuum plumbing."
    - "For future local manufacture, model separate processes for blower housing and impeller fabrication, motor manufacture or import, bearing/seal/filter sourcing, mechanical assembly, electrical hookup, and performance/leak/sound testing."
  source:
    url_or_path: "https://www.becker-international.com/de/de/produkte/vakuumpumpen/seitenkanal-vakuumpumpen/sv201-einstufig.htm; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/31_circulation_pump.step"
    cited_fact_or_basis: "The Becker page identifies the SV 201/1 as a motorized single-stage side-channel vacuum pump/blower with oil-free non-contact operation, sealed bearings, integrated silencers, pedestal/vibration-isolator mounting, and published performance specifications. FreeCAD confirms the row CAD is one large vendor-component solid. targeted_web_search: 'Becker SV 201/1 datasheet weight material G050508' and related material/manufacturing queries found product/datasheet pages but no row-specific factory manufacturing route."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Procurement is the appropriate near-term manufacturing/procurement route because the row is a vendor pump module without sub-BOM detail."
    - "The local-manufacture decomposition is a planning hypothesis based on the vendor function and common electromechanical blower architecture."
  uncertainty_notes:
    - "A self-manufacturing path would need subcomponent specifications, tolerances, balancing requirements, motor data, bearing sizes, and acceptance tests before this can become a concrete KB recipe."
kb_implications:
  - "item_granularity: complex_module - Model this as one Becker circulation/vacuum pump complex module for this pass; split into motor, blower housing/impeller, bearings, seals, filters, and mounts only if pump manufacturing becomes a priority."
---
