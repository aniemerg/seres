# Press Ram Set Machine Reality Research

## Machine identity

- KB item id: `press_ram_set`
- KB name: Press ram set
- KB file: `kb/items/parts/press_ram_set.yaml`
- Current KB kind: `machine`
- Current KB mass: 30 kg
- Current BOM: `bom_press_ram_set_v0`
- Current recipe: `recipe_press_ram_set_v0`

## KB usage and needed function

The item is required by `pressing_operations_basic_v0` alongside `hydraulic_press`. Its needed function is a set of rams, plungers, adapters, or ram tooling that transfers force from a press to the workpiece or die.

It does not provide actuation, press force, frame rigidity, hydraulic power, or controls by itself. It is a component/accessory/tooling set for arbor, toggle, hydraulic, or forming presses.

## Reality classification

Real practical press component/tooling set, not a standalone machine.

Press rams/slides/plungers are real press components. Arbor press rams and ram accessories are also real, purchasable components. The KB's 30 kg mass is plausible for a small set of hardened adapters/rams, but the `kind: machine` classification is a simulator convenience rather than a literal machine category.

## Evidence links

- Beckwood's hydraulic press anatomy defines the ram or slide as the moving weldment that creates pressure on the tool or die: <https://beckwoodpress.com/articles/press-anatomy/>
- Pacific Press describes hydraulic press components including cylinder, bolster, and ram/platen systems for forming/stamping/drawing/punching applications: <https://blog.pacific-press.com/blog/parts-of-a-hydraulic-press>
- SteelStampsInc sells an arbor-press ram accessory for 1-ton and 1/2-ton arbor presses, showing ram attachments as commercial accessories rather than complete machines: <https://www.steelstampsinc.com/products/ram-accessory-for-stamping-press>
- Dake explains hydraulic press operation in terms of ram and plunger/cylinder force transmission: <https://blog.dakecorp.com/en-us/4-types-of-hydraulic-presses-and-why-you-need-them>

## Commercial alternatives

- Replacement arbor press ram.
- Hydraulic press ram/cylinder rod or moving platen assembly.
- Ram nose/tool holder adapters for stamping, broaching, pressing, and coining.
- Press V-blocks, plates, and die adapters.
- Dedicated press tooling/die set for a specific operation.

## Build or open-source references

Simple ram adapters and press tooling can be machined from steel and heat treated where needed. Hydraulic cylinder rods/rams require proper material, finish, straightness, seals, and sometimes chrome plating or induction hardening.

The current recipe is plausible for hardened steel accessories, but it should not be read as manufacturing the hydraulic cylinder or entire press.

## Related machine research

Related local reports:

- `research/machines/hydraulic_press.md`
- `research/machines/pressing_mold_set.md`
- `research/machines/forging_press_v0.md`
- `research/machines/press_brake_die_set.md`

## Recommendation for KB realism

Keep as tooling/component if needed, but do not count it as an imported machine.

Recommended options:

- Treat `press_ram_set` as a press tooling/accessory set.
- Keep it paired with `hydraulic_press` or another actual press in process requirements.
- Consider folding it into `pressing_mold_set` or press tooling requirements if it is only a generic adapter inventory.
- Retain separately only where ram adapters materially affect process capability, such as broaching, stamping, or special press work.
- Reclassify from `machine` to part/tooling when schema support allows.

## Confidence and open questions

Confidence: high that press rams/accessories are real; high that the item is not a standalone machine; medium on whether it deserves a separate KB item instead of being included with press tooling.

Open questions:

- Does any process require specific ram geometry, or just general press force?
- Should `pressing_operations_basic_v0` require `press_ram_set` separately, or should the hydraulic press include a basic ram/platen by default?
- Is 30 kg intended as several adapters or a major moving ram/platen subassembly?
