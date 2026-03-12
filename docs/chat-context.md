# Chat Context

## Project Summary

This project is an event-driven ambient assistant runtime that coordinates reasoning, tool use, and response generation through a shared asynchronous event architecture.

## Current System Architecture

Implemented subsystems:

- FastAPI ingress endpoint
- Async event bus
- Orchestrator
- Reasoning engine
- Tool resolver and example knowledge tool
- Policy stub
- Response generator
- Event logger
- Configuration via dotenv
- Docker dev container environment

## Current Working Event Flow

1. assistant.message.received
2. assistant.reasoning.step
3. assistant.tool.request
4. assistant.tool.invoke
5. assistant.tool.result
6. assistant.response.generated

## Next Development Step

Memory Phase 1: episodic memory recording.
