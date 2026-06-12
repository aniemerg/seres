# Blast Furnace or Smelter Machine Reality Research

## Machine identity

- KB machine id: `blast_furnace_or_smelter`
- KB name: Blast furnace or smelter
- KB file: `kb/items/machines/blast_furnace_or_smelter.yaml`
- Current KB mass: 5000 kg
- Current BOM: `bom_blast_furnace_or_smelter_v0`
- Current recipe: `recipe_blast_furnace_or_smelter_v0`

## KB usage and needed function

The item is used by `iron_smelting_reduction_v0` and appears in the self-reproducing set as iron/metal smelting equipment.

The needed function is high-temperature reduction or melting of metal-bearing feedstock with slag separation and tapping. For iron ore reduction, this implies a blast furnace or related shaft/bloomery/cupola-style furnace with tuyeres, forced air, fuel/reductant, flux, refractory lining, tapping, and slag handling. For simple remelting, an induction, crucible, cupola, or electric arc furnace may be more appropriate.

## Reality classification

Real practical machine category, but the current name conflates several different machines.

Blast furnaces, cupola furnaces, induction furnaces, electric arc furnaces, and generic smelters are all real, but they differ in feedstock, fuel, reductant chemistry, atmosphere, scale, emissions, metal quality, and infrastructure. A 5000 kg compact smelter is plausible for a small foundry/cupola/smelter, but much too small for a modern industrial iron blast furnace. It should be treated as a small smelting furnace, not a full steelworks blast furnace.

## Evidence links

- Encyclopaedia/Wikipedia overview: blast furnaces use coke/ore/flux charging, hot blast through tuyeres, countercurrent reduction, and tapping of molten metal and slag: <https://en.wikipedia.org/wiki/Blast_furnace>
- Cupola furnace overview: cupolas are small vertical foundry furnaces for melting cast iron and some bronzes, with coke, air blast, tuyeres, tapping, and slag handling: <https://en.wikipedia.org/wiki/Cupola_furnace>
- Across International summarizes foundry furnace types including cupola, crucible, induction, electric arc, and vacuum induction furnaces, showing that "smelter" is not one machine class: <https://www.acrossinternational.com/news/post/foundry-furnaces-understanding-the-different-methods-and-systems>
- IspatGuru's blast furnace glossary describes tapping as the removal of hot metal and liquid slag from the blast furnace hearth: <https://www.ispatguru.com/glossary-of-terms-used-for-a-blast-furnace/>

## Commercial alternatives

- Small cupola furnace for melting cast iron from scrap/pig iron.
- Bloomery or small shaft furnace for direct iron reduction at small scale.
- Blast furnace for continuous pig iron production from ore, coke, and flux.
- Induction furnace for clean controlled remelting of metal, but not ore reduction.
- Electric arc furnace for scrap melting and steelmaking.
- Crucible furnace for small nonferrous or specialty melts.

## Build or open-source references

Small cupola and foundry furnaces can be built from steel shell, refractory lining, blower, tuyeres, charging opening, tap hole, slag handling, and exhaust handling. Ore reduction and blast furnace operation require more than heat: reductant chemistry, flux balance, slag control, charge preparation, air blast, tapping practice, and emissions handling.

The current KB BOM appears directionally plausible for a compact smelter, but the "blast furnace or smelter" label should not imply it can process iron ore, copper ore, aluminum feedstock, and scrap interchangeably without process-specific changes.

## Related machine research

Related local reports:

- `research/machines/casting_furnace_v0.md`
- `research/machines/glass_furnace_v0.md`
- `research/machines/crucible_refractory.md`
- `research/machines/induction_forge_v0.md`

## Recommendation for KB realism

Keep as a temporary coarse smelting machine, but eventually split or rename.

Recommended options:

- Rename to `small_smelter_furnace_v0` if this represents a compact ore/scrap smelting furnace.
- Use `blast_furnace` only for ironmaking from ore/coke/flux with blast air and slag tapping.
- Use cupola/induction/electric arc/crucible furnaces for remelting or alloying, depending on process needs.
- Do not use one generic item for aluminum, copper, iron ore, scrap steel, and specialty alloys without notes.
- Add explicit process requirements for blower, tuyeres, flux, reductant, refractory, tapping system, slag handling, and emissions/gas handling.

## Confidence and open questions

Confidence: high that the underlying machines are real; high that the current "or" item is too broad; medium on whether the KB can tolerate the abstraction for current iron smelting.

Open questions:

- Is `iron_smelting_reduction_v0` meant to produce pig iron by blast furnace, bloom iron by direct reduction, or just melt/reduce ore in a generic smelter?
- What fuel/reductant is available in the self-reproducing system?
- Should the KB separate reduction furnaces from remelting/casting furnaces?
