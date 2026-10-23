import { Effect, Layer, Context } from "effect"

export interface SwarmConfig {
  topology: "mesh" | "hierarchical" | "adaptive"
  consensus: boolean
  agentCount: number
  federationEnabled: boolean
}

export interface AgentFederationResult {
  discovered: string[]
  verified: string[]
  rejected: string[]
  trustLevel: "low" | "medium" | "high" | "verified"
}

export const SwarmService = Context.Service<{ init: Effect.Effect<SwarmConfig, never> }, { init: Effect.Effect<SwarmConfig, never> }>()("@openfable/ruflo/swarm")

export const initSwarm = (cfg: Partial<SwarmConfig>): Effect.Effect<SwarmConfig, never, never> =>
  Effect.sync(() => ({
    topology: cfg.topology ?? "mesh",
    consensus: cfg.consensus ?? true,
    agentCount: cfg.agentCount ?? 5,
    federationEnabled: cfg.federationEnabled ?? true,
  }))
