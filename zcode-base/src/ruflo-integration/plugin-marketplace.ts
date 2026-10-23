import { Effect, Context } from "effect"

export interface PluginInfo {
  id: string
  name: string
  version: string
  installed: boolean
  active: boolean
}

export const PluginMarketplaceService = Context.Service<{ listPlugins: () => Promise<PluginInfo[]> }, { listPlugins: () => Promise<PluginInfo[]> }>()("@openfable/ruflo/plugin-marketplace")

export const listPlugins = (): Effect.Effect<PluginInfo[], never, never> =>
  Effect.sync(() => [
    { id: "ruflo-core", name: "Core", version: "1.0.0", installed: true, active: true },
    { id: "ruflo-swarm", name: "Swarm", version: "1.0.0", installed: true, active: true },
    { id: "ruflo-rag-memory", name: "RAG Memory", version: "1.0.0", installed: true, active: true },
    { id: "ruflo-security", name: "Security Audit", version: "1.0.0", installed: true, active: true },
    { id: "ruflo-console", name: "Console", version: "1.0.0", installed: true, active: true },
    { id: "ruflo-mods", name: "Mods", version: "1.0.0", installed: true, active: true },
  ])
