# HV Tank Core Decomposition Plan

Status: combined Level-2 core-internals planning completed; concise
section-module-set model adopted.

Purpose:

- Review HV-3/HV-4/HV-5/HV-6/HV-7 together because the strongest source models
  them as sectioned transformer/rectifier/filter hardware rather than fully
  independent simple parts.
- Avoid creating child BOMs that duplicate the current scaffold.

Parent/current items:

- `ebf3_sectioned_hv_step_up_transformer` (HV-3)
- `ebf3_hv_rectifier_stack_tank_side` (HV-4)
- `ebf3_hv_output_filter_capacitor` (HV-5)
- `ebf3_internal_hv_leads_terminals` (HV-6)
- `ebf3_transformer_insulation_spacers` (HV-7)

Source registry:

- `research/ebf3_bom_sources/sources/level_2_parts/hv_tank_core/hv_tank_core_sources.md`

Target KB BOMs:

- None yet. Current evidence shows an architecture mismatch that should be
  resolved before child BOMs are created.

## Source Evidence And Use

### RAW-BINP-60KV-15KW-HV-TANK

Evidence:

- "two parallel branches with tree section each"
- "Each section is complete design"
- "includes winding, half-bridge rectifier and output filter capacitors"
- "section is 20 kV"
- "oil-filled tank"
- "silicon oil"

Use:

- Strongly supports a section-module architecture for the comparable 60 kV / 15
  kW HV tank.
- Creates a mismatch with the current scaffold, which represents transformer,
  rectifier stack, and output filter capacitor as separate Level-2 siblings.

### RAW-BINP-60KEV-30KW

Evidence:

- "four step-up high voltage sections"
- "winding, half-bridge rectifier and output filter capacitors"
- "15 kV for 60 kV operations"
- "addition high voltage output capacitor"

Use:

- Confirms a related sectioned architecture, but with four sections rather than
  two branches of three sections.
- Supports deferring exact section count for EBF3.

### LOCAL-EBF3-HV-TANK-TABLE

Evidence:

- HV-3 candidates include magnetic core, primary winding, sectioned secondary
  winding, interlayer insulation, bobbin/support, terminals, and oil-immersed
  mounting.
- HV-4 candidates include HV diodes, equalizing resistors, terminals, insulating
  supports, and oil-side mounting.
- HV-5 candidates include HV capacitors, series/parallel connections, equalizing
  or discharge resistors, terminals, and oil-side supports.
- HV-6 candidates include internal conductors, terminals, bushings, rounded
  terminals, clamps, and connection studs.
- HV-7 candidates include spacers, barriers, support blocks, pressboard sheets,
  and locating pieces.

Use:

- Introduces possible child items but cannot decide architecture by itself.

### WEB-WEIDMANN-SPACING-ELEMENTS

Evidence:

- "transformer winding assemblies"
- "radial separation between conductors"
- "support insulation integrity"
- "cooling efficiency"

Use:

- Supports transformer insulation spacer/support functions for HV-7.
- Does not justify specific EBF3 spacer geometry.

### WEB-WEIDMANN-INSULATION-COMPONENTS

Evidence:

- "oil-immersed"
- "insulation components"
- "transformers"

Use:

- Supports insulation-component class for oil-immersed transformer hardware.

### WEB-GE-BAC-OIL-COOLED-TRANSFORMER-RECTIFIER

Evidence:

- "transformer rectifier is housed inside an oil tank"
- "power transformer, choke, diode assembly and shunt"
- "mounted inside the oil tank"

Use:

- Supports transformer/rectifier/shunt hardware packaged inside an oil tank in
  industrial equipment.
- Does not override the BINP sectioned architecture.

### WEB-IET-RECTIFIER-TRANSFORMER-FILTER

Evidence:

- "transform"
- "rectify"
- "filter"

Use:

- Supports the broad transformer/rectifier/filter function sequence only.

## Architecture Decision

The current KB keeps HV-3 transformer, HV-4 rectifier stack, and HV-5 output
filter capacitor as separate Level-2 siblings. The strongest source says each HV
section is a complete design that includes winding, half-bridge rectifier, and
output filter capacitors.

Decision: use a concise **section-module-set model**.

Create one `ebf3_hv_section_module_set` rather than repeated individual section
items. The set owns the sectioned transformer/rectifier/filter architecture and
contains HV-3/HV-4/HV-5 as functional constituents. This keeps the presented BOM
short while preserving the source-backed sectioned architecture.

## Decision Matrix

| Candidate/function | Status | Applies to | KB representation | Decision basis |
| --- | --- | --- | --- | --- |
| HV section module set | adopt | HV-3/HV-4/HV-5 | `ebf3_hv_section_module_set` | Strong BINP support for sectioned architecture; represented as one concise set to avoid repeated section clutter. |
| Transformer winding pack | defer | HV-3 / section module set | Existing `ebf3_sectioned_hv_step_up_transformer` remains functional constituent | Source supports winding inside each section; exact count and geometry unresolved. |
| Magnetic core | defer | HV-3 | None | User-derived candidate; source does not expose core geometry. |
| Half-bridge rectifier per section | defer | HV-4 / section module set | Existing `ebf3_hv_rectifier_stack_tank_side` remains functional constituent | Source places rectifier inside sections; detailed per-section child split remains deferred. |
| Output filter capacitors per section | defer | HV-5 / section module set | Existing `ebf3_hv_output_filter_capacitor` remains functional constituent | Source places capacitors inside sections; detailed per-section child split remains deferred. |
| Additional final output capacitor | defer | HV-5 | None | RAW-BINP-60KEV-30KW mentions additional output capacitor; exact EBF3 topology unknown. |
| Oil-side internal leads/terminals | keep leaf | HV-6 | `ebf3_internal_hv_leads_terminals` | Needed to connect sections/bushing; detailed conductors/rounded terminals deferred. |
| Transformer insulation spacers/barriers | keep leaf | HV-7 | `ebf3_transformer_insulation_spacers` | Weidmann supports spacer functions; detailed materials/geometry deferred. |
| Diode/equalizing resistor/capacitor dielectric children | defer | HV-4/HV-5 | None | Material/component-level split is premature without architecture and ratings. |

## KB Action

- Create `ebf3_hv_section_module_set` and
  `bom_ebf3_hv_section_module_set`.
- Move HV-3/HV-4/HV-5 under the section-module set in the top-level HV tank BOM
  and recipe.
- Do not split the section-module set into repeated individual sections until
  section count and topology are selected.

## Manufacturing Readiness

No core-internal item is local-ready. Section count, winding geometry, magnetic
core, insulation system, oil compatibility, rectifier topology, capacitor type,
ripple/energy rating, clearances, thermal design, and HV test procedure all need
separate design and material/process review.
