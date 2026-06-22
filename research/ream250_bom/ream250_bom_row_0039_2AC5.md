---
row_identity:
  item: "2AC5"
  cad_file: "2AC5_part_5"
  source_row_number: 39
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
function:
  summary: "Small spherical rolling/contact element in the bottom axis bearing group; it likely serves as one ball or pivot-contact element that supports low-friction axis motion."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC5_part_5.step; research/ream250_bom/ream250_bom_row_0039_2AC5__views_2x2.png"
    cited_fact_or_basis: "BOM row 39 names item 2AC5, quantity 1, description 'axis bearing bottom'; FreeCAD measured one solid with 5.4 x 5.4 x 5.4 mm bounding box, and the rendered preview shows a smooth sphere."
    evidence_basis: "bom_provided"
  assumptions:
    - "The spherical CAD solid represents the physical row item, not merely an envelope or placeholder."
  uncertainty_notes:
    - "The BOM description names the bearing group but does not state the exact contact role within the lower-axis bearing assembly."
mass:
  value_kg: 0.000644
  basis: "Per-unit estimate for quantity 1. FreeCAD volume is 82.448 mm^3, equal to 0.082448 cm^3; using 7.81 g/cm^3 for AISI 52100 bearing chrome steel gives 0.644 g, or 0.000644 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC5_part_5.step; https://www.redhillballs.com/product/bearing-steel-balls/bearing-chrome-steel-balls/"
    cited_fact_or_basis: "FreeCAD measured volume 82.44795760081057 mm^3. Redhill Balls describes bearing chrome steel balls as AISI 52100, diameter range 0.5-150.0 mm, density about 7.81 g/cm^3. targeted_web_search: queries tried were '5.4 mm bearing ball material chrome steel stainless steel bearing balls' and 'axis bearing bottom 5.4 mm ball bearing material reAM250 2AC5'; no row-specific vendor mass was found, but general bearing-ball material/density evidence matched the CAD sphere and bearing description."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The row item is modeled as a solid bearing chrome-steel ball."
    - "The CAD volume is taken as the physical solid volume for one item."
  uncertainty_notes:
    - "Mass would change if the actual part is stainless steel, ceramic, or another bearing-ball material rather than chrome bearing steel."
material:
  primary_material: "unknown bearing-ball metal/alloy"
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC5_part_5.step; https://www.redhillballs.com/product/bearing-steel-balls/bearing-chrome-steel-balls/; https://blog.igus.eu/what-materials-are-used-to-make-ball-bearing-balls/"
    cited_fact_or_basis: "BOM-side evidence gives an axis-bearing context and CAD sphere geometry; assembly STEP material extraction for 2AC5_part_5 returns only placeholder 'Generic' at density 1000.0. Redhill Balls identifies bearing chrome steel balls as AISI 52100 and available in 0.5-150.0 mm diameters. igus states chrome steel is the most often used material for bearing balls. targeted_web_search: queries tried were '5.4 mm bearing ball material chrome steel stainless steel bearing balls' and 'axis bearing bottom 5.4 mm ball bearing material reAM250 2AC5'; no row-specific material source was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "A small spherical item in a bottom-axis bearing is more likely a hardened bearing-steel ball, such as chrome bearing steel, than a polymer spacer or non-bearing decorative sphere."
  uncertainty_notes:
    - "The reAM250 CAD/STEP package does not provide a non-placeholder material for this row, so the material should be treated as inferred until a drawing, purchase record, or assembly note confirms it."
how_to_make:
  summary: "Procure as a precision bearing ball when possible; local manufacture would use bearing-steel wire or rod slugging, cold heading or forging, flashing removal, heat treatment, grinding/lapping, polishing, and inspection."
  manufacturing_steps:
    - "Select bearing-quality chrome steel stock sized for a roughly 5.4 mm ball."
    - "Form near-spherical blanks by cold heading or similar ball-blank forming."
    - "Remove flash, harden and temper, then precision grind/lap and polish to final diameter and roundness."
    - "Inspect diameter, roundness, surface finish, and hardness before installation in the bottom axis bearing."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/2AC5_part_5.step; https://www.redhillballs.com/product/bearing-steel-balls/bearing-chrome-steel-balls/"
    cited_fact_or_basis: "CAD shows a small sphere used in an axis-bearing context. Redhill Balls identifies chrome steel bearing balls as high-precision AISI 52100 components with hardened martensitic structure and high hardness; the detailed local forming, grinding, lapping, and inspection sequence is inferred from standard bearing-ball manufacturing practice. targeted_web_search: queries tried were '5.4 mm bearing ball material chrome steel stainless steel bearing balls' and 'axis bearing bottom 5.4 mm ball bearing material reAM250 2AC5'; no row-specific manufacturing drawing or supplier route was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "The KB should initially model this as a finished precision rolling element rather than raw spherical stock."
  uncertainty_notes:
    - "A true local manufacturing route would need tolerance, grade, heat-treatment, and surface-finish requirements that are not present in the BOM row."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable small precision bearing-ball item, likely shared with adjacent 2AC bottom-axis-bearing rows, rather than as a purchased module or raw stock."
---
