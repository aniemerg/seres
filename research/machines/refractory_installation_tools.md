# Refractory installation tools

## Machine identity

- Queue item: `machine_reality_refractory_installation_tools`
- KB ID: `refractory_installation_tools`
- KB file: `kb/items/machines/refractory_installation_tools.yaml`
- KB name: Refractory installation tools
- KB kind: `machine`
- KB modeled mass: 10 kg

The KB defines this as a tool bundle for refractory installation: hot wire cutters, trowels, anchoring equipment, refractory cement mixers, and wire brushes. The BOM includes `hot_wire_cutter`, `refractory_trowel_set`, `cement_mixer_small`, `wire_brush_set`, `anchor_installation_kit`, and `fastener_kit_small`.

## KB usage and needed function

`refractory_installation_tools` is used by:

- `refractory_lining_installation_v0`
- `refractory_casting_v0`

The needed function is installing refractory linings in furnaces or other high-temperature equipment: preparing surfaces, installing anchors, cutting/fitting refractory insulation or shapes, mixing castables, troweling/placing/packing material, brushing/cleaning, and supporting small-scale casting or repair.

## Reality classification

Classification: real practical tool kit / equipment bundle, not a standalone machine.

The KB item is real in function but should not be described as a single machine. Refractory work uses a mix of hand tools, mixers, vibrators, rammers, gunning equipment, anchor/stud welding tools, forms, brushes, and cutting tools. The KB's 10 kg mass is plausible only for a compact hand-tool kit plus small cutter/anchor tools; it is too low if the item includes a real cement mixer or refractory mixer as a separate component.

## Evidence links

- Allied Mineral Products installation equipment: https://alliedmineral.com/partnerships/thermal-integrated-materials/installation-equipment/
  - Lists refractory installation equipment including tampers, electric vibration systems, rammers, ceramic refractory mixers, vibrators, refractory gunning equipment, and ceramic fiber module stud gun kits.
  - Shows that refractory installation has specialized equipment beyond generic hand tools.

- Becht, "Installation of Monolithic Refractory and Resulting Properties": https://becht.com/becht-blog/entry/installation-of-monolithic-refractory-and-resulting-properties/
  - Describes refractory installation as mixing and placing dry refractory plus liquid, with casting, gunning, and handpacking/ramming methods.
  - Notes that installation quality and dryout are common causes of refractory problems.
  - Discusses gunning hoses/nozzles, air pressure, final water injection, and ramming with pneumatic tampers.

- Malco refractory anchors overview: https://malco-pc.com/what-are-refractory-anchors/
  - Defines refractory anchors as metal components that hold ceramic fiber or castable refractory linings in place inside furnaces, kilns, burners, reformers, and other high-temperature systems.
  - Notes anchors are welded or embedded before lining installation and are essential for stability under heat, load, and vibration.

- Able Refractory castable installation instructions: https://www.ablerefractory.com/castinfo.html
  - Recommends clean tools/equipment, clean water, and paddle-type mixers for uniform refractory castable mixing.
  - Notes castables can be cast, poured, gunned, or troweled.

- Leadcrete refractory gunning machines and mixers: https://www.leadcrete.com/refractory-gunning-machine/
  - Commercial refractory gunning machines are used for lining kilns, boilers, furnaces, steel plant castable maintenance, and glass factory kilns.
  - Also lists refractory pan mixers with 100 kg, 250 kg, and 500 kg capacities.

## Commercial alternatives

- Basic hand-tool kit: refractory trowels, brushes, forms, buckets, measuring tools, cutters, and anchor installation tools.
- Refractory mixer: paddle/pan mixer sized for castable batches.
- Vibrator/tamper/rammer: used for dry-vibratable or rammed installations.
- Gunning machine/shotcrete system: used for larger sprayed refractory linings.
- Stud gun/anchor welding kit: used for ceramic fiber modules or castable anchors.
- Professional refractory installation service: realistic option for large industrial furnaces, but outside the KB's local-manufacturing focus.

## Build or open-source references

The hand tools are locally manufacturable at small scale: trowels, brushes, simple cutters, forms, and anchor fixtures can be made or adapted from general shop tools. The cement mixer component overlaps with `cement_mixer_small`, which already has a related research report.

Gunning machines, refractory mixers, and vibration systems are real but heavier and more specialized than a 10 kg kit. If the KB wants those capabilities, they should be modeled as separate machine/equipment items rather than hidden inside this small tool kit.

## Related machine research

Existing related reports:

- `research/machines/hand_tools_basic.md`
- `research/machines/saw_or_cutting_tool.md`
- `research/machines/cement_mixer_small.md`
- `research/machines/glass_furnace_v0.md`
- `research/machines/casting_furnace_v0.md`
- `research/machines/furnace_high_temp.md`
- `research/machines/heating_furnace.md`

These support interpreting this as a specialized extension of basic tools, not as a full standalone machine.

## Recommendation for KB realism

Keep the item, but rename/interpret it as a tool kit.

Specific recommendation:

- Keep as real practical tooling for refractory work.
- Treat as `refractory_installation_toolkit` or "refractory lining tool kit" if future edits are allowed.
- Do not model this as a machine unless the simulator needs all capacity providers under `kind: machine`.
- Keep `labor_bot_general_v0` or equivalent labor in the process; the tools do not perform installation autonomously.
- Consider removing `cement_mixer_small` from the 10 kg tool kit mass accounting or treating it as a separate required machine/resource, because an actual mixer likely exceeds the kit mass by itself.
- If gunning, ramming, or vibratory installation is required at scale, add/use separate equipment for `refractory_gunning_machine`, `refractory_vibrator`, or `refractory_rammer` rather than overloading this item.

## Confidence and open questions

Confidence: high that the function is real; high that the current item is a toolkit/bundle rather than a single machine.

Open questions:

- Does `refractory_casting_v0` require only hand casting/troweling, or does it need vibration/gunning/ramming equipment?
- Is the 10 kg mass intended to exclude `cement_mixer_small`, despite the BOM including it?
- Are anchor welding/stud tools required, or can existing welding equipment plus an anchor kit cover that role?

