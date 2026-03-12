# AI Context

## Project Purpose

The goal is to build an ambient AI assistant platform, not a simple request-response chatbot. The runtime is designed to reason over events, use tools as capabilities, and evolve into a context-aware assistant system.

## Architecture Rules

- Subsystems communicate only through the event bus.
- No direct subsystem-to-subsystem calls.
- Every event uses the standard event envelope.
- Each event carries a trace_id.
- Subsystems self-register with the event bus.

## Current System State

Implemented components:

- Docker dev container
- Configuration system using dotenv
- Async event bus
- Event logger
- Orchestrator
- Reasoning engine
- Tool resolver
- Example knowledge tool
- Policy stub
- Response generator
- FastAPI API endpoint

## Next Planned Subsystem

Memory Phase 1: episodic recording.
