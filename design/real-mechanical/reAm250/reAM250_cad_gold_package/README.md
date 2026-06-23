# reAM250 CAD Gold Package

This package contains the cleaned reAM250 BOM-to-CAD mapping for research queue work.

## Files

- `reAm250_BOM_gold.csv` - gold BOM, one row per research item.
- `gold_export/manifest.csv` - authoritative BOM-to-CAD mapping, one row per gold BOM row.
- `gold_export/parts/` - canonical part STEP files where available.
- `gold_export/assemblies/` - full-machine and context assembly STEP files.
- `gold_export/instances/` - alternate candidate instance STEP files only.
- `gold_export/reports/export_summary.md` - export summary and known limitations.
- `gold_export/reports/missing_or_suspicious_items.md` - details on assembly-only, ambiguous, and missing CAD rows.

## Use

Use `reAm250_BOM_gold.csv` as the source of research rows. Join each row to `gold_export/manifest.csv` using `source_row_number`, `item`, and `cad_file`. Do not use the older `enrichment/exported_parts` directory as the primary CAD source.

`canonical_step_path` and `alternate_step_paths` in `gold_export/manifest.csv` are relative to this package root.

## Export Status Summary

- 401 BOM rows processed.
- 389 exact part files matched into `gold_export/parts/`.
- 9 `assembly_only` rows.
- 2 `ambiguous` rows.
- 1 `missing_in_cad` row.
- `2AP6_outer_seal` is `missing_in_cad`.
- `2AP6_inner_seal` is mapped separately.

For research tasks, treat `assembly_only`, `ambiguous`, and `missing_in_cad` rows as limited CAD evidence and explain the limitation in the result.
