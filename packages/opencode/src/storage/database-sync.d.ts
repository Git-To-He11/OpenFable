declare module "node:sqlite" {
  interface DatabaseSync {
    query(sql: string): {
      all(...params: any[]): any[]
      get(...params: any[]): any
      run(...params: any[]): { changes: number; lastInsertRowid: number | bigint }
    }
    run(sql: string, ...params: any[]): { changes: number; lastInsertRowid: number | bigint }
    prepare(sql: string): StatementSync
    exec(sql: string): void
    close(): void
    transaction<T>(fn: (tx: DatabaseSync) => T, options?: { behavior?: "deferred" | "immediate" | "exclusive" }): T
  }

  interface StatementSync {
    all(...params: any[]): any[]
    get(...params: any[]): any
    run(...params: any[]): { changes: number; lastInsertRowid: number | bigint }
  }
}