import { useEffect, useMemo, useRef, useState, type ReactNode } from 'react'
import type {
  Article,
  ArticlesPayload,
  InventoryCheckpoint,
  InventoryDelta,
  KBEntitiesPayload,
  KBEntity,
  MachineAssignment,
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
  | { view: 'wiki'; id?: string }
  | { view: 'kbsearch' }

const BAR_MIN_PX = 3
const ROW_HEIGHT = 28
const WIKI_HOME_ID = 'about_seres'
type ColorMode = 'status' | 'process' | 'recipe' | 'goal'

function parseRoute(hash: string): Route {
  const clean = hash.replace(/^#\/?/, '')
  const parts = clean.split('/').filter(Boolean)
  if (parts[0] === 'gantt') return { view: 'gantt' }
  if (parts[0] === 'recipes') return { view: 'recipes' }
  if (parts[0] === 'wiki') return { view: 'wiki', id: parts[1] }
  if (parts[0] === 'kb-search') return { view: 'kbsearch' }
  if (parts[0] === 'home') return { view: 'home' }
  return { view: 'wiki', id: WIKI_HOME_ID }
}

function hashTo(route: Route): string {
  if (route.view === 'gantt') return '#/gantt'
  if (route.view === 'recipes') return '#/recipes'
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
          const tag = `h${Math.min(6, Math.max(1, b.level))}` as keyof JSX.IntrinsicElements
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

function isProcessEntity(entity: KBEntity): boolean {
  return entity.kind === 'process'
}

function isMachineEntity(entity: KBEntity): boolean {
  return entity.kind === 'machine'
}

function collectRefIds(node: unknown, out: Set<string>): void {
  if (Array.isArray(node)) {
    for (const entry of node) collectRefIds(entry, out)
    return
  }
  if (!node || typeof node !== 'object') return
  const obj = node as Record<string, unknown>
  for (const [key, value] of Object.entries(obj)) {
    if (key === 'item_id' || key === 'machine_id' || key === 'process_id' || key === 'recipe_id' || key === 'target_item_id') {
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

export function App() {
  const [route, setRoute] = useState<Route>(() => parseRoute(window.location.hash || `#/wiki/${WIKI_HOME_ID}`))
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)
  const [simData, setSimData] = useState<SimData | null>(null)
  const [simQuery, setSimQuery] = useState<SimQueryData | null>(null)
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
    ])
      .then(([sim, kb, art, warn, query]) => {
        setSimData(sim)
        setEntities(kb.entities)
        setArticles(art.articles)
        setWarnings(warn)
        setSimQuery(query)
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

  const openWiki = (id: string) => navigate({ view: 'wiki', id })

  const kbIndex = useMemo(() => {
    const kbRows = entities.map((e) => ({ id: e.id, label: e.name || e.id, type: e.kind }))
    const articleRows = articles.map((a) => ({ id: a.id, label: a.title, type: 'article' }))
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
        <button className={route.view === 'wiki' ? 'nav active' : 'nav'} onClick={() => navigate({ view: 'wiki', id: WIKI_HOME_ID })}>
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
            onWikiJump={(id) => navigate({ view: 'wiki', id })}
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
            onSelect={(id) => navigate({ view: 'wiki', id })}
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
            {recipesTargetingEntity.length > 0 && (
              <p>
                <strong>Recipes targeting this item:</strong>{' '}
                {recipesTargetingEntity.map((r, i) => (
                  <span key={r.id}>
                    {i > 0 ? ', ' : ''}
                    <button className="wiki-link" onClick={() => onWikiJump(r.id)}>{r.id}</button>
                  </span>
                ))}
              </p>
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
                <h3>Machine Entry</h3>
                <p><strong>Capabilities:</strong> {JSON.stringify(raw.capabilities ?? raw.resource_types ?? [])}</p>
                <p><strong>Requires IDs:</strong> {JSON.stringify(raw.requires_ids ?? [])}</p>
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
            {isRecipeEntity(entity) && raw && (
              <div className="kb-block">
                <h3>Recipe</h3>
                {Boolean(raw.target_item_id) && (
                  <p>
                    <strong>Target:</strong>{' '}
                    <button className="wiki-link" onClick={() => onWikiJump(String(raw.target_item_id))}>{String(raw.target_item_id)}</button>
                  </p>
                )}
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
            {deferRefs && references.length > 0 && (
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
            {raw && (
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

function KBSearchView({
  indexRows,
  search,
  onSearch,
  topMachines,
  topProcesses,
  topRecipes,
  onSelect,
}: {
  indexRows: Array<{ id: string; label: string; type: string }>
  search: string
  onSearch: (s: string) => void
  topMachines: Array<{ id: string; label: string; count: number; type: string }>
  topProcesses: Array<{ id: string; label: string; count: number; type: string }>
  topRecipes: Array<{ id: string; label: string; count: number; type: string }>
  onSelect: (id: string) => void
}) {
  const query = search.trim().toLowerCase()
  const suggestions = useMemo(
    () =>
      indexRows
        .filter((row) => !query || row.id.toLowerCase().includes(query) || row.label.toLowerCase().includes(query))
        .slice(0, 12),
    [indexRows, query],
  )
  const showSuggestions = query.length > 0

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
            {showSuggestions && (
              <div className="kb-suggest">
                {suggestions.length === 0 && <div className="kb-suggest-empty">No matches.</div>}
                {suggestions.map((row) => (
                  <button key={`${row.type}:${row.id}`} className="kb-suggest-row" onClick={() => onSelect(row.id)}>
                    <span>{row.label}</span>
                    <small>{row.type}</small>
                  </button>
                ))}
              </div>
            )}
          </div>
        </div>

        <div className="kb-featured-grid">
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
        </div>
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
