# Wire crimping tools

## Machine identity

- Queue item: `machine_reality_wire_crimping_tools`
- KB ID: `wire_crimping_tools`
- KB file: `kb/items/machines/wire_crimping_tools.yaml`
- KB name: Wire crimping tools
- KB kind: `machine`
- KB modeled mass: 5 kg

The KB defines this as hand and pneumatic crimping tools for wire terminals, connectors, and cable assemblies. Its BOM includes crimping dies, crimper frame/handles, ratchet mechanism, and fasteners.

## KB usage and needed function

`wire_crimping_tools` is used by `wiring_and_electronics_integration_v0`.

The needed function is making repeatable electrical crimp terminations during wiring integration: positioning a stripped wire and terminal/contact in the correct die nest, applying the correct crimp force/geometry, and supporting connector-specific die changes.

## Reality classification

Classification: real practical tool kit/station; not a standalone industrial machine in the usual sense.

Wire crimping tools are real and widely used. The KB entry's 5 kg mass is plausible for a kit of ratcheting hand crimpers, interchangeable die sets, and perhaps a small pneumatic hand tool. The current `kind: machine` is acceptable as a simulator capacity-provider convention, but for imported-machine-list realism this is better described as a tool kit or hand/pneumatic tooling set.

## Evidence links

- TE Connectivity hand crimping tools: https://www.te.com/en/products/application-tooling/hand-crimping-tools.html
  - TE lists commercial hand crimping tools, certified crimp tools, hydraulic crimp tools, 4-way indent crimp tools, and mass-termination crimp tools.
  - The page notes interchangeable die/head designs and manual, battery-powered, and pneumatic alternatives.

- TE Connectivity PRO-CRIMPER III: https://www.te.com/en/products/application-tooling/hand-crimping-tools/intersection/pro-crimper-dies.html
  - Commercial ratcheting hand crimper for prototyping, networking, commercial, industrial, and maintenance work.
  - Features include interchangeable die sets, user-adjustable ratchet control, emergency ratchet release, and broad connector/wire support.

- TE Connectivity pneumatic crimping tools: https://www.te.com/en/products/application-tooling/hand-crimping-tools/intersection/pneumatic-tools.html
  - Pneumatic tools exist for open and closed barrel terminals and 4-way indent crimps.
  - Portable and bench-mount options are available; hand or foot switch operation reduces operator fatigue.

- Molex application tooling: https://www.molex.com/en-us/products/application-tooling
  - Molex lists hand tools, pneumatic hand tools, battery-powered hand tools, applicators, crimping presses, wire stripping/cutting, and support tooling.
  - It distinguishes low-volume hand tools from bench/manual press tools and high-volume fully automatic machines.

- Molex hand crimp tool specification PDF: https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/applicationtoolingspecificationpdf/638/63819/ATS-638190000-001.pdf?inline=
  - Example connector-specific hand crimp tool specification.
  - Lists full-cycle ratcheting, ergonomic handles, terminal locator/wire stop, crimp height, strip length, and specific terminal/wire ranges.

## Commercial alternatives

- Ratcheting hand crimpers with interchangeable die sets: best fit for the KB's 5 kg mass and low-volume wiring integration.
- Connector-specific certified hand crimp tools: higher assurance for aerospace/industrial connectors; less generic but more realistic for reliable terminations.
- Pneumatic portable or bench crimp tools: useful for repeated operations with lower fatigue and better throughput.
- Manual/electric crimp presses and applicators: appropriate for medium/high-volume harness production, but more like a machine than the current KB item.
- Fully automatic cut-strip-crimp machines: not equivalent to this item; much larger and only justified for high-volume cable harness manufacturing.

## Build or open-source references

No credible open-source crimp-tool design was found during this task. Crimpers are mechanically understandable, but reliable electrical crimps depend on precise die geometry, terminal compatibility, ratchet/full-cycle behavior, crimp height, and pull-force validation. Connector-specific commercial tooling is often the realistic choice.

Local fabrication of simple crimp frames and dies may be possible for coarse terminals, but for electronics connectors the KB should treat die/tool precision as important. A labor bot plus commercial or locally machined die sets is more realistic than a generic "crimping machine" unless throughput is high.

## Related machine research

Existing related research found:

- `research/machines/saw_or_cutting_tool.md`

Related KB items or queue topics may include `assembly_tools_basic`, `measurement_equipment`, `multimeter_set`, `pcb_development_station`, and other wiring/electronics integration tools.

## Recommendation for KB realism

Keep the item as real, but consider reclassifying in documentation as a tool kit or station rather than a machine if future KB edits are allowed.

Recommended interpretation:

- Keep as a capacity provider for wiring integration.
- Prefer name/notes like "wire crimping tool kit" or "hand/pneumatic crimping tools" over a machine-like interpretation.
- Do not split into a dedicated crimping station unless the KB models high-volume harness production.
- Preserve crimping dies and ratchet mechanism in the BOM; those are realistic and functionally important.
- Consider pairing with inspection/test resources such as pull tester, multimeter, or visual inspection process if wiring reliability becomes important.

## Confidence and open questions

Confidence: high that the item is real; high that it is better described as a tool kit than a machine.

Open questions:

- Does the KB need connector-specific die sets, or is one generic die set acceptable under the 5x Conservative Mode rule?
- Are crimp pull-force tests modeled anywhere, or is integration/test assumed to cover wiring quality?
- Should pneumatic tooling be included at 5 kg, or should the current item be limited to manual hand tools?

