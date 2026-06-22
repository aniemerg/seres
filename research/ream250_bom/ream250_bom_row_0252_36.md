---
row_identity:
  item: "36"
  cad_file: "36_seal_ISO_KF_DN50"
  source_row_number: 252
  source_csv: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv"
  link_url: "https://www.pfeiffer-vacuum.com/global/de/shop/products/172ZRG050"
function:
  summary: "ISO-KF DN50 centering seal/ring used between KF vacuum flanges to center the joint and carry the elastomer sealing element."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/reAm250_BOM_gold.csv; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/36_seal_ISO_KF_DN50.step; https://www.idealvac.com/en-no/svpproduct.asp?PID=172zrg050"
    cited_fact_or_basis: "BOM row 252 identifies item 36 as 36_seal_ISO_KF_DN50, quantity 4, product 172ZRG050 by Pfeiffer Vacuum; the row STEP is a thin annular part; Ideal Vacuum identifies 172ZRG050 as a Pfeiffer Vacuum centering ring, DN 50 ISO-KF. bom_url_route_check: the original BOM-provided Pfeiffer product route from row_identity.link_url was checked first but did not expose extractable product facts in this browsing session, so the row-matched distributor page was used for the functional name."
    evidence_basis: "independent_vendor_spec"
  assumptions:
    - "The BOM word seal and the vendor word centering ring refer to the same KF sealing-ring component for this row."
  uncertainty_notes:
    - "The row CAD has no assembly context beyond neighboring BOM row references, so exact installed joint location is not resolved here."
mass:
  value_kg: 0.0055
  basis: "Per-unit estimate for one seal/centering ring. FreeCAD measured one solid with volume 2612.361 mm^3 and bounding box 61.64 x 61.64 x 8.00 mm; using a 2100 kg/m^3 effective density for mostly PTFE with an FKM O-ring gives 2612.361e-9 m^3 * 2100 kg/m^3 = 0.00549 kg. BOM quantity is 4, giving an optional row total of about 0.022 kg."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/36_seal_ISO_KF_DN50.step; kb/materials/properties.yaml; https://www.vacuumservice.fi/wp-content/uploads/2019/03/Vacuum-Technology-Book-II-Part-3-3.pdf"
    cited_fact_or_basis: "FreeCAD measured STEP volume 2612.361 mm^3 and one solid; local properties list fluoroelastomer/FKM density as 1800 kg/m^3; the Pfeiffer catalog text for order number 172ZRG050 identifies DN 50 KF, FKM O-ring, plastic PTFE centering ring dimensions. targeted_web_search: queries tried included '172ZRG050 Pfeiffer Vacuum seal ISO-KF DN 50 material weight', '\"172ZRG050\"', and '\"172ZRG050\" \"DN50\"'; no row-specific catalog mass was found."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Effective density of 2100 kg/m^3 approximates a mostly PTFE plastic centering ring with a smaller FKM elastomer sealing element."
  uncertainty_notes:
    - "Mass is limited by unresolved PTFE/FKM volume fractions and by the CAD export representing the combined row as one solid."
material:
  primary_material: "PTFE plastic centering ring with FKM fluoroelastomer O-ring"
  source:
    url_or_path: "https://www.vacuumservice.fi/wp-content/uploads/2019/03/Vacuum-Technology-Book-II-Part-3-3.pdf; design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/assemblies/00_assembly.step"
    cited_fact_or_basis: "The Pfeiffer catalog listing for 172ZRG050 is under ISO-KF Centering Ring, Plastic, states PTFE, and lists DN 50 KF with O-ring material FKM. Local assembly material extraction for 36_seal_ISO_KF_DN50 returned only Generic with density 1000.0, which is placeholder metadata. bom_url_route_check: the original BOM-provided Pfeiffer product route from row_identity.link_url was checked first but did not expose extractable material facts in this browsing session; the row-matched Pfeiffer catalog copy was used for material."
    evidence_basis: "independent_vendor_spec"
  assumptions: []
  uncertainty_notes:
    - "The local STEP metadata does not independently confirm the material, so material relies on catalog/product-number matching."
how_to_make:
  summary: "Procure as Pfeiffer 172ZRG050 or manufacture as a small vacuum fitting by machining/molding a PTFE centering ring profile and fitting an FKM O-ring to the KF DN50 geometry."
  manufacturing_steps:
    - "Cut or mold PTFE ring blank for the DN50 KF centering geometry."
    - "Machine the annular centering profile and O-ring groove/features to the catalog/CAD dimensions."
    - "Install a compatible FKM O-ring and inspect fit, surface finish, and vacuum sealing cleanliness."
  source:
    url_or_path: "design/real-mechanical/reAm250/reAM250_cad_gold_package/gold_export/parts/36_seal_ISO_KF_DN50.step; https://www.vacuumservice.fi/wp-content/uploads/2019/03/Vacuum-Technology-Book-II-Part-3-3.pdf; https://www.idealvac.com/en-no/svpproduct.asp?PID=172zrg050"
    cited_fact_or_basis: "CAD preview shows a shallow annular profile; the catalog identifies the component as a PTFE plastic ISO-KF centering ring with FKM O-ring; the distributor page identifies 172ZRG050 as a purchasable Pfeiffer DN50 ISO-KF centering ring. targeted_web_search: queries tried included '172ZRG050 Pfeiffer Vacuum seal ISO-KF DN 50 material weight' and '\"172ZRG050\"'; searches resolved product identity/material but did not find a source that states the manufacturing process."
    evidence_basis: "engineering_hypothesis"
  assumptions:
    - "Local manufacturing route is inferred from the simple annular CAD geometry and PTFE/FKM component materials rather than stated by the vendor."
  uncertainty_notes:
    - "Actual commercial production may use molded PTFE, machined PTFE, or another supplier-specific process."
kb_implications:
  - "item_granularity: consumable - Model as a replaceable ISO-KF DN50 seal/centering-ring consumable rather than a unique machine subsystem."
---
