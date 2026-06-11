# General Findings from Machine Reality Research

## Executive summary

The machine-reality research found that most entries represent real physical things, but many are not cleanly standalone commercial equipment items in the sense needed for an imported-machine list. The main issue is not fake machinery; it is modeling granularity.

In this repo, `machine`/`machine_id` is used broadly for reusable process resources. The recommendations below are not saying those entries are invalid process resources. They are saying the imported-machine list should distinguish reusable resource subtypes: standalone equipment, tooling, instruments, consumables, infrastructure, stations, subsystems, and placeholders.

Out of 117 researched machine files, the triage pass found:

| Bucket | Count | Interpretation |
|---|---:|---|
| Clear commercial/practical machine | 36 | Commercially recognizable machine class with relatively direct KB fit. |
| Tooling/instrument/consumable resource | 38 | Real and often essential reusable process resources, but not standalone equipment. |
| Generic/ambiguous/duplicate needing cleanup | 27 | Real underlying capability, but the KB item is too broad, overloaded, deprecated, or should be split/consolidated. |
| Subsystem/station/infrastructure, not single machine | 15 | Real equipment, but better modeled as infrastructure, a station, a skid, or a subsystem. |
| Experimental or uncertain commercial maturity | 1 | Real research/prototype technology, not ordinary commodity equipment. |

The machine-by-machine triage table is in `research/machines_analysis/machine_research_triage.csv`.

## How the queue-driven research work was done

The machine-reality research was driven by manually added queue items in
`out/work_queue.jsonl`. Each task identified one imported machine-like KB entry,
the KB file to inspect, the required output report path, the evidence standard,
and the required report sections. Agents leased one task at a time, inspected the
KB usage first, performed best-effort external research, wrote a report under
`research/machines/`, and then marked the queue item complete. Research tasks did
not modify KB files and were completed according to their task instructions,
without queue verification.

Example queue task:

```json
{
  "id": "research_task:machine_reality_steel_forming_press",
  "kind": "research",
  "reason": "research_task",
  "gap_type": "research_task",
  "item_id": "machine_reality_steel_forming_press",
  "source": "manual",
  "context": {
    "machine_id": "steel_forming_press",
    "machine_name": "Steel forming press",
    "kb_item_file": "kb/items/machines/steel_forming_press.yaml",
    "source_list": "docs/self_reproduction_imported_machines.md",
    "output_path": "research/machines/steel_forming_press.md",
    "compare_existing_research_dir": "research/machines",
    "evidence_standard": "Best effort, defined as two independent external sources when available; document uncertainty and search attempts if fewer are found.",
    "done_criteria": "Inspect KB usage before web research. Determine whether the machine is a real practical machine, a generic category, a kit/station/tool bundle, or a placeholder. The goal is to make the imported machine list more realistic. Best-effort evidence standard: collect two independent external sources for reality/use/make-buy/build evidence when available; if fewer than two credible sources are found, document search attempts and uncertainty. Include usage interpretation, evidence links, commercially available alternates where useful, build/open-source instructions where useful, related researched machines if relevant, and recommendations such as keep, rename, split, replace, or mark uncertain. Do not modify KB and do not enqueue follow-up tasks.",
    "required_report_sections": [
      "Machine identity",
      "KB usage and needed function",
      "Reality classification",
      "Evidence links",
      "Commercial alternatives",
      "Build or open-source references",
      "Related machine research",
      "Recommendation for KB realism",
      "Confidence and open questions"
    ],
    "constraints": [
      "Do not modify KB files",
      "Do not enqueue follow-up tasks",
      "Recommendations should focus on making the imported machine list more realistic"
    ],
    "description": "Research whether steel_forming_press represents a real practical machine; write findings to research/machines/steel_forming_press.md. Do not modify KB.",
    "added_at": 1781118861.427862
  },
  "status": "done",
  "lease_id": "codex-3",
  "lease_expires_at": 1781120033.989666,
  "completed_at": 1781119209.259326
}
```

For this example, the agent inspected `kb/items/machines/steel_forming_press.yaml`,
its BOM, recipe, and processes that require the machine, then wrote
`research/machines/steel_forming_press.md`. The report classified the item as a
real hydraulic metal-forming press category, recommended keeping it with clearer
scope, and noted overlap with `hydraulic_press`, `press_brake`, and
`stamping_press_basic`.

## Main finding

The imported-machine list is too uniform. It currently includes several different resource types under the same broad imported-resource shape:

- actual machines, such as furnaces, presses, mills, pumps, grinders, feeders, and excavators;
- tooling and consumables, such as dies, molds, crucibles, grinding wheels, electrodes, cutting tools, and welding consumables;
- instruments and metrology kits, such as multimeters, oscilloscopes, precision levels, inspection tools, and measurement equipment;
- infrastructure and stations, such as solar arrays, power buses, hydraulic power units, electrical test benches, PCB stations, and fixturing workbenches;
- broad placeholders, such as generic chemical reactors, generic electrolysis cells, metal forming bundles, and generic furnaces.

That means the list is useful as an import seed inventory, but it should not be interpreted as a list of only standalone purchasable production equipment.

## Highest-priority non-clear cases

These items are the strongest candidates for cleanup because they are not clearly one standalone commercial equipment item:

| Item | Finding | Recommendation |
|---|---|---|
| `generic_chemical_reactor_v0` | Placeholder for many incompatible chemistries. | Keep temporarily, but annotate as a generic stirred/jacketed reactor placeholder and split high-pressure, acid, packed-bed, gas-phase, and high-temperature chemistry later. |
| `electrolysis_cell_unit_v0` | Real electrochemical hardware category, but currently covers incompatible cell types. | Split into chemistry-specific cells: chlor-alkali membrane cell, aqueous electrowinning cell, Hall-Heroult cell, and molten/regolith electrolysis where needed. |
| `metal_forming_basic_v0` | Bundle of press, roll, anvil, fixtures, and hydraulics, not a standard machine. | Treat as a forming cell or replace references with specific machines: hydraulic press, press brake, plate roll, forging press/power hammer. |
| `blast_furnace_or_smelter` | Broad smelting placeholder. | Rename/scope to a small smelter if that is intended; otherwise split blast furnace, crucible furnace, reduction furnace, and casting furnace roles. |
| `mre_reactor_v0` | Real molten regolith electrolysis research hardware, not mature commodity equipment. | Keep as advanced experimental ISRU equipment with explicit uncertainty and subsystem requirements. |
| `temperature_sensing` | Instrumentation resource category, not standalone equipment. | Remove from imported-machine list or replace with explicit sensor items already modeled elsewhere. |
| `control_compute_module_imported` | Real imported boundary component, but broad electronics category. | Keep as an import boundary resource, not standalone process equipment; clarify scope and avoid hiding specialized controllers. |
| `resource_3d_printer_cartesian_v0_machine` | Real machine concept with naming/duplicate problems. | Consolidate under one canonical basic Cartesian FDM/FFF printer item. |
| `milling_machine_general_v0` | Real machine, but appears to be a deprecated duplicate of `cnc_mill` unless manual milling is intentionally separate. | Either finish consolidation into `cnc_mill` or rename as manual/vertical milling machine with adjusted BOM. |
| `casting_furnace_v0`, `heating_furnace`, `drying_basic_v0` | Real equipment, but overlap with canonical furnace/drying items. | Resolve duplicate/deprecated status and keep process-specific furnaces only when requirements differ materially. |

## Recurring patterns

### Tooling Modeled as Reusable Resources

The largest non-clear group is real tooling or consumables represented through reusable `machine_id` resource slots. That can be a valid simulator convention, but the imported-machine analysis should call them tooling/resources rather than standalone machines. Examples:

- die and mold items: `dies`, `anvil_or_die_set`, `drawing_die_set_basic`, `wire_drawing_die_set`, `press_brake_die_set`, `press_ram_set`, `pressing_mold_set`, `casting_mold_set`, `sand_casting_flask_set`;
- consumables and wear items: `grinding_wheels`, `welding_consumables`, `electrodes`, `crucible_graphite`, `crucible_refractory`;
- general tool kits: `hand_tools_basic`, `hand_tools_mechanical`, `hand_tools_electrical`, `assembly_tools_basic`, `welding_tools_set`, `wire_crimping_tools`, `wire_stripper_set`, `refractory_installation_tools`;
- metrology/instruments: `inspection_tools_basic`, `measurement_equipment`, `precision_levels`, `multimeter_set`, `oscilloscope_basic`, `power_supply_benchtop`, `tension_gauge`.

Recommendation: keep these as required reusable inventory, but classify them conceptually as tooling, instruments, consumables, parts, or subassemblies. They are often more important than their mass suggests, because calibration, wear, geometry, and material compatibility drive realism.

### Generic categories hiding incompatible requirements

Several entries are real categories but too broad for the process requirements they cover:

- `generic_chemical_reactor_v0` and `chemical_reactor_basic` hide pressure, corrosion, catalyst geometry, heat transfer, gas handling, and safety differences.
- `electrolysis_cell_unit_v0` hides major differences between chlor-alkali, electrowinning, Hall-Heroult, water electrolysis, and molten-regolith electrolysis.
- `furnace_basic`, `heating_furnace`, `sintering_furnace_v0`, `reduction_furnace_v0`, and `glass_furnace_v0` are all real, but should be separated by temperature, atmosphere, feed/product handling, and process chemistry.
- `metal_shear_or_saw`, `mixer_or_blender`, `power_hammer_or_press`, and `molding_press_basic` are plausible catch-alls, but process references should use more specific equipment when the operation is known.

Recommendation: keep generic items only where the KB deliberately models a coarse capability. Add notes that define the allowed envelope and split when pressure, temperature, atmosphere, corrosion, precision, or product geometry changes materially.

### Stations, subsystems, and infrastructure

Some entries are real but not single standalone production equipment items:

- electrical/power infrastructure: `power_distribution_bus`, `power_conditioning_equipment`, `solar_array_v0`, `solar_tracking_optional`;
- process stations: `pcb_development_station`, `pcb_fab_equipment`, `test_bench_electrical`, `fixturing_workbench`;
- subsystems: `hydraulic_power_unit_basic`, `tension_control_system`, `vapor_capture_system_v0`, `chemical_reactor_vessel_v0`;
- large systems: `heliostat_array_system_v0`.

Recommendation: keep these if they are needed for scheduling or capability, but label them as infrastructure, station, subsystem, or system rather than standalone manufacturing equipment. This avoids treating a complete installed solar array or power bus as equivalent to a lathe or furnace.

### Locally buildable, but calibration or consumables are the hard part

Many non-clear items are physically simple but hard to make useful:

- `precision_levels`, `measurement_equipment`, and `inspection_tools_basic` depend on calibration references.
- `dies`, `pressing_mold_set`, `drawing_die_set_basic`, and `cutting_tools_general` depend on hardened/wear-resistant materials and precision geometry.
- `grinding_wheels` depend on abrasive grain, bond chemistry, firing, balancing, and dressing.
- `electrodes` and `crucibles` depend on material compatibility, thermal shock, chemical corrosion, and wear.

Recommendation: do not judge these only by mass or shape. If they are required for self-reproduction, the KB should model calibration, wear, replacement, and material compatibility more explicitly than it does for ordinary structural parts.

## Recommended cleanup policy

Use this decision policy when turning the research into KB edits:

1. If an entry is a real standalone commercial equipment item with a clear function, keep it and tighten notes only where needed.
2. If it is tooling, instrument, consumable, or accessory inventory, keep the concept but label the resource subtype clearly.
3. If it is a station or subsystem, keep it only if scheduling/capability needs that abstraction; otherwise model it as BOM components of the actual process machine.
4. If it is a generic placeholder, add an explicit envelope and split only when a process crosses a major compatibility boundary.
5. If it duplicates another item, prefer the canonical item already supported by dedupe notes and route references there.
6. If it is experimental, keep it only with explicit maturity and uncertainty notes.

## Suggested next artifacts

The next useful artifacts would be:

- `kb_machine_reclassification_plan.md`: proposed `machine` to `tooling`/`instrument`/`infrastructure`/`subsystem` conceptual moves.
- `kb_placeholder_split_plan.md`: proposed split points for chemical reactors, electrolysis cells, furnace families, and generic forming equipment.
- `imported_machine_list_v2.md`: a cleaned list that separates actual machines from tools, infrastructure, instruments, consumables, and experimental systems.

No KB files were modified in this analysis pass.
