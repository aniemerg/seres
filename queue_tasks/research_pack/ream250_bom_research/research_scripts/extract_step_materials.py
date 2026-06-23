#!/usr/bin/env python3
"""Extract product material metadata from a STEP assembly file.

This is intentionally small and STEP-text oriented. It targets the AP214-style
material properties exported in the reAM250 gold package, where product
definitions have PROPERTY_DEFINITION entries for "material name" and
"density of part".
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, Iterable, List


ENTITY_RE = re.compile(r"#(\d+)\s*=\s*(.*?);", re.DOTALL)
REF_RE = re.compile(r"#(\d+)")
STRING_RE = re.compile(r"'((?:[^']|'')*)'")
POSITIVE_RATIO_RE = re.compile(r"POSITIVE_RATIO_MEASURE\(([-+0-9.Ee]+)\)")


def load_entities(path: Path) -> Dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    return {match.group(1): normalize(match.group(2)) for match in ENTITY_RE.finditer(text)}


def normalize(value: str) -> str:
    return " ".join(value.split())


def step_strings(entity: str) -> List[str]:
    return [value.replace("''", "'") for value in STRING_RE.findall(entity)]


def refs(entity: str) -> List[str]:
    return REF_RE.findall(entity)


def first_ref(entity: str) -> str | None:
    found = refs(entity)
    return found[0] if found else None


def find_product_definitions(entities: Dict[str, str], product_name: str) -> List[str]:
    needle = product_name.lower()
    matches: List[str] = []
    for entity_id, body in entities.items():
        if not body.startswith("PRODUCT_DEFINITION("):
            continue
        strings = [value.lower() for value in step_strings(body)]
        if any(needle == value or needle in value for value in strings):
            matches.append(entity_id)
    return matches


def property_definitions(
    entities: Dict[str, str], product_definition_id: str, property_label: str
) -> Iterable[str]:
    wanted_ref = f"#{product_definition_id}"
    for entity_id, body in entities.items():
        if not body.startswith("PROPERTY_DEFINITION("):
            continue
        strings = [value.lower() for value in step_strings(body)]
        if len(strings) < 2:
            continue
        if strings[0] == "material property" and strings[1] == property_label:
            if refs(body)[-1:] == [product_definition_id] or wanted_ref in body:
                yield entity_id


def representation_for_property(entities: Dict[str, str], property_definition_id: str) -> str | None:
    for body in entities.values():
        if not body.startswith("PROPERTY_DEFINITION_REPRESENTATION("):
            continue
        entity_refs = refs(body)
        if len(entity_refs) >= 2 and entity_refs[0] == property_definition_id:
            return entity_refs[1]
    return None


def representation_item(entities: Dict[str, str], representation_id: str | None) -> str | None:
    if not representation_id:
        return None
    body = entities.get(representation_id)
    if not body or not body.startswith("REPRESENTATION("):
        return None
    entity_refs = refs(body)
    return entity_refs[0] if entity_refs else None


def descriptive_value(entities: Dict[str, str], item_id: str | None) -> str | None:
    if not item_id:
        return None
    body = entities.get(item_id, "")
    values = step_strings(body)
    return values[0] if values else None


def density_value(entities: Dict[str, str], item_id: str | None) -> float | None:
    if not item_id:
        return None
    body = entities.get(item_id, "")
    match = POSITIVE_RATIO_RE.search(body)
    if not match:
        return None
    return float(match.group(1))


def extract_for_product(entities: Dict[str, str], product_name: str) -> List[dict]:
    results: List[dict] = []
    for product_definition_id in find_product_definitions(entities, product_name):
        material_prop_ids = list(
            property_definitions(entities, product_definition_id, "material name")
        )
        density_prop_ids = list(
            property_definitions(entities, product_definition_id, "density of part")
        )
        material_repr = representation_for_property(
            entities, material_prop_ids[0]
        ) if material_prop_ids else None
        density_repr = representation_for_property(
            entities, density_prop_ids[0]
        ) if density_prop_ids else None
        material_item = representation_item(entities, material_repr)
        density_item = representation_item(entities, density_repr)
        results.append(
            {
                "product_definition_id": f"#{product_definition_id}",
                "material_property_id": f"#{material_prop_ids[0]}" if material_prop_ids else None,
                "density_property_id": f"#{density_prop_ids[0]}" if density_prop_ids else None,
                "material": descriptive_value(entities, material_item),
                "density": density_value(entities, density_item),
                "density_unit_note": "STEP positive ratio measure; reAM250 export uses kg/m^3-like material densities",
            }
        )
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract STEP material metadata for one product")
    parser.add_argument("--step", required=True, type=Path, help="STEP assembly path")
    parser.add_argument("--product-name", required=True, help="Product name to match")
    args = parser.parse_args()

    entities = load_entities(args.step)
    results = extract_for_product(entities, args.product_name)
    print(json.dumps({"product_name": args.product_name, "matches": results}, indent=2))
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
