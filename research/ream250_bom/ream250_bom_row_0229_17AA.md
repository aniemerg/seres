---
row_identity:
  item: "17AA"
  cad_file: "17AA_strut_profile_20X20_271"
  source_row_number: 229
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://store.boschrexroth.com/Montagetechnik/Mechanik-Grundelemente/Profile-und-Zubeh%C3%B6r/Strebenprofil?cclcl=de_DE"
function:
  summary: "Short 20 mm x 20 mm Bosch Rexroth aluminum T-slot strut profile used as a light structural rail/member in the reAM250 frame or fixture assembly."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; research/ream250_bom/ream250_bom_row_0229_17AA__views_2x2.png; https://www.boschrexroth.com/en/us/products/industrial-solutions/assembly-technology/aluminum-profile-kit/"
    cited_fact_or_basis: "BOM row 229 identifies item 17AA as 'strut profile' from Bosch Rexroth AG; CAD preview shows a 271 mm long 20 x 20 mm slotted extrusion; Bosch describes its aluminum profile system as used to construct machine frames, workstations, shelves, safety fences, and similar structures. official_alternate_route_check: original BOM link points to the Bosch Rexroth store strut-profile category; the Bosch Rexroth aluminum-profile-kit page is a first-party Bosch route for the same aluminum strut-profile product family and links to the profile catalog."
    evidence_basis: "bom_provided"
  assumptions:
    - "The row's short profile is a frame/fixture rail rather than a precision motion guide because the BOM description, CAD cross-section, and Bosch profile family all indicate modular framing stock."
  uncertainty_notes:
    - "The parent assembly location is not specified in the leased context, so the exact frame subassembly function is inferred only at the structural-member level."
mass:
  value_kg: 0.121
  basis: "Per unit, not row total. FreeCAD measured one solid with volume 44,882.764 mm^3 and bounding box 271.00 x 20.00 x 20.00 mm. Using aluminum density 2700 kg/m^3 from kb/materials/properties.yaml gives 44,882.764e-9 m^3 * 2700 = 0.12118 kg per profile. The BOM quantity is 2, so the row total is about 0.242 kg. As a catalog cross-check, the Bosch 20x20 sheet lists mass about 0.4 kg/m, which gives about 0.108 kg for 0.271 m; the CAD-volume estimate is retained because it is row-specific."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/17AA_strut_profile_20X20_271.step; kb/materials/properties.yaml; https://docs.rs-online.com/ea04/A700000007302204.pdf"
    cited_fact_or_basis: "FreeCAD measurement of the row STEP file returned volume 44,882.76366211526 mm^3 and bounding box 271.0, 20.0, 20.0 mm; local material table gives aluminum density 2700 kg/m^3; the Bosch Rexroth 20x20 datasheet lists anodized aluminum material and rounded mass data for the 20x20 profile. bom_url_route_check: original Bosch store URL was checked as the BOM route; it did not expose parseable row-specific technical values in this environment, so the calculation uses the local CAD package plus a Bosch-branded datasheet copy hosted by RS for the exact 20x20 strut profile family."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The CAD solid represents the aluminum body volume for one physical profile and excludes no major inserts or fasteners."
    - "The generic local aluminum density is close enough for anodized aluminum extrusion alloy at this planning precision."
  uncertainty_notes:
    - "Assembly STEP material metadata for this product reports only 'Generic' at density 1000.0, so it was ignored as placeholder metadata."
    - "CAD-density mass and catalog mass-per-length differ by roughly 12%; downstream KB use should treat 0.121 kg as a supported estimate, not a weighed value."
material:
  primary_material: "anodized aluminum"
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Bosch Rexroth 20x20 strut-profile datasheet lists the 20x20 profile material as anodized aluminum for the matching profile/order-code family. Local assembly STEP metadata was checked for product 17AA_strut_profile_20X20_271 but returned only Generic material with density 1000.0. bom_url_route_check: original Bosch store URL was checked first as the BOM-provided route; exact material text was resolved from a Bosch-branded 20x20 datasheet copy because the store route did not expose parseable technical data here."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "No specific aluminum alloy temper was found in the BOM row, CAD metadata, or checked datasheet, so the material is kept at family/finish precision."
how_to_make:
  summary: "Procure or specify a Bosch Rexroth 20x20 anodized aluminum strut profile cut to the 271 mm CAD length; for local manufacture, extrude an aluminum 20x20 T-slot profile, anodize or otherwise protect the surface, cut to length, and deburr/inspect the ends."
  manufacturing_steps:
    - "Procurement route: order the Bosch Rexroth 20x20 strut-profile family in a specified length or standard stock, then cut to 271 mm if supplied oversize."
    - "Local fabrication route: extrude an aluminum billet through a die for the 20x20 four-slot profile with central bore."
    - "Apply anodized or equivalent protective finish, then saw-cut to 271 mm and deburr open ends."
    - "Inspect length, straightness, slot geometry, and end condition before assembly with standard slot hardware."
  source:
    url_or_path: "https://docs.rs-online.com/ea04/A700000007302204.pdf; https://www.part-on.co.uk/product/20-x-20mm-aluminium-profile-part-on-range/; research/ream250_bom/ream250_bom_row_0229_17AA__views_2x2.png"
    cited_fact_or_basis: "The Bosch 20x20 datasheet lists specified-length order options from 50 to 3000 mm for the 20x20 strut profile; a distributor page for genuine Bosch Rexroth 20 x 20 mm aluminum strut profile states it can be cut to required size; the CAD preview confirms the row is a straight slotted extrusion. bom_url_route_check: original Bosch store URL was checked as the BOM route; because parseable manufacturing/procurement details were limited there, the route uses the Bosch-branded datasheet copy and a distributor page matching the same genuine Bosch Rexroth 20x20 strut-profile family."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The local manufacturing route uses standard aluminum extrusion practice for T-slot framing; the cited sources support product identity and cut-to-length procurement, not every extrusion process parameter."
  uncertainty_notes:
    - "The exact Bosch alloy, anodizing specification, and end-finish option for this row are not stated; model as a simple structural aluminum profile unless later KB work requires the specific commercial order code."
kb_implications:
  - "item_granularity: simple_part - Model as a reusable cut-to-length 20x20 aluminum T-slot profile/simple structural extrusion, not as a unique machine assembly."
---
