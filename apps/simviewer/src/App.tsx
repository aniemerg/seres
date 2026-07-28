import { useEffect, useMemo, useRef, useState, type CSSProperties, type ReactNode } from 'react'
import type {
  Article,
  ArticlesPayload,
  InventoryCheckpoint,
  InventoryDelta,
  KBEntitiesPayload,
  KBEntity,
  MachineAssignment,
  MachineSetsPayload,
  ProcessRun,
  QuantityMap,
  SimQueryData,
  SimData,
  Warnings,
} from './types'

type Route =
  | { view: 'home' }
  | { view: 'gantt' }
  | { view: 'recipes' }
  | { view: 'machines' }
  | { view: 'ebfissues' }
  | { view: 'wiki'; id?: string }
  | { view: 'kbsearch' }

const BAR_MIN_PX = 3
const ROW_HEIGHT = 28
const WIKI_HOME_ID = 'about_seres'
const EMPTY_EBF_ROUTE_AUDIT: EbfRouteAuditPayload = {
  summary: {
    total: 0,
    route_groups: {},
    route_decisions: {},
    simulation_import_mass_policy: {},
    availability_class: {},
    confidence: {},
    audit_verdict: {},
    severity: {},
    issue_type: {},
  },
  rows: [],
}
const EMPTY_EBF_PROCESS_ISSUES: EbfProcessIssuesPayload = {
  summary: {
    total: 0,
    worker_decision: {},
    policy: {},
    queue_reason: {},
    route_decision: {},
  },
  rows: [],
  sources: {},
}
type ColorMode = 'status' | 'process' | 'recipe' | 'goal'
type MachineCatalogFilter = 'all' | 'ready' | 'audit' | 'target' | 'used' | 'seeded' | 'produced' | 'unused'
type MachineCatalogSort = 'usage' | 'name'
type KBSearchTypeFilter = 'all' | 'process' | 'machine' | 'recipe' | 'bom' | 'item' | 'article'

type MachineCatalogRow = {
  id: string
  label: string
  path: string
  family: string
  capabilities: string[]
  auditTags: string[]
  recipeId: string | null
  bomId: string | null
  massLabel: string
  runCount: number
  busyHours: number
  utilizationPercent: number
  totalEnergyKwh: number
  reservedCount: number
  supportedProcessCount: number
  isTarget: boolean
  isUsed: boolean
  isSeeded: boolean
  isProduced: boolean
  covered: boolean
  importedQuantity: number
  producedQuantity: number
}

type SupportedProcessRow = { id: string; name: string; relation: string }
type KBSearchRow = {
  id: string
  label: string
  type: string
  path: string
  searchableText: string
}
type EbfRouteAuditRow = {
  batch_id: string
  item_id: string
  parent_ids: string[]
  source_queue_type: string
  mass_nominal_kg: number | null
  material: string
  availability_class: string
  route_group: string
  route_decision: string
  primary_process_id: string
  secondary_process_ids: string[]
  ready_machine_ids: string[]
  blocked_machine_or_process_reason: string
  critical_performance_requirements: string
  simulation_import_mass_policy: string
  confidence: string
  flags: string[]
  reasoning_brief: string
  item_path: string
  audit_verdict: string
  proposed_decision: string
  proposed_policy: string
  severity: string
  issue_type: string
  semantic_reasoning: string
  recommended_edit: string
  integration_decision: string
  integration_note: string
}
type EbfRouteAuditPayload = {
  summary: {
    total: number
    route_groups: Record<string, number>
    route_decisions: Record<string, number>
    simulation_import_mass_policy: Record<string, number>
    availability_class: Record<string, number>
    confidence: Record<string, number>
    audit_verdict: Record<string, number>
    severity: Record<string, number>
    issue_type: Record<string, number>
    sources?: Record<string, string>
  }
  rows: EbfRouteAuditRow[]
}
type EbfProcessIssueRow = {
  priority: number | null
  queue_reason: string
  item_id: string
  policy: string
  route_decision: string
  mass_nominal_kg: number | null
  material: string
  availability_class: string
  confidence: string
  active_recipe_id: string
  recipe_exists: boolean
  current_process_ids: string[]
  process_paths: string
  current_machine_ids: string[]
  decision_machine_ids: string[]
  machine_selection_statuses: string[]
  machine_risk_flags: string[]
  machine_evidence_sources: string[]
  reasoning_brief: string
  item_path: string
  worker_task: string
  worker_decision: string
  worker_notes: string
}
type EbfProcessIssuesPayload = {
  summary: {
    total: number
    worker_decision: Record<string, number>
    policy: Record<string, number>
    queue_reason: Record<string, number>
    route_decision: Record<string, number>
  }
  rows: EbfProcessIssueRow[]
  sources: Record<string, string>
}
type BomTreeNode = {
  itemId: string
  name: string
  kind: string | null
  qty: number | null
  unit: string | null
  depth: number
  recipeId: string | null
  bomId: string | null
  childCount: number
  missingEntity: boolean
  cycle: boolean
  children: BomTreeNode[]
}
type BomTreeSummary = {
  uniqueItems: number
  bomCount: number
  leafOccurrences: number
  totalOccurrences: number
  missingEntities: number
  cycles: number
  maxDepth: number
}
type BomTreeBuildResult = {
  root: BomTreeNode
  summary: BomTreeSummary
}

const EBF3_BOM_TREE_ROOT_ID = 'ebf3_3d_printer'

const MACHINE_CATALOG_ALIASES = new Set([
  'resource_3d_printer_cartesian_v0_machine',
  'wire_arc_additive_machine',
])

const MACHINE_FAMILY_ORDER = [
  'Metal making / high-temp',
  'Additive manufacturing',
  'Metal forming / machining',
  'Mining / material prep',
  'Chemical / electrochemical',
  'Vacuum / gas / safety',
  'Assembly / robotics',
  'Power / energy',
  'Electronics / compute',
  'Metrology / lab',
  'Coating / fiber',
  'Support / other',
]

function parseRoute(hash: string): Route {
  const clean = hash.replace(/^#\/?/, '')
  const parts = clean.split('/').filter(Boolean)
  if (parts[0] === 'gantt') return { view: 'gantt' }
  if (parts[0] === 'recipes') return { view: 'recipes' }
  if (parts[0] === 'machines') return { view: 'machines' }
  if (parts[0] === 'ebf3-process-issues') return { view: 'ebfissues' }
  if (parts[0] === 'wiki') return { view: 'wiki', id: parts[1] }
  if (parts[0] === 'kb-search') return { view: 'kbsearch' }
  if (parts[0] === 'home') return { view: 'home' }
  return { view: 'wiki', id: WIKI_HOME_ID }
}

function hashTo(route: Route): string {
  if (route.view === 'gantt') return '#/gantt'
  if (route.view === 'recipes') return '#/recipes'
  if (route.view === 'machines') return '#/machines'
  if (route.view === 'ebfissues') return '#/ebf3-process-issues'
  if (route.view === 'wiki') return route.id ? `#/wiki/${route.id}` : `#/wiki/${WIKI_HOME_ID}`
  if (route.view === 'kbsearch') return '#/kb-search'
  return '#/home'
}

function formatQty(entry: { quantity: number; unit: string }): string {
  return `${entry.quantity.toFixed(2)} ${entry.unit}`
}

type MarkdownBlock =
  | { type: 'heading'; level: number; text: string }
  | { type: 'paragraph'; text: string }
  | { type: 'ul'; items: string[] }
  | { type: 'ol'; items: string[] }
  | { type: 'blockquote'; lines: string[] }
  | { type: 'hr' }
  | { type: 'table'; headers: string[]; rows: string[][] }
  | {
      type: 'simquery'
      queryType: 'table' | 'two-table'
      title?: string
      source?: string
      columns?: string[]
      left_source?: string
      right_source?: string
      left_title?: string
      right_title?: string
      left_columns?: string[]
      right_columns?: string[]
    }
  | { type: 'code'; lang: string; code: string }

function splitTableRow(line: string): string[] {
  let clean = line.trim()
  if (clean.startsWith('|')) clean = clean.slice(1)
  if (clean.endsWith('|')) clean = clean.slice(0, -1)
  return clean.split('|').map((c) => c.trim())
}

function isTableSeparator(line: string): boolean {
  const cells = splitTableRow(line)
  if (cells.length === 0) return false
  return cells.every((c) => /^:?-{3,}:?$/.test(c))
}

function parseInternalTarget(rawHref: string, validTargets: Set<string>): string | null {
  const href = rawHref.trim()
  if (!href) return null
  if (/^[a-zA-Z][a-zA-Z\d+.-]*:/.test(href)) return null
  if (href.startsWith('/')) return null

  const noHash = href.replace(/^#\/?/, '')
  if (noHash.startsWith('wiki/')) {
    const id = noHash.slice('wiki/'.length).trim()
    return validTargets.has(id) ? id : null
  }

  const candidate = noHash.replace(/^\.\/+/, '').replace(/\/+$/, '')
  return validTargets.has(candidate) ? candidate : null
}

function parseInlineArgs(raw: string): Record<string, string> {
  const out: Record<string, string> = {}
  const re = /([a-zA-Z_][a-zA-Z0-9_-]*)="([^"]*)"/g
  let match: RegExpExecArray | null
  while ((match = re.exec(raw)) !== null) out[match[1]] = match[2]
  return out
}

function formatScalarValue(value: unknown, format?: string, unit?: string): string {
  let rendered: string
  if (typeof value === 'number') {
    if (format?.startsWith('number:')) {
      const decimals = Number(format.split(':')[1] || '2')
      rendered = value.toFixed(Number.isFinite(decimals) ? decimals : 2)
    } else if (format === 'number') {
      rendered = value.toLocaleString()
    } else if (format === 'percent') {
      rendered = `${(value * 100).toFixed(2)}%`
    } else {
      rendered = String(value)
    }
  } else if (typeof value === 'boolean') {
    rendered = value ? 'true' : 'false'
  } else if (value === null || value === undefined) {
    rendered = ''
  } else {
    rendered = String(value)
  }
  return unit ? `${rendered} ${unit}` : rendered
}

function renderInlineMarkdown(
  text: string,
  onJump: (id: string) => void,
  validTargets: Set<string>,
  simQuery: SimQueryData | null,
): ReactNode[] {
  const out: ReactNode[] = []
  const re = /(\{\{\s*sim\.value\s+([^}]+)\}\}|\[\[([^\]]+)\]\]|\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`|\*\*\*([^*]+)\*\*\*|\*\*([^*]+)\*\*|__([^_]+)__|\*([^*]+)\*|_([^_]+)_|~~([^~]+)~~)/g
  let idx = 0
  let match: RegExpExecArray | null
  let nodeKey = 0

  const pushText = (start: number, end: number) => {
    if (end > start) out.push(<span key={`t-${nodeKey++}`}>{text.slice(start, end)}</span>)
  }

  while ((match = re.exec(text)) !== null) {
    pushText(idx, match.index)

    if (match[2]) {
      const args = parseInlineArgs(match[2])
      const scalarKey = args.key
      const value = scalarKey && simQuery ? simQuery.scalars[scalarKey] : undefined
      const rendered = scalarKey ? formatScalarValue(value, args.format, args.unit) : ''
      out.push(<span key={`sv-${nodeKey++}`} className="sim-inline-value">{rendered || `[unknown:${scalarKey ?? 'key'}]`}</span>)
    } else if (match[3]) {
      const target = match[3].trim()
      out.push(
        <button key={`w-${nodeKey++}`} className="wiki-link" onClick={() => onJump(target)}>
          {target}
        </button>,
      )
    } else if (match[4] && match[5]) {
      const internal = parseInternalTarget(match[5], validTargets)
      if (internal) {
        out.push(
          <button key={`il-${nodeKey++}`} className="wiki-link" onClick={() => onJump(internal)}>
            {match[4]}
          </button>,
        )
      } else {
        out.push(
          <a key={`a-${nodeKey++}`} className="md-link" href={match[5]} target="_blank" rel="noreferrer">
            {match[4]}
          </a>,
        )
      }
    } else if (match[6]) {
      out.push(<code key={`c-${nodeKey++}`}>{match[6]}</code>)
    } else if (match[7]) {
      out.push(<strong key={`b3-${nodeKey++}`}><em>{renderInlineMarkdown(match[7], onJump, validTargets, simQuery)}</em></strong>)
    } else if (match[8]) {
      out.push(<strong key={`b2-${nodeKey++}`}>{renderInlineMarkdown(match[8], onJump, validTargets, simQuery)}</strong>)
    } else if (match[9]) {
      out.push(<strong key={`bu-${nodeKey++}`}>{renderInlineMarkdown(match[9], onJump, validTargets, simQuery)}</strong>)
    } else if (match[10]) {
      out.push(<em key={`i1-${nodeKey++}`}>{renderInlineMarkdown(match[10], onJump, validTargets, simQuery)}</em>)
    } else if (match[11]) {
      out.push(<em key={`i2-${nodeKey++}`}>{renderInlineMarkdown(match[11], onJump, validTargets, simQuery)}</em>)
    } else if (match[12]) {
      out.push(<del key={`d-${nodeKey++}`}>{renderInlineMarkdown(match[12], onJump, validTargets, simQuery)}</del>)
    }

    idx = re.lastIndex
  }
  pushText(idx, text.length)
  return out
}

function parseListValue(raw: string | undefined): string[] | undefined {
  if (!raw) return undefined
  const trimmed = raw.trim()
  if (!trimmed.startsWith('[') || !trimmed.endsWith(']')) return undefined
  const body = trimmed.slice(1, -1).trim()
  if (!body) return []
  return body.split(',').map((p) => p.trim()).filter(Boolean)
}

function parseSimQueryBlock(lang: string, code: string): MarkdownBlock | null {
  if (!(lang === 'sim-query' || lang === 'sim-table')) return null
  const kv: Record<string, string> = {}
  for (const rawLine of code.split('\n')) {
    const line = rawLine.trim()
    if (!line || line.startsWith('#')) continue
    const idx = line.indexOf(':')
    if (idx <= 0) continue
    const key = line.slice(0, idx).trim()
    const value = line.slice(idx + 1).trim()
    kv[key] = value
  }

  const queryType = (kv.type || (lang === 'sim-table' ? 'table' : 'table')) as 'table' | 'two-table'
  if (queryType !== 'table' && queryType !== 'two-table') return null

  return {
    type: 'simquery',
    queryType,
    title: kv.title,
    source: kv.source,
    columns: parseListValue(kv.columns),
    left_source: kv.left_source,
    right_source: kv.right_source,
    left_title: kv.left_title,
    right_title: kv.right_title,
    left_columns: parseListValue(kv.left_columns),
    right_columns: parseListValue(kv.right_columns),
  }
}

function parseMarkdownBlocks(content: string): MarkdownBlock[] {
  const lines = content.replace(/\r\n/g, '\n').split('\n')
  const blocks: MarkdownBlock[] = []
  let i = 0

  while (i < lines.length) {
    const line = lines[i]
    if (!line.trim()) {
      i += 1
      continue
    }

    const codeFence = line.match(/^```([A-Za-z0-9_-]+)?\s*$/)
    if (codeFence) {
      const lang = codeFence[1] ?? ''
      i += 1
      const buf: string[] = []
      while (i < lines.length && !/^```/.test(lines[i])) {
        buf.push(lines[i])
        i += 1
      }
      if (i < lines.length) i += 1
      const simQueryBlock = parseSimQueryBlock(lang, buf.join('\n'))
      if (simQueryBlock) {
        blocks.push(simQueryBlock)
        continue
      }
      blocks.push({ type: 'code', lang, code: buf.join('\n') })
      continue
    }

    if (/^\s*---+\s*$/.test(line) || /^\s*\*\*\*+\s*$/.test(line)) {
      blocks.push({ type: 'hr' })
      i += 1
      continue
    }

    const heading = line.match(/^(#{1,6})\s+(.+)$/)
    if (heading) {
      blocks.push({ type: 'heading', level: heading[1].length, text: heading[2].trim() })
      i += 1
      continue
    }

    const blockquote = line.match(/^\s*>\s?(.*)$/)
    if (blockquote) {
      const rows: string[] = []
      while (i < lines.length) {
        const m = lines[i].match(/^\s*>\s?(.*)$/)
        if (!m) break
        rows.push(m[1])
        i += 1
      }
      blocks.push({ type: 'blockquote', lines: rows })
      continue
    }

    if (line.includes('|') && i + 1 < lines.length && isTableSeparator(lines[i + 1])) {
      const headers = splitTableRow(line)
      i += 2
      const rows: string[][] = []
      while (i < lines.length && lines[i].trim() && lines[i].includes('|')) {
        rows.push(splitTableRow(lines[i]))
        i += 1
      }
      blocks.push({ type: 'table', headers, rows })
      continue
    }

    const ul = line.match(/^\s*[-*]\s+(.+)$/)
    if (ul) {
      const items: string[] = []
      while (i < lines.length) {
        const m = lines[i].match(/^\s*[-*]\s+(.+)$/)
        if (!m) break
        items.push(m[1].trim())
        i += 1
      }
      blocks.push({ type: 'ul', items })
      continue
    }

    const ol = line.match(/^\s*\d+\.\s+(.+)$/)
    if (ol) {
      const items: string[] = []
      while (i < lines.length) {
        const m = lines[i].match(/^\s*\d+\.\s+(.+)$/)
        if (!m) break
        items.push(m[1].trim())
        i += 1
      }
      blocks.push({ type: 'ol', items })
      continue
    }

    const para: string[] = [line.trim()]
    i += 1
    while (i < lines.length) {
      const peek = lines[i]
      if (!peek.trim()) break
      if (
        /^```/.test(peek) ||
        /^(#{1,6})\s+/.test(peek) ||
        /^\s*[-*]\s+/.test(peek) ||
        /^\s*\d+\.\s+/.test(peek) ||
        /^\s*>\s?/.test(peek) ||
        /^\s*---+\s*$/.test(peek) ||
        /^\s*\*\*\*+\s*$/.test(peek) ||
        (peek.includes('|') && i + 1 < lines.length && isTableSeparator(lines[i + 1]))
      ) break
      para.push(peek.trim())
      i += 1
    }
    blocks.push({ type: 'paragraph', text: para.join(' ') })
  }

  return blocks
}

function renderSimTable(
  rows: Array<Record<string, unknown>>,
  columns: string[] | undefined,
  onJump: (id: string) => void,
  validTargets: Set<string>,
  simQuery: SimQueryData | null,
) {
  const cols = columns && columns.length > 0 ? columns : Object.keys(rows[0] ?? {})
  return (
    <div className="table-wrap">
      <table>
        <thead>
          <tr>{cols.map((h, i) => <th key={i}>{h}</th>)}</tr>
        </thead>
        <tbody>
          {rows.map((row, ridx) => (
            <tr key={ridx}>
              {cols.map((col) => {
                const val = row[col]
                if (typeof val === 'boolean') return <td key={col}>{val ? 'yes' : 'no'}</td>
                if (typeof val === 'number') return <td key={col}>{Number.isInteger(val) ? String(val) : val.toFixed(2)}</td>
                const text = val == null ? '' : String(val)
                if ((col === 'id' || col.endsWith('_id')) && validTargets.has(text)) {
                  return (
                    <td key={col}>
                      <button className="wiki-link" onClick={() => onJump(text)}>
                        {text}
                      </button>
                    </td>
                  )
                }
                return <td key={col}>{renderInlineMarkdown(text, onJump, validTargets, simQuery)}</td>
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

function MarkdownArticle({
  content,
  onJump,
  validTargets,
  simQuery,
}: {
  content: string
  onJump: (id: string) => void
  validTargets: Set<string>
  simQuery: SimQueryData | null
}) {
  const blocks = useMemo(() => parseMarkdownBlocks(content), [content])
  return (
    <article className="article">
      {blocks.map((b, idx) => {
        if (b.type === 'heading') {
          const tag = `h${Math.min(6, Math.max(1, b.level))}` as 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6'
          return tag === 'h1' ? (
            <h1 key={idx}>{renderInlineMarkdown(b.text, onJump, validTargets, simQuery)}</h1>
          ) : tag === 'h2' ? (
            <h2 key={idx}>{renderInlineMarkdown(b.text, onJump, validTargets, simQuery)}</h2>
          ) : tag === 'h3' ? (
            <h3 key={idx}>{renderInlineMarkdown(b.text, onJump, validTargets, simQuery)}</h3>
          ) : tag === 'h4' ? (
            <h4 key={idx}>{renderInlineMarkdown(b.text, onJump, validTargets, simQuery)}</h4>
          ) : tag === 'h5' ? (
            <h5 key={idx}>{renderInlineMarkdown(b.text, onJump, validTargets, simQuery)}</h5>
          ) : (
            <h6 key={idx}>{renderInlineMarkdown(b.text, onJump, validTargets, simQuery)}</h6>
          )
        }
        if (b.type === 'ul') return <ul key={idx}>{b.items.map((it, i) => <li key={i}>{renderInlineMarkdown(it, onJump, validTargets, simQuery)}</li>)}</ul>
        if (b.type === 'ol') return <ol key={idx}>{b.items.map((it, i) => <li key={i}>{renderInlineMarkdown(it, onJump, validTargets, simQuery)}</li>)}</ol>
        if (b.type === 'blockquote') return <blockquote key={idx}>{b.lines.map((l, i) => <p key={i}>{renderInlineMarkdown(l, onJump, validTargets, simQuery)}</p>)}</blockquote>
        if (b.type === 'hr') return <hr key={idx} />
        if (b.type === 'table') {
          return (
            <div key={idx} className="table-wrap">
              <table>
                <thead>
                  <tr>{b.headers.map((h, i) => <th key={i}>{renderInlineMarkdown(h, onJump, validTargets, simQuery)}</th>)}</tr>
                </thead>
                <tbody>
                  {b.rows.map((row, rIdx) => (
                    <tr key={rIdx}>
                      {b.headers.map((_, cIdx) => <td key={cIdx}>{renderInlineMarkdown(row[cIdx] ?? '', onJump, validTargets, simQuery)}</td>)}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )
        }
        if (b.type === 'simquery') {
          if (!simQuery) return <div key={idx} className="simquery-warning">SimQuery data unavailable.</div>
          if (b.queryType === 'table') {
            const rows = (b.source ? simQuery.tables[b.source] : null) ?? []
            return (
              <section key={idx} className="simquery-block">
                {b.title && <h3>{b.title}</h3>}
                {renderSimTable(rows, b.columns, onJump, validTargets, simQuery)}
              </section>
            )
          }
          const leftRows = (b.left_source ? simQuery.tables[b.left_source] : null) ?? []
          const rightRows = (b.right_source ? simQuery.tables[b.right_source] : null) ?? []
          return (
            <section key={idx} className="simquery-block">
              {b.title && <h3>{b.title}</h3>}
              <div className="sim-two-table">
                <div>
                  <h4>{b.left_title || b.left_source || 'Left'}</h4>
                  {renderSimTable(leftRows, b.left_columns, onJump, validTargets, simQuery)}
                </div>
                <div>
                  <h4>{b.right_title || b.right_source || 'Right'}</h4>
                  {renderSimTable(rightRows, b.right_columns, onJump, validTargets, simQuery)}
                </div>
              </div>
            </section>
          )
        }
        if (b.type === 'code') return <pre key={idx}><code>{b.code}</code></pre>
        return <p key={idx}>{renderInlineMarkdown(b.text, onJump, validTargets, simQuery)}</p>
      })}
    </article>
  )
}

function hashColor(input: string): string {
  let h = 0
  for (let i = 0; i < input.length; i += 1) h = (h * 31 + input.charCodeAt(i)) >>> 0
  const hue = h % 360
  return `hsl(${hue} 62% 52%)`
}

function runColor(run: ProcessRun, mode: ColorMode): string {
  if (mode === 'status') {
    if (run.status === 'failed') return '#d55a5a'
    if (run.status === 'pending') return '#a2a2a2'
    return '#74d16a'
  }
  if (mode === 'process') return hashColor(run.process_id || 'process')
  if (mode === 'goal') {
    const tags = getGoalTags(run)
    const goalMachine = tags['goal.machine_id']
    if (goalMachine) return hashColor(goalMachine.split('|')[0].trim() || 'goal-machine')
    const goalRecipe = tags['goal.recipe_id']
    if (goalRecipe) return hashColor(goalRecipe)
    return hashColor(run.recipe_id || run.recipe_run_id || run.process_id || 'goal')
  }
  return hashColor(run.recipe_id || run.recipe_run_id || 'recipe')
}

function getGoalTags(run: ProcessRun): Record<string, string> {
  const ctx = asObject(run.goal_context)
  if (!ctx) return {}
  const tags = asObject(ctx.tags)
  if (!tags) return {}
  const out: Record<string, string> = {}
  for (const [k, v] of Object.entries(tags)) {
    if (typeof v === 'string' || typeof v === 'number' || typeof v === 'boolean') {
      out[k] = String(v)
    }
  }
  return out
}

function asObject(v: unknown): Record<string, unknown> | null {
  return v && typeof v === 'object' && !Array.isArray(v) ? (v as Record<string, unknown>) : null
}

function asArray(v: unknown): unknown[] {
  return Array.isArray(v) ? v : []
}

function isRecipeEntity(entity: KBEntity): boolean {
  return entity.kind === 'recipe' || entity.id.startsWith('recipe_')
}

function isBomEntity(entity: KBEntity): boolean {
  return entity.kind === 'bom' || entity.id.startsWith('bom_')
}

function isProcessEntity(entity: KBEntity): boolean {
  return entity.kind === 'process'
}

function isMachineEntity(entity: KBEntity): boolean {
  return entity.kind === 'machine'
}

function stringField(obj: Record<string, unknown> | undefined, key: string): string | null {
  const value = obj?.[key]
  if (typeof value === 'string' && value.trim()) return value.trim()
  return null
}

function numberField(obj: Record<string, unknown> | undefined, key: string): number {
  const value = obj?.[key]
  return typeof value === 'number' && Number.isFinite(value) ? value : 0
}

function stringArrayField(obj: Record<string, unknown> | undefined, key: string): string[] {
  const value = obj?.[key]
  if (!Array.isArray(value)) return []
  return value
    .map((entry) => (typeof entry === 'string' ? entry.trim() : ''))
    .filter(Boolean)
}

function textField(obj: Record<string, unknown> | undefined, key: string): string {
  const value = obj?.[key]
  return typeof value === 'string' ? value.trim() : ''
}

function stringListFromField(obj: Record<string, unknown> | undefined, key: string): string[] {
  const value = obj?.[key]
  if (Array.isArray(value)) {
    return value
      .map((entry) => {
        if (typeof entry === 'string') return entry.trim()
        if (entry && typeof entry === 'object') return JSON.stringify(entry)
        return ''
      })
      .filter(Boolean)
  }
  if (typeof value === 'string' && value.trim()) return [value.trim()]
  return []
}

function getMachineAuditTags(raw: Record<string, unknown> | undefined): string[] {
  return stringListFromField(raw, 'trust_tags').filter((tag) => tag.startsWith('machine_audit_'))
}

function formatMachineAuditTag(tag: string): string {
  return tag.replace(/^machine_audit_/, '').replace(/_/g, ' ')
}

function tableById(rows: Array<Record<string, unknown>> | undefined): Map<string, Record<string, unknown>> {
  const out = new Map<string, Record<string, unknown>>()
  for (const row of rows ?? []) {
    const id = stringField(row, 'id')
    if (id) out.set(id, row)
  }
  return out
}

function inferMachineFamily(entity: KBEntity): string {
  const raw = entity.raw
  const text = [
    entity.id,
    entity.name,
    ...(stringArrayField(raw, 'capabilities')),
  ].join(' ').toLowerCase().replace(/[-_]/g, ' ')

  const rules: Array<[string, string[]]> = [
    ['Additive manufacturing', ['ebf3', 'ebam', 'electron beam freeform', 'electron beam additive', 'wire feed metal deposition', 'selective solar sinter', 'fresnel solar sinter', 'solar thermal melting', 'regolith sinter', 'fdm', 'fff', 'fused deposition', '3d printer', '3d print', 'polymer printing', 'silicone plastic printing', 'ceramic glass precursor', 'additive']],
    ['Metal making / high-temp', ['furnace', 'kiln', 'oven', 'anneal', 'sinter', 'smelt', 'casting', 'crucible', 'quench', 'pyrolysis', 'reduction', 'heating', 'forge']],
    ['Metal forming / machining', ['fabrication', 'machin', 'mill', 'lathe', 'grind', 'cutting', 'saw', 'press', 'forming', 'bending', 'rolling', 'welding', 'welder', 'molding', 'extruder', 'die set']],
    ['Mining / material prep', ['crusher', 'screen', 'feeder', 'conveyor', 'loader', 'hauler', 'drill', 'separator', 'beneficiation', 'regolith', 'ball mill', 'powder']],
    ['Assembly / robotics', ['assembly', 'assembler', 'robot', 'gantry', 'scara', 'delta', 'gripper', 'constructor', 'labor bot', 'workbench', 'fixtur']],
    ['Chemical / electrochemical', ['chemical', 'reactor', 'acid', 'electroly', 'distillation', 'leaching', 'bath', 'mixer', 'filtration', 'ammonia', 'carbonyl', 'co2']],
    ['Vacuum / gas / safety', ['vacuum', 'gas', 'atmosphere', 'inert', 'chiller', 'cryo', 'cold trap', 'condenser', 'compressor', 'safety', 'scrubbing']],
    ['Power / energy', ['solar', 'power', 'battery', 'thermionic', 'heat pipe', 'heat transport', 'storage', 'generator', 'converter', 'inverter']],
    ['Electronics / compute', ['pcb', 'circuit', 'solder', 'electronic', 'compute', 'computer', 'memory', 'neural', 'signal generator', 'oscilloscope', 'antenna', 'communication']],
    ['Metrology / lab', ['measurement', 'metrology', 'calibration', 'inspection', 'test', 'spectrometer', 'microscope', 'sensor', 'temperature', 'load cell', 'lab', 'analysis', 'quality', 'alignment']],
    ['Coating / fiber', ['coating', 'surface treatment', 'encapsulation', 'spin coating', 'fiber', 'spinning', 'winding', 'tension', 'cleaning']],
  ]

  for (const [family, keywords] of rules) {
    if (keywords.some((keyword) => text.includes(keyword))) return family
  }
  return 'Support / other'
}

function formatMachineMass(raw: Record<string, unknown> | undefined): string {
  const mass = numberField(raw, 'mass_kg') || numberField(raw, 'mass')
  if (!mass) return 'n/a'
  if (mass >= 1000) return `${(mass / 1000).toFixed(1)} t`
  if (mass >= 10) return `${mass.toFixed(0)} kg`
  return `${mass.toFixed(2)} kg`
}

function getMachineSupportedProcessRows(entity: KBEntity, allEntities: KBEntity[]): SupportedProcessRow[] {
  if (!isMachineEntity(entity)) return []
  const machineRaw = asObject(entity.raw) ?? undefined
  const listedProcessIds = new Set(stringListFromField(machineRaw, 'processes_supported'))
  const rows: SupportedProcessRow[] = []

  for (const candidate of allEntities) {
    if (!isProcessEntity(candidate)) continue
    const processRaw = asObject(candidate.raw)
    const requiredByProcess = asArray(processRaw?.resource_requirements).some((req) => {
      const obj = asObject(req)
      return obj?.machine_id === entity.id
    })
    const listedByMachine = listedProcessIds.has(candidate.id)
    if (!requiredByProcess && !listedByMachine) continue
    const relation = [
      requiredByProcess ? 'resource requirement' : '',
      listedByMachine ? 'listed on machine' : '',
    ].filter(Boolean).join(', ')
    rows.push({ id: candidate.id, name: candidate.name || candidate.id, relation })
  }

  for (const processId of listedProcessIds) {
    if (rows.some((row) => row.id === processId)) continue
    rows.push({ id: processId, name: processId, relation: 'listed on machine' })
  }

  return rows.sort((a, b) => a.name.localeCompare(b.name) || a.id.localeCompare(b.id))
}

function getBomOwnerItemId(entity: KBEntity): string | null {
  if (!isBomEntity(entity)) return null
  const raw = asObject(entity.raw)
  return stringField(raw ?? undefined, 'owner_item_id')
    ?? stringField(raw ?? undefined, 'target_item_id')
    ?? (entity.id.startsWith('bom_') ? entity.id.slice(4) : null)
}

function buildBomOwnerIndex(allEntities: KBEntity[]): Map<string, KBEntity> {
  const out = new Map<string, KBEntity>()
  for (const candidate of allEntities) {
    if (!isBomEntity(candidate)) continue
    const ownerItemId = getBomOwnerItemId(candidate)
    if (!ownerItemId || out.has(ownerItemId)) continue
    out.set(ownerItemId, candidate)
  }
  return out
}

function getBomTreeRootItemId(entity: KBEntity | undefined): string | null {
  if (!entity) return null
  const itemId = isBomEntity(entity) ? getBomOwnerItemId(entity) : entity.id
  if (!itemId) return null
  if (itemId === EBF3_BOM_TREE_ROOT_ID || itemId.startsWith('ebf3_') || entity.id.startsWith('bom_ebf3_')) {
    return EBF3_BOM_TREE_ROOT_ID
  }
  return itemId
}

function getBomTreeSelectedItemId(entity: KBEntity | undefined): string | null {
  if (!entity) return null
  if (isBomEntity(entity)) return getBomOwnerItemId(entity)
  return entity.id
}

function formatBomTreeQty(qty: number | null): string {
  if (qty === null) return 'root'
  if (!Number.isFinite(qty)) return 'n/a'
  if (Number.isInteger(qty)) return String(qty)
  return String(Number(qty.toFixed(4)))
}

function formatEntryMass(raw: Record<string, unknown> | null): string | null {
  if (!raw) return null
  const mass = raw.mass_kg ?? raw.mass
  if (typeof mass === 'number' && Number.isFinite(mass)) return `${formatBomTreeQty(mass)} kg`
  if (typeof mass === 'string' && mass.trim()) return mass.trim()
  return null
}

function formatEntryMaterial(raw: Record<string, unknown> | null): string | null {
  if (!raw) return null
  const value = raw.material ?? raw.material_class
  if (typeof value === 'string' && value.trim()) return value.trim()
  if (Array.isArray(value)) {
    const entries = value.map((entry) => String(entry).trim()).filter(Boolean)
    return entries.length > 0 ? entries.join(', ') : null
  }
  return null
}

function formatEntryImportStatus(entity: KBEntity | undefined, raw: Record<string, unknown> | null): string {
  if (!entity || !raw) return 'not listed'
  const policy = typeof raw.simulation_import_mass_policy === 'string' ? raw.simulation_import_mass_policy.trim() : ''
  if (policy === 'import_nominal') return 'yes (import nominal)'
  if (policy === 'import_until_gap_resolved') return 'yes (import until gap resolved)'
  if (raw.is_import === true || entity.path.startsWith('kb/imports/')) return 'yes'
  return 'no'
}

function buildBomTree(rootItemId: string, allEntities: KBEntity[], entitiesById: Record<string, KBEntity>): BomTreeBuildResult | null {
  const bomByOwner = buildBomOwnerIndex(allEntities)
  if (!bomByOwner.has(rootItemId)) return null

  const uniqueItems = new Set<string>()
  const bomIds = new Set<string>()
  const summary: BomTreeSummary = {
    uniqueItems: 0,
    bomCount: 0,
    leafOccurrences: 0,
    totalOccurrences: 0,
    missingEntities: 0,
    cycles: 0,
    maxDepth: 0,
  }

  const visit = (
    itemId: string,
    qty: number | null,
    unit: string | null,
    depth: number,
    ancestors: string[],
  ): BomTreeNode => {
    const entity = entitiesById[itemId]
    const entityRaw = asObject(entity?.raw)
    const isCycle = ancestors.includes(itemId)
    const bom = bomByOwner.get(itemId)
    const bomRaw = asObject(bom?.raw)

    uniqueItems.add(itemId)
    summary.totalOccurrences += 1
    summary.maxDepth = Math.max(summary.maxDepth, depth)
    if (!entity) summary.missingEntities += 1
    if (isCycle) summary.cycles += 1
    if (bom) bomIds.add(bom.id)

    const components = !isCycle ? asArray(bomRaw?.components) : []
    const children = components
      .map((component) => {
        const obj = asObject(component)
        const childItemId = typeof obj?.item_id === 'string' ? obj.item_id.trim() : ''
        if (!childItemId) return null
        const childQtyRaw = obj?.qty ?? obj?.quantity ?? obj?.amount
        const childQty = typeof childQtyRaw === 'number' && Number.isFinite(childQtyRaw) ? childQtyRaw : 0
        const childUnit = typeof obj?.unit === 'string' && obj.unit.trim() ? obj.unit.trim() : 'unit'
        return visit(childItemId, childQty, childUnit, depth + 1, [...ancestors, itemId])
      })
      .filter((node): node is BomTreeNode => Boolean(node))

    if (children.length === 0) summary.leafOccurrences += 1

    return {
      itemId,
      name: entity?.name || itemId,
      kind: entity?.kind ?? null,
      qty,
      unit,
      depth,
      recipeId: typeof entityRaw?.recipe === 'string' ? entityRaw.recipe : null,
      bomId: bom?.id ?? null,
      childCount: children.length,
      missingEntity: !entity,
      cycle: isCycle,
      children,
    }
  }

  const root = visit(rootItemId, null, null, 0, [])
  summary.uniqueItems = uniqueItems.size
  summary.bomCount = bomIds.size
  return { root, summary }
}

function countBomTreeDescendants(node: BomTreeNode): number {
  return node.children.reduce((total, child) => total + 1 + countBomTreeDescendants(child), 0)
}

function formatBomVisualLabel(itemId: string): string {
  return itemId
    .replace(/^ebf3_/, '')
    .replace(/^gun_/, '')
    .replace(/_/g, ' ')
}

function bomTreeContainsItem(node: BomTreeNode, itemId: string | null): boolean {
  if (!itemId) return false
  if (node.itemId === itemId) return true
  return node.children.some((child) => bomTreeContainsItem(child, itemId))
}

function findBomTreeL1ForItem(root: BomTreeNode, itemId: string | null): string | null {
  if (!itemId || root.itemId === itemId) return null
  return root.children.find((child) => bomTreeContainsItem(child, itemId))?.itemId ?? null
}

function collectRefIds(node: unknown, out: Set<string>): void {
  if (Array.isArray(node)) {
    for (const entry of node) collectRefIds(entry, out)
    return
  }
  if (!node || typeof node !== 'object') return
  const obj = node as Record<string, unknown>
  for (const [key, value] of Object.entries(obj)) {
    if (key === 'item_id' || key === 'machine_id' || key === 'process_id' || key === 'recipe_id' || key === 'target_item_id' || key === 'owner_item_id') {
      if (typeof value === 'string' && value.trim()) out.add(value.trim())
      continue
    }
    if ((key === 'requires_ids' || key === 'requires_id') && Array.isArray(value)) {
      for (const v of value) if (typeof v === 'string' && v.trim()) out.add(v.trim())
      continue
    }
    collectRefIds(value, out)
  }
}

function stringifyForSearch(value: unknown, omittedKeys = new Set<string>()): string {
  if (value === null || value === undefined) return ''
  if (typeof value === 'string' || typeof value === 'number' || typeof value === 'boolean') return String(value)
  if (Array.isArray(value)) return value.map((entry) => stringifyForSearch(entry, omittedKeys)).join(' ')
  if (typeof value === 'object') {
    return Object.entries(value as Record<string, unknown>)
      .filter(([key]) => !omittedKeys.has(key))
      .map(([key, entry]) => `${key} ${stringifyForSearch(entry, omittedKeys)}`)
      .join(' ')
  }
  return ''
}

function normalizeKbSearchType(kind: string): KBSearchTypeFilter | 'material' | 'part' | 'resource' {
  if (kind === 'process' || kind === 'machine' || kind === 'recipe' || kind === 'bom' || kind === 'article') return kind
  if (kind === 'part' || kind === 'material' || kind === 'resource') return kind
  return 'item'
}

function matchesKbTypeFilter(row: KBSearchRow, filter: KBSearchTypeFilter): boolean {
  if (filter === 'all') return true
  const normalized = normalizeKbSearchType(row.type)
  if (filter === 'item') return normalized === 'item' || normalized === 'part' || normalized === 'material' || normalized === 'resource'
  return normalized === filter
}

function kbTypeSortWeight(kind: string): number {
  const normalized = normalizeKbSearchType(kind)
  if (normalized === 'process') return 0
  if (normalized === 'machine') return 1
  if (normalized === 'recipe') return 2
  if (normalized === 'part' || normalized === 'material' || normalized === 'resource' || normalized === 'item') return 3
  if (normalized === 'bom') return 4
  if (normalized === 'article') return 5
  return 9
}

function scoreKbSearchRow(row: KBSearchRow, terms: string[]): number {
  const id = row.id.toLowerCase()
  const label = row.label.toLowerCase()
  const path = row.path.toLowerCase()
  const text = row.searchableText.toLowerCase()
  let score = 0
  for (const term of terms) {
    if (id === term) score += 1200
    else if (id.startsWith(term)) score += 700
    else if (id.includes(term)) score += 360

    if (label === term) score += 900
    else if (label.startsWith(term)) score += 600
    else if (label.includes(term)) score += 420

    if (row.type.toLowerCase().includes(term)) score += 180
    if (path.includes(term)) score += 90
    if (text.includes(term)) score += 60
  }
  score -= kbTypeSortWeight(row.type) * 8
  return score
}

export function App() {
  const [route, setRoute] = useState<Route>(() => parseRoute(window.location.hash || `#/wiki/${WIKI_HOME_ID}`))
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)
  const [simData, setSimData] = useState<SimData | null>(null)
  const [simQuery, setSimQuery] = useState<SimQueryData | null>(null)
  const [machineSets, setMachineSets] = useState<MachineSetsPayload>({ sets: [] })
  const [ebfRouteAudit, setEbfRouteAudit] = useState<EbfRouteAuditPayload>(EMPTY_EBF_ROUTE_AUDIT)
  const [ebfProcessIssues, setEbfProcessIssues] = useState<EbfProcessIssuesPayload>(EMPTY_EBF_PROCESS_ISSUES)
  const [entities, setEntities] = useState<KBEntity[]>([])
  const [articles, setArticles] = useState<Article[]>([])
  const [warnings, setWarnings] = useState<Warnings | null>(null)
  const [selectedRunId, setSelectedRunId] = useState<string | null>(null)
  const [selectedRunSource, setSelectedRunSource] = useState<'timeline' | 'recipes' | null>(null)
  const [selectedTimeHours, setSelectedTimeHours] = useState<number | null>(null)
  const [zoom, setZoom] = useState(0.28)
  const [colorMode, setColorMode] = useState<ColorMode>('process')
  const [search, setSearch] = useState('')

  useEffect(() => {
    const onHash = () => setRoute(parseRoute(window.location.hash || `#/wiki/${WIKI_HOME_ID}`))
    window.addEventListener('hashchange', onHash)
    return () => window.removeEventListener('hashchange', onHash)
  }, [])

  useEffect(() => {
    Promise.all([
      fetch('./data/sim_data.json').then((r) => r.json() as Promise<SimData>),
      fetch('./data/kb_entities.json').then((r) => r.json() as Promise<KBEntitiesPayload>),
      fetch('./data/articles.json').then((r) => r.json() as Promise<ArticlesPayload>),
      fetch('./data/warnings.json').then((r) => r.json() as Promise<Warnings>),
      fetch('./data/simquery.json').then((r) => r.json() as Promise<SimQueryData>).catch(() => null),
      fetch('./data/machine_sets.json').then((r) => r.json() as Promise<MachineSetsPayload>).catch(() => ({ sets: [] })),
      fetch('./data/ebf3_route_audit.json').then((r) => r.json() as Promise<EbfRouteAuditPayload>).catch(() => EMPTY_EBF_ROUTE_AUDIT),
      fetch('./data/ebf3_process_issue_review.json').then((r) => r.json() as Promise<EbfProcessIssuesPayload>).catch(() => EMPTY_EBF_PROCESS_ISSUES),
    ])
      .then(([sim, kb, art, warn, query, sets, routeAudit, processIssues]) => {
        setSimData(sim)
        setEntities(kb.entities)
        setArticles(art.articles)
        setWarnings(warn)
        setSimQuery(query)
        setMachineSets(sets)
        setEbfRouteAudit(routeAudit)
        setEbfProcessIssues(processIssues)
      })
      .catch((err) => {
        console.error(err)
      })
  }, [])

  const entitiesById = useMemo(() => Object.fromEntries(entities.map((e) => [e.id, e])), [entities])
  const articlesById = useMemo(() => Object.fromEntries(articles.map((a) => [a.id, a])), [articles])
  const markdownTargets = useMemo(() => new Set<string>([...entities.map((e) => e.id), ...articles.map((a) => a.id)]), [entities, articles])
  const kbBacklinks = useMemo(() => {
    const map = new Map<string, Array<{ id: string; name: string; kind: string }>>()
    for (const entity of entities) {
      const refs = new Set<string>()
      collectRefIds(entity.raw, refs)
      refs.delete(entity.id)
      for (const target of refs) {
        const list = map.get(target) ?? []
        list.push({ id: entity.id, name: entity.name || entity.id, kind: entity.kind })
        map.set(target, list)
      }
    }
    for (const article of articles) {
      for (const target of article.wiki_links ?? []) {
        const list = map.get(target) ?? []
        list.push({ id: article.id, name: article.title || article.id, kind: 'article' })
        map.set(target, list)
      }
    }
    for (const [k, list] of map.entries()) {
      list.sort((a, b) => (a.kind + a.id).localeCompare(b.kind + b.id))
      map.set(k, list)
    }
    return map
  }, [entities, articles])
  const simItemUsage = useMemo(() => {
    type UsageRow = { id: string; label: string; kind: 'process' | 'recipe'; count: number; quantity: number; units: string[] }
    const byItem = new Map<string, { consumers: Map<string, UsageRow>; recipes: Map<string, UsageRow> }>()
    for (const run of simData?.process_runs ?? []) {
      for (const [itemId, q] of Object.entries(run.inputs)) {
        const bucket = byItem.get(itemId) ?? { consumers: new Map(), recipes: new Map() }
        const processKey = run.process_id
        const processRow = bucket.consumers.get(processKey) ?? {
          id: processKey,
          label: entitiesById[processKey]?.name || processKey,
          kind: 'process',
          count: 0,
          quantity: 0,
          units: [],
        }
        processRow.count += 1
        processRow.quantity += q.quantity
        if (!processRow.units.includes(q.unit)) processRow.units.push(q.unit)
        bucket.consumers.set(processKey, processRow)

        if (run.recipe_id) {
          const recipeKey = run.recipe_id
          const recipeRow = bucket.recipes.get(recipeKey) ?? {
            id: recipeKey,
            label: entitiesById[recipeKey]?.name || recipeKey,
            kind: 'recipe',
            count: 0,
            quantity: 0,
            units: [],
          }
          recipeRow.count += 1
          recipeRow.quantity += q.quantity
          if (!recipeRow.units.includes(q.unit)) recipeRow.units.push(q.unit)
          bucket.recipes.set(recipeKey, recipeRow)
        }
        byItem.set(itemId, bucket)
      }
    }
    return byItem
  }, [simData, entitiesById])
  const machineProcessUsage = useMemo(() => {
    const byMachine = new Map<string, Map<string, { processId: string; label: string; count: number; totalEnergy: number }>>()
    for (const run of simData?.process_runs ?? []) {
      if (!run.machine_type) continue
      const bucket = byMachine.get(run.machine_type) ?? new Map<string, { processId: string; label: string; count: number; totalEnergy: number }>()
      const cur = bucket.get(run.process_id) ?? {
        processId: run.process_id,
        label: entitiesById[run.process_id]?.name || run.process_id,
        count: 0,
        totalEnergy: 0,
      }
      cur.count += 1
      cur.totalEnergy += run.energy_kwh ?? 0
      bucket.set(run.process_id, cur)
      byMachine.set(run.machine_type, bucket)
    }
    const out = new Map<string, Array<{ processId: string; label: string; count: number; totalEnergy: number }>>()
    for (const [machineId, bucket] of byMachine.entries()) {
      out.set(
        machineId,
        Array.from(bucket.values()).sort((a, b) => b.count - a.count || b.totalEnergy - a.totalEnergy),
      )
    }
    return out
  }, [simData, entitiesById])

  const selectedRun = useMemo(() => simData?.process_runs.find((r) => r.process_run_id === selectedRunId) ?? null, [simData, selectedRunId])
  const selectedRecipeRuns = useMemo(
    () => (
      selectedRun?.recipe_run_id
        ? (simData?.process_runs.filter((r) => r.recipe_run_id === selectedRun.recipe_run_id) ?? [])
        : []
    ),
    [selectedRun, simData],
  )

  const recipeContextByRunId = useMemo(() => {
    const byRecipe = new Map<string, ProcessRun[]>()
    const ctxByRun = new Map<string, { finalOutputs: QuantityMap; consumedOutputIds: Set<string> }>()
    if (!simData) return ctxByRun

    for (const run of simData.process_runs) {
      if (!run.recipe_run_id) continue
      const bucket = byRecipe.get(run.recipe_run_id)
      if (bucket) bucket.push(run)
      else byRecipe.set(run.recipe_run_id, [run])
    }

    for (const runs of byRecipe.values()) {
      runs.sort((a, b) => (a.end_time ?? a.start_time ?? 0) - (b.end_time ?? b.start_time ?? 0))
      const finalRun = runs[runs.length - 1]
      const finalOutputs = finalRun?.outputs ?? {}
      const consumedOutputIds = new Set<string>()
      const inputIds = new Set<string>()
      for (const run of runs) {
        for (const itemId of Object.keys(run.inputs)) inputIds.add(itemId)
      }
      for (const run of runs) {
        for (const outId of Object.keys(run.outputs)) {
          if (inputIds.has(outId)) consumedOutputIds.add(outId)
        }
      }
      for (const run of runs) {
        ctxByRun.set(run.process_run_id, { finalOutputs, consumedOutputIds })
      }
    }

    return ctxByRun
  }, [simData])

  const deltasByRunId = useMemo(() => {
    const m = new Map<string, { idx: number; delta: InventoryDelta }>()
    simData?.inventory_deltas.forEach((d, idx) => m.set(d.process_run_id, { idx, delta: d }))
    return m
  }, [simData])

  const resolveInventoryAtRun = (runId: string): QuantityMap => {
    if (!simData) return {}
    const hit = deltasByRunId.get(runId)
    if (!hit) return {}
    const targetIdx = hit.idx
    const targetTime = hit.delta.time_hours ?? 0

    const checkpoints = simData.inventory_checkpoints
    let checkpoint: InventoryCheckpoint | null = null
    for (const c of checkpoints) {
      if (c.time_hours <= targetTime) checkpoint = c
      else break
    }

    const inv: QuantityMap = checkpoint ? JSON.parse(JSON.stringify(checkpoint.inventory)) : {}
    const startIdx = checkpoint ? Math.max(0, checkpoint.process_complete_count) : 0

    for (let i = startIdx; i <= targetIdx; i += 1) {
      const d = simData.inventory_deltas[i]
      if (!d) continue
      for (const [itemId, q] of Object.entries(d.delta)) {
        const cur = inv[itemId]
        if (!cur) {
          inv[itemId] = { quantity: q.quantity, unit: q.unit }
        } else if (cur.unit === q.unit) {
          inv[itemId] = { quantity: cur.quantity + q.quantity, unit: cur.unit }
        }
      }
    }

    return Object.fromEntries(
      Object.entries(inv)
        .filter(([, q]) => Math.abs(q.quantity) > 1e-9)
        .sort((a, b) => a[0].localeCompare(b[0])),
    )
  }

  const inventoryForSelected = useMemo(
    () => (selectedRun ? resolveInventoryAtRun(selectedRun.process_run_id) : {}),
    [selectedRun, simData],
  )
  const selectedRecipeBounds = useMemo(() => {
    if (!selectedRun || selectedRecipeRuns.length === 0) return null
    const start = Math.min(...selectedRecipeRuns.map((r) => r.start_time ?? 0))
    const end = Math.max(...selectedRecipeRuns.map((r) => (r.end_time ?? r.start_time ?? 0)))
    return { start, end }
  }, [selectedRun, selectedRecipeRuns])
  const resolveInventoryAtTime = (timeHours: number): QuantityMap => {
    if (!simData) return {}
    const targetTime = Math.max(0, timeHours)
    const checkpoints = simData.inventory_checkpoints
    let checkpoint: InventoryCheckpoint | null = null
    for (const c of checkpoints) {
      if (c.time_hours <= targetTime) checkpoint = c
      else break
    }
    const inv: QuantityMap = checkpoint ? JSON.parse(JSON.stringify(checkpoint.inventory)) : {}
    const startIdx = checkpoint ? Math.max(0, checkpoint.process_complete_count) : 0
    for (let i = startIdx; i < simData.inventory_deltas.length; i += 1) {
      const d = simData.inventory_deltas[i]
      if (!d) continue
      const t = d.time_hours ?? 0
      if (t > targetTime) break
      for (const [itemId, q] of Object.entries(d.delta)) {
        const cur = inv[itemId]
        if (!cur) inv[itemId] = { quantity: q.quantity, unit: q.unit }
        else if (cur.unit === q.unit) inv[itemId] = { quantity: cur.quantity + q.quantity, unit: cur.unit }
      }
    }
    return Object.fromEntries(
      Object.entries(inv)
        .filter(([, q]) => Math.abs(q.quantity) > 1e-9)
        .sort((a, b) => a[0].localeCompare(b[0])),
    )
  }
  const inventoryAtSelectedTime = useMemo(
    () => (selectedTimeHours === null ? {} : resolveInventoryAtTime(selectedTimeHours)),
    [selectedTimeHours, simData],
  )
  const inventoryAtRecipeStart = useMemo(
    () => (selectedRecipeBounds ? resolveInventoryAtTime(selectedRecipeBounds.start) : {}),
    [selectedRecipeBounds, simData],
  )
  const inventoryAtRecipeEnd = useMemo(
    () => (selectedRecipeBounds ? resolveInventoryAtTime(selectedRecipeBounds.end) : {}),
    [selectedRecipeBounds, simData],
  )

  const navigate = (next: Route) => {
    window.location.hash = hashTo(next)
  }

  const openWiki = (id: string) => {
    const next: Route = { view: 'wiki', id }
    if (route.view === 'wiki') {
      navigate(next)
      return
    }
    const url = new URL(window.location.href)
    url.hash = hashTo(next)
    window.open(url.toString(), '_blank', 'noopener,noreferrer')
  }

  const kbIndex = useMemo<KBSearchRow[]>(() => {
    const kbRows = entities.map((e) => ({
      id: e.id,
      label: e.name || e.id,
      type: e.kind,
      path: e.path,
      searchableText: [
        e.id,
        e.name || '',
        e.kind,
        e.category || '',
        e.path,
        e.kind === 'process' ? '' : stringifyForSearch(e.raw, new Set(['inputs'])),
      ].join(' '),
    }))
    const articleRows = articles.map((a) => ({
      id: a.id,
      label: a.title,
      type: 'article',
      path: a.path,
      searchableText: [
        a.id,
        a.title,
        a.path,
        stringifyForSearch(a.frontmatter),
        a.content,
        (a.wiki_links ?? []).join(' '),
      ].join(' '),
    }))
    return [...kbRows, ...articleRows]
  }, [entities, articles])

  const topMachineRows = useMemo(() => {
    const counts = new Map<string, number>()
    for (const run of simData?.process_runs ?? []) {
      if (!run.machine_type) continue
      counts.set(run.machine_type, (counts.get(run.machine_type) ?? 0) + 1)
    }
    return Array.from(counts.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(([id, count]) => ({
        id,
        label: entitiesById[id]?.name || id,
        count,
        type: 'machine',
      }))
  }, [simData, entitiesById])

  const topProcessRows = useMemo(() => {
    const counts = new Map<string, number>()
    for (const run of simData?.process_runs ?? []) {
      counts.set(run.process_id, (counts.get(run.process_id) ?? 0) + 1)
    }
    return Array.from(counts.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(([id, count]) => ({
        id,
        label: entitiesById[id]?.name || id,
        count,
        type: 'process',
      }))
  }, [simData, entitiesById])

  const topRecipeRows = useMemo(() => {
    const counts = new Map<string, number>()
    for (const run of simData?.process_runs ?? []) {
      if (!run.recipe_id) continue
      counts.set(run.recipe_id, (counts.get(run.recipe_id) ?? 0) + 1)
    }
    return Array.from(counts.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(([id, count]) => ({
        id,
        label: entitiesById[id]?.name || id,
        count,
        type: 'recipe',
      }))
  }, [simData, entitiesById])

  const machineCatalogRows = useMemo<MachineCatalogRow[]>(() => {
    const utilizationById = tableById(simQuery?.tables['sim.machines.utilization'])
    const seededById = tableById(simQuery?.tables['sim.machines.seeded'])
    const producedById = tableById(simQuery?.tables['sim.machines.produced'])
    const coverageById = tableById(simQuery?.tables['sim.machines.coverage'])
    const targetSet = new Set(machineSets.sets.find((set) => set.id === 'self_reproducing_target')?.ids ?? [])
    const runCounts = new Map<string, number>()
    const reservedCounts = new Map<string, number>()

    for (const run of simData?.process_runs ?? []) {
      if (run.machine_type) runCounts.set(run.machine_type, (runCounts.get(run.machine_type) ?? 0) + 1)
      for (const reserved of run.reserved_machines ?? []) {
        reservedCounts.set(reserved.machine_id, (reservedCounts.get(reserved.machine_id) ?? 0) + 1)
      }
    }

    return entities
      .filter(isMachineEntity)
      .filter((entity) => !MACHINE_CATALOG_ALIASES.has(entity.id))
      .map((entity) => {
        const raw = entity.raw
        const util = utilizationById.get(entity.id)
        const seeded = seededById.get(entity.id)
        const produced = producedById.get(entity.id)
        const coverage = coverageById.get(entity.id)
        const reservedCount = reservedCounts.get(entity.id) ?? 0
        const runCount = numberField(util, 'run_count') || runCounts.get(entity.id) || reservedCount
        const busyHours = numberField(util, 'busy_hours')
        const producedQuantity = numberField(produced, 'produced_quantity') || numberField(coverage, 'produced_quantity')
        const importedQuantity = numberField(seeded, 'imported_quantity') || numberField(coverage, 'imported_quantity')

        return {
          id: entity.id,
          label: entity.name || entity.id,
          path: entity.path,
          family: entity.category || inferMachineFamily(entity),
          capabilities: stringArrayField(raw, 'capabilities'),
          auditTags: getMachineAuditTags(raw),
          recipeId: stringField(raw, 'recipe'),
          bomId: stringField(raw, 'bom'),
          massLabel: formatMachineMass(raw),
          runCount,
          busyHours,
          utilizationPercent: numberField(util, 'utilization_percent'),
          totalEnergyKwh: numberField(util, 'total_energy_kwh'),
          reservedCount,
          supportedProcessCount: getMachineSupportedProcessRows(entity, entities).length,
          isTarget: targetSet.has(entity.id),
          isUsed: runCount > 0 || reservedCount > 0 || busyHours > 0,
          isSeeded: Boolean(seeded || importedQuantity > 0),
          isProduced: Boolean(produced || producedQuantity > 0),
          covered: Boolean(coverage?.covered),
          importedQuantity,
          producedQuantity,
        }
      })
      .sort((a, b) => b.runCount - a.runCount || a.family.localeCompare(b.family) || a.label.localeCompare(b.label))
  }, [entities, simData, simQuery, machineSets])

  return (
    <div className={`app ${sidebarCollapsed ? 'sidebar-collapsed' : ''}`}>
      <aside className="sidebar">
        <div className="sidebar-head">
          <button className="menu-toggle" onClick={() => setSidebarCollapsed((v) => !v)} title="Toggle sidebar">
            ☰
          </button>
          {!sidebarCollapsed && <div className="brand">SERES Simviewer</div>}
        </div>
        <button className={route.view === 'home' ? 'nav active' : 'nav'} onClick={() => navigate({ view: 'home' })}>
          {sidebarCollapsed ? '🏠' : '🏠 Home'}
        </button>
        <button className={route.view === 'gantt' ? 'nav active' : 'nav'} onClick={() => navigate({ view: 'gantt' })}>
          {sidebarCollapsed ? '📈' : '📈 Timeline'}
        </button>
        <button className={route.view === 'recipes' ? 'nav active' : 'nav'} onClick={() => navigate({ view: 'recipes' })}>
          {sidebarCollapsed ? '🧪' : '🧪 Recipes'}
        </button>
        <button className={route.view === 'machines' ? 'nav active' : 'nav'} onClick={() => navigate({ view: 'machines' })}>
          {sidebarCollapsed ? '⚙' : '⚙ Machines'}
        </button>
        <button className={route.view === 'ebfissues' ? 'nav active' : 'nav'} onClick={() => navigate({ view: 'ebfissues' })}>
          {sidebarCollapsed ? 'EBF' : 'EBF3 Issue Review'}
        </button>
        <button className={route.view === 'wiki' ? 'nav active' : 'nav'} onClick={() => openWiki(WIKI_HOME_ID)}>
          {sidebarCollapsed ? '📚' : '📚 Wiki'}
        </button>
        <button className={route.view === 'kbsearch' ? 'nav active' : 'nav'} onClick={() => navigate({ view: 'kbsearch' })}>
          {sidebarCollapsed ? '🔎' : '🔎 KB Search'}
        </button>
        <div className="meta">
          {simData ? (
            <>
              {!sidebarCollapsed && <div>Sim: {simData.sim_id}</div>}
              <div>{sidebarCollapsed ? `${simData.summary.time_days.toFixed(1)} d` : `Time: ${simData.summary.time_days.toFixed(1)} d`}</div>
              {!sidebarCollapsed && <div>Energy: {simData.summary.total_energy_kwh.toLocaleString()} kWh</div>}
            </>
          ) : (
            <div>Loading data...</div>
          )}
        </div>
      </aside>

      <main className="main">
        {route.view === 'home' && (
          <HomeView
            simData={simData}
            articles={articles}
            warnings={warnings}
            markdownTargets={markdownTargets}
            simQuery={simQuery}
            onJumpKB={openWiki}
          />
        )}

        {route.view === 'gantt' && simData && (
          <GanttView
            simData={simData}
            entitiesById={entitiesById}
            onSelectRun={(id) => {
              setSelectedRunId(id)
              setSelectedRunSource('timeline')
            }}
            selectedTimeHours={selectedTimeHours}
            onSelectTime={(t) => {
              setSelectedRunId(null)
              setSelectedRunSource(null)
              setSelectedTimeHours(t)
            }}
            zoom={zoom}
            onZoom={setZoom}
            colorMode={colorMode}
            onColorMode={setColorMode}
            onOpenKB={openWiki}
          />
        )}
        {route.view === 'recipes' && simData && (
          <RecipeTimelineView
            simData={simData}
            entitiesById={entitiesById}
            onSelectRun={(id) => {
              setSelectedRunId(id)
              setSelectedRunSource('recipes')
            }}
            selectedTimeHours={selectedTimeHours}
            onSelectTime={(t) => {
              setSelectedRunId(null)
              setSelectedRunSource(null)
              setSelectedTimeHours(t)
            }}
            zoom={zoom}
            onZoom={setZoom}
            onOpenKB={openWiki}
          />
        )}

        {route.view === 'machines' && (
          <MachineCatalogView
            rows={machineCatalogRows}
            onSelect={openWiki}
          />
        )}

        {route.view === 'ebfissues' && (
          <EbfProcessIssuesView
            payload={ebfProcessIssues}
            entitiesById={entitiesById}
            onSelect={openWiki}
          />
        )}

        {route.view === 'wiki' && (
          <WikiView
            selectedId={route.id}
            entitiesById={entitiesById}
            articlesById={articlesById}
            markdownTargets={markdownTargets}
            simQuery={simQuery}
            kbBacklinks={kbBacklinks}
            simItemUsage={simItemUsage}
            machineProcessUsage={machineProcessUsage}
            ebfRouteAudit={ebfRouteAudit}
            onWikiJump={openWiki}
            allEntities={entities}
          />
        )}

        {route.view === 'kbsearch' && (
          <KBSearchView
            indexRows={kbIndex}
            search={search}
            onSearch={setSearch}
            topMachines={topMachineRows}
            topProcesses={topProcessRows}
            topRecipes={topRecipeRows}
            onSelect={openWiki}
          />
        )}
      </main>

      {selectedRun && (
        <Drawer
          run={selectedRun}
          entitiesById={entitiesById}
          mode={selectedRunSource === 'recipes' ? 'recipe' : 'process'}
          recipeRuns={selectedRecipeRuns}
          inventory={selectedRunSource === 'recipes' ? inventoryAtRecipeEnd : inventoryForSelected}
          inventoryStart={selectedRunSource === 'recipes' ? inventoryAtRecipeStart : undefined}
          inventoryLabel={selectedRunSource === 'recipes' ? 'end of recipe' : 'end of process'}
          recipeContext={recipeContextByRunId.get(selectedRun.process_run_id)}
          onClose={() => {
            setSelectedRunId(null)
            setSelectedRunSource(null)
          }}
          onOpenKB={openWiki}
        />
      )}
      {!selectedRun && selectedTimeHours !== null && (
        <TimeDrawer
          timeHours={selectedTimeHours}
          inventory={inventoryAtSelectedTime}
          onClose={() => setSelectedTimeHours(null)}
        />
      )}
    </div>
  )
}

function HomeView({
  simData,
  articles,
  warnings,
  markdownTargets,
  simQuery,
  onJumpKB,
}: {
  simData: SimData | null
  articles: Article[]
  warnings: Warnings | null
  markdownTargets: Set<string>
  simQuery: SimQueryData | null
  onJumpKB: (id: string) => void
}) {
  const article = articles.find((a) => a.id === WIKI_HOME_ID) ?? articles[0]
  const simId = typeof simQuery?.scalars['sim.id'] === 'string' ? String(simQuery?.scalars['sim.id']) : (simData?.sim_id || 'unknown')
  const pageTitle = article?.title || `SERES Simulation: ${simId}`

  return (
    <div className="panel-wrap">
      <div className="panel home-title-panel">
        <h1 className="home-title">{pageTitle}</h1>
      </div>
      <div className="panel article-shell">
        {article ? (
          <MarkdownArticle content={article.content} onJump={onJumpKB} validTargets={markdownTargets} simQuery={simQuery} />
        ) : (
          <p>No article configured.</p>
        )}
      </div>
      {warnings && (
        <div className="panel">
          <h3>Warnings</h3>
          <p>Undefined refs: {warnings.undefined_references.length}</p>
          <p>Missing machine categories: {warnings.missing_kb_categories.length}</p>
        </div>
      )}
    </div>
  )
}

function GanttView({
  simData,
  entitiesById,
  onSelectRun,
  selectedTimeHours,
  onSelectTime,
  zoom,
  onZoom,
  colorMode,
  onColorMode,
  onOpenKB,
}: {
  simData: SimData
  entitiesById: Record<string, KBEntity>
  onSelectRun: (id: string) => void
  selectedTimeHours: number | null
  onSelectTime: (timeHours: number) => void
  zoom: number
  onZoom: (z: number) => void
  colorMode: ColorMode
  onColorMode: (mode: ColorMode) => void
  onOpenKB: (id: string) => void
}) {
  const lanes = simData.machine_lanes
  const runsById = useMemo(() => {
    const m = new Map<string, ProcessRun>()
    for (const run of simData.process_runs) m.set(run.process_run_id, run)
    return m
  }, [simData.process_runs])
  const machineAssignments = useMemo<MachineAssignment[]>(() => {
    if (simData.machine_assignments && simData.machine_assignments.length > 0) {
      return simData.machine_assignments
    }
    const fallback: MachineAssignment[] = []
    for (const run of simData.process_runs) {
      if (!run.lane_id || !run.machine_type) continue
      fallback.push({
        assignment_id: `${run.process_run_id}:${run.machine_type}:0`,
        process_run_id: run.process_run_id,
        machine_id: run.machine_type,
        machine_instance_id: null,
        start_time: run.start_time,
        end_time: run.end_time,
        duration_hours: run.duration_hours,
        lane_id: run.lane_id,
        lane_index: null,
      })
    }
    return fallback
  }, [simData.machine_assignments, simData.process_runs])
  const laneRuns = useMemo(() => {
    const m = new Map<string, Array<{ run: ProcessRun; assignment: MachineAssignment }>>()
    for (const lane of lanes) m.set(lane.lane_id, [])
    for (const assignment of machineAssignments) {
      if (!assignment.lane_id) continue
      const run = runsById.get(assignment.process_run_id)
      if (!run) continue
      const arr = m.get(assignment.lane_id)
      if (arr) arr.push({ run, assignment })
    }
    return m
  }, [lanes, machineAssignments, runsById])

  const leftRef = useRef<HTMLDivElement>(null)
  const rightRef = useRef<HTMLDivElement>(null)
  const totalHours = Math.max(simData.summary.time_hours, ...simData.process_runs.map((r) => r.end_time ?? 0))
  const widthPx = Math.max(1200, totalHours * zoom)
  const processLabel = (run: ProcessRun) => {
    const name = entitiesById[run.process_id]?.name
    if (name && name !== run.process_id) return `${name} (${run.process_id})`
    return run.process_id
  }

  return (
    <div className="gantt-page">
      <div className="gantt-toolbar">
        <label>
          Zoom
          <input type="range" min="0.005" max="1.5" step="0.005" value={zoom} onChange={(e) => onZoom(Number(e.target.value))} />
          <span>{zoom.toFixed(3)} px/hr</span>
        </label>
        <div className="color-toggle">
          <span>Color:</span>
          {(['status', 'process', 'recipe', 'goal'] as const).map((m) => (
            <button key={m} className={colorMode === m ? 'toggle active' : 'toggle'} onClick={() => onColorMode(m)}>
              {m}
            </button>
          ))}
        </div>
        <span>Total: {totalHours.toFixed(1)} h</span>
      </div>
      <div className="gantt-wrap">
        <div className="gantt-left" ref={leftRef}>
          {lanes.map((lane) => {
            return (
              <div key={lane.lane_id} className="lane-label" style={{ height: ROW_HEIGHT }}>
                <button className="lane-link" onClick={() => onOpenKB(lane.machine_type)}>{lane.lane_id}</button>
              </div>
            )
          })}
        </div>
        <div className="gantt-right" ref={rightRef} onScroll={(e) => { if (leftRef.current) leftRef.current.scrollTop = e.currentTarget.scrollTop }}>
          <div
            className="gantt-canvas"
            style={{ width: widthPx, height: lanes.length * ROW_HEIGHT }}
            onClick={(e) => {
              if (!rightRef.current) return
              const rect = rightRef.current.getBoundingClientRect()
              const x = rightRef.current.scrollLeft + (e.clientX - rect.left)
              onSelectTime(Math.max(0, x / zoom))
            }}
          >
            {lanes.map((lane, row) => {
              const runs = laneRuns.get(lane.lane_id) ?? []
              return (
                <div key={lane.lane_id} className="lane-row" style={{ top: row * ROW_HEIGHT, height: ROW_HEIGHT }}>
                  {runs.map(({ run, assignment }) => {
                    const start = assignment.start_time ?? run.start_time ?? 0
                    const dur = assignment.duration_hours ?? run.duration_hours ?? ((assignment.end_time ?? run.end_time ?? start) - start)
                    const left = start * zoom
                    const width = Math.max(BAR_MIN_PX, dur * zoom)
                    return (
                      <button
                        key={assignment.assignment_id}
                        className={`bar ${run.status}`}
                        style={{
                          left,
                          width,
                          background: runColor(run, colorMode),
                          color: run.status === 'failed' ? '#fff' : '#0c1220',
                          border: run.status === 'failed' ? '1px solid #ffb3b3' : '1px solid rgba(0,0,0,0.15)',
                        }}
                        title={`${processLabel(run)} on ${assignment.machine_id} (${run.status})`}
                        onClick={(e) => {
                          e.stopPropagation()
                          onSelectRun(run.process_run_id)
                        }}
                      >
                        {zoom > 0.03 ? processLabel(run) : ''}
                      </button>
                    )
                  })}
                </div>
              )
            })}
            {selectedTimeHours !== null && (
              <div className="time-cursor" style={{ left: selectedTimeHours * zoom }} />
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

type RecipeTimelineRow = {
  recipe_run_id: string
  recipe_id: string | null
  lane_key: string
  lane_label: string
  lane_slot: number
  start_time: number
  end_time: number
  duration_hours: number
  status: 'success' | 'failed' | 'pending'
  anchor_process_run_id: string
}

type RecipeDisplayLane = {
  lane_row_key: string
  lane_key: string
  lane_label: string
  lane_slot: number
  lane_slot_count: number
}

const UNATTRIBUTED_RECIPE_LANE_KEY = '__unattributed_machine_goal__'
const UNATTRIBUTED_RECIPE_LANE_LABEL = 'Unattributed Machine Goal'

function RecipeTimelineView({
  simData,
  entitiesById,
  onSelectRun,
  selectedTimeHours,
  onSelectTime,
  zoom,
  onZoom,
  onOpenKB,
}: {
  simData: SimData
  entitiesById: Record<string, KBEntity>
  onSelectRun: (id: string) => void
  selectedTimeHours: number | null
  onSelectTime: (timeHours: number) => void
  zoom: number
  onZoom: (z: number) => void
  onOpenKB: (id: string) => void
}) {
  const rows = useMemo<RecipeTimelineRow[]>(() => {
    const byRecipeRun = new Map<string, ProcessRun[]>()
    for (const run of simData.process_runs) {
      if (!run.recipe_run_id) continue
      const arr = byRecipeRun.get(run.recipe_run_id)
      if (arr) arr.push(run)
      else byRecipeRun.set(run.recipe_run_id, [run])
    }

    const out: RecipeTimelineRow[] = []
    for (const [recipeRunId, runs] of byRecipeRun.entries()) {
      if (runs.length === 0) continue
      const sorted = runs.slice().sort((a, b) => (a.start_time ?? 0) - (b.start_time ?? 0))
      const first = sorted[0]
      const recipeId = first.recipe_id ?? null
      const recipeEntity = recipeId ? entitiesById[recipeId] : undefined
      const rawRecipe = recipeEntity?.raw as Record<string, unknown> | undefined
      const targetItemId = typeof rawRecipe?.target_item_id === 'string' ? rawRecipe.target_item_id : null
      const targetEntity = targetItemId ? entitiesById[targetItemId] : undefined
      let goalMachineId: string | null = null
      for (const run of sorted) {
        const goalMachineRaw = getGoalTags(run)['goal.machine_id']
        if (!goalMachineRaw) continue
        const parsed = goalMachineRaw.split('|')[0].trim()
        if (!parsed) continue
        goalMachineId = parsed
        break
      }
      const goalMachineEntity = goalMachineId ? entitiesById[goalMachineId] : undefined

      const laneKey = goalMachineId || (targetEntity?.kind === 'machine' && targetItemId ? targetItemId : UNATTRIBUTED_RECIPE_LANE_KEY)
      const laneLabel =
        goalMachineId
          ? `${goalMachineEntity?.name || goalMachineId} (${goalMachineId})`
          : targetEntity?.kind === 'machine' && targetItemId
            ? `${targetEntity.name || targetItemId} (${targetItemId})`
            : UNATTRIBUTED_RECIPE_LANE_LABEL

      const start = Math.min(...sorted.map((r) => r.start_time ?? 0))
      const end = Math.max(...sorted.map((r) => r.end_time ?? r.start_time ?? 0))
      const duration = Math.max(0, end - start)
      const status = sorted.some((r) => r.status === 'failed')
        ? 'failed'
        : sorted.some((r) => r.status === 'pending')
          ? 'pending'
          : 'success'

      out.push({
        recipe_run_id: recipeRunId,
        recipe_id: recipeId,
        lane_key: laneKey,
        lane_label: laneLabel,
        lane_slot: 0,
        start_time: start,
        end_time: end,
        duration_hours: duration,
        status,
        anchor_process_run_id: first.process_run_id,
      })
    }

    const groupedByLane = new Map<string, RecipeTimelineRow[]>()
    for (const row of out) {
      const bucket = groupedByLane.get(row.lane_key)
      if (bucket) bucket.push(row)
      else groupedByLane.set(row.lane_key, [row])
    }

    for (const laneRows of groupedByLane.values()) {
      laneRows.sort((a, b) => a.start_time - b.start_time || a.recipe_run_id.localeCompare(b.recipe_run_id))
      const slotEndTimes: number[] = []
      for (const row of laneRows) {
        let assignedSlot = -1
        for (let i = 0; i < slotEndTimes.length; i += 1) {
          if (row.start_time >= slotEndTimes[i]) {
            assignedSlot = i
            break
          }
        }
        if (assignedSlot < 0) {
          assignedSlot = slotEndTimes.length
          slotEndTimes.push(row.end_time)
        } else {
          slotEndTimes[assignedSlot] = row.end_time
        }
        row.lane_slot = assignedSlot
      }
    }

    out.sort(
      (a, b) => a.lane_label.localeCompare(b.lane_label)
        || a.lane_slot - b.lane_slot
        || a.start_time - b.start_time
        || a.recipe_run_id.localeCompare(b.recipe_run_id),
    )
    return out
  }, [entitiesById, simData.process_runs])

  const lanes = useMemo<RecipeDisplayLane[]>(() => {
    const byKey = new Map<string, { lane_key: string; lane_label: string; lane_slot_count: number }>()
    for (const row of rows) {
      const slotCount = row.lane_slot + 1
      const existing = byKey.get(row.lane_key)
      if (!existing) {
        byKey.set(row.lane_key, {
          lane_key: row.lane_key,
          lane_label: row.lane_label,
          lane_slot_count: slotCount,
        })
      } else if (slotCount > existing.lane_slot_count) {
        existing.lane_slot_count = slotCount
      }
    }
    const expanded: RecipeDisplayLane[] = []
    for (const lane of Array.from(byKey.values()).sort((a, b) => a.lane_label.localeCompare(b.lane_label))) {
      for (let slot = 0; slot < lane.lane_slot_count; slot += 1) {
        expanded.push({
          lane_row_key: `${lane.lane_key}#${slot}`,
          lane_key: lane.lane_key,
          lane_label: lane.lane_label,
          lane_slot: slot,
          lane_slot_count: lane.lane_slot_count,
        })
      }
    }
    return expanded
  }, [rows])

  const laneIndexByKey = useMemo(() => new Map(lanes.map((lane, idx) => [lane.lane_row_key, idx])), [lanes])

  const leftRef = useRef<HTMLDivElement>(null)
  const rightRef = useRef<HTMLDivElement>(null)
  const totalHours = Math.max(simData.summary.time_hours, ...rows.map((r) => r.end_time))
  const widthPx = Math.max(1200, totalHours * zoom)

  return (
    <div className="gantt-page">
      <div className="gantt-toolbar">
        <label>
          Zoom
          <input type="range" min="0.005" max="1.5" step="0.005" value={zoom} onChange={(e) => onZoom(Number(e.target.value))} />
          <span>{zoom.toFixed(3)} px/hr</span>
        </label>
        <span>Recipe Runs: {rows.length}</span>
        <span>Total: {totalHours.toFixed(1)} h</span>
      </div>
      <div className="gantt-wrap">
        <div className="gantt-left" ref={leftRef}>
          {lanes.map((lane) => (
            <div key={lane.lane_row_key} className="lane-label" style={{ height: ROW_HEIGHT }}>
              {lane.lane_key === UNATTRIBUTED_RECIPE_LANE_KEY ? (
                <span>
                  {lane.lane_label}
                  {lane.lane_slot_count > 1 ? ` #${lane.lane_slot + 1}` : ''}
                </span>
              ) : (
                <button className="lane-link" onClick={() => onOpenKB(lane.lane_key)}>
                  {lane.lane_label}
                  {lane.lane_slot_count > 1 ? ` #${lane.lane_slot + 1}` : ''}
                </button>
              )}
            </div>
          ))}
        </div>
        <div className="gantt-right" ref={rightRef} onScroll={(e) => { if (leftRef.current) leftRef.current.scrollTop = e.currentTarget.scrollTop }}>
          <div
            className="gantt-canvas"
            style={{ width: widthPx, height: lanes.length * ROW_HEIGHT }}
            onClick={(e) => {
              if (!rightRef.current) return
              const rect = rightRef.current.getBoundingClientRect()
              const x = rightRef.current.scrollLeft + (e.clientX - rect.left)
              onSelectTime(Math.max(0, x / zoom))
            }}
          >
            {lanes.map((lane, row) => (
              <div key={lane.lane_row_key} className="lane-row" style={{ top: row * ROW_HEIGHT, height: ROW_HEIGHT }} />
            ))}
            {rows.map((row) => {
              const laneIndex = laneIndexByKey.get(`${row.lane_key}#${row.lane_slot}`)
              if (laneIndex === undefined) return null
              const left = row.start_time * zoom
              const width = Math.max(BAR_MIN_PX, row.duration_hours * zoom)
              const top = laneIndex * ROW_HEIGHT + 4
              const label = row.recipe_id || row.recipe_run_id
              return (
                <button
                  key={row.recipe_run_id}
                  className={`bar ${row.status}`}
                  style={{
                    left,
                    top,
                    width,
                    background: row.status === 'failed'
                      ? 'linear-gradient(90deg, #d55a5a, #ff8585)'
                      : row.status === 'pending'
                        ? 'linear-gradient(90deg, #a2a2a2, #c6c6c6)'
                        : 'linear-gradient(90deg, #6bb8ff, #99d0ff)',
                    color: row.status === 'failed' ? '#fff' : '#0c1220',
                    border: row.status === 'failed' ? '1px solid #ffb3b3' : '1px solid rgba(0,0,0,0.15)',
                  }}
                  title={`${label} (${row.status})`}
                  onClick={(e) => {
                    e.stopPropagation()
                    onSelectRun(row.anchor_process_run_id)
                  }}
                >
                  {zoom > 0.03 ? label : ''}
                </button>
              )
            })}
            {selectedTimeHours !== null && (
              <div className="time-cursor" style={{ left: selectedTimeHours * zoom }} />
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

function BomTreeSection({
  result,
  selectedItemId,
  routeRows,
  onWikiJump,
}: {
  result: BomTreeBuildResult
  selectedItemId: string | null
  routeRows: EbfRouteAuditRow[]
  onWikiJump: (id: string) => void
}) {
  const summary = result.summary
  const [visualZoom, setVisualZoom] = useState(1)
  const [visualBranchId, setVisualBranchId] = useState<string>('__all__')
  const [auditPolicyFilter, setAuditPolicyFilter] = useState('all')
  const routeByItemId = useMemo(() => new Map(routeRows.map((row) => [row.item_id, row])), [routeRows])
  const l1Branches = result.root.children
  const selectedL1BranchId = findBomTreeL1ForItem(result.root, selectedItemId) ?? l1Branches[0]?.itemId ?? '__all__'
  const activeBranchId = visualBranchId === 'auto' ? selectedL1BranchId : visualBranchId
  const activeBranch = l1Branches.find((branch) => branch.itemId === activeBranchId) ?? null
  const visualRoot = activeBranchId === '__all__' || !activeBranch
    ? result.root
    : { ...result.root, children: [activeBranch] }
  const fullTreePolicyCounts = useMemo(() => countBomRoutePolicies(result.root, routeByItemId), [result.root, routeByItemId])
  const fullTreePolicyItemCount = useMemo(
    () => Object.values(fullTreePolicyCounts).reduce((sum, count) => sum + count, 0),
    [fullTreePolicyCounts],
  )
  const routeRowsOutsideTreeCount = Math.max(0, routeRows.length - fullTreePolicyItemCount)
  const visiblePolicyCounts = useMemo(() => countBomRoutePolicies(visualRoot, routeByItemId), [visualRoot, routeByItemId])
  const visibleNodeCount = useMemo(
    () => countVisibleBomTreeRows(visualRoot, routeByItemId, auditPolicyFilter),
    [auditPolicyFilter, routeByItemId, visualRoot],
  )
  const visiblePolicyItemCount = useMemo(
    () => auditPolicyFilter === 'all'
      ? Object.values(visiblePolicyCounts).reduce((sum, count) => sum + count, 0)
      : visiblePolicyCounts[auditPolicyFilter] ?? 0,
    [auditPolicyFilter, visiblePolicyCounts],
  )
  const visualScaleStyle = { zoom: visualZoom } as CSSProperties
  return (
    <div className="kb-block bom-tree-block">
      <div className="bom-tree-head">
        <div>
          <h3>Recursive BOM Tree</h3>
          <p className="muted-text">
            Root: <button className="wiki-link" onClick={() => onWikiJump(result.root.itemId)}>{result.root.itemId}</button>
            {' '}expanded through every nested BOM component.
          </p>
        </div>
        <div className="bom-tree-stats">
          <div><label>Unique items</label><strong>{summary.uniqueItems}</strong></div>
          <div><label>BOMs</label><strong>{summary.bomCount}</strong></div>
          <div><label>Leaves</label><strong>{summary.leafOccurrences}</strong></div>
          <div><label>Depth</label><strong>{summary.maxDepth}</strong></div>
        </div>
      </div>
      <div className="bom-audit-toolbar">
        <span>L1 branch</span>
        <select
          value={visualBranchId}
          onChange={(event) => setVisualBranchId(event.target.value)}
          aria-label="BOM audit L1 branch"
        >
          <option value="auto">Auto selected L1</option>
          <option value="__all__">All L1 branches</option>
          {l1Branches.map((branch) => (
            <option key={branch.itemId} value={branch.itemId}>
              {branch.itemId} ({countBomTreeDescendants(branch)} descendants)
            </option>
          ))}
        </select>
        <span>Policy</span>
        <select value={auditPolicyFilter} onChange={(event) => setAuditPolicyFilter(event.target.value)}>
          <option value="all">All policies</option>
          <option value="local_nominal">local_nominal</option>
          <option value="sensitivity_flag">sensitivity_flag</option>
          <option value="import_nominal">import_nominal</option>
          <option value="import_until_gap_resolved">import_until_gap_resolved</option>
        </select>
        <strong>
          {visiblePolicyItemCount.toLocaleString()} policy items / {visibleNodeCount.toLocaleString()} tree nodes
          {routeRows.length > 0 && (
            <> · all tree {fullTreePolicyItemCount.toLocaleString()} / outside tree {routeRowsOutsideTreeCount.toLocaleString()} / route rows {routeRows.length.toLocaleString()}</>
          )}
        </strong>
      </div>
      {routeRows.length > 0 && (
        <div className="bom-policy-summary" aria-label="BOM route policy summary">
          {['local_nominal', 'sensitivity_flag', 'import_nominal', 'import_until_gap_resolved'].map((policy) => (
            <span key={policy} className={`route-badge policy-${policy}`}>
              {formatRouteLabel(policy)} {visiblePolicyCounts[policy] ?? 0}
            </span>
          ))}
        </div>
      )}
      {(summary.missingEntities > 0 || summary.cycles > 0) && (
        <p className="bom-tree-alert">
          {summary.missingEntities > 0 ? `${summary.missingEntities} missing item definitions. ` : ''}
          {summary.cycles > 0 ? `${summary.cycles} cyclic references stopped.` : ''}
        </p>
      )}
      <h4 className="bom-audit-title">Audit List</h4>
      <div className="bom-tree">
        <BomTreeNodeView
          node={visualRoot}
          selectedItemId={selectedItemId}
          routeByItemId={routeByItemId}
          policyFilter={auditPolicyFilter}
          onWikiJump={onWikiJump}
        />
      </div>
      <details className="bom-visual-details">
        <summary>Recursive visual tree</summary>
        <div className="bom-visual-toolbar">
          <span>Visual zoom</span>
          <button type="button" onClick={() => setVisualZoom((z) => Math.max(0.25, Number((z - 0.1).toFixed(2))))} title="Zoom out">−</button>
          <input
            type="range"
            min="0.25"
            max="1.2"
            step="0.05"
            value={visualZoom}
            onChange={(event) => setVisualZoom(Number(event.target.value))}
            aria-label="BOM visual tree zoom"
          />
          <button type="button" onClick={() => setVisualZoom((z) => Math.min(1.2, Number((z + 0.1).toFixed(2))))} title="Zoom in">+</button>
          <button type="button" onClick={() => setVisualZoom(1)} title="Reset zoom">Reset</button>
          <strong>{Math.round(visualZoom * 100)}%</strong>
        </div>
        <div className="bom-visual-wrap" aria-label="BOM visual hierarchy">
          <div className="bom-visual-scale" style={visualScaleStyle}>
            <ul className="bom-visual-tree">
              <BomVisualTreeNode node={visualRoot} selectedItemId={selectedItemId} routeByItemId={routeByItemId} onWikiJump={onWikiJump} />
            </ul>
          </div>
        </div>
      </details>
    </div>
  )
}

function countVisibleBomTreeRows(node: BomTreeNode, routeByItemId: Map<string, EbfRouteAuditRow>, policyFilter: string): number {
  const route = routeByItemId.get(node.itemId)
  const selfVisible = policyFilter === 'all' || route?.simulation_import_mass_policy === policyFilter
  return (selfVisible ? 1 : 0) + node.children.reduce((sum, child) => sum + countVisibleBomTreeRows(child, routeByItemId, policyFilter), 0)
}

function countBomRoutePolicies(node: BomTreeNode, routeByItemId: Map<string, EbfRouteAuditRow>): Record<string, number> {
  const counts: Record<string, number> = {}
  const visit = (current: BomTreeNode) => {
    const route = routeByItemId.get(current.itemId)
    if (route?.simulation_import_mass_policy) {
      counts[route.simulation_import_mass_policy] = (counts[route.simulation_import_mass_policy] ?? 0) + 1
    }
    for (const child of current.children) visit(child)
  }
  visit(node)
  return counts
}

function BomVisualTreeNode({
  node,
  selectedItemId,
  routeByItemId,
  onWikiJump,
}: {
  node: BomTreeNode
  selectedItemId: string | null
  routeByItemId: Map<string, EbfRouteAuditRow>
  onWikiJump: (id: string) => void
}) {
  const route = routeByItemId.get(node.itemId)
  const policy = route?.simulation_import_mass_policy ?? ''
  return (
    <li>
      <button
        className={[
          'bom-visual-node',
          node.childCount > 0 ? 'has-children' : 'is-leaf',
          selectedItemId === node.itemId ? 'is-selected' : '',
          node.missingEntity ? 'is-missing' : '',
          node.cycle ? 'is-cycle' : '',
        ].filter(Boolean).join(' ')}
        onClick={() => onWikiJump(node.itemId)}
        title={`${node.itemId}${node.childCount > 0 ? `, ${node.childCount} components` : ''}${policy ? `\nPolicy: ${policy}\nDecision: ${route?.route_decision ?? ''}` : ''}`}
      >
        <span>{formatBomVisualLabel(node.itemId)}</span>
        <small>{node.qty === null ? 'root' : `${formatBomTreeQty(node.qty)} ${node.unit ?? 'unit'}`}</small>
        {policy && <small className={`bom-visual-policy policy-${policy}`}>{formatRouteLabel(policy)}</small>}
      </button>
      {node.children.length > 0 && (
        <ul>
          {node.children.map((child, i) => (
            <BomVisualTreeNode key={`${child.itemId}:${child.depth}:${i}`} node={child} selectedItemId={selectedItemId} routeByItemId={routeByItemId} onWikiJump={onWikiJump} />
          ))}
        </ul>
      )}
    </li>
  )
}

function BomTreeNodeView({
  node,
  selectedItemId,
  routeByItemId,
  policyFilter,
  onWikiJump,
}: {
  node: BomTreeNode
  selectedItemId: string | null
  routeByItemId: Map<string, EbfRouteAuditRow>
  policyFilter: string
  onWikiJump: (id: string) => void
}) {
  const route = routeByItemId.get(node.itemId)
  const policy = route?.simulation_import_mass_policy ?? ''
  const isVisible = policyFilter === 'all' || policy === policyFilter
  const visibleChildren = node.children.filter((child) => hasVisibleBomTreeRow(child, routeByItemId, policyFilter))
  if (!isVisible && visibleChildren.length === 0) return null
  const isContextOnly = !isVisible && visibleChildren.length > 0

  const style = { '--depth': node.depth } as CSSProperties
  const qtyLabel = node.qty === null ? 'root' : `${formatBomTreeQty(node.qty)} ${node.unit ?? 'unit'}`

  return (
    <div className="bom-tree-node">
      {(isVisible || isContextOnly) && (
        <div
          className={[
            'bom-tree-row',
            node.childCount > 0 ? 'has-children' : 'is-leaf',
            isContextOnly ? 'is-context-only' : '',
            route ? 'has-route-policy' : '',
            node.missingEntity ? 'is-missing' : '',
            node.cycle ? 'is-cycle' : '',
            selectedItemId === node.itemId ? 'is-selected' : '',
          ].filter(Boolean).join(' ')}
          style={style}
        >
          <span className="bom-tree-depth">L{node.depth}</span>
          <span className="bom-tree-qty">{qtyLabel}</span>
          <button className="wiki-link bom-tree-item" onClick={() => onWikiJump(node.itemId)}>{node.itemId}</button>
          {node.name !== node.itemId && <span className="bom-tree-name">{node.name}</span>}
          {node.kind && <span className="bom-tree-kind">{node.kind}</span>}
          {policy && <span className={`route-badge bom-tree-policy policy-${policy}`}>{formatRouteLabel(policy)}</span>}
          {node.recipeId && (
            <a className="bom-tree-action" href={`#/wiki/${node.recipeId}`} target="_blank" rel="noreferrer" title={node.recipeId}>Recipe</a>
          )}
          {node.bomId && (
            <button className="bom-tree-action" onClick={() => onWikiJump(node.bomId!)} title={node.bomId}>BOM</button>
          )}
          {node.childCount > 0 && <span className="bom-tree-count">{node.childCount} components</span>}
          {isContextOnly && <span className="bom-tree-context">context</span>}
          {node.missingEntity && <span className="bom-tree-warning">missing entity</span>}
          {node.cycle && <span className="bom-tree-warning">cycle stopped</span>}
        </div>
      )}
      {visibleChildren.length > 0 && (
        <div className="bom-tree-children">
          {visibleChildren.map((child, i) => (
            <BomTreeNodeView
              key={`${child.itemId}:${child.depth}:${i}`}
              node={child}
              selectedItemId={selectedItemId}
              routeByItemId={routeByItemId}
              policyFilter={policyFilter}
              onWikiJump={onWikiJump}
            />
          ))}
        </div>
      )}
    </div>
  )
}

function hasVisibleBomTreeRow(node: BomTreeNode, routeByItemId: Map<string, EbfRouteAuditRow>, policyFilter: string): boolean {
  const route = routeByItemId.get(node.itemId)
  if (policyFilter === 'all' || route?.simulation_import_mass_policy === policyFilter) return true
  return node.children.some((child) => hasVisibleBomTreeRow(child, routeByItemId, policyFilter))
}

function WikiIdList({
  ids,
  onWikiJump,
  empty = 'none',
}: {
  ids: string[]
  onWikiJump: (id: string) => void
  empty?: string
}) {
  const uniqueIds = Array.from(new Set(ids.filter((id) => id.trim())))
  if (uniqueIds.length === 0) return <>{empty}</>
  return (
    <>
      {uniqueIds.map((id, i) => (
        <span key={id}>
          {i > 0 ? ', ' : ''}
          <button className="wiki-link" onClick={() => onWikiJump(id)}>{id}</button>
        </span>
      ))}
    </>
  )
}

function WikiView({
  selectedId,
  entitiesById,
  articlesById,
  allEntities,
  markdownTargets,
  simQuery,
  kbBacklinks,
  simItemUsage,
  machineProcessUsage,
  ebfRouteAudit,
  onWikiJump,
}: {
  selectedId?: string
  entitiesById: Record<string, KBEntity>
  articlesById: Record<string, Article>
  allEntities: KBEntity[]
  markdownTargets: Set<string>
  simQuery: SimQueryData | null
  kbBacklinks: Map<string, Array<{ id: string; name: string; kind: string }>>
  simItemUsage: Map<string, { consumers: Map<string, { id: string; label: string; kind: 'process' | 'recipe'; count: number; quantity: number; units: string[] }>; recipes: Map<string, { id: string; label: string; kind: 'process' | 'recipe'; count: number; quantity: number; units: string[] }> }>
  machineProcessUsage: Map<string, Array<{ processId: string; label: string; count: number; totalEnergy: number }>>
  ebfRouteAudit: EbfRouteAuditPayload
  onWikiJump: (id: string) => void
}) {
  const entity = selectedId ? entitiesById[selectedId] : undefined
  const article = selectedId ? articlesById[selectedId] : undefined
  const raw = asObject(entity?.raw)
  const references = useMemo(() => (selectedId ? kbBacklinks.get(selectedId) ?? [] : []), [selectedId, kbBacklinks])
  const simConsumers = useMemo(() => {
    if (!selectedId) return []
    const bucket = simItemUsage.get(selectedId)
    if (!bucket) return []
    return Array.from(bucket.consumers.values()).sort((a, b) => b.count - a.count || b.quantity - a.quantity)
  }, [selectedId, simItemUsage])
  const simRecipes = useMemo(() => {
    if (!selectedId) return []
    const bucket = simItemUsage.get(selectedId)
    if (!bucket) return []
    return Array.from(bucket.recipes.values()).sort((a, b) => b.count - a.count || b.quantity - a.quantity)
  }, [selectedId, simItemUsage])
  const machineUsage = useMemo(() => {
    if (!selectedId) return []
    return machineProcessUsage.get(selectedId) ?? []
  }, [selectedId, machineProcessUsage])
  const deferRefs = Boolean(entity && (isMachineEntity(entity) || isProcessEntity(entity)))
  const recipesTargetingEntity = useMemo(
    () =>
      entity
        ? allEntities.filter((e) => {
            if (!isRecipeEntity(e)) return false
            const recipeRaw = asObject(e.raw)
            return recipeRaw?.target_item_id === entity.id
          })
        : [],
    [allEntities, entity],
  )
  const bomsTargetingEntity = useMemo(
    () =>
      entity
        ? allEntities.filter((e) => {
            if (!isBomEntity(e)) return false
            const bomRaw = asObject(e.raw)
            return bomRaw?.owner_item_id === entity.id || bomRaw?.target_item_id === entity.id
          })
        : [],
    [allEntities, entity],
  )
  const machineSupportedProcesses = useMemo(() => {
    if (!entity || !isMachineEntity(entity)) return []
    return getMachineSupportedProcessRows(entity, allEntities)
  }, [allEntities, entity])
  const machineSupportedProcessIds = useMemo(
    () => new Set(machineSupportedProcesses.map((row) => row.id)),
    [machineSupportedProcesses],
  )
  const nonSupportReferences = useMemo(
    () => references.filter((ref) => !machineSupportedProcessIds.has(ref.id)),
    [references, machineSupportedProcessIds],
  )
  const bomTreeRootItemId = useMemo(() => getBomTreeRootItemId(entity), [entity])
  const bomTreeSelectedItemId = useMemo(() => getBomTreeSelectedItemId(entity), [entity])
  const bomTree = useMemo(
    () => (bomTreeRootItemId ? buildBomTree(bomTreeRootItemId, allEntities, entitiesById) : null),
    [allEntities, bomTreeRootItemId, entitiesById],
  )
  const entryMass = formatEntryMass(raw)
  const entryMaterial = entity?.kind === 'part' ? formatEntryMaterial(raw) : null
  const entryImportStatus = formatEntryImportStatus(entity, raw)
  const entryRouteDecision = textField(raw ?? undefined, 'route_decision')
  const entryImportPolicy = textField(raw ?? undefined, 'simulation_import_mass_policy')
  const entryNotes = textField(raw ?? undefined, 'notes')
  const entryFutureImprovements = stringListFromField(raw ?? undefined, 'future_improvements')
  const entryAuditTags = entity && isMachineEntity(entity) ? getMachineAuditTags(raw ?? undefined) : []
  const buildRecipeIds = [
    ...(typeof raw?.recipe === 'string' ? [raw.recipe] : []),
    ...recipesTargetingEntity.map((recipe) => recipe.id),
  ]
  const buildBomIds = [
    ...(typeof raw?.bom === 'string' ? [raw.bom] : []),
    ...bomsTargetingEntity.map((bom) => bom.id),
  ]
  const buildOwnerIds = typeof raw?.owner_item_id === 'string' ? [raw.owner_item_id] : []
  const buildTargetIds = typeof raw?.target_item_id === 'string' ? [raw.target_item_id] : []

  return (
    <div className="wiki-page">
      <section className="kb-detail wiki-detail">
        {!selectedId && <p>Select an item from the index.</p>}
        {entity && (
          <>
            <h2>{entity.name}</h2>
            <p><strong>ID:</strong> {entity.id}</p>
            <p><strong>Kind:</strong> {entity.kind}</p>
            <p><strong>Category:</strong> {entity.category || 'Uncategorized'}</p>
            <p><strong>Source:</strong> {entity.path}</p>
            {raw && (
              <>
                <p><strong>Mass:</strong> {entryMass || 'not listed'}</p>
                {entity.kind === 'part' && <p><strong>Material:</strong> {entryMaterial || 'not listed'}</p>}
                <p><strong>Import:</strong> {entryImportStatus}</p>
                {entryRouteDecision && <p><strong>Route decision:</strong> {entryRouteDecision}</p>}
                {entryImportPolicy && <p><strong>Route policy:</strong> {formatRouteLabel(entryImportPolicy)}</p>}
                <p><strong>Notes:</strong> {entryNotes || 'not listed'}</p>
                {entryFutureImprovements.length > 0 && (
                  <p><strong>Future improvements:</strong> {entryFutureImprovements.join('; ')}</p>
                )}
                {entryAuditTags.length > 0 && (
                  <p>
                    <strong>Machine audit:</strong>{' '}
                    {entryAuditTags.map((tag, i) => (
                      <span key={tag} className="audit-inline-tag">
                        {i > 0 ? ', ' : ''}
                        {formatMachineAuditTag(tag)}
                      </span>
                    ))}
                  </p>
                )}
              </>
            )}
            {raw && (
              <div className="kb-block build-data-block">
                <h3>Build Data</h3>
                <p><strong>Recipe:</strong> <WikiIdList ids={buildRecipeIds} onWikiJump={onWikiJump} /></p>
                <p><strong>BOM:</strong> <WikiIdList ids={buildBomIds} onWikiJump={onWikiJump} /></p>
                {buildOwnerIds.length > 0 && (
                  <p><strong>Owner:</strong> <WikiIdList ids={buildOwnerIds} onWikiJump={onWikiJump} /></p>
                )}
                {buildTargetIds.length > 0 && (
                  <p><strong>Target:</strong> <WikiIdList ids={buildTargetIds} onWikiJump={onWikiJump} /></p>
                )}
              </div>
            )}
            {entity.sim_stats && (
              <div className="stats-grid compact">
                {entity.sim_stats.process_run_count !== undefined && <div><label>Process Runs</label><strong>{entity.sim_stats.process_run_count}</strong></div>}
                {entity.sim_stats.produced_quantity_total !== undefined && <div><label>Produced</label><strong>{entity.sim_stats.produced_quantity_total.toFixed(2)}</strong></div>}
              </div>
            )}
            {!deferRefs && references.length > 0 && (
              <div className="kb-block">
                <h3>Referenced By (KB + Articles)</h3>
                <ul>
                  {references.slice(0, 80).map((ref, i) => (
                    <li key={`${ref.kind}:${ref.id}:${i}`}>
                      <button className="wiki-link" onClick={() => onWikiJump(ref.id)}>{ref.name}</button> <small>({ref.kind})</small>
                    </li>
                  ))}
                </ul>
              </div>
            )}
            {simConsumers.length > 0 && (
              <div className="kb-block">
                <h3>Used In Simulation (Consumed Inputs, Ranked)</h3>
                <div className="table-wrap">
                  <table>
                    <thead>
                      <tr>
                        <th>Process</th>
                        <th>Runs</th>
                        <th>Total Qty</th>
                        <th>Units</th>
                      </tr>
                    </thead>
                    <tbody>
                      {simConsumers.slice(0, 40).map((row) => (
                        <tr key={row.id}>
                          <td><button className="wiki-link" onClick={() => onWikiJump(row.id)}>{row.label}</button></td>
                          <td>{row.count}</td>
                          <td>{row.quantity.toFixed(2)}</td>
                          <td>{row.units.join(', ')}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            )}
            {simRecipes.length > 0 && (
              <div className="kb-block">
                <h3>Used In Recipes (Ranked by Consuming Runs)</h3>
                <div className="table-wrap">
                  <table>
                    <thead>
                      <tr>
                        <th>Recipe</th>
                        <th>Runs</th>
                        <th>Total Qty</th>
                        <th>Units</th>
                      </tr>
                    </thead>
                    <tbody>
                      {simRecipes.slice(0, 40).map((row) => (
                        <tr key={row.id}>
                          <td><button className="wiki-link" onClick={() => onWikiJump(row.id)}>{row.label}</button></td>
                          <td>{row.count}</td>
                          <td>{row.quantity.toFixed(2)}</td>
                          <td>{row.units.join(', ')}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            )}
            {isMachineEntity(entity) && raw && (
              <div className="kb-block">
                <h3>Machine Details</h3>
                <div className="machine-summary-grid">
                  <div>
                    <label>Capabilities</label>
                    <div className="chip-list">
                      {stringListFromField(raw, 'capabilities').concat(stringListFromField(raw, 'resource_types')).length > 0
                        ? stringListFromField(raw, 'capabilities').concat(stringListFromField(raw, 'resource_types')).map((cap) => <span key={cap}>{cap}</span>)
                        : <em>none listed</em>}
                    </div>
                  </div>
                  <div>
                    <label>Requirements</label>
                    <div className="chip-list">
                      {stringListFromField(raw, 'requires_ids').length > 0
                        ? stringListFromField(raw, 'requires_ids').map((id) => <button key={id} className="chip-link" onClick={() => onWikiJump(id)}>{id}</button>)
                        : <em>none listed</em>}
                    </div>
                  </div>
                </div>
                {machineUsage.length > 0 && (
                  <>
                    <h4>Processes Run On This Machine (Simulation)</h4>
                    <div className="table-wrap">
                      <table>
                        <thead>
                          <tr>
                            <th>Process</th>
                            <th>Runs</th>
                            <th>Total Energy (kWh)</th>
                          </tr>
                        </thead>
                        <tbody>
                          {machineUsage.slice(0, 40).map((row) => (
                            <tr key={row.processId}>
                              <td><button className="wiki-link" onClick={() => onWikiJump(row.processId)}>{row.label}</button></td>
                              <td>{row.count}</td>
                              <td>{row.totalEnergy.toFixed(2)}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </>
                )}
              </div>
            )}
            {isMachineEntity(entity) && (machineSupportedProcesses.length > 0 || nonSupportReferences.length > 0) && (
              <div className="kb-block">
                <h3>Machine References</h3>
                <div className="machine-reference-grid">
                  <div>
                    <h4>Supported Process Steps</h4>
                    {machineSupportedProcesses.length > 0 ? (
                      <ul>
                        {machineSupportedProcesses.slice(0, 120).map((row) => (
                          <li key={row.id}>
                            <button className="wiki-link" onClick={() => onWikiJump(row.id)}>{row.name}</button>
                            <small> ({row.relation})</small>
                          </li>
                        ))}
                      </ul>
                    ) : (
                      <p className="muted-text">No process steps explicitly require this machine in exported KB data.</p>
                    )}
                  </div>
                  <div>
                    <h4>Other Referenced By</h4>
                    {nonSupportReferences.length > 0 ? (
                      <ul>
                        {nonSupportReferences.slice(0, 120).map((ref, i) => (
                          <li key={`${ref.kind}:${ref.id}:${i}`}>
                            <button className="wiki-link" onClick={() => onWikiJump(ref.id)}>{ref.name}</button> <small>({ref.kind})</small>
                          </li>
                        ))}
                      </ul>
                    ) : (
                      <p className="muted-text">No other references found.</p>
                    )}
                  </div>
                </div>
              </div>
            )}
            {isRecipeEntity(entity) && raw && (
              <div className="kb-block">
                <h3>Recipe</h3>
                <h4>Inputs</h4>
                <ul>
                  {asArray(raw.inputs).map((q, i) => {
                    const obj = asObject(q)
                    if (!obj) return null
                    const itemId = String(obj.item_id ?? '')
                    const qty = Number(obj.qty ?? obj.quantity ?? 0)
                    const unit = String(obj.unit ?? 'unit')
                    return (
                      <li key={`in-${i}`}>
                        <button className="wiki-link" onClick={() => onWikiJump(itemId)}>{itemId}</button>: {qty} {unit}
                      </li>
                    )
                  })}
                </ul>
                <h4>Outputs</h4>
                <ul>
                  {asArray(raw.outputs).map((q, i) => {
                    const obj = asObject(q)
                    if (!obj) return null
                    const itemId = String(obj.item_id ?? '')
                    const qty = Number(obj.qty ?? obj.quantity ?? 0)
                    const unit = String(obj.unit ?? 'unit')
                    return (
                      <li key={`out-${i}`}>
                        <button className="wiki-link" onClick={() => onWikiJump(itemId)}>{itemId}</button>: {qty} {unit}
                      </li>
                    )
                  })}
                </ul>
                <h4>Steps</h4>
                <ol>
                  {asArray(raw.steps).map((step, i) => {
                    const obj = asObject(step)
                    if (!obj) return <li key={`s-${i}`}>step {i}</li>
                    const pid = obj.process_id ? String(obj.process_id) : ''
                    return (
                      <li key={`s-${i}`}>
                        step {i}:{' '}
                        {pid ? <button className="wiki-link" onClick={() => onWikiJump(pid)}>{pid}</button> : 'inline/unknown process'}
                      </li>
                    )
                  })}
                </ol>
              </div>
            )}
            {isBomEntity(entity) && raw && (
              <div className="kb-block">
                <h3>BOM</h3>
                <h4>Components</h4>
                {asArray(raw.components).length > 0 ? (
                  <ul>
                    {asArray(raw.components).map((component, i) => {
                      const obj = asObject(component)
                      if (!obj) return null
                      const itemId = String(obj.item_id ?? '')
                      const qty = Number(obj.qty ?? obj.quantity ?? obj.amount ?? 0)
                      const unit = String(obj.unit ?? 'unit')
                      return (
                        <li key={`bom-component-${i}`}>
                          {itemId ? (
                            <button className="wiki-link" onClick={() => onWikiJump(itemId)}>{itemId}</button>
                          ) : (
                            <span>unknown item</span>
                          )}
                          : {qty} {unit}
                        </li>
                      )
                    })}
                  </ul>
                ) : (
                  <p className="muted-text">No components listed.</p>
                )}
              </div>
            )}
            {isProcessEntity(entity) && raw && (
              <div className="kb-block">
                <h3>Process</h3>
                <h4>Inputs</h4>
                <ul>
                  {asArray(raw.inputs).map((q, i) => {
                    const obj = asObject(q)
                    if (!obj) return null
                    const itemId = String(obj.item_id ?? '')
                    const qty = Number(obj.qty ?? obj.quantity ?? 0)
                    const unit = String(obj.unit ?? 'unit')
                    return (
                      <li key={`pin-${i}`}>
                        <button className="wiki-link" onClick={() => onWikiJump(itemId)}>{itemId}</button>: {qty} {unit}
                      </li>
                    )
                  })}
                </ul>
                <h4>Outputs</h4>
                <ul>
                  {asArray(raw.outputs).map((q, i) => {
                    const obj = asObject(q)
                    if (!obj) return null
                    const itemId = String(obj.item_id ?? '')
                    const qty = Number(obj.qty ?? obj.quantity ?? 0)
                    const unit = String(obj.unit ?? 'unit')
                    return (
                      <li key={`pout-${i}`}>
                        <button className="wiki-link" onClick={() => onWikiJump(itemId)}>{itemId}</button>: {qty} {unit}
                      </li>
                    )
                  })}
                </ul>
                <h4>Required Machines</h4>
                <ul>
                  {asArray(raw.resource_requirements).map((req, i) => {
                    const obj = asObject(req)
                    if (!obj || !obj.machine_id) return null
                    const machineId = String(obj.machine_id)
                    return (
                      <li key={`m-${i}`}>
                        <button className="wiki-link" onClick={() => onWikiJump(machineId)}>{machineId}</button>
                      </li>
                    )
                  })}
                </ul>
              </div>
            )}
            {deferRefs && !isMachineEntity(entity) && references.length > 0 && (
              <div className="kb-block">
                <h3>Referenced By (KB + Articles)</h3>
                <ul>
                  {references.slice(0, 80).map((ref, i) => (
                    <li key={`${ref.kind}:${ref.id}:${i}`}>
                      <button className="wiki-link" onClick={() => onWikiJump(ref.id)}>{ref.name}</button> <small>({ref.kind})</small>
                    </li>
                  ))}
                </ul>
              </div>
            )}
            {bomTree && (
              <BomTreeSection
                result={bomTree}
                selectedItemId={bomTreeSelectedItemId}
                routeRows={ebfRouteAudit.rows}
                onWikiJump={onWikiJump}
              />
            )}
            {raw && !isBomEntity(entity) && (
              <details className="kb-block">
                <summary>Raw Entry (JSON)</summary>
                <pre>{JSON.stringify(raw, null, 2)}</pre>
              </details>
            )}
          </>
        )}
        {article && (
          <>
            <h2>{article.title}</h2>
            <MarkdownArticle content={article.content} onJump={onWikiJump} validTargets={markdownTargets} simQuery={simQuery} />
          </>
        )}
        {selectedId && !entity && !article && (
          <div className="undefined">
            <h2>Undefined Entry</h2>
            <p>{selectedId} is referenced but not defined in exported KB/articles.</p>
          </div>
        )}
      </section>
    </div>
  )
}

function formatRouteLabel(value: string): string {
  if (!value) return 'not listed'
  return value.replace(/_/g, ' ')
}

function normalizeIssueQueueReason(value: string): string {
  if (value === 'known_labor_only_route_gap' || value === 'labor_only_route_check') {
    return 'labor_only_route_gap_or_check'
  }
  return value || 'blank'
}

function formatIssueQueueReason(value: string): string {
  const normalized = normalizeIssueQueueReason(value)
  if (normalized === 'labor_only_route_gap_or_check') return 'labor only route gap/check'
  return formatRouteLabel(normalized)
}

function formatIssueMass(value: number | null): string {
  if (typeof value !== 'number' || !Number.isFinite(value)) return 'n/a'
  if (Math.abs(value) < 1) return `${value.toFixed(3)} kg`
  if (Math.abs(value) < 10) return `${value.toFixed(2)} kg`
  return `${value.toFixed(1)} kg`
}

type EbfProcessIssueGroup = {
  processId: string
  processName: string
  rows: EbfProcessIssueRow[]
  itemIds: string[]
  recipeIds: string[]
  itemCount: number
  totalMass: number
  priority: number
  decisions: Record<string, number>
  policies: Record<string, number>
  reasons: Record<string, number>
  machines: string[]
  riskFlags: string[]
  sampleNotes: string[]
}

function incrementCount(map: Record<string, number>, key: string): void {
  const normalized = key || 'blank'
  map[normalized] = (map[normalized] ?? 0) + 1
}

function formatIssueCountBadges(counts: Record<string, number>, classPrefix: string): ReactNode {
  return (
    <span className="issue-count-badges">
      {Object.entries(counts)
        .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
        .slice(0, 4)
        .map(([key, count]) => (
          <span key={key} className={`route-badge ${classPrefix}-${key}`}>
            {classPrefix === 'reason' ? formatIssueQueueReason(key) : formatRouteLabel(key)} {count}
          </span>
        ))}
    </span>
  )
}

function EbfProcessIssuesView({
  payload,
  entitiesById,
  onSelect,
}: {
  payload: EbfProcessIssuesPayload
  entitiesById: Record<string, KBEntity>
  onSelect: (id: string) => void
}) {
  const [decision, setDecision] = useState('all')
  const [policy, setPolicy] = useState('all')
  const [material, setMaterial] = useState('all')
  const [reason, setReason] = useState('all')
  const [query, setQuery] = useState('')
  const [viewMode, setViewMode] = useState<'process' | 'items'>('process')
  const [sort, setSort] = useState<'items' | 'mass' | 'priority' | 'process'>('items')

  const rows = payload.rows
  const decisionOptions = useMemo(() => Object.keys(payload.summary.worker_decision).sort(), [payload.summary.worker_decision])
  const policyOptions = useMemo(() => Object.keys(payload.summary.policy).sort(), [payload.summary.policy])
  const materialOptions = useMemo(() => {
    const counts = new Map<string, number>()
    for (const row of rows) {
      const key = row.material || 'blank'
      counts.set(key, (counts.get(key) ?? 0) + 1)
    }
    return Array.from(counts.entries()).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
  }, [rows])
  const reasonOptions = useMemo(
    () => Array.from(new Set(rows.map((row) => normalizeIssueQueueReason(row.queue_reason)))).sort(),
    [rows],
  )
  const filteredItemRows = useMemo(() => {
    const needle = query.trim().toLowerCase()
    return rows
      .filter((row) => decision === 'all' || row.worker_decision === decision)
      .filter((row) => policy === 'all' || row.policy === policy)
      .filter((row) => material === 'all' || (row.material || 'blank') === material)
      .filter((row) => reason === 'all' || normalizeIssueQueueReason(row.queue_reason) === reason)
      .filter((row) => {
        if (!needle) return true
        return [
          row.item_id,
          row.material,
          row.worker_notes,
          row.reasoning_brief,
          row.queue_reason,
          formatIssueQueueReason(row.queue_reason),
          row.worker_decision,
          row.policy,
          row.route_decision,
          row.current_process_ids.join(' '),
          row.current_machine_ids.join(' '),
        ].join(' ').toLowerCase().includes(needle)
      })
  }, [decision, material, policy, query, reason, rows])

  const processGroups = useMemo<EbfProcessIssueGroup[]>(() => {
    const groups = new Map<string, EbfProcessIssueGroup>()
    for (const row of filteredItemRows) {
      const processIds = row.current_process_ids.length > 0 ? row.current_process_ids : [row.active_recipe_id || 'unassigned_process']
      for (const processId of processIds) {
        const existing = groups.get(processId) ?? {
          processId,
          processName: entitiesById[processId]?.name || processId,
          rows: [],
          itemIds: [],
          recipeIds: [],
          itemCount: 0,
          totalMass: 0,
          priority: 9999,
          decisions: {},
          policies: {},
          reasons: {},
          machines: [],
          riskFlags: [],
          sampleNotes: [],
        }
        existing.rows.push(row)
        if (!existing.itemIds.includes(row.item_id)) existing.itemIds.push(row.item_id)
        if (row.active_recipe_id && !existing.recipeIds.includes(row.active_recipe_id)) existing.recipeIds.push(row.active_recipe_id)
        existing.totalMass += row.mass_nominal_kg ?? 0
        existing.priority = Math.min(existing.priority, row.priority ?? 9999)
        incrementCount(existing.decisions, row.worker_decision)
        incrementCount(existing.policies, row.policy)
        incrementCount(existing.reasons, normalizeIssueQueueReason(row.queue_reason))
        for (const machineId of row.current_machine_ids) if (!existing.machines.includes(machineId)) existing.machines.push(machineId)
        for (const flag of row.machine_risk_flags) if (!existing.riskFlags.includes(flag)) existing.riskFlags.push(flag)
        const note = row.worker_notes || row.reasoning_brief
        if (note && !existing.sampleNotes.includes(note)) existing.sampleNotes.push(note)
        groups.set(processId, existing)
      }
    }
    const out = Array.from(groups.values()).map((group) => ({ ...group, itemCount: group.itemIds.length }))
    return out.sort((a, b) => {
      if (sort === 'mass') return b.totalMass - a.totalMass || b.itemCount - a.itemCount || a.processId.localeCompare(b.processId)
      if (sort === 'priority') return a.priority - b.priority || b.itemCount - a.itemCount || a.processId.localeCompare(b.processId)
      if (sort === 'process') return a.processName.localeCompare(b.processName) || a.processId.localeCompare(b.processId)
      return b.itemCount - a.itemCount || b.totalMass - a.totalMass || a.processId.localeCompare(b.processId)
    })
  }, [entitiesById, filteredItemRows, sort])

  const filteredMass = useMemo(
    () => filteredItemRows.reduce((sum, row) => sum + (row.mass_nominal_kg ?? 0), 0),
    [filteredItemRows],
  )

  return (
    <div className="ebf-issues-page">
      <div className="ebf-issues-head">
        <div>
          <h1>EBF3 Process Issue Review</h1>
          <p>{viewMode === 'process' ? 'Process-level view grouped by current process reference.' : 'Item-level view showing every EBF issue item row.'}</p>
        </div>
        <div className="ebf-issue-stats">
          <div><label>Issue items</label><strong>{payload.summary.total.toLocaleString()}</strong></div>
          <div><label>Visible processes</label><strong>{processGroups.length.toLocaleString()}</strong></div>
          <div><label>Visible items</label><strong>{filteredItemRows.length.toLocaleString()}</strong></div>
          <div><label>Visible mass</label><strong>{formatIssueMass(filteredMass)}</strong></div>
        </div>
      </div>

      <div className="ebf-issue-pills">
        {Object.entries(payload.summary.worker_decision).sort((a, b) => b[1] - a[1]).map(([key, count]) => (
          <button
            key={key}
            className={`route-badge decision-${key} ${decision === key ? 'is-active' : ''}`}
            onClick={() => setDecision(decision === key ? 'all' : key)}
            title={key}
          >
            {formatRouteLabel(key)} {count}
          </button>
        ))}
      </div>

      <div className="ebf-issue-controls">
        <select value={viewMode} onChange={(event) => setViewMode(event.target.value as 'process' | 'items')} aria-label="View mode">
          <option value="process">By process</option>
          <option value="items">Issue items</option>
        </select>
        <select value={decision} onChange={(event) => setDecision(event.target.value)} aria-label="Worker decision">
          <option value="all">All decisions</option>
          {decisionOptions.map((value) => <option key={value} value={value}>{formatRouteLabel(value)}</option>)}
        </select>
        <select value={policy} onChange={(event) => setPolicy(event.target.value)} aria-label="Policy">
          <option value="all">All policies</option>
          {policyOptions.map((value) => <option key={value} value={value}>{formatRouteLabel(value)}</option>)}
        </select>
        <select value={material} onChange={(event) => setMaterial(event.target.value)} aria-label="Material">
          <option value="all">All materials ({materialOptions.length})</option>
          {materialOptions.map(([value, count]) => (
            <option key={value} value={value}>{formatRouteLabel(value)} ({count})</option>
          ))}
        </select>
        <select value={reason} onChange={(event) => setReason(event.target.value)} aria-label="Queue reason">
          <option value="all">All queue reasons</option>
          {reasonOptions.map((value) => <option key={value} value={value}>{formatIssueQueueReason(value)}</option>)}
        </select>
        <select value={sort} onChange={(event) => setSort(event.target.value as 'items' | 'mass' | 'priority' | 'process')} aria-label="Sort">
          <option value="items">Item count</option>
          <option value="mass">Mass</option>
          <option value="priority">Priority</option>
          <option value="process">Process name</option>
        </select>
        <input
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search item, material, process, machine, notes"
        />
      </div>

      {viewMode === 'process' ? (
        <EbfProcessIssueProcessTable groups={processGroups} onSelect={onSelect} />
      ) : (
        <EbfProcessIssueItemTable rows={filteredItemRows} onSelect={onSelect} />
      )}
    </div>
  )
}

function EbfProcessIssueProcessTable({
  groups,
  onSelect,
}: {
  groups: EbfProcessIssueGroup[]
  onSelect: (id: string) => void
}) {
  return (
    <div className="ebf-issue-table-wrap">
      <table className="ebf-issue-table">
        <thead>
          <tr>
            <th>Process</th>
            <th>EBF items</th>
            <th>Mass</th>
            <th>Decisions</th>
            <th>Policies</th>
            <th>Queue reasons</th>
            <th>Items</th>
          </tr>
        </thead>
        <tbody>
          {groups.map((group) => (
            <tr key={group.processId}>
              <td>
                <button className="wiki-link issue-item-link" onClick={() => onSelect(group.processId)}>{group.processName}</button>
                <div className="issue-route-meta">{group.processId}</div>
              </td>
              <td><strong>{group.itemCount.toLocaleString()}</strong></td>
              <td>{formatIssueMass(group.totalMass)}</td>
              <td>{formatIssueCountBadges(group.decisions, 'decision')}</td>
              <td>{formatIssueCountBadges(group.policies, 'policy')}</td>
              <td>{formatIssueCountBadges(group.reasons, 'reason')}</td>
              <td>
                <details className="issue-item-details">
                  <summary>{group.itemCount.toLocaleString()} items</summary>
                  <ul>
                    {group.rows
                      .slice()
                      .sort((a, b) => (a.priority ?? 9999) - (b.priority ?? 9999) || a.item_id.localeCompare(b.item_id))
                      .map((row) => (
                        <li key={`${group.processId}:${row.item_id}`}>
                          <button className="wiki-link" onClick={() => onSelect(row.item_id)}>{row.item_id}</button>
                          <span className="issue-route-meta"> {formatRouteLabel(row.worker_decision)} · {formatRouteLabel(row.policy)} · {row.material}</span>
                          {row.active_recipe_id && (
                            <span> · <button className="wiki-link" onClick={() => onSelect(row.active_recipe_id)}>{row.active_recipe_id}</button></span>
                          )}
                        </li>
                      ))}
                  </ul>
                </details>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {groups.length === 0 && <div className="empty-table">No EBF3 process groups match the current filters.</div>}
    </div>
  )
}

function EbfProcessIssueItemTable({
  rows,
  onSelect,
}: {
  rows: EbfProcessIssueRow[]
  onSelect: (id: string) => void
}) {
  const sortedRows = useMemo(
    () => rows.slice().sort((a, b) => (a.priority ?? 9999) - (b.priority ?? 9999) || a.item_id.localeCompare(b.item_id)),
    [rows],
  )
  return (
    <div className="ebf-issue-table-wrap">
      <table className="ebf-issue-table item-mode">
        <thead>
          <tr>
            <th>Item</th>
            <th>Decision</th>
            <th>Policy</th>
            <th>Mass</th>
            <th>Material</th>
            <th>Process refs</th>
            <th>Machines / risk</th>
            <th>Reason</th>
          </tr>
        </thead>
        <tbody>
          {sortedRows.map((row) => (
            <tr key={row.item_id}>
              <td>
                <button className="wiki-link issue-item-link" onClick={() => onSelect(row.item_id)}>{row.item_id}</button>
                {row.active_recipe_id && (
                  <div><button className="wiki-link issue-sub-link" onClick={() => onSelect(row.active_recipe_id)}>{row.active_recipe_id}</button></div>
                )}
              </td>
              <td><span className={`route-badge decision-${row.worker_decision}`}>{formatRouteLabel(row.worker_decision)}</span></td>
              <td><span className={`route-badge policy-${row.policy}`}>{formatRouteLabel(row.policy)}</span></td>
              <td>{formatIssueMass(row.mass_nominal_kg)}</td>
              <td>{row.material || 'n/a'}</td>
              <td>
                {row.current_process_ids.length > 0 ? row.current_process_ids.map((processId, i) => (
                  <span key={processId}>
                    {i > 0 ? ', ' : ''}
                    <button className="wiki-link" onClick={() => onSelect(processId)}>{processId}</button>
                  </span>
                )) : <span className="muted-text">none</span>}
              </td>
              <td>
                {row.current_machine_ids.length > 0 ? row.current_machine_ids.map((machineId, i) => (
                  <span key={machineId}>
                    {i > 0 ? ', ' : ''}
                    <button className="wiki-link" onClick={() => onSelect(machineId)}>{machineId}</button>
                  </span>
                )) : <span className="muted-text">none</span>}
                {row.machine_risk_flags.length > 0 && <div className="issue-route-meta">{row.machine_risk_flags.slice(0, 3).join('; ')}</div>}
              </td>
              <td>
                <div>{formatIssueQueueReason(row.queue_reason)}</div>
                <div className="issue-route-meta">{row.worker_notes || row.reasoning_brief || 'n/a'}</div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {sortedRows.length === 0 && <div className="empty-table">No EBF3 issue items match the current filters.</div>}
    </div>
  )
}

function MachineCatalogView({
  rows,
  onSelect,
}: {
  rows: MachineCatalogRow[]
  onSelect: (id: string) => void
}) {
  const [query, setQuery] = useState('')
  const [filter, setFilter] = useState<MachineCatalogFilter>('all')
  const [family, setFamily] = useState('all')
  const [sort, setSort] = useState<MachineCatalogSort>('usage')

  const families = useMemo(() => {
    const counts = new Map<string, number>()
    for (const row of rows) counts.set(row.family, (counts.get(row.family) ?? 0) + 1)
    return Array.from(counts.entries()).sort((a, b) => a[0].localeCompare(b[0]))
  }, [rows])

  const stats = useMemo(() => ({
    all: rows.length,
    ready: rows.filter((row) => row.auditTags.length === 0).length,
    audit: rows.filter((row) => row.auditTags.length > 0).length,
    target: rows.filter((row) => row.isTarget).length,
    used: rows.filter((row) => row.isUsed).length,
    seeded: rows.filter((row) => row.isSeeded).length,
    produced: rows.filter((row) => row.isProduced).length,
    unused: rows.filter((row) => !row.isUsed).length,
  }), [rows])

  const visibleRows = useMemo(() => {
    const q = query.trim().toLowerCase()
    const filtered = rows.filter((row) => {
      if (filter === 'target' && !row.isTarget) return false
      if (filter === 'ready' && row.auditTags.length > 0) return false
      if (filter === 'audit' && row.auditTags.length === 0) return false
      if (filter === 'used' && !row.isUsed) return false
      if (filter === 'seeded' && !row.isSeeded) return false
      if (filter === 'produced' && !row.isProduced) return false
      if (filter === 'unused' && row.isUsed) return false
      if (family !== 'all' && row.family !== family) return false
      if (!q) return true
      return [
        row.id,
        row.label,
        row.family,
        row.path,
        row.recipeId ?? '',
        row.bomId ?? '',
        ...row.capabilities,
        ...row.auditTags,
      ].some((value) => value.toLowerCase().includes(q))
    })

    return [...filtered].sort((a, b) => {
      if (sort === 'name') return a.label.localeCompare(b.label) || a.id.localeCompare(b.id)
      return Number(b.isUsed) - Number(a.isUsed)
        || b.runCount - a.runCount
        || b.busyHours - a.busyHours
        || a.label.localeCompare(b.label)
    })
  }, [rows, query, filter, family, sort])

  const groupedRows = useMemo(() => {
    const groups = new Map<string, MachineCatalogRow[]>()
    for (const row of visibleRows) {
      const bucket = groups.get(row.family) ?? []
      bucket.push(row)
      groups.set(row.family, bucket)
    }
    return Array.from(groups.entries()).sort((a, b) => {
      if (family !== 'all') return 0
      const ai = MACHINE_FAMILY_ORDER.indexOf(a[0])
      const bi = MACHINE_FAMILY_ORDER.indexOf(b[0])
      return (ai === -1 ? 999 : ai) - (bi === -1 ? 999 : bi) || a[0].localeCompare(b[0])
    })
  }, [visibleRows, family])

  const filters: Array<{ key: MachineCatalogFilter; label: string; count: number }> = [
    { key: 'all', label: 'All', count: stats.all },
    { key: 'ready', label: 'Ready', count: stats.ready },
    { key: 'audit', label: 'Audit', count: stats.audit },
    { key: 'target', label: 'Target', count: stats.target },
    { key: 'used', label: 'Used', count: stats.used },
    { key: 'seeded', label: 'Seeded', count: stats.seeded },
    { key: 'produced', label: 'Produced', count: stats.produced },
    { key: 'unused', label: 'Unused', count: stats.unused },
  ]

  return (
    <section className="machine-page">
      <div className="machine-head">
        <div>
          <h1>Machines</h1>
          <p>{visibleRows.length.toLocaleString()} shown from {rows.length.toLocaleString()} KB machine entries</p>
        </div>
        <div className="machine-stat-grid">
          <div><label>Total</label><strong>{stats.all.toLocaleString()}</strong></div>
          <div><label>Target set</label><strong>{stats.target.toLocaleString()}</strong></div>
          <div><label>Used in current run</label><strong>{stats.used.toLocaleString()}</strong></div>
          <div><label>Seeded</label><strong>{stats.seeded.toLocaleString()}</strong></div>
        </div>
      </div>

      <div className="machine-controls">
        <div className="segmented">
          {filters.map((item) => (
            <button
              key={item.key}
              className={filter === item.key ? 'active' : ''}
              onClick={() => setFilter(item.key)}
            >
              {item.label} <span>{item.count}</span>
            </button>
          ))}
        </div>
        <input
          className="machine-search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search machine id, name, capability, recipe, or BOM"
        />
        <select value={family} onChange={(e) => setFamily(e.target.value)}>
          <option value="all">All families</option>
          {families.map(([name, count]) => (
            <option key={name} value={name}>{name} ({count})</option>
          ))}
        </select>
        <select value={sort} onChange={(e) => setSort(e.target.value as MachineCatalogSort)}>
          <option value="usage">Sort by usage</option>
          <option value="name">Sort by name</option>
        </select>
      </div>

      <div className="machine-legend">
        <span><span className="machine-mini-badge target">T</span> Target</span>
        <span><span className="machine-mini-badge used">U</span> Used in current run</span>
        <span><span className="machine-mini-badge seeded">S</span> Seeded</span>
        <span><span className="machine-mini-badge produced">P</span> Produced</span>
        <span><span className="machine-mini-badge audit">A</span> Needs audit before process selection</span>
      </div>

      <div className="machine-matrix-wrap">
        {groupedRows.map(([groupName, groupRows]) => (
          <section key={groupName} className="machine-group">
            <header>
              <h2>{groupName} <span>({groupRows.length.toLocaleString()} machines)</span></h2>
            </header>
            <div className="machine-cell-grid">
              {groupRows.map((row) => (
                <button
                  key={row.id}
                  className={`machine-cell ${row.isTarget ? 'is-target' : ''} ${row.isUsed ? 'is-used' : ''} ${row.auditTags.length ? 'is-audit' : ''}`}
                  onClick={() => onSelect(row.id)}
                  title={`${row.label}\n${row.id}\n${row.family}\n${row.capabilities.slice(0, 6).join(', ') || 'no capabilities'}${row.auditTags.length ? `\nAudit: ${row.auditTags.map(formatMachineAuditTag).join(', ')}` : ''}`}
                >
                  <span className="machine-cell-name">{row.label}</span>
                  <span className="machine-cell-id">{row.id}</span>
                  <span className="machine-cell-meta">
                    {row.isTarget && <span className="machine-mini-badge target">T</span>}
                    {row.isUsed && <span className="machine-mini-badge used">U</span>}
                    {row.isSeeded && <span className="machine-mini-badge seeded">S</span>}
                    {row.isProduced && <span className="machine-mini-badge produced">P</span>}
                    {row.auditTags.length > 0 && <span className="machine-mini-badge audit">A</span>}
                    <span className="machine-cell-runs">{row.runCount ? `${row.runCount} runs` : row.massLabel}</span>
                    <span className="machine-cell-steps">{row.supportedProcessCount} steps</span>
                  </span>
                </button>
              ))}
            </div>
          </section>
        ))}
        {visibleRows.length === 0 && <div className="empty-table">No machines match the current filters.</div>}
      </div>
    </section>
  )
}

function KBSearchView({
  indexRows,
  search,
  onSearch,
  topMachines,
  topProcesses,
  topRecipes,
  onSelect,
}: {
  indexRows: KBSearchRow[]
  search: string
  onSearch: (s: string) => void
  topMachines: Array<{ id: string; label: string; count: number; type: string }>
  topProcesses: Array<{ id: string; label: string; count: number; type: string }>
  topRecipes: Array<{ id: string; label: string; count: number; type: string }>
  onSelect: (id: string) => void
}) {
  const [typeFilter, setTypeFilter] = useState<KBSearchTypeFilter>('all')
  const query = search.trim().toLowerCase()
  const queryTerms = useMemo(() => query.split(/\s+/).filter(Boolean), [query])
  const searchResults = useMemo(() => {
    if (queryTerms.length === 0) return []
    return indexRows
      .filter((row) => matchesKbTypeFilter(row, typeFilter))
      .filter((row) => {
        const text = row.searchableText.toLowerCase()
        return queryTerms.every((term) => text.includes(term))
      })
      .map((row) => ({ row, score: scoreKbSearchRow(row, queryTerms) }))
      .sort((a, b) => b.score - a.score || kbTypeSortWeight(a.row.type) - kbTypeSortWeight(b.row.type) || a.row.label.localeCompare(b.row.label))
      .slice(0, 80)
      .map(({ row }) => row)
  }, [indexRows, queryTerms, typeFilter])
  const resultCounts = useMemo(() => {
    const counts: Record<KBSearchTypeFilter, number> = { all: 0, process: 0, machine: 0, recipe: 0, bom: 0, item: 0, article: 0 }
    if (queryTerms.length === 0) return counts
    for (const row of indexRows) {
      const text = row.searchableText.toLowerCase()
      if (!queryTerms.every((term) => text.includes(term))) continue
      counts.all += 1
      const normalized = normalizeKbSearchType(row.type)
      if (normalized === 'process' || normalized === 'machine' || normalized === 'recipe' || normalized === 'bom' || normalized === 'article') {
        counts[normalized] += 1
      } else {
        counts.item += 1
      }
    }
    return counts
  }, [indexRows, queryTerms])
  const showResults = query.length > 0
  const filters: Array<{ id: KBSearchTypeFilter; label: string }> = [
    { id: 'all', label: 'All' },
    { id: 'process', label: 'Processes' },
    { id: 'machine', label: 'Machines' },
    { id: 'recipe', label: 'Recipes' },
    { id: 'bom', label: 'BOMs' },
    { id: 'item', label: 'Items' },
    { id: 'article', label: 'Articles' },
  ]

  return (
    <div className="kb-page">
      <section className="kb-search-shell">
        <div className="kb-search-center">
          <h1>Knowledge Base Search</h1>
          <div className="kb-search-input-wrap">
            <input
              className="kb-search-input"
              value={search}
              onChange={(e) => onSearch(e.target.value)}
              placeholder="Search machines, processes, recipes, and articles"
            />
          </div>
        </div>

        {showResults && (
          <section className="kb-results-panel">
            <div className="kb-filter-row">
              {filters.map((filter) => (
                <button
                  key={filter.id}
                  className={typeFilter === filter.id ? 'kb-filter active' : 'kb-filter'}
                  onClick={() => setTypeFilter(filter.id)}
                >
                  {filter.label} <span>{resultCounts[filter.id].toLocaleString()}</span>
                </button>
              ))}
            </div>
            <div className="kb-result-summary">
              {searchResults.length.toLocaleString()} shown from {resultCounts[typeFilter].toLocaleString()} matches
            </div>
            <div className="kb-results-list">
              {searchResults.length === 0 && <div className="kb-suggest-empty">No matches.</div>}
              {searchResults.map((row) => (
                <button key={`${row.type}:${row.id}`} className="kb-result-row" onClick={() => onSelect(row.id)}>
                  <span className="kb-result-main">
                    <strong>{row.label}</strong>
                    <span>{row.id}</span>
                  </span>
                  <span className="kb-result-side">
                    <small>{row.type}</small>
                    <em>{row.path}</em>
                  </span>
                </button>
              ))}
            </div>
          </section>
        )}

        {!showResults && <div className="kb-featured-grid">
          <section className="kb-featured-panel">
            <h3>Most Used Machines</h3>
            <div className="kb-list">
              {topMachines.map((row) => (
                <button key={`${row.type}:${row.id}`} className="kb-row" onClick={() => onSelect(row.id)}>
                  <span>{row.label}</span>
                  <small>{row.count} runs</small>
                </button>
              ))}
            </div>
          </section>
          <section className="kb-featured-panel">
            <h3>Most Used Processes</h3>
            <div className="kb-list">
              {topProcesses.map((row) => (
                <button key={`${row.type}:${row.id}`} className="kb-row" onClick={() => onSelect(row.id)}>
                  <span>{row.label}</span>
                  <small>{row.count} runs</small>
                </button>
              ))}
            </div>
          </section>
          <section className="kb-featured-panel">
            <h3>Most Used Recipes</h3>
            <div className="kb-list">
              {topRecipes.map((row) => (
                <button key={`${row.type}:${row.id}`} className="kb-row" onClick={() => onSelect(row.id)}>
                  <span>{row.label}</span>
                  <small>{row.count} runs</small>
                </button>
              ))}
            </div>
          </section>
        </div>}
      </section>
    </div>
  )
}

function Drawer({
  run,
  entitiesById,
  mode,
  recipeRuns,
  inventory,
  inventoryStart,
  inventoryLabel,
  recipeContext,
  onClose,
  onOpenKB,
}: {
  run: ProcessRun
  entitiesById: Record<string, KBEntity>
  mode: 'process' | 'recipe'
  recipeRuns: ProcessRun[]
  inventory: QuantityMap
  inventoryStart?: QuantityMap
  inventoryLabel: string
  recipeContext?: { finalOutputs: QuantityMap; consumedOutputIds: Set<string> }
  onClose: () => void
  onOpenKB: (id: string) => void
}) {
  const sortedRecipeRuns = recipeRuns
    .slice()
    .sort((a, b) => (a.start_time ?? 0) - (b.start_time ?? 0))
  const aggregateStart = sortedRecipeRuns.length > 0 ? Math.min(...sortedRecipeRuns.map((r) => r.start_time ?? 0)) : (run.start_time ?? 0)
  const aggregateEnd = sortedRecipeRuns.length > 0
    ? Math.max(...sortedRecipeRuns.map((r) => (r.end_time ?? r.start_time ?? 0)))
    : (run.end_time ?? run.start_time ?? 0)
  const aggregateDuration = Math.max(0, aggregateEnd - aggregateStart)
  const aggregateEnergy = sortedRecipeRuns.reduce((acc, r) => acc + (r.energy_kwh ?? 0), 0)
  const hasFailedStep = sortedRecipeRuns.some((r) => r.status === 'failed')
  const hasPendingStep = sortedRecipeRuns.some((r) => r.status === 'pending')
  const aggregateStatus: ProcessRun['status'] = hasFailedStep ? 'failed' : (hasPendingStep ? 'pending' : 'success')
  const recipeTitle = run.recipe_id ? (entitiesById[run.recipe_id]?.name || run.recipe_id) : 'Recipe Run'
  const processName = entitiesById[run.process_id]?.name
  const hasDistinctName = Boolean(processName && processName !== run.process_id)
  const title = mode === 'recipe'
    ? recipeTitle
    : (hasDistinctName ? String(processName) : run.process_id)
  const status = mode === 'recipe' ? aggregateStatus : run.status
  const displayStart = mode === 'recipe' ? aggregateStart : (run.start_time ?? 0)
  const displayEnd = mode === 'recipe' ? aggregateEnd : (run.end_time ?? run.start_time ?? 0)
  const displayDuration = mode === 'recipe' ? aggregateDuration : (run.duration_hours ?? 0)
  const displayEnergy = mode === 'recipe' ? aggregateEnergy : (run.energy_kwh ?? 0)
  const goalTags = getGoalTags(run)
  const infoCards: Array<{ label: string; value: string }> = [
    { label: 'Time', value: `${displayStart.toFixed(2)}h -> ${displayEnd.toFixed(2)}h` },
    { label: 'Duration', value: `${displayDuration.toFixed(2)}h` },
    { label: 'Energy', value: `${displayEnergy.toFixed(2)} kWh` },
  ]
  if (mode === 'process') infoCards.unshift({ label: 'Machine', value: run.machine_type ?? 'n/a' })
  const statusLabel = status === 'success' ? 'OK' : (status === 'failed' ? 'FAILED' : 'PENDING')
  const goalMachineTag = goalTags['goal.machine_id']
  const goalMachineIds = goalMachineTag
    ? goalMachineTag.split('|').map((x) => x.trim()).filter(Boolean)
    : []
  const linkedId = (id: string) => (
    <button className="drawer-link-btn" onClick={() => onOpenKB(id)}>{id}</button>
  )
  return (
    <aside className="drawer">
      <div className="drawer-head">
        <div className="drawer-title-wrap">
          <h3>{title}</h3>
          <span className={`status-pill ${status}`}>{statusLabel}</span>
        </div>
        <button onClick={onClose}>Close</button>
      </div>
      <div className="drawer-body">
        <div className="drawer-meta-grid">
          {infoCards.map((card) => (
            <div key={card.label} className="drawer-meta-card">
              <label>{card.label}</label>
              <strong>{card.value}</strong>
            </div>
          ))}
        </div>
        {mode === 'recipe' && (
          <div className="drawer-section">
            <p className="drawer-subtle"><strong>Recipe:</strong> {run.recipe_id ? linkedId(run.recipe_id) : 'unknown'}</p>
            {run.recipe_run_id && <p className="drawer-subtle"><strong>Run ID:</strong> {run.recipe_run_id}</p>}
            {goalMachineIds.length > 0 && (
              <p className="drawer-subtle">
                <strong>Goal Machine{goalMachineIds.length > 1 ? 's' : ''}:</strong>{' '}
                {goalMachineIds.map((id, idx) => (
                  <span key={id}>
                    {idx > 0 ? ', ' : ''}
                    {linkedId(id)}
                  </span>
                ))}
              </p>
            )}
            {run.recipe_id && (
              <div className="drawer-links">
                <button className="drawer-link-btn" onClick={() => onOpenKB(run.recipe_id!)}>Open Recipe KB</button>
              </div>
            )}
            {recipeContext && (
              <>
                <h4>Final Outputs</h4>
                <ul>
                  {Object.entries(recipeContext.finalOutputs).map(([id, q]) => <li key={id}>{linkedId(id)}: {formatQty(q)}</li>)}
                </ul>
              </>
            )}
            <h4>Selected Step Inputs</h4>
            <ul>
              {Object.entries(run.inputs).map(([id, q]) => <li key={id}>{linkedId(id)}: {formatQty(q)}</li>)}
              {Object.keys(run.inputs).length === 0 && <li>None</li>}
            </ul>
            {sortedRecipeRuns.length > 0 && (
              <>
                <h4>Steps</h4>
                <ul>
                  {sortedRecipeRuns.map((step) => {
                    const stepName = entitiesById[step.process_id]?.name
                    return (
                      <li key={step.process_run_id}>
                        <span className={`step-pill ${step.status}`}>{step.status}</span> {stepName && stepName !== step.process_id ? `${stepName} (` : ''}{linkedId(step.process_id)}{stepName && stepName !== step.process_id ? ')' : ''}: {(step.start_time ?? 0).toFixed(2)}h {'->'} {(step.end_time ?? 0).toFixed(2)}h
                      </li>
                    )
                  })}
                </ul>
              </>
            )}
          </div>
        )}
        <div className="drawer-section">
          {hasDistinctName && <p className="drawer-subtle"><strong>Process ID:</strong> {linkedId(run.process_id)}</p>}
          <p className="drawer-subtle"><strong>Recipe:</strong> {run.recipe_id ? linkedId(run.recipe_id) : 'unknown'}</p>
          <div className="drawer-links">
            {run.machine_type && <button className="drawer-link-btn" onClick={() => onOpenKB(run.machine_type!)}>Open Machine KB</button>}
            {run.recipe_id && <button className="drawer-link-btn" onClick={() => onOpenKB(run.recipe_id!)}>Open Recipe KB</button>}
          </div>
          {run.reserved_machines && run.reserved_machines.length > 0 && (
            <>
              <h4>Reserved Machines</h4>
              <ul>
                {run.reserved_machines.map((m, idx) => (
                  <li key={`${m.machine_id}:${idx}`}>
                    {linkedId(m.machine_id)}: {m.qty} {m.unit}
                  </li>
                ))}
              </ul>
            </>
          )}
        </div>
        {run.error_message && <p className="error-text">{run.error_message}</p>}
        {mode === 'process' && (
          <div className="drawer-section">
            <h4>Inputs</h4>
            <ul>
              {Object.entries(run.inputs).map(([id, q]) => <li key={id}>{linkedId(id)}: {formatQty(q)}</li>)}
              {Object.keys(run.inputs).length === 0 && <li>None</li>}
            </ul>
            <h4>Outputs</h4>
            <ul>
              {Object.entries(run.outputs).map(([id, q]) => <li key={id}>{linkedId(id)}: {formatQty(q)}</li>)}
              {Object.keys(run.outputs).length === 0 && <li>None</li>}
            </ul>
          </div>
        )}
        <div className="drawer-section">
          <h4>Inventory Snapshot ({inventoryLabel})</h4>
          <div className="inventory-snapshot">
            {Object.entries(inventory).map(([id, q]) => (
              <div key={id} className="inv-row">
                <span>{linkedId(id)}</span>
                <span>{formatQty(q)}</span>
              </div>
            ))}
          </div>
        </div>
        {mode === 'recipe' && inventoryStart && (
          <details className="drawer-section">
            <summary>Inventory Snapshot (beginning of recipe)</summary>
            <div className="inventory-snapshot">
              {Object.entries(inventoryStart).map(([id, q]) => (
                <div key={id} className="inv-row">
                  <span>{linkedId(id)}</span>
                  <span>{formatQty(q)}</span>
                </div>
              ))}
            </div>
          </details>
        )}
        {Object.keys(goalTags).length > 0 && (
          <details className="drawer-section">
            <summary>Context Tags</summary>
            <ul>
              {Object.entries(goalTags).map(([key, value]) => (
                <li key={key}>{key}={value}</li>
              ))}
            </ul>
          </details>
        )}
      </div>
    </aside>
  )
}

function TimeDrawer({
  timeHours,
  inventory,
  onClose,
}: {
  timeHours: number
  inventory: QuantityMap
  onClose: () => void
}) {
  return (
    <aside className="drawer">
      <div className="drawer-head">
        <div className="drawer-title-wrap">
          <h3>Time Cursor</h3>
          <span className="status-pill pending">{timeHours.toFixed(2)}h</span>
        </div>
        <button onClick={onClose}>Close</button>
      </div>
      <div className="drawer-body">
        <div className="drawer-meta-grid">
          <div className="drawer-meta-card">
            <label>Snapshot Time</label>
            <strong>{timeHours.toFixed(2)}h</strong>
          </div>
          <div className="drawer-meta-card">
            <label>Unique Items</label>
            <strong>{Object.keys(inventory).length}</strong>
          </div>
        </div>
        <div className="drawer-section">
          <h4>Inventory At Cursor</h4>
          <div className="inventory-snapshot">
            {Object.entries(inventory).map(([id, q]) => (
              <div key={id} className="inv-row">
                <span>{id}</span>
                <span>{formatQty(q)}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </aside>
  )
}
