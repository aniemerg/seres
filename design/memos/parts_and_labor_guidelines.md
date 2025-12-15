# Parts, BOM, and Labor Modeling Guidelines (v0)

Context: Extends Memo A/B and Build v0 with concrete practices for parts/BOMs and labor resources.

## Parts and BOMs
- One part = one identifiable thing; avoid “miscellaneous” buckets. Group near-substitutable items: e.g., `fastener_kit_medium` instead of many similar screws; `copper_wire_general` unless performance depends on gauge.
- Always include an estimated mass (within 5× of reality is acceptable). Do not leave masses null; add a note/provenance if guessed.
- BOMs enumerate parts/materials with quantities; long-tail items can be grouped as kits (fasteners, gaskets) but still point to identifiable part IDs.
- Use `bom` on machine items to point to `kb/boms/*.yaml`; keep BOM scrap rates explicit when known (or omit).
- Prefer reuse: if two recipes need similar hardware, share the part ID rather than proliferating near-duplicates.

## Labor / Assembly
- Introduce explicit labor machines/resources (replicable robots) to account for assembly, glue tasks, and supervision.
- Treat labor as machine-hours of specific labor bots; include `resource_requirements` entries for labor in processes/recipes where assembly occurs.
- Labor bots are machines themselves (with BOMs later) and have resource_type IDs so they can be scheduled/accounted for.
- Imported compute is allowed (smart controller/AI), but do not hide sensors/actuators; list major physical components normally.

## Process/Recipe Use
- Many fabrication/assembly processes can be modeled as “one primary machine + one labor bot”; capture that in resource requirements.
- When precision matters (special gauge, alloy), encode it in `notes`; default to shared part IDs otherwise.

Labor tiers:
- Start with one general labor bot. Only add additional tiers (heavy lift, precision) if required capabilities differ by >5× (payload/precision/speed) from the base bot.

Sensors/compute:
- Sensors and compute should be explicit (camera arrays, lidar/radar, control compute). Compute can be modeled as imported; still list major modules in BOMs.

Open questions to revisit:
- Should labor capacity be treated as renewable with availability factors, or just machine-hours for now (current: machine-hours)?
