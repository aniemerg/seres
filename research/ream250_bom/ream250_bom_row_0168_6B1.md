---
row_identity:
  item: "6B1"
  cad_file: "6B1_gliding_surface"
  source_row_number: 168
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Long, narrow stainless gliding surface or wear rail used to provide a smooth sliding/contact face in the reAM250 assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B1_gliding_surface.step; research/ream250_bom/ream250_bom_row_0168_6B1__views_2x2.png"
    cited_fact_or_basis: "BOM row 168 names item 6B1 with quantity 1 and CAD file 6B1_gliding_surface; manifest row 168 maps it to one matched part STEP. FreeCAD measured one solid with bounding box 50.00 x 10.00 x 274.00 mm, and the rendered preview shows a long thin rail-like contact member."
    evidence_basis: "bom_provided"
  assumptions:
    - "The BOM/CAD name 'gliding_surface' is interpreted as the functional role rather than a decorative cover."
  uncertainty_notes:
    - "The mating component and exact sliding load direction are not identified by the isolated part export."
mass:
  value_kg: 0.864
  basis: "Per-unit mass for quantity 1. FreeCAD volume is 107985.102 mm^3 = 0.000107985 m^3; assembly STEP metadata reports Stainless Steel with density 8000 kg/m^3, giving 0.863881 kg, rounded to 0.864 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B1_gliding_surface.step; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step; kb/materials/properties.yaml"
    cited_fact_or_basis: "FreeCAD measured one solid with volume 107985.102 mm^3. Local STEP material extraction for product 6B1_gliding_surface found material 'Stainless Steel' and density 8000.0 in the full assembly. The local material properties table lists stainless_steel density as 8000 kg/m^3."
    evidence_basis: "bom_provided"
  assumptions:
    - "The exported single-solid STEP volume represents one physical 6B1 part."
    - "The stainless steel density applies uniformly to the whole modeled solid."
  uncertainty_notes:
    - "CAD mass excludes any separate coatings, lubricants, or fasteners not present in the isolated gliding-surface solid."
material:
  primary_material: "stainless steel"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "Local assembly STEP material extraction for product 6B1_gliding_surface returned material 'Stainless Steel' with density 8000.0."
    evidence_basis: "bom_provided"
  assumptions: []
  uncertainty_notes:
    - "The STEP metadata does not specify a stainless grade or surface finish."
how_to_make:
  summary: "Plausible route: cut stainless bar or plate stock to length, machine the profiled ends and contact geometry, deburr, and finish or polish the sliding/contact face before inspection."
  manufacturing_steps:
    - "Prepare stainless steel rectangular bar or plate stock sized for the 50 x 10 x 274 mm envelope"
    - "Saw or abrasive-cut the blank to length."
    - "Mill the end profiles and any relieved rail features visible in the CAD preview."
    - "Deburr edges and polish or grind the gliding contact face to the required sliding finish."
    - "Inspect length, thickness, straightness, and contact-surface finish against the CAD model."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/6B1_gliding_surface.step; research/ream250_bom/ream250_bom_row_0168_6B1__views_2x2.png; https://pbclinear.com/pages/gliding-surface-technology-catalog; https://www.pobcoplastics.com/product-categories/wear-strips-guide-rails/"
    cited_fact_or_basis: "CAD shows a single stainless rail-like solid with a 50.00 x 10.00 x 274.00 mm envelope and profiled ends. Web sanity check found gliding-surface linear guides and wear-strip/guide-rail product families, but no row-specific manufacturing route. targeted_web_search: queries tried 'stainless steel gliding surface wear strip manufacturing machined ground guide rail', 'stainless steel wear strip gliding surface guide rail', and 'stainless steel sliding surface guide rail ground finish manufacturing'; results supported the guide/wear-surface interpretation but did not identify a reAM250-specific process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Because the part is a simple monolithic stainless rail, subtractive machining from bar or plate stock is more plausible than casting or a vendor module route at this modeling resolution."
    - "A smoother sliding face is required by the 'gliding_surface' role, so a final deburr and finish operation is included."
  uncertainty_notes:
    - "The actual production drawing may require a specific roughness, hardening, passivation, or coating not visible in the STEP export."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable stainless machined wear rail/gliding surface rather than a purchased module; no sub-BOM is implied by the single-solid CAD and BOM row."
---
