# Epoxy Synthesis Unit Machine Reality Research

## Machine identity

- KB machine id: `epoxy_synthesis_unit`
- KB name: Epoxy synthesis unit
- KB file: `kb/items/machines/epoxy_synthesis_unit.yaml`
- Current KB mass: 200 kg
- Current BOM: `bom_epoxy_synthesis_unit`
- Current recipe: `recipe_machine_epoxy_synthesis_unit_v0`

## KB usage and needed function

The item is used by `epoxy_resin_base_synthesis_v0`, but also by unrelated `hcl_synthesis_from_h2_cl2_v0` and `mos2_solid_lubricant_synthesis_v0`. It appears in the self-reproducing set as polymer processing equipment.

The needed epoxy function is a small resin synthesis reactor/unit with heating/cooling, agitation, feed addition, corrosion-compatible materials, condensation/distillation or solvent recovery, washing/separation, and controls. For ordinary epoxy potting compound mixing, a mixer may be enough; for synthesizing epoxy resin base, a chemical reactor/process line is needed.

## Reality classification

Real practical equipment category, but chemistry-specific and partly misused.

Epoxy resin production equipment is real, usually a resin reactor or resin production line built around stirred reactors, metering, heating/cooling, vacuum/distillation, filtration, and filling. A 200 kg machine could be plausible as a small pilot reactor or lab synthesis unit, but not a complete industrial epoxy plant. The current BOM is a placeholder and does not yet reflect actual reactor/process equipment.

## Evidence links

- IFA Technology describes resin reactors customized for producing epoxy, phenolic, polyester, formaldehyde, and other resins: <https://www.ifa-technology.net/en/industrial-reactors/industrial-resin-reactors/>
- Valco Group summarizes epoxy resin manufacture from epichlorohydrin and bisphenol A, including reactor charging, washing, and vacuum distillation: <https://www.valcogroup-valves.com/faq-2/epoxy-resins-manufacturing-process-of-epoxy-resins/>
- EPA documentation describes continuous production of epoxy resins from epichlorohydrin and bisphenol A, with raw materials contacted in a reactor and brine byproduct formation: <https://www.epa.gov/sites/default/files/2020-11/documents/epichlorohydrin.pdf>
- SIEHE describes resin production lines with raw material metering, conveying, droplet addition, mixing/reacting, heating/cooling, vacuum, filtration, and filling: <https://www.sieheindustry.com/product_detail/resin-complete-production-line>

## Commercial alternatives

- Small stirred resin reactor for lab/pilot synthesis.
- Jacketed reactor with condenser/vacuum/distillation for epoxy base synthesis.
- Complete resin production line with metering, reactor, vacuum, filtration, cooling, and filling.
- Generic chemical reactor for non-epoxy reactions.
- Mixer/dispensing station for mixing purchased epoxy resin with hardener/fillers.

## Build or open-source references

Local construction is plausible only as a chemical reactor system: vessel, agitator, jacket/heating/cooling, seals, condenser, vacuum/vent handling, metering, controls, and chemical-resistant materials. For epichlorohydrin/caustic/BPA chemistry, toxicity, volatility, corrosion, and brine/solvent separation matter.

The current placeholder recipe should not be treated as sufficient for realistic resin synthesis.

## Related machine research

Related local reports:

- `research/machines/chemical_reactor_basic.md`
- `research/machines/generic_chemical_reactor_v0.md`
- `research/machines/chemical_reactor_vessel_v0.md`
- `research/machines/mixer_or_blender.md`
- `research/machines/plastic_extruder.md`

## Recommendation for KB realism

Keep only for epoxy/resin synthesis, and move unrelated chemistry elsewhere.

Recommended options:

- Define `epoxy_synthesis_unit` as a small resin reactor or resin synthesis skid, not a generic chemical reactor.
- Use `chemical_reactor_basic` or a specific HCl reactor for `hcl_synthesis_from_h2_cl2_v0`; an epoxy unit is not the right semantic machine.
- Use `generic_chemical_reactor_v0` or a sulfur/solid-lubricant synthesis reactor for `mos2_solid_lubricant_synthesis_v0` unless epoxy equipment is truly needed.
- If the KB only needs epoxy mixing/curing, use a mixer/dispensing station instead of synthesis equipment.
- Add missing process equipment assumptions for distillation/vacuum/condensation, corrosion compatibility, and waste/byproduct handling.

## Confidence and open questions

Confidence: high that epoxy/resin reactors are real; high that the current KB item is too generic in usage; medium on the 200 kg mass because scale is unspecified.

Open questions:

- Does the KB intend to synthesize epoxy monomers/resins from basic chemicals or just formulate resin/hardener mixtures?
- What feedstocks are assumed for epoxy synthesis?
- Should epoxy resin production be modeled as a generic stirred-reactor process plus separation instead of a dedicated machine?
