export type QuantityMap = Record<string, { quantity: number; unit: string }>

export type ProcessRun = {
  process_run_id: string
  process_id: string
  recipe_run_id: string | null
  recipe_id: string | null
  start_time: number | null
  end_time: number | null
  duration_hours: number | null
  energy_kwh: number | null
  status: 'success' | 'failed' | 'pending'
  machine_type: string | null
  lane_id: string | null
  inputs: QuantityMap
  outputs: QuantityMap
  error_message?: string | null
}

export type MachineLane = {
  machine_type: string
  lane_id: string
  lane_index: number
}

export type InventoryCheckpoint = {
  idx: number
  time_hours: number
  process_complete_count: number
  inventory: QuantityMap
}

export type InventoryDelta = {
  process_run_id: string
  time_hours: number | null
  delta: QuantityMap
}

export type SimData = {
  sim_id: string
  summary: {
    sim_id: string
    time_hours: number
    time_days: number
    total_energy_kwh: number
    process_runs_total: number
    process_runs_completed: number
    process_runs_by_status: Record<string, number>
    inventory_items: number
    imports_tracked: number
  }
  machine_lanes: MachineLane[]
  process_runs: ProcessRun[]
  inventory_checkpoints: InventoryCheckpoint[]
  inventory_deltas: InventoryDelta[]
}

export type KBEntity = {
  id: string
  kind: string
  category?: string | null
  path: string
  name: string
  raw?: Record<string, unknown>
  sim_stats?: {
    process_run_count?: number
    produced_quantity_total?: number
  }
}

export type KBEntitiesPayload = { entities: KBEntity[] }

export type Article = {
  id: string
  title: string
  path: string
  frontmatter: Record<string, unknown>
  content: string
  wiki_links: string[]
}

export type ArticlesPayload = { articles: Article[] }

export type Warnings = {
  unresolved_wiki_links: Array<{ source_article_id: string; target: string; message: string }>
  missing_kb_categories: string[]
  undefined_references: string[]
}

export type SimQueryData = {
  version: string
  scalars: Record<string, string | number | boolean | null>
  tables: Record<string, Array<Record<string, unknown>>>
}
