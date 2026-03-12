# Architecture

## Overview

This project is an event-driven ambient AI assistant runtime designed to support reasoning, tool use, memory, environment awareness, and automation.

## Core Architecture Principles

- Event-driven communication: subsystems exchange state and intent through events.
- Subsystem isolation: each subsystem has a focused responsibility and minimal coupling.
- Asynchronous event bus: event handling is non-blocking and supports concurrent workflows.
- Traceable event envelopes: all events use a standard envelope with trace metadata.
- Capability-based tools: tool access is mediated through explicit capabilities and resolution.

## System Components

- API Layer (FastAPI ingress): accepts user requests and emits initial assistant events.
- Event Bus: async publish/subscribe backbone connecting all subsystems.
- Orchestrator: coordinates high-level assistant flow by reacting to events.
- Reasoning Engine: performs assistant reasoning steps and emits intermediate decisions.
- Tool Resolver: maps tool requests to approved tool implementations.
- Tools: executable capabilities used by the assistant during reasoning.
- Memory subsystem (planned): persistent episodic and semantic context storage.
- Environment service (planned): ambient signal ingestion and normalization.
- Automation engine (planned): proactive and scheduled behavior execution.
- Policy engine: safety and permission decision layer.
- Response generator: produces final user-facing assistant responses.
- Event logger: records event traffic for observability and debugging.

## Event Model

Standard event envelope fields:

- id
- type
- timestamp
- trace_id
- parent_id
- user_id
- context
- payload

The trace_id enables reconstruction of end-to-end reasoning chains across subsystems.

## Current Event Flow

Currently implemented pipeline:

1. assistant.message.received
2. assistant.reasoning.step
3. assistant.tool.request
4. assistant.tool.invoke
5. assistant.tool.result
6. assistant.response.generated

## Development Environment

Development runs inside a Docker dev container using VS Code Dev Containers.
