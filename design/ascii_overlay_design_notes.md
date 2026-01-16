# ASCII Overlay Design Notes (Image + Table)

Goal: Render a Unicode/ASCII image and overlay a table on top of it with precise positioning, while preserving colors for both layers.

## Core challenges to solve

1) Terminal geometry and layout planning
- How to detect terminal width/height reliably in Python (shutil.get_terminal_size or env vars)?
- How to handle unknown or very small terminals (fallback width, clipping)?
- How to define a "canvas" space so placement is stable and predictable?

2) Measuring strings that include ANSI color
- ANSI escape sequences do not take up visual width.
- We must compute visible width/height separately from raw string length.
- Need helpers to strip ANSI and calculate display width per line.
- Unicode width handling: some glyphs are double-width (full-width, CJK, emoji).

3) Positioning the image in the canvas
- Choose anchor points (top-left, center, bottom-right).
- Allow offsets (x, y) and alignment options.
- Decide whether image can be clipped or should be wrapped if larger than canvas.
- Ensure the image layer is rendered into the canvas buffer with color intact.

4) Table rendering and sizing
- Table width depends on content; need to render table first to know width/height.
- Table borders must be consistent with data width after color stripping.
- Table should support multiline cells and alignment.
- Table color should not leak into the image layer or vice versa.

5) Overlay logic (table over image)
- Overlay should happen in a buffer, not on terminal directly.
- Table must fully occlude the image under its footprint (no transparency, no bleed).
- Spaces inside the table are still table pixels and should overwrite image pixels.
- Background colors are out of scope; table uses only foreground color.

6) ANSI color boundaries
- When overlaying, color resets and reapplication must be correct per segment.
- ANSI codes apply forward until reset; overlay could break color spans.
- Need a strategy to store colored tokens at each cell rather than raw strings.
- Option: represent each cell as a "styled char" with fg/bg color data.

7) Unicode width and overlay grid
- Some characters take 2 columns (wide glyphs, e.g., certain emojis, CJK).
- If an image or table includes a wide glyph, it occupies two grid columns.
- Overlay logic must either:
  - replace both columns when writing a wide glyph, or
  - disallow wide glyphs in table content (safe mode).

8) Performance and complexity
- Building a full styled grid can be heavy for large canvases.
- Need to balance accuracy with speed for interactive output.
- Consider progressive rendering or a limited render region.

## Proposed rendering pipeline

1) Define canvas
- width, height from terminal or explicit config.
- Initialize a blank grid of cells.

2) Render image to grid
- Parse ANSI and Unicode into styled cells.
- Place the image at (x, y) in grid coordinates.
- Clip if image exceeds canvas bounds.

3) Render table to temporary grid
- Build table lines from content, measuring visible widths.
- Parse ANSI into styled cells for the table layer.

4) Overlay table on image grid
- For each table cell, write it into the main grid.
- Option: treat table spaces as transparent or opaque.
- Ensure color reset for each cell if using ANSI.

5) Serialize grid to terminal output
- Emit ANSI codes only when style changes (reduce noise).
- Reset at end of each line or at the end of output.

## Questions / decisions to resolve

- Table occlusion is opaque; all table cells overwrite the image.
- Background colors are not needed and can be excluded from the renderer.
- Wide glyph handling should support two modes:
  - Reject mode: table content must be single-width only; error on wide glyphs.
  - Flex mode: allow wide glyphs and reserve two columns when present.
- Multiple overlays are optional; start with a single table over an image.
- Placement should support both anchor presets (left/center/right) and explicit column/row offsets.
- Default config can use anchors, but explicit "top-left at (x,y)" should be allowed.

## Risks to track

- ANSI parsing errors causing color bleed.
- Incorrect width calculations due to wide glyphs.
- Table size exceeding canvas causing ugly clipping.
- Overlay alignment shifting due to mixed-width characters.

## Suggested utilities

- visible_width(str) -> int  (strip ANSI + measure Unicode width)
- parse_ansi(str) -> list[StyledToken]
- render_to_grid(tokens, x, y)
- overlay_grid(base, overlay, x, y)
- grid_to_ansi(grid) -> str
 - validate_single_width(str) -> bool  (reject mode)
 - expand_wide_glyphs(tokens) -> list[StyledToken]  (flex mode)

## Next steps

- Decide on a minimal prototype: fixed-width ASCII + no wide glyphs in tables.
- Implement ANSI-aware width calc + overlay for table over image.
- Validate with a sample image + small table.

## Clarifications added from feedback

- Table spaces are opaque (image should not show through).
- Avoid background colors; use foreground colors only.
- Allow explicit (x,y) positioning for image and table; anchors are optional defaults.
- Wide glyph handling: either replace both columns or disallow wide glyphs in table content.

## Code separation / extraction

If this renderer may become its own project, keep boundaries clean:

- Create a standalone module/package (e.g., `ascii_overlay/`) with no repo-specific imports.
- Define a minimal API surface: `render(image, table, config) -> str`.
- Keep ANSI parsing + grid rendering pure (no file I/O, no CLI).
- Add optional helpers for reading files or terminal size in a thin CLI wrapper.
- Keep data structures (tokens, grid, styles) independent of the simulation code.
- Prefer dependency-free implementation; if Unicode width handling is needed, consider an optional dependency.

This allows us to lift the module into a separate repo later with minimal changes.
