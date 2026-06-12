# Metal Shear or Saw Machine Reality Research

## Machine identity

- KB machine id: `metal_shear_or_saw`
- KB name: Metal shear or saw
- KB file: `kb/items/machines/metal_shear_or_saw.yaml`
- Current KB mass: 78 kg
- Current BOM: `bom_metal_shear_or_saw`
- Current recipe: `recipe_metal_shear_or_saw_v0`

## KB usage and needed function

The item is used for `shear_metal_cutting_v0`, tube cutting/bending workflows, sheet metal fabrication, welding/fabrication, and general metal stock preparation.

The needed function is cutting steel sheet, plate, bar, tube, and structural sections down to usable blanks. A shear is best for sheet and plate straight cuts. A horizontal bandsaw or cold saw is better for bar, tube, and structural sections. The KB's combined name is therefore a broad stock-prep capability rather than one precise commercial machine.

## Reality classification

Real practical machine category or shop station, but not a single exact machine type.

Metal shears and metal-cutting bandsaws are both real, common fabrication-shop machines. The KB item is realistic as an abstract shop cutting capability. The main issue is that a "shear or saw" conflates two different mechanisms, cutting geometries, blade consumables, and stock envelopes. The 78 kg current mass is plausible for a small horizontal bandsaw or light shop shear, but much lower than many industrial hydraulic plate shears. Local dedupe notes previously describe it as the canonical heavier metal-cutting tool, but older mass values in those notes were higher.

## Evidence links

- JET sells manual and semi-automatic horizontal metal bandsaws for shop metal cutting, with capacities such as 7 x 12, 8 x 12, and 10 x 16 inches: <https://jettools.com/metalworking/sawing/manual-semi-automatic-horizontal-bandsaws>
- KAAST describes automatic horizontal bandsaws for cutting steel, aluminum, tubing, and structural profiles to programmed lengths: <https://kaast-usa.com/band-saws/>
- Piranha sells hydraulic guillotine metal shears for accurate plate shearing from 1/4 inch to 1 inch plate, showing the heavier industrial shear end of this family: <https://piranhafab.com/hydraulic-shears/>
- Boyd Metals summarizes sawing and shearing as common metal cutting methods, with band saws used for bar and pipe stock and shears used for sheet/plate: <https://blog.boydmetals.com/everything-you-need-to-know-about-sawing-shearing>

## Commercial alternatives

- Horizontal metal-cutting bandsaw: best fit for tube, bar, billet, and structural sections.
- Cold saw: cleaner accurate cuts on tube/bar/sections, usually smaller capacity.
- Hydraulic guillotine shear: best for sheet and plate straight cuts.
- Ironworker with shear/punch/notch stations: compact multi-function fabrication-shop tool.
- Abrasive chop saw: low-cost, rougher, more consumable-heavy option for small shops.

## Build or open-source references

The KB recipe is plausible for a simple local shop-built bandsaw or light shear frame: welded frame/bed, machined guide and clamp surfaces, motor drive, blade/band, feed/clamp system, and basic controls.

The hard parts differ by variant. A bandsaw needs wheels, blade tensioning, guides, coolant, speed reduction, and blade consumables. A shear needs a rigid frame, hold-downs, knife clearance adjustment, hardened blades, and high force. Treating one BOM as both should remain a coarse abstraction.

## Related machine research

Related local reports:

- `research/machines/saw_or_cutting_tool.md`
- `research/machines/press_brake.md`
- `research/machines/steel_forming_press.md`

Relevant local decision:

- `docs/dedupe_decisions.md` keeps `metal_shear_or_saw` as the canonical primary metal cutting tool and uses `saw_or_cutting_tool` for smaller hand/manual cutting.

## Recommendation for KB realism

Keep for now as a generic metal stock-prep machine, but make the abstraction explicit.

Recommended options:

- Keep `metal_shear_or_saw` as the broad canonical machine for low-detail fabrication recipes.
- For higher realism, split into `metal_cutting_bandsaw` and `sheet_metal_shear` when process geometry matters.
- Keep `saw_or_cutting_tool` separate for small hand/power tools and gasket/core cutting.
- Update notes if desired to say it represents a small shop cutting station, not a full industrial plate shear.
- Revisit mass if processes imply industrial plate shearing; 78 kg is small for hydraulic shears but plausible for a light bandsaw.

## Confidence and open questions

Confidence: high that the underlying machines are real; medium that the combined KB abstraction is adequate for all current uses.

Open questions:

- Do current plate and sheet processes need straight shear cuts, or would a bandsaw/cutoff saw be acceptable at the modeled scale?
- Should blade/band wear be modeled as consumable tooling?
- Is the 78 kg mass intentional after dedupe, or should it be reconciled with older notes that mentioned 350 kg?
