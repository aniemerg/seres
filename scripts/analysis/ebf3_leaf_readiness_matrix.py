#!/usr/bin/env python3
"""Generate a material/process readiness matrix for reachable EBF3 leaf items."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
KB_DIR = REPO_ROOT / "kb"
DEFAULT_CSV = (
    REPO_ROOT
    / "research"
    / "ebf3_bom_sources"
    / "derived"
    / "ebf3_leaf_material_process_readiness.csv"
)
DEFAULT_REPLACEMENT_REGISTER = (
    REPO_ROOT
    / "research"
    / "ebf3_bom_sources"
    / "derived"
    / "ebf3_existing_item_replacement_register.md"
)
PERFORMANCE_REQUIREMENT_FIELDS = (
    "tolerance",
    "surface_finish",
    "sealing_quality",
    "alignment_accuracy",
)


@dataclass(frozen=True)
class CandidateRule:
    tokens: tuple[str, ...]
    candidate_id: str
    fit: str
    note: str


CANDIDATE_RULES: tuple[CandidateRule, ...] = (
    CandidateRule(("ball", "nut"), "ball_screw_assembly", "accuracy_risk", "Ball-nut detail is part of screw-drive accuracy/lubrication review."),
    CandidateRule(("rolling", "ball"), "ball_bearing_steel_v0", "accuracy_risk", "Ball size, grade, material, and finish need review."),
    CandidateRule(("hv", "rectifier"), "hv_rectifier_stack", "accuracy_risk", "HV/oil/vacuum rating must be checked."),
    CandidateRule(("rectifier", "diode"), "rectifier_diode_set", "accuracy_risk", "Diode package/rating detail is hidden."),
    CandidateRule(("rectifier",), "rectifier_bridge_heavy_duty", "accuracy_risk", "Broad rectifier family match."),
    CandidateRule(("capacitor",), "capacitor_bank_filter", "accuracy_risk", "Voltage, ripple current, and dielectric assumptions are hidden."),
    CandidateRule(("inductor",), "inductor_filter_large", "accuracy_risk", "Core, winding, insulation, and rating assumptions are hidden."),
    CandidateRule(("choke",), "inductor_filter_large", "accuracy_risk", "Core, winding, insulation, and rating assumptions are hidden."),
    CandidateRule(("transformer", "core"), "transformer_core", "accuracy_risk", "Core geometry and lamination material need scaling."),
    CandidateRule(("transformer",), "high_voltage_transformer", "accuracy_risk", "Voltage class and insulation package need scaling."),
    CandidateRule(("heat", "sink"), "heat_sink_base_machined", "likely_reuse", "Same-level heat-sink hardware if heat load is modest."),
    CandidateRule(("thermal", "interface"), "thermal_interface_material", "likely_reuse", "Material proxy; check temperature and vacuum/outgassing."),
    CandidateRule(("busbar",), "busbar_distribution_system_v0", "accuracy_risk", "Current rating and conductor geometry need scaling."),
    CandidateRule(("terminal",), "terminal_block_set", "likely_reuse", "Same broad terminal-block set; check voltage/current class."),
    CandidateRule(("connector",), "connector_electrical_multi_pin", "accuracy_risk", "Pin count, seal, and rating assumptions are hidden."),
    CandidateRule(("feedthrough",), "electrical_feedthrough_vacuum", "accuracy_risk", "Vacuum seal, pin, dielectric, and voltage rating are fidelity-critical."),
    CandidateRule(("seal",), "vacuum_seal_assembly", "accuracy_risk", "Seal geometry/material/leak rate are hidden."),
    CandidateRule(("cable",), "assembled_cable_harness", "accuracy_risk", "Length, shield, insulation, and rating need scaling."),
    CandidateRule(("harness",), "assembled_wire_harness", "accuracy_risk", "Length, connectors, shield, and routing need scaling."),
    CandidateRule(("lead",), "electrical_wire_and_connectors", "accuracy_risk", "Length, conductor, insulation, and termination need scaling."),
    CandidateRule(("conductor",), "electrical_wire_and_connectors", "accuracy_risk", "Length, conductor, insulation, and termination need scaling."),
    CandidateRule(("linear", "encoder"), "linear_encoder_set", "accuracy_risk", "Scale/read-head/grating precision assumptions are hidden."),
    CandidateRule(("rotary", "encoder"), "encoder_rotary_incremental", "accuracy_risk", "Resolution, vacuum, and mounting assumptions are hidden."),
    CandidateRule(("encoder",), "encoder_rotary_incremental", "accuracy_risk", "Resolution, vacuum, and mounting assumptions are hidden."),
    CandidateRule(("linear", "guide"), "linear_guide_rails", "accuracy_risk", "Rail/carriage split, preload, straightness, and lubrication need review."),
    CandidateRule(("ball", "screw"), "ball_screw_assembly", "accuracy_risk", "Shaft/nut split, preload, and accuracy class need review."),
    CandidateRule(("bearing",), "bearing_set_heavy", "accuracy_risk", "Load, runout, lubrication, and vacuum compatibility need review."),
    CandidateRule(("worm",), "worm_gear_set_v0", "likely_reuse", "Same gear family if torque/load is modest."),
    CandidateRule(("gearbox",), "gearbox_reducer_small", "accuracy_risk", "Torque ratio, lubrication, and vacuum compatibility need review."),
    CandidateRule(("motor",), "stepper_motor_precision", "accuracy_risk", "Torque, vacuum compatibility, encoder, and insulation need review."),
    CandidateRule(("fastener",), "fastener_kit_medium", "likely_reuse", "Generic fastener kit is acceptable for non-precision interfaces."),
    CandidateRule(("screw",), "fastener_kit_medium", "likely_reuse", "Generic fastener kit is acceptable unless it is a precision lead screw."),
    CandidateRule(("washer",), "fastener_kit_medium", "likely_reuse", "Generic washer/fastener kit is acceptable unless material is special."),
    CandidateRule(("nut",), "fastener_kit_medium", "likely_reuse", "Generic nut/fastener kit is acceptable unless material is special."),
    CandidateRule(("hinge",), "door_hinge_assembly", "likely_reuse", "Same function; check vacuum and load."),
    CandidateRule(("pressure", "relief"), "pressure_relief_valve", "likely_reuse", "Same function; check setpoint and fluid compatibility."),
    CandidateRule(("camera",), "machine_vision_camera_v0", "accuracy_risk", "Sensor, lens, thermal/vacuum environment need review."),
    CandidateRule(("lens",), "lens_assembly_magnifying", "accuracy_risk", "Optical material, wavelength, and thermal/vacuum environment need review."),
    CandidateRule(("window",), "glazed_panel_or_door", "accuracy_risk", "Viewport material/thickness/seal need review."),
    CandidateRule(("viewport",), "glazed_panel_or_door", "accuracy_risk", "Viewport material/thickness/seal need review."),
    CandidateRule(("panel",), "panel_or_door_assembly", "accuracy_risk", "Panel geometry, stiffness, and sealing assumptions need scaling."),
    CandidateRule(("door",), "panel_or_door_assembly", "accuracy_risk", "Door geometry, stiffness, and sealing assumptions need scaling."),
    CandidateRule(("enclosure",), "enclosure_electrical_medium", "likely_reuse", "Same-level enclosure if scale and environment pass review."),
    CandidateRule(("housing",), "enclosure_electrical_medium", "accuracy_risk", "Housing geometry and interface assumptions are hidden."),
    CandidateRule(("frame",), "structural_frame_small_v0", "accuracy_risk", "Frame geometry, stiffness, and mounting assumptions need scaling."),
    CandidateRule(("plate",), "metal_sheet_or_plate", "accuracy_risk", "Stock is not a same-level replacement; use for material/process only."),
    CandidateRule(("shaft",), "steel_shaft", "accuracy_risk", "Length, diameter, finish, and straightness need scaling."),
    CandidateRule(("software",), "compiled_firmware_binary", "likely_reuse", "Information artifact proxy; machine behavior requirements still need review."),
)


MATERIAL_SUGGESTIONS: tuple[tuple[tuple[str, ...], str, str, str], ...] = (
    (("terminal",), "copper_alloy_contact", "steel_mounting_hardware", "Electrical contact material; check voltage/current and insulation."),
    (("connector",), "copper_alloy_contact", "ceramic_or_polymer_body", "Contact/body materials should be split if closure matters."),
    (("standoff",), "alumina_ceramic", "steel", "Use ceramic when electrical/thermal isolation matters; steel only for structural standoffs."),
    (("frame",), "steel_structural_stock", "aluminum_structural_stock", "Select by stiffness and fabrication route."),
    (("bracket",), "steel", "aluminum", "Simple machined/bent/welded hardware."),
    (("mount",), "steel", "aluminum; alumina_ceramic", "Simple machined/bent/welded hardware unless insulating."),
    (("spacer",), "steel", "aluminum; alumina_ceramic", "Choose ceramic if electrical/thermal isolation matters."),
    (("retainer",), "steel", "aluminum", "Simple retaining hardware unless high temperature."),
    (("shield",), "steel", "aluminum; refractory_foil", "Radiation/HV shields may need refractory metal."),
    (("cathode",), "tungsten", "lanthanum_hexaboride; tantalum", "Emission material and lunar availability need dedicated review."),
    (("anode",), "molybdenum", "tungsten", "Electron-gun electrode material; aperture/thermal stability dominate."),
    (("electrode",), "molybdenum", "tungsten", "Electron-gun electrode material; precision and thermal stability dominate."),
    (("insulator",), "alumina_ceramic", "porcelain; fused_silica", "Use ceramic route; dielectric/creepage rating required."),
    (("seal",), "silicone_rubber", "metal_gasket", "Vacuum/oil compatibility decides final material."),
    (("window",), "aluminosilicate_glass", "fused_silica", "Optical and thermal requirements decide final material."),
    (("viewport",), "aluminosilicate_glass", "fused_silica", "Optical and thermal requirements decide final material."),
    (("cable",), "aluminum_conductor", "copper_conductor", "Voltage, vacuum, and temperature decide insulation."),
    (("lead",), "aluminum_conductor", "copper_conductor", "Voltage, vacuum, and temperature decide insulation."),
    (("conductor",), "aluminum", "copper", "Use copper only when conductivity/size penalty matters."),
    (("busbar",), "aluminum", "copper", "Use copper only when current density or thermal penalty matters."),
    (("heat", "sink"), "aluminum", "steel", "Aluminum is the normal heat-sink material; steel only as closure proxy."),
    (("panel",), "steel_sheet", "aluminum_sheet", "Select by stiffness, thermal exposure, and manufacturability."),
    (("plate",), "steel_plate", "aluminum_plate", "Select by stiffness, flatness, thermal exposure, and manufacturability."),
    (("spring",), "spring_steel", "", "Elastic performance dominates material selection."),
    (("knob",), "steel", "ceramic", "Simple hardware; choose ceramic for heat/electrical isolation."),
)


def load_yaml(path: Path) -> dict:
    with path.open() as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, dict) else {}


def load_items() -> dict[str, dict]:
    items: dict[str, dict] = {}
    for path in (KB_DIR / "items").rglob("*.yaml"):
        data = load_yaml(path)
        item_id = data.get("id")
        if item_id:
            data["_path"] = str(path.relative_to(REPO_ROOT))
            items[item_id] = data
    return items


def load_boms() -> dict[str, dict]:
    boms: dict[str, dict] = {}
    for path in (KB_DIR / "boms").glob("*.yaml"):
        data = load_yaml(path)
        owner = data.get("owner_item_id")
        if owner:
            data["_path"] = str(path.relative_to(REPO_ROOT))
            boms[owner] = data
    return boms


def load_replacement_register_decisions(path: Path = DEFAULT_REPLACEMENT_REGISTER) -> dict[str, str]:
    if not path.exists():
        return {}
    decisions: dict[str, str] = {}
    section = ""
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            section = line.removeprefix("## ").strip()
            continue
        if not line.startswith("| `ebf3_"):
            continue
        item_id = line.split("|", 2)[1].strip().strip("`")
        if section == "Active Approved Replacements":
            decisions[item_id] = "registered_approved_reuse"
        elif section == "Candidate Exists But Not Enough Accuracy":
            decisions[item_id] = "registered_not_enough_accuracy"
        elif section == "Wrong Functional Object":
            decisions[item_id] = "registered_wrong_functional_object"
    return decisions


def reachable_from(root_id: str, boms: dict[str, dict]) -> tuple[set[str], dict[str, set[str]]]:
    seen = {root_id}
    parents: dict[str, set[str]] = defaultdict(set)
    queue: deque[str] = deque([root_id])
    while queue:
        owner = queue.popleft()
        for component in boms.get(owner, {}).get("components", []):
            child = component.get("item_id")
            if not child:
                continue
            parents[child].add(owner)
            if child not in seen:
                seen.add(child)
                queue.append(child)
    return seen, parents


def tokens_for(*parts: object) -> set[str]:
    text = " ".join(str(part or "") for part in parts).lower()
    for ch in "_-/(),:;":
        text = text.replace(ch, " ")
    return {token for token in text.split() if token}


def mass_kg(item: dict) -> float | None:
    value = item.get("mass_kg", item.get("mass"))
    if isinstance(value, int | float):
        return float(value)
    return None


def scale_tag(item: dict, mass: float | None) -> str:
    if item.get("unit_kind") == "bulk" or item.get("unit") in {"kg", "g", "m", "m2", "m3"}:
        return "bulk_stock"
    if mass is None:
        return "unknown_scale"
    if mass < 0.05:
        return "tiny_discrete"
    if mass < 0.5:
        return "small_discrete"
    if mass < 5:
        return "medium_discrete"
    if mass < 50:
        return "large_discrete"
    return "very_large_discrete"


def mass_basis(tokens: set[str]) -> tuple[str, str]:
    if {"plate", "panel"} & tokens:
        return "area_thickness_density", "Scale by area * thickness * density; use stiffness/flatness as constraints."
    if {"shell", "tank", "cabin", "enclosure", "housing"} & tokens:
        return "surface_area_wall_thickness_density", "Scale by wetted/surface area * wall thickness * density, then add flanges/ports."
    if {"shaft", "rod", "screw"} & tokens:
        return "length_cross_section_density", "Scale by length * cross-section * density; add finish/straightness requirements."
    if {"wire", "cable", "lead", "conductor", "harness"} & tokens:
        return "length_gauge_insulation_factor", "Scale conductor length/gauge, then add insulation, shield, and terminations."
    if {"coil", "winding", "inductor", "transformer", "choke"} & tokens:
        return "rating_scaled_magnetic_component", "Scale from voltage/current/power/frequency plus insulation/thermal class."
    if {"board", "sensor", "processor", "module", "software"} & tokens:
        return "functional_module_proxy", "Use module proxy until board area, channel count, latency, or firmware role is known."
    if {"bearing"} & tokens:
        return "catalog_geometry_load_class", "Scale by bore/OD/width/load/runout/lubrication environment."
    if {"gear", "gearbox", "worm"} & tokens:
        return "torque_ratio_catalog_scale", "Scale by torque, ratio, speed, lubrication, and backlash."
    if {"seal", "gasket", "insulation"} & tokens:
        return "interface_area_material_density", "Scale by perimeter/area and material class; verify leak/dielectric/temperature requirement."
    if {"window", "viewport", "lens"} & tokens:
        return "aperture_thickness_density", "Scale by aperture, thickness, glass density, and optical/thermal requirements."
    if {"bracket", "mount", "retainer", "spacer", "foot", "clamp", "tab"} & tokens:
        return "bounding_box_fill_factor", "Scale by envelope * density * fill factor; check load and interface tolerances."
    return "nominal_estimate_with_uncertainty", "Use current nominal estimate; refine when geometry/rating is selected."


def performance_tags(tokens: set[str], material_class: str | None = None) -> list[str]:
    tags: list[str] = []
    electrical_interface_tokens = {
        "busbar",
        "cable",
        "connector",
        "conductor",
        "feedthrough",
        "harness",
        "lead",
        "terminal",
    }
    if (
        {"hv", "voltage", "dielectric", "insulator", "bushing"} & tokens
        or electrical_interface_tokens & tokens
    ):
        tags.append("electrical_rating")
    if {"vacuum", "feedthrough", "seal", "viewport", "window", "cabin", "tank"} & tokens:
        tags.append("vacuum_leak_outgassing")
    if {"linear", "rotary", "axis", "encoder", "bearing", "screw", "guide", "gear", "motor"} & tokens:
        tags.append("precision_motion")
    if {"cathode", "anode", "electrode", "lens", "beam", "gun", "aperture"} & tokens:
        tags.append("electron_beam_geometry")
    if {"board", "sensor", "processor", "driver", "module", "rectifier", "capacitor", "inductor", "transformer"} & tokens:
        tags.append("electrical_function")
    if {"heat", "thermal", "cooling", "sink"} & tokens:
        tags.append("thermal_load")
    electronicish = material_class in {"electronic", "software"} or bool(
        electrical_interface_tokens & tokens
    )
    if (
        {"frame", "plate", "panel", "bracket", "mount", "clamp", "shaft"} & tokens
        and not electronicish
    ):
        tags.append("mechanical_stiffness_tolerance")
    return tags or ["general_fit"]


def mass_range(mass: float | None, tags: Iterable[str], basis: str) -> tuple[str, str]:
    if mass is None:
        return "", ""
    tag_set = set(tags)
    if {"electron_beam_geometry", "electrical_rating", "vacuum_leak_outgassing"} & tag_set:
        factor_low, factor_high = 0.33, 3.0
    elif "electrical_function" in tag_set or "precision_motion" in tag_set:
        factor_low, factor_high = 0.4, 2.5
    elif basis in {"area_thickness_density", "surface_area_wall_thickness_density", "bounding_box_fill_factor"}:
        factor_low, factor_high = 0.5, 2.0
    else:
        factor_low, factor_high = 0.5, 2.0
    return f"{mass * factor_low:.4g}", f"{mass * factor_high:.4g}"


def material_suggestion(tokens: set[str], material_class: str | None) -> tuple[str, str, str]:
    for required, material, alternates, note in MATERIAL_SUGGESTIONS:
        if all(token in tokens for token in required):
            return material, alternates, note
    if material_class in {"metal", "precision_metal", "vacuum_structural_metal"}:
        return "steel", "aluminum", "Default to steel for structural closure; switch to aluminum if mass/thermal benefit matters."
    if material_class == "ceramic":
        return "alumina_ceramic", "porcelain; fused_silica", "Select dielectric/thermal grade before recipe work."
    if material_class == "electronic":
        return "electronics_board_proxy", "imported_electronics", "Needs electronics readiness/import decision."
    if material_class == "composite":
        return "composite_placeholder", "split_into_materials", "Split or proxy if material mix affects closure."
    if material_class == "polymer":
        return "silicone_rubber", "other_kb_polymer", "Check vacuum/outgassing and temperature limits."
    if material_class:
        return material_class, "", "Current material_class is the starting point."
    return "unselected", "", "Material selection required before local recipe work."


def performance_checks(tags: Iterable[str]) -> str:
    labels = {
        "electrical_rating": "voltage/current/dielectric rating",
        "vacuum_leak_outgassing": "vacuum leak rate/outgassing",
        "precision_motion": "motion tolerance/load/lubrication",
        "electron_beam_geometry": "electron-beam geometry/thermal stability",
        "electrical_function": "circuit function/rating",
        "thermal_load": "thermal load/temperature rise",
        "mechanical_stiffness_tolerance": "stiffness/tolerance/interface fit",
        "general_fit": "basic function/material/scale",
    }
    return "; ".join(labels.get(tag, tag) for tag in tags)


def performance_requirement_value(item: dict, field: str) -> str:
    requirements = item.get("performance_requirements")
    if isinstance(requirements, dict):
        value = requirements.get(field)
        if isinstance(value, dict):
            return "; ".join(
                f"{key}={subvalue}"
                for key, subvalue in value.items()
                if subvalue not in {None, ""}
            )
        if value not in {None, ""}:
            return str(value)
    value = item.get(field)
    return "" if value in {None, ""} else str(value)


def implied_performance_requirements(tags: Iterable[str]) -> dict[str, str]:
    tag_set = set(tags)
    requirements = {field: "" for field in PERFORMANCE_REQUIREMENT_FIELDS}
    if {
        "precision_motion",
        "electron_beam_geometry",
        "mechanical_stiffness_tolerance",
    } & tag_set:
        requirements["tolerance"] = "review_required"
    if {
        "precision_motion",
        "electron_beam_geometry",
        "vacuum_leak_outgassing",
        "mechanical_stiffness_tolerance",
    } & tag_set:
        requirements["surface_finish"] = "review_required"
    if "vacuum_leak_outgassing" in tag_set:
        requirements["sealing_quality"] = "review_required"
    if {"precision_motion", "electron_beam_geometry"} & tag_set:
        requirements["alignment_accuracy"] = "review_required"
    return requirements


def find_candidate(tokens: set[str], items: dict[str, dict]) -> tuple[str, str, str, str]:
    for rule in CANDIDATE_RULES:
        if all(token in tokens for token in rule.tokens) and rule.candidate_id in items:
            candidate = items[rule.candidate_id]
            candidate_mass = mass_kg(candidate)
            return (
                rule.candidate_id,
                "" if candidate_mass is None else f"{candidate_mass:.4g}",
                rule.fit,
                rule.note,
            )
    return "", "", "none", "No same-level existing KB candidate found by rule."


def suggested_decision(
    candidate_id: str,
    candidate_fit: str,
    tags: list[str],
    tokens: set[str],
    material_class: str | None,
) -> str:
    high_fidelity = {
        "electron_beam_geometry",
        "electrical_rating",
        "vacuum_leak_outgassing",
        "precision_motion",
    }
    if "electron_beam_geometry" in tags or (
        {"feedthrough", "thermal", "imager"} & tokens
    ):
        return "needs_decomposition_or_dedicated_readiness"
    if candidate_fit == "likely_reuse" and not (high_fidelity & set(tags)):
        return "reuse_existing_review"
    if candidate_id:
        return "reuse_with_accuracy_risk"
    if material_class in {"metal", "precision_metal", "ceramic", "polymer"}:
        return "create_leaf_choose_material"
    return "needs_decomposition_or_import_decision"


def build_rows(root_id: str) -> list[dict[str, str]]:
    items = load_items()
    boms = load_boms()
    registered_decisions = load_replacement_register_decisions()
    reachable, parents = reachable_from(root_id, boms)
    rows: list[dict[str, str]] = []
    for item_id in sorted(reachable):
        if item_id == root_id or item_id in boms or not item_id.startswith("ebf3_"):
            continue
        item = items.get(item_id)
        if not item:
            continue
        token_set = tokens_for(item_id, item.get("name"))
        mass = mass_kg(item)
        tags = performance_tags(token_set, item.get("material_class"))
        basis, _scaling = mass_basis(token_set)
        mass_low, mass_high = mass_range(mass, tags, basis)
        material, material_alternates, material_note = material_suggestion(token_set, item.get("material_class"))
        candidate_id, candidate_mass, candidate_fit, candidate_note = find_candidate(token_set, items)
        decision = registered_decisions.get(
            item_id,
            suggested_decision(candidate_id, candidate_fit, tags, token_set, item.get("material_class")),
        )
        implied_requirements = implied_performance_requirements(tags)
        rows.append(
            {
                "item_id": item_id,
                "parent_ids": ";".join(sorted(parents.get(item_id, []))),
                "name": str(item.get("name", "")),
                "current_mass_kg": "" if mass is None else f"{mass:.4g}",
                "mass_low_kg": mass_low,
                "mass_high_kg": mass_high,
                "unit": str(item.get("unit", "")),
                "unit_kind": str(item.get("unit_kind", "")),
                "material_class": str(item.get("material_class", "")),
                "material_candidate": material,
                "material_alternates": material_alternates,
                "material_note": material_note,
                "performance_checks": performance_checks(tags),
                **{
                    field: performance_requirement_value(item, field)
                    or implied_requirements[field]
                    for field in PERFORMANCE_REQUIREMENT_FIELDS
                },
                "existing_candidate": candidate_id,
                "candidate_mass_kg": candidate_mass,
                "candidate_fit": candidate_fit,
                "candidate_note": candidate_note,
                "suggested_decision": decision,
                "item_path": str(item.get("_path", "")),
            }
        )
    return rows


def write_csv(rows: list[dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else []
    with output_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root-id", default="ebf3_3d_printer")
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = build_rows(args.root_id)
    write_csv(rows, args.csv)
    print(f"Wrote {len(rows)} rows to {args.csv.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
