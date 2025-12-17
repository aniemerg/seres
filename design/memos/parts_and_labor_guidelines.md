# Parts, BOM, and Labor Modeling Guidelines (v0)

Context: Extends Memo A/B and Build v0 with concrete practices for parts/BOMs and labor resources.

## Parts and BOMs
- One part = one identifiable thing; avoid "miscellaneous" buckets. Group near-substitutable items: e.g., `fastener_kit_medium` instead of many similar screws; `copper_wire_general` unless performance depends on gauge.
- Always include an estimated mass (within 5× of reality is acceptable). Do not leave masses null; add a note/provenance if guessed.
- BOMs enumerate parts/materials with quantities; long-tail items can be grouped as kits (fasteners, gaskets) but still point to identifiable part IDs.
- Use `bom` on machine items to point to `kb/boms/*.yaml`; keep BOM scrap rates explicit when known (or omit).
- **Prefer reuse: ALWAYS check existing parts before creating new ones.**
  - Check inventory: `out/reports/inventory.md` (regenerate: `.venv/bin/python -m kbtool report inventory`)
  - Search for similar parts: `grep -i "keyword" out/reports/inventory.md`
  - Reuse existing parts if "reasonably equivalent" (see criteria below)
  - Only create new parts if no suitable existing part exists

### Reasonable Equivalence Criteria

Parts should be **shared/reused** if they are "reasonably equivalent":

**Equivalence allowed when:**
- **Magnitude within ~5x**: Since this is an approximation exercise, differences <5x in dimensions, mass, or capability are essentially the same
  - Strut vs. strut 3x longer → use same part ID
  - 5 kW motor vs. 10 kW motor → use same part ID
  - Aluminum gear vs. similar gear 2x larger → use same part ID
- **Shape variations, same purpose**: Parts with different shapes but same function and construction method
  - Support frame with/without cross beams → use same part ID
  - Document specific differences in BOM/recipe `notes` field
- **Similar construction/function**: Parts made the same way serving the same purpose
  - Different pump types (vacuum vs. water) → use same part ID IF materials compatible

**NOT equivalent when:**
- **Materials incompatible**: Material properties matter for function/process compatibility
  - Steel beam ≠ plastic beam (structural strength differs)
  - Electrical conductor ≠ electrically resistive material (function differs)
  - High-temp component ≠ low-melting material (process incompatible)
- **Process requirements conflict**: Cannot substitute if material would fail in the target process (melting, corrosion, mechanical failure)

When reusing a part with different specs, note the variation in the BOM or recipe `notes` field.

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
