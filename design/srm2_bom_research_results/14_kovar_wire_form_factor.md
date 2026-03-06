1. `System boundary`
   Convert locally available `kovar_alloy_fe_ni_co_v0` (bulk alloy stock: bar/rod/strip/ingot) into `kovar_wire` suitable for:

* glass/ceramic-to-metal seal lead pins and feedthrough preforms,
* welded/brazed electrical leads in vacuum/thermal-cycling hardware,
* springs/strain-relief tie wires, lacing, and small harnessing where CTE match matters.

Includes: hot working to rod, cold drawing to wire, intermediate anneals, surface prep, optional inorganic insulation (glass/enamel/ceramic sleeve). Excludes: primary alloymaking chemistry (already `kovar_alloy_fe_ni_co_v0`) and final hermetic seal assembly (handled by feedthrough/packaging subsystems).

---

2. `Functional decomposition`

* **F1 Geometry transformation:** bulk → rod → wire with controlled diameter/ovality.
* **F2 Property control:** temper (soft/annealed vs half-hard), grain size, residual stress (for bendability and seal reliability).
* **F3 Surface condition control:** oxide/cleanliness/roughness (critical for glass sealing and coating adhesion).
* **F4 Insulation integration:** inorganic or low-outgassing insulation compatible with vacuum + thermal cycling.
* **F5 QA and traceability:** verify composition/CTE class, dimensional tolerances, mechanical and surface metrics.

---

3. `Candidate architecture options (A/B/C)`
   **A) First-generation “import-critical tooling” wire line (high confidence)**

* Import: precision drawing dies (WC/PCD), capstan draw bench, controlled-atmosphere anneal tube/furnace hardware, inspection tools.
* Local: Kovar rod/strip feedstock, simple cleaning/pickling chemicals (or electro-clean), spooling.
* Outcome: reliable wire for feedthrough pins/leads; scalable by adding dies + spools.

**B) Hybrid line with local die fabrication (medium confidence)**

* Import: starter die set + metrology.
* Local: sintered ceramic or WC-Co die blanks (later), lapping/polishing station.
* Outcome: reduces die resupply; higher process development burden.

**C) “Melt-spin / extrude micro-wire” (second-generation, low confidence)**

* Direct molten stream + rapid solidification or extrusion to fine wire.
* Outcome: attractive on paper but high risk (diameter control, defects, tooling complexity).

---

4. `Recommended architecture`
   **Option A** for first-generation: it is the smallest credible set of imported tooling that unlocks a *huge* range of electrical interconnect and hermetic packaging primitives. Kovar’s controlled expansion matching to borosilicate glass/alumina is the key reason it exists in the system at all (i.e., you don’t pick Kovar for conductivity; you pick it for seal integrity under thermal cycling). Kovar is commonly specified as ~29% Ni / 17% Co / balance Fe (ASTM F15 class) ([niwire.com][1]), and published datasheets give nominal CTE behavior in the relevant ranges ([ametekinterconnect.com][2]).

**Why wire form is needed beyond bulk alloy**

* **Hermetic feedthrough “pins” want long, straight, small cross-section stock** (wire is the natural precursor to cut-to-length pins, headers, eyelets, and lead frames).
* **Harnessing and strain relief:** thin wire can be routed, tied, and spot-welded; bulk can’t.
* **Spring elements & compliant leads:** fine wire enables controlled compliance to reduce seal stress during vibration/thermal cycling.
* **Coating/insulation:** many insulation strategies (glass enamel, ceramic sleeving, multi-pass polymer) assume a wire-like substrate.

---

5. `BOM draft` (component, material, qty, unit, rationale, manufacturability)

**Process cell: Kovar wire drawing + anneal (baseline for 0.2–2.0 mm wire)**

* Rod feedstock billets, `kovar_alloy_fe_ni_co_v0`, 1, kg, starting stock for breakdown to rod, **Local** (you already have alloy).
* Hot breakdown mill OR small forging press + grooved rolls, steel + refractory, 1, set, reduce ingot/bar to ~6–10 mm rod, **Partially local** (structure local; bearings/motors imported initially).
* Draw bench / bull-block capstan, steel frame + motor, 1, unit, controlled multi-pass drawing, **Import early** (precision + reliability).
* Drawing dies set (sequence), WC/PCD, 20–60, pcs, defines diameter schedule/finish, **Import early**; **local later** (Option B).
* Die holders + alignment fixtures, steel, 1, set, concentricity and repeatability, **Local**.
* Lubrication system (soap/lime carrier or polymer drawing lube), consumables, 1, lot, reduces die wear + surface damage, **Import consumables initially**; local substitutes later.
* Controlled-atmosphere anneal furnace (tube + seals), Inconel/ceramic tube + heaters, 1, unit, intermediate anneal without heavy oxidation; typical anneal practices emphasize controlled atmospheres and avoiding excessive grain growth ([espimetals.com][3]), **Import early** (but can be staged).
* Atmosphere gas supply (forming gas / H₂/N₂) *or* cracked ammonia equivalent, 1, system, limit oxidation; common anneal atmospheres include hydrogen/dissociated ammonia-type neutral atmospheres ([espimetals.com][3]), **Import first-generation**.
* Cleaning line: degrease + rinse + dry, stainless tankage, 1, set, cleanliness for sealing/coating; typical practice begins with wash/degrease ([Eagle Alloys Corporation][4]), **Local**.
* Surface conditioning: light acid pickle / electroclean OR abrasive polish, chemicals + power supply, 1, set, control oxide and adhesion; **Local-ish** (chemicals may be imported early).
* Spooler/take-up + tension control, steel + motor, 1, unit, prevent kinks/ovality, **Local frame / imported controls**.
* Metrology: laser micrometer or precision micrometer + ovality gauge, 1, set, diameter/ovality control, **Import**.
* Mechanical test: simple tensile tester (bench), 1, unit, verify temper; annealed property envelopes are commonly specified for rod/wire per ASTM F15-oriented data ([EFINEA Metals][5]), **Import early**.

**Optional insulation add-ons (choose per use-case)**

* Ceramic bead sleeving (alumina beads), alumina, as needed, m, vacuum-stable insulation on lead wires, **Import first-gen; local later**.
* Glass/enamel insulation coat (inorganic), glass frit/enamel, as needed, lot, highest vacuum compatibility; processing complexity moderate, **Second-gen** unless you already run glass frit lines.
* Polyimide enamel / high-temp magnet-wire coatings, polymer, as needed, lot, easy electrically but outgassing/thermal limits vs inorganic; **Use cautiously** in high-vacuum hot zones.

---

6. `Manufacturing route draft` (ordered process steps with inputs/outputs)

### A. Breakdown: bulk → rod (if starting from bar/ingot)

1. **Homogenize (optional but helpful)**

   * Input: Kovar billet/bar
   * Process: heat soak below “excessive grain growth” regime; keep cycles conservative.
   * Output: more uniform workability.

2. **Hot work to rod**

   * Input: billet/bar
   * Process: hot forge + groove-roll to ~6–10 mm rod.
   * Output: rod coil/lengths.

3. **Descale / straighten**

   * Input: hot-worked rod
   * Process: mechanical descale + light pickle/electroclean.
   * Output: clean rod for drawing.

### B. Wire drawing: rod → final wire diameter

4. **Pointing**

   * Input: rod end
   * Process: swage/grind point to thread through first die.
   * Output: drawable lead.

5. **Multi-pass cold drawing**

   * Input: rod, die sequence, lubricant
   * Process: reduce area in steps (e.g., 10–25% area reduction per pass as a starting envelope; tune by experience).
   * Output: work-hardened intermediate wire.

6. **Intermediate anneal (critical)**

   * Input: work-hardened wire
   * Process: atmosphere-controlled anneal; typical cycle guidance often cites ~850 °C for ~30 min and cautions against >900 °C or long holds due to grain growth ([espimetals.com][3]).
   * Output: softened wire, restored ductility.

7. **Repeat draw + anneal until final diameter**

   * Output: final size wire.

8. **Final anneal / temper set**

   * Two product classes:

     * **Temper A / annealed (preferred for sealing, tight bends):** full anneal in controlled atmosphere.
     * **Half-hard (preferred for springs/strain relief):** reduced anneal or final cold reduction without full anneal.
   * Output: specified temper wire.

### C. Surface prep for sealing / insulation

9. **Cleanliness prep**

   * Degrease → rinse → dry (no residue).

10. **Oxide control (for glass sealing)**

* Many sealing workflows require a controlled oxide on Kovar for glass wetting; treat this as a separate, tightly controlled “seal-prep” step owned by the feedthrough process, but ensure your wire can accept it (consistent surface, no embedded lube).

11. **Insulation application (optional)**

* **Ceramic sleeving:** thread beads, stake ends.
* **Glass/enamel:** dip/flow coat with frit + fire; verify adhesion/cracks.
* **Polymer enamel:** apply/coat/cure per material limits.

---

7. `Test/verification steps`
   **Incoming alloy verification**

* Composition spot check per batch (XRF/OES if available) to confirm nominal F15-class chemistry (~29 Ni / 17 Co / bal Fe) ([niwire.com][1]).
* CTE class verification on representative samples if you can (dilatometry). Datasheets give nominal CTE curves/ranges ([ametekinterconnect.com][2]).

**In-process**

* Diameter every pass (micrometer/laser), ovality, surface visual (scratches, die lines).
* Hardness proxy (bend test / simple hardness) to decide anneal timing.

**Final wire**

* Tensile test for temper consistency (compare to your own spec limits; annealed rod/wire limits are commonly published for F15-class material ([EFINEA Metals][5])).
* 180° wrap/bend test around mandrels (no cracks).
* Surface cleanliness: solvent wipe + UV/gravimetric residue (simple).
* For insulation: dielectric withstand + adhesion (tape pull) + thermal cycle (hot/cold) + vacuum bake outgassing screen (mass loss).

**Seal-specific (hand-off to packaging process)**

* Glass wetting trials on short coupons after the chosen oxide schedule.
* Helium leak test on representative sealed assemblies (system-level).

---

8. `Failure modes and maintenance plan`

* **Wire breakage during drawing:** too much reduction per pass, damaged die, insufficient lube → reduce schedule, polish/replace die, improve lube filtration.
* **Orange peel / surface tearing:** poor anneal, inclusions, bad surface prep → adjust anneal, add rod conditioning, improve cleanliness.
* **Excessive oxidation / scale:** anneal atmosphere leaks → improve seals, purge, monitor dew point / O₂.
* **Grain growth → brittle bends / seal cracks:** overheating or over-soak; sources caution that >900 °C or long holds promote grain growth ([espimetals.com][3]).
* **Insulation delamination/cracking:** CTE mismatch or poor adhesion; prefer ceramic sleeving for highest robustness; qualify enamel/polymer per thermal cycle.
* **Spool set / kinks:** bad tension control → add dancer/tension feedback, larger spool diameters for thin wire.

Maintenance

* Die inspection schedule (microscope), diameter drift tracking.
* Furnace leak checks; replace seals/retorts.
* Lube change/filtration; keep particles out (die wear accelerant).
* Periodic recalibration of metrology tools.

---

9. `Assumptions and uncertainties`

* Assumes `kovar_alloy_fe_ni_co_v0` is close to ASTM F15-type Kovar composition and cleanliness; tight composition control matters for predictable CTE ([niwire.com][1]).
* Anneal recipes are *starting points*; actual draw schedule depends on initial stock condition, reduction ratio, and die quality. Published guidance emphasizes controlled atmosphere and avoiding very high/long anneals ([espimetals.com][3]).
* Lunar operations: availability of anneal atmospheres (H₂/N₂) is a logistics constraint; vacuum anneal is tempting but oxidation/oxide-control needs for sealing complicate the story.
* Long-term local die fabrication is feasible but requires mature ceramic/carbide processing and precision lapping (Option B).

---

10. `Sources and confidence`

* **Kovar nominal composition (~29% Ni, ~17% Co, balance Fe) / ASTM F15 framing:** high confidence ([niwire.com][1])
* **Anneal guidance (controlled atmosphere; typical ~850 °C/30 min; avoid >900 °C or long holds due to grain growth):** medium-high confidence ([espimetals.com][3])
* **CTE nominal curve values in common datasheet ranges:** medium confidence (datasheet values vary by product form/heat) ([ametekinterconnect.com][2])
* **Wire necessity for hermetic feedthroughs/leads (functionality rationale):** high confidence (standard industry use; supported broadly by Kovar application descriptions) ([cdn.thomasnet.com][6])
* **Insulation stack recommendations (ceramic sleeving best for vacuum; enamel/polymer conditional):** medium confidence (application-dependent; requires local qualification rather than single authoritative rule).

[1]: https://www.niwire.com/uploads/documents/ASTM%20F15%20Kovar.pdf?utm_source=chatgpt.com "Kovar Alloy Alloy F15 (Kovar)"
[2]: https://www.ametekinterconnect.com/-/media/ametek-ecp/v2/files/cw_datasheets_sds_cfsi/datasheets/kovar.pdf?la=en&utm_source=chatgpt.com "Kovar"
[3]: https://www.espimetals.com/index.php/technical-data/99-Kovar?utm_source=chatgpt.com "Kovar"
[4]: https://www.eaglealloys.com/machine-guide/?utm_source=chatgpt.com "Machining Nickle-Iron Alloys - Kovar®, Invar®36 & Super ..."
[5]: https://www.efineametals.com/controlled-expansion-alloys/kovar-astm-f-15-pernifer-nilo-rod-bar-sheet-plate/kovar-properties/?utm_source=chatgpt.com "ASTM F15 - Kovar® Mechanical & Physical Properties"
[6]: https://cdn.thomasnet.com/ccp/10014080/322273.pdf?utm_source=chatgpt.com "Kovar ® ASTM F15 Technical Data Sheet | Ed Fagan Inc."
