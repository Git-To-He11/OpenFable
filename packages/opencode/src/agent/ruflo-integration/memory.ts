import { Effect, Context } from "effect"

export interface MemoryStore {
  store(key: string, value: unknown): Promise<void>
  retrieve(key: string): Promise<unknown>
  query(query: string): Promise<unknown[]>
}

export const MemoryService = Context.Service<MemoryStore, MemoryStore>()("@openfable/ruflo/memory")

export const store = (key: string, value: unknown): Effect.Effect<void, never, never> =>
  Effect.sync(() => {
    console.log("[RUFLO MEMORY] store", key)
  })
