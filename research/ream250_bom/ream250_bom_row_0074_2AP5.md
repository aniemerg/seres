---
row_identity:
  item: "2AP5"
  cad_file: "2AP5_bolt_DIN 912 - M6x1x20x17,5"
  source_row_number: 74
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "DIN 912 M6 x 20 socket-head cap screw used as mechanical fastening hardware; the BOM quantity is 8."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP5_bolt_DIN 912 - M6x1x20x17,5.step; research/ream250_bom/ream250_bom_row_0074_2AP5__views_2x2.png"
    cited_fact_or_basis: "BOM row 74 lists item 2AP5, quantity 8, CAD file '2AP5_bolt_DIN 912 - M6x1x20x17,5', and description 'cylinder head cap screw'. FreeCAD measured one solid with a bounding box about 26.00 x 10.82 x 10.82 mm; the rendered preview shows a cylindrical socket head, threaded shank, and internal hex socket."
    evidence_basis: "bom_provided"
  assumptions:
    - "The DIN 912 M6x1x20 designation is interpreted as a metric socket-head cap screw with nominal M6 coarse thread and 20 mm screw length."
  uncertainty_notes: []
mass:
  value_kg: 0.00747
  basis: "Per-unit estimate: FreeCAD STEP volume 952.219 mm^3 converted to 9.52219e-7 m^3 and multiplied by the BOM-provided STEP material density 7850 kg/m^3, giving about 0.00747 kg per screw. BOM quantity is 8, so the row total is about 0.0598 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP5_bolt_DIN 912 - M6x1x20x17,5.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "FreeCAD measured 1 solid, 952.219 mm^3 volume, 762.910 mm^2 area, and about 26.00 x 10.82 x 10.82 mm bounding box. The assembly STEP material extractor matched this product to material 'Steel, Mild' with density 7850.0."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported STEP volume represents the physical screw volume closely enough for BOM mass estimation."
  uncertainty_notes:
    - "Thread detail, socket recess fidelity, and any coating/plating are not separately resolved, so the mass should be treated as a CAD-derived estimate rather than a catalog weight."
material:
  primary_material: "mild steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The local assembly STEP material extractor matched product '2AP5_bolt_DIN 912 - M6x1x20x17,5' to material 'Steel, Mild' and density 7850.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The exact screw property class, heat treatment, alloy specification, and surface finish are not specified by the BOM fields or local STEP material metadata."
how_to_make:
  summary: "Model as a standard steel socket-head cap screw: form a steel blank and cylindrical head, create the hex socket, form the M6 thread, finish/deburr, optionally coat, and inspect dimensions."
  manufacturing_steps:
    - "Start from steel wire or bar stock sized for an M6 socket-head screw blank."
    - "Cold head or machine the cylindrical cap head and shank blank."
    - "Broach or form the internal hex socket in the head."
    - "Roll or cut the M6x1 thread on the shank to the DIN 912 M6 x 20 convention."
    - "Deburr, clean, optionally apply a protective finish, and inspect thread fit, socket size, head geometry, and length."
  source:
    url_or_path: "https://www.intafast.com/wp-content/uploads/2019/09/Din912_ISO_4762_Socket_cap_screws-1.pdf; https://www.carpentertechnology.com/hubfs/PDFs/HeadingHintsAGuidetoColdFormingSpecialtyAlloys.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AP5_bolt_DIN 912 - M6x1x20x17,5.step"
    cited_fact_or_basis: "The DIN 912 / ISO 4762 fastener reference identifies hexagon socket head screws and lists material as steel for grade 12.9 examples. The cold-forming reference discusses cold heading practices, hex head cap screws, thread rolling, and secondary operations. The row CAD is a one-solid socket-head screw geometry. targeted_web_search: searched 'socket head cap screw manufacturing process cold heading thread rolling heat treatment', 'DIN 912 socket head cap screw material steel 8.8 12.9', and 'M6 DIN 912 socket head cap screw dimensions head diameter 10 mm head height 6 mm'; found general standard/vendor/manufacturing references but no row-specific manufacturing process sheet."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Cold heading, socket forming/broaching, and thread rolling are treated as the representative scalable process route for standard steel socket-head screws; machining is an acceptable low-volume fallback."
    - "The BOM does not require modeling a special-purpose bespoke part beyond reusable standard fastener stock or a fastener kit."
  uncertainty_notes:
    - "The exact production route, property class, heat treatment, and coating are not specified for this row."
kb_implications:
  - "item_granularity: simple_part - Finished DIN 912 socket-head cap screws should map to reusable standard fastener hardware or a fastener kit, not raw stock or a machine-specific custom part."
---
