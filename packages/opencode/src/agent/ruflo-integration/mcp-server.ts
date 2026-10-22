import { Context } from "effect"

export interface MCPServerConfig {
  command: string
  args: string[]
  running: boolean
}

export const MCPServerService = Context.Service<MCPServerConfig, MCPServerConfig>()("@openfable/ruflo/mcp-server")
