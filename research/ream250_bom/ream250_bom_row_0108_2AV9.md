---
row_identity:
  item: 2AV9
  cad_file: "2AV9_DIN 912 - M6x1x16x13,5"
  source_row_number: 108
  source_csv: design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv
function:
  summary: "M6 x 1 socket-head cap screw used as a removable threaded fastener; the cylindrical head and internal hex socket allow high-clamp assembly in a compact counterbore or limited-access location."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV9_DIN 912 - M6x1x16x13,5.step; research/ream250_bom/ream250_bom_row_0108_2AV9__views_2x2.png"
    cited_fact_or_basis: "BOM row 108 identifies item 2AV9 as quantity 5, description 'cylinder head cap screw', CAD name 'DIN 912 - M6x1x16x13,5'. FreeCAD reads one solid with a 22.00 x 10.82 x 10.82 mm bounding box; preview shows a cylindrical socket head, internal hex drive, and threaded shank."
    evidence_basis: bom_provided
  assumptions:
    - "The row uses the DIN 912 designation conventionally: M6 nominal thread, 1 mm pitch, about 16 mm screw length, with the trailing 13.5 value treated as CAD/source-specific thread or engagement detail rather than a separate BOM item."
  uncertainty_notes:
    - "The exact mating component in the parent assembly is not identified in this row-level task, so the function is limited to generic fastening/clamping rather than a named joint."
mass:
  value_kg: 0.00659
  basis: "Per-unit mass for one screw. FreeCAD volume is 839.121 mm^3; STEP assembly material metadata gives Steel, Mild with density 7850 kg/m^3. Calculation: 839.121e-9 m^3 * 7850 kg/m^3 = 0.006587 kg per screw. BOM quantity is 5, so row total is about 0.0329 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AV9_DIN 912 - M6x1x16x13,5.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD shape measurement: 1 solid, volume 839.121 mm^3, area 687.511 mm^2, bounding box 22.00 x 10.82 x 10.82 mm. Local STEP material extractor returns material 'Steel, Mild' and density 7850.0 kg/m^3; local material properties list generic steel density as 7850 kg/m^3."
    evidence_basis: bom_provided
  assumptions:
    - "The STEP volume is treated as the physical solid volume for the screw, including modeled thread and socket geometry."
    - "The row-specific STEP density is used directly and cross-checks the local generic steel density."
  uncertainty_notes:
    - "Real purchased fasteners may vary slightly with thread simplification, head socket modeling, coating, and tolerance, but the CAD-derived value is adequate for BOM mass planning."
material:
  primary_material: "mild steel / generic steel fastener material"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The row-specific assembly STEP material extraction for product '2AV9_DIN 912 - M6x1x16x13,5' returns material 'Steel, Mild' with density 7850.0 kg/m^3."
    evidence_basis: bom_provided
  assumptions: []
  uncertainty_notes:
    - "The BOM-side metadata does not state property class, coating, or heat-treatment condition; do not infer 8.8, 10.9, 12.9, zinc-plated, or black-oxide specifics from this row alone."
how_to_make:
  summary: "Best modeled as a external standard DIN 912 / ISO 4762 style steel socket-head cap screw. A Manufacturing route would use steel wire or rod, cold heading to form the cylindrical socket head, hex-socket forming, thread rolling for the M6 x 1 external thread, then heat treatment and optional surface finish"
  manufacturing_steps:
    - "Manufacturing route: cut steel wire or rod blank to length."
    - "Cold-head the cap screw blank and form the cylindrical head and internal hex socket."
    - "Roll the M6 x 1 external thread rather than machining it when using standard high-volume fastener practice."
    - "Apply heat treatment and a protective finish if required by the final fastener property class or corrosion environment."
  source:
    url_or_path: "https://www.metricmcc.com/full-thread-912-c-1_19_20_23.html; https://fastcoindustries.com/thread-rolling-service-cold-heading-fastener-manufacturers-usa/; https://www.tannerbolt.com/trc/post/fastener-tech-cold-heading"
    cited_fact_or_basis: "Metric & Multistandard describes DIN 912 socket head screws as Allen-key fasteners made to DIN 912 specifications and supplied in materials including property class 12.9. Fastco describes thread rolling as forming external screw threads by pressing dies against a cold-headed blank. Tanner Bolt describes roll threading after cold heading with flat-faced reciprocating dies. These sources support the standard procurement and manufacturing route; row identity still comes from the BOM/CAD package."
    evidence_basis: independent_vendor_spec
  assumptions:
    - "For KB planning, this row should not require a unique custom machine component; it can be represented by a reusable standard socket-head cap screw family or fastener kit unless a later model needs exact DIN 912 variants."
  uncertainty_notes:
    - "The cited manufacturing sources support standard cap-screw and thread-rolling practice, but they are not row-specific production records for this exact reAM250 screw."
kb_implications:
  - "item_granularity: simple_part - Model as a standard purchased/manufacturable socket-head cap screw or reusable fastener-kit member, not as a custom assembly or raw stock."
---
