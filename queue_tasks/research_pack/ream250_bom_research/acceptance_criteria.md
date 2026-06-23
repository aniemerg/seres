# reAM250 BOM Research Acceptance Criteria

This file is the authority for result-quality decisions in this task pack.
`agent.md` remains the worker SOP. `research_result.schema.yaml` remains the
structural contract. `validate_results.py` enforces only the mechanically
checkable subset of these criteria.

Each leased task represents exactly one reAM250 BOM row. The result must keep
that row identity fixed and may use research only to fill attributes for that
same row identity.

## Classification

Use these rule types:

- `Validator-enforced` - the current validator checks the rule mechanically.
- `Partially validator-enforced` - the validator checks a marker or structure,
  but the worker must still judge whether the content is true and sufficient.
- `Judgment-required` - the rule requires engineering or source-quality
  judgment and is not reliably machine-checkable.

## AC-EVID-001: Row Identity Is Locked First

Type: Judgment-required

Rule:
The BOM row, item, CAD file, quantity, manufacturer, product ID/description, and
manifest mapping define the row identity. Web/vendor evidence may fill missing
attributes for that identity, but must not reinterpret the row as a different
product.

Given a leased queue item for one BOM row
When the worker finds a plausible web result with a similar product name
Then the worker must keep the leased row identity fixed
And must reject sources that do not match the row item, product ID, manufacturer,
CAD geometry, standard designation, or same-row product family.

## AC-EVID-002: BOM-Side Evidence Counts As `bom_provided`

Type: Judgment-required

Rule:
Use `evidence_basis: bom_provided` when the section value is stated or measured
by BOM-side supplied evidence. BOM-side evidence includes BOM row fields,
manifest mappings, the supplied CAD/STEP package, local metadata extracted from
that package, rendered CAD previews, and the BOM-provided vendor/product URL
route.

Given a value is directly stated by the BOM row, manifest, local CAD/STEP
metadata, CAD measurement, rendered CAD preview, or BOM-provided vendor URL route
When the worker writes the section using that value
Then the section should use `evidence_basis: bom_provided`
And the worker should not perform web search only to second-guess directly
provided BOM-side evidence.

## AC-EVID-003: Evidence Basis Uses The Least Reliable Required Source

Type: Judgment-required

Rule:
When a section conclusion depends on multiple evidence classes, set
`evidence_basis` to the least reliable evidence class needed for that
conclusion.

Reliability order, highest to lowest:

1. `bom_provided`
2. `independent_vendor_spec`
3. `standard_part_convention`
4. `engineering_hypothesis`

`unresolved` is not a reliability tier.

Given a section uses BOM CAD volume and an independently searched vendor
material fact
When both are required for the section value
Then the section evidence basis must be `independent_vendor_spec`, not
`bom_provided`.

Given a mass estimate uses BOM CAD volume and BOM-side component material facts
But also depends on an unsupported effective-density guess
When that guess is required for the mass value
Then `mass.source.evidence_basis` must be `engineering_hypothesis`.

## AC-EVID-004: Row-Specific STEP Material Is BOM-Provided

Type: Partially validator-enforced

Rule:
Non-placeholder material metadata extracted from the row's provided STEP/CAD
package is BOM-side evidence. Use `evidence_basis: bom_provided` for the
material fact, and for CAD-volume mass calculations that only need that material
and a local density constant. Use `standard_part_convention` only when the
claimed fact is resolved from a standard designation, suffix, class, or
part-family convention rather than directly from row-specific BOM/CAD metadata.

Given local assembly STEP material extraction returns a non-placeholder material
such as `Steel, Mild`, `Aluminum`, `Steel`, `Stainless Steel`, or another real
material name for the row product
When the worker writes the material section using that fact
Then `material.source.evidence_basis` should be `bom_provided`
And any DIN/ISO/vendor standard cited for the same material should be described
as a cross-check, not the reason to lower evidence to
`standard_part_convention`.

Given a mass value uses row CAD volume
And the row-specific STEP material extraction gives a non-placeholder material
density
When no unsupported material split, effective-density guess, or independent
vendor fact is required
Then `mass.source.evidence_basis` should be `bom_provided`.

## AC-WEB-001: Hypothesis Requires Targeted Web Search

Type: Partially validator-enforced

Rule:
If a section uses `evidence_basis: engineering_hypothesis` or
`evidence_basis: unresolved`, that same section must include a grep-able
lowercase `targeted_web_search:` note in `source.cited_fact_or_basis` or
`uncertainty_notes`.

Given BOM-side evidence does not resolve a section value
When the worker writes that section with `engineering_hypothesis` or `unresolved`
Then the same section must include lowercase `targeted_web_search:`
And the note must list query terms tried
And the note must state the result, such as no row-specific usable vendor source
or only duplicate/non-matching evidence.

## AC-WEB-002: Search Before Falling Back

Type: Judgment-required

Rule:
Before falling back to `engineering_hypothesis` or `unresolved`, perform at
least one targeted web/search sanity check when BOM-side evidence is missing,
placeholder/generic, or conflicting for the needed value.

Given the BOM row has no manufacturer, product ID, standard designation, or URL
When BOM-side evidence still does not resolve the needed value
Then the worker must still try low-cost searches using available row clues such
as `cad_file`, `description_or_product_id`, BOM item, parent assembly, sibling
row names, part-family nouns, and terms like `material`, `datasheet`, `catalog`,
`drawing`, `technical data`, or `weight`.

## AC-ROUTE-001: Official Alternate Routes Can Remain `bom_provided`

Type: Partially validator-enforced

Rule:
Redirects, official canonical replacements, official regional/shop domains,
first-party support/product-family/technology/download pages, and official
group-company pages can remain `bom_provided` when they are reached from or
derived from the BOM-provided URL route and still match the same row.

Given `row_identity.link_url` exists
And the worker follows an official alternate route on a different domain
And the alternate page matches the same manufacturer, product ID, legacy number,
or same-row product family
When a section uses facts from that alternate official route
Then the section may use `evidence_basis: bom_provided`
And the section must include `official_alternate_route_check:`
And the note must explain the original BOM URL, alternate URL/domain,
official-route evidence, and row-match evidence.

## AC-ROUTE-002: Independent Different-Domain Sources Need A BOM Route Check

Type: Partially validator-enforced

Rule:
If the BOM row has `link_url` and a section relies on a different-domain
`independent_vendor_spec`, the section must explain why the BOM-provided URL
route did not resolve that section value.

Given `row_identity.link_url` exists
And a section uses a different-domain source with
`evidence_basis: independent_vendor_spec`
When the worker writes that section
Then the section must include `bom_url_route_check:`
And the note must state the BOM-provided URL, redirect/canonical, or first-party
route checked
And the note must explain why that route did not resolve the section value
before the worker used the independent source.

## AC-ROUTE-003: Do Not Prefer Easier Independent Sources Over Row-Matched BOM Routes

Type: Judgment-required

Rule:
Do not replace a row-matched BOM-provided/canonical source with an independent
PDF, catalog, or distributor page only because the independent source is easier
to parse. Independent sources may supplement, but the evidence basis remains
`bom_provided` when the same fact was resolved from the BOM-provided route.

Given a BOM-provided or official canonical page contains row-matched material or
function facts
When an independent catalog also states the same facts
Then the section should cite the BOM route as contributing evidence
And should keep `evidence_basis: bom_provided` if no lower-tier evidence is
needed for the conclusion.

## AC-MAT-001: Placeholder CAD Material Does Not Resolve Material

Type: Judgment-required

Rule:
Local STEP metadata values such as `Generic`, `Default`, `Material`, `None`,
`unspecified`, empty strings, or density `1000.0` without a real material name do
not resolve material.

Given local assembly STEP material extraction returns only `Generic` and density
`1000.0`
When BOM row fields do not directly state material
Then the worker must continue to BOM-provided URL/vendor/web research before
assigning `material.primary_material`.

## AC-MAT-002: Material Precision Must Match The Evidence

Type: Partially validator-enforced

Rule:
Do not write assumed specific materials as if they were sourced. If evidence
supports only a broad family, write the broad family and use
`engineering_hypothesis`.

Given no source states an exact material grade
When function or geometry supports only a broad material family
Then `material.primary_material` should be broad, such as `unknown metal/alloy`,
`elastomer seal material`, `ceramic insulation material`, or `polymer cable
jacket material`
And it must not contain wording such as `steel, assumed` or `aluminum, assumed`.

## AC-MAT-003: Preserve Component Material Wording

Type: Judgment-required

Rule:
When a source names component materials, preserve that component-specific
wording instead of collapsing the item to one material.

Given a BOM-provided vendor page states `aluminum outer ring` and `NBR`
When the worker writes `material.primary_material`
Then the material should preserve both component material facts
And should not collapse the item to only `aluminum` or only `NBR`.

## AC-MASS-001: Arithmetic Does Not Downgrade Evidence

Type: Judgment-required

Rule:
Arithmetic does not by itself lower evidence class. A mass computed from
BOM-provided CAD/STEP volume and BOM-provided material identity remains
`bom_provided`.

Given FreeCAD measures the row-specific CAD volume
And BOM-side evidence resolves the material family or grade
When the worker computes mass using a standard/common density
Then `mass.source.evidence_basis` may remain `bom_provided`
And the density value should be recorded in `mass.basis` or `mass.assumptions`.

## AC-MASS-002: Local Common Density Is A Calculation Constant

Type: Judgment-required

Rule:
Before searching the web for a common material density, check
`kb/materials/properties.yaml`. If the resolved material maps to that local
table, use the density as a calculation constant and do not add an external
density source solely to determine `evidence_basis`.

Given material is resolved as stainless steel 304/1.4301, aluminum, steel,
copper, brass, NBR, FKM, or silicone rubber
When the local density table contains that family/grade or an obvious alias
Then the worker should use the local density table
And should not cite a generic external density page only to justify evidence
basis.

## AC-MASS-003: Unsupported Multi-Material Fractions Downgrade Mass

Type: Judgment-required

Rule:
For multi-material parts, distinguish sourced material facts from unsupported
composition estimates. If the mass requires guessed material volume fractions or
an assumed effective density, mass is an engineering hypothesis.

Given CAD volume is available
And component materials are known
And the item has multiple material regions
But no source provides material fractions, split-volume CAD, catalog mass, or
another physical input resolving composition
When the worker estimates mass using an assumed effective density or guessed
material ratio
Then `mass.source.evidence_basis` must be `engineering_hypothesis`
And `mass.assumptions` must state the effective-density or fraction assumption
And `mass.uncertainty_notes` must describe the remaining mass limitation.

## AC-MASS-004: Mass Value Is Per Unit

Type: Judgment-required

Rule:
`mass.value_kg` is the mass of one physical item represented by the BOM row, not
the BOM row quantity multiplied by that mass. Use `mass.basis` to state the BOM
quantity and optional row total when quantity is not 1.

Given a BOM row has quantity greater than 1
When the worker writes `mass.value_kg`
Then `mass.value_kg` must remain the per-unit mass
And `mass.basis` should state the quantity
And `mass.basis` may state the row total as `quantity * mass.value_kg` for
planning context.

Given a row has quantity 4
And one clamp has estimated mass 0.0323 kg
When the worker writes the mass section
Then `mass.value_kg` should be `0.0323`
And `mass.basis` may say the row total is about `0.129 kg` if needed.

## AC-MAKE-001: Inferred Manufacturing Routes Lower `how_to_make`

Type: Judgment-required

Rule:
A sourced product identity can support procurement as a route, but it does not
by itself source the detailed local manufacturing process. If `how_to_make`
includes inferred operations such as turning, milling, grinding, hobbing,
cutting, forming, heat treatment, inspection, or finishing that are not stated by
the cited source, set `how_to_make.source.evidence_basis` to
`engineering_hypothesis`.

Given a BOM-provided vendor page identifies a standard purchased component
And the worker adds a plausible local manufacturing route inferred from CAD
geometry or common practice
When the worker writes `how_to_make`
Then the section may cite the vendor page and CAD as source facts
But `how_to_make.source.evidence_basis` must be `engineering_hypothesis` unless
the cited source directly states the relevant manufacturing route.

## AC-STD-001: Standard Part Conventions Need Complete Parameters

Type: Partially validator-enforced

Rule:
Use `standard_part_convention` only when a standard designation, suffix, class,
or part-family convention is complete enough for the claimed fact. Explain
parameter completeness in `source.cited_fact_or_basis`.

Given a DIN/ISO/SKF/SMC-style designation is present
When the worker uses `evidence_basis: standard_part_convention`
Then `source.cited_fact_or_basis` must state which parameters were present
And whether they are sufficient for function, interface, dimensions, material,
or none of those.

## AC-FIELD-001: Source, Assumptions, And Uncertainty Must Stay Separate

Type: Partially validator-enforced

Rule:
`source.cited_fact_or_basis` is for source facts. `assumptions` is for modeling
premises used to transform facts into the section value. `uncertainty_notes` is
for residual limitations that affect downstream trust, specification, or use.
Do not repeat the same idea across these fields.

Given FreeCAD measured a CAD volume
When the worker writes the mass section
Then the measured value belongs in `source.cited_fact_or_basis` or `mass.basis`
And using the single-solid volume as a per-unit item proxy belongs in
`assumptions`
And remaining volume-fidelity or material-split consequences belong in
`uncertainty_notes`.

## AC-FIELD-002: Uncertainty Is Not An Audit Log

Type: Judgment-required

Rule:
Do not list failed checks, missing fields, rejected sources, redirects, HTTP
failures, `Generic` STEP material, or "No catalog mass found" as uncertainty
notes when they do not affect the final section value. Keep only the downstream
consequence if it matters.

Given a BOM-provided official alternate page resolves the material
When the original BOM URL did not directly load or did not directly expose the
material
Then the material uncertainty should not record the failed original URL as a
standalone audit detail
And should record only residual limitations that still affect material trust or
use.

## AC-GRAN-001: Exactly One Item Granularity Signal

Type: Partially validator-enforced

Rule:
`kb_implications` must include exactly one machine-searchable item granularity
signal starting with `item_granularity: <value> - ...`.

Allowed values:

- `simple_part`
- `assembly`
- `purchased_module`
- `consumable`
- `raw_material_or_stock`
- `unknown`

Given the result has `kb_implications`
When the worker writes item granularity
Then exactly one bullet should start with `item_granularity: <value> - `
And `<value>` must be one of the allowed values.

## AC-GRAN-002: Multi-Material Does Not Imply Assembly

Type: Judgment-required

Rule:
Multi-material construction alone does not imply `assembly`. Choose the value
that best predicts how the KB should model the row next.

Given a row item contains multiple materials
When it is a replaceable seal, centering ring, O-ring, filter element, belt, or
similar maintenance item
Then prefer `item_granularity: consumable`
And explain any multi-material construction after the dash
But do not classify it as `assembly` solely because more than one material is
present.

Given the row is a replaceable timing belt, conveyor belt, O-ring, gasket, seal,
filter element, lubricant, adhesive, or similar wear/replacement item
When choosing item granularity
Then prefer `item_granularity: consumable`
Unless the row is clearly a larger calibrated vendor subsystem rather than the
replaceable item itself.

## AC-GRAN-003: Standard Hardware Is Not A Purchased Module

Type: Judgment-required

Rule:
Standard hardware purchased from a vendor is not automatically a
`purchased_module`, and finished standard fasteners are not raw stock. Use
`simple_part` for one-piece or simple standard hardware such as clamps,
brackets, bolts, screws, nuts, washers, simple pulleys, and similar fasteners
unless the row is a calibrated functional module or a multi-part assembly that
should be modeled as such. Reserve `raw_material_or_stock` for stock forms such
as sheet, bar, tube, extrusion, profile, wire, plate, rod, hose/pipe stock, or
cut-to-length stock where later KB work should model length/size variants rather
than a finished hardware item.

Given the row is a standard ISO-K claw clamp or similar vacuum fastener
When the row is one simple hardware item without a sub-BOM or calibration
workflow
Then prefer `item_granularity: simple_part`
And explain that it should later map to reusable standard hardware rather than a
machine-specific custom part.

Given the row is a finished DIN/ISO bolt, screw, nut, washer, or similar
fastener
When the worker writes item granularity
Then prefer `item_granularity: simple_part`
And do not use `raw_material_or_stock`
And explain that later KB work should reuse or create generic standard hardware
or a fastener kit.

## AC-GRAN-004: Purchased Module Is A Current Modeling Hint

Type: Judgment-required

Rule:
`purchased_module` means the row is best treated as a vendor functional module
or calibrated subsystem until a sub-BOM and calibration/manufacturing workflow
are modeled. It does not mean the item can never be self-manufactured later.

Given the row is a sensor head, pump, controller, laser module, or calibrated
vendor subsystem
When no sub-BOM and calibration workflow are available
Then `item_granularity: purchased_module` may be appropriate
And the explanation should distinguish current KB modeling from long-term
self-manufacturing goals.
