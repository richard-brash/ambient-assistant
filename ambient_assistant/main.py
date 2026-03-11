from __future__ import annotations

import logging

import uvicorn
from fastapi import FastAPI

from ambient_assistant.api.routes import router
from ambient_assistant.assistant.orchestrator import Orchestrator
from ambient_assistant.assistant.reasoning import ReasoningEngine
from ambient_assistant.assistant.response import ResponseHandler
from ambient_assistant.automation.engine import AutomationEngine
from ambient_assistant.config import get_config
from ambient_assistant.environment.service import EnvironmentService
from ambient_assistant.events.bus import EventBus
from ambient_assistant.memory.manager import MemoryManager
from ambient_assistant.policy.engine import PolicyEngine
from ambient_assistant.system.event_logger import EventLogger
from ambient_assistant.tools.resolver import ToolResolver

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
)

app = FastAPI(title="Ambient Assistant", version="0.1.0")

# ── Shared event bus ──────────────────────────────────────────────────────────
bus = EventBus()

# ── Subsystem instantiation (each self-registers on the bus) ─────────────────
# Order: logger first so it sees every event from the start.
event_logger = EventLogger(bus)
orchestrator = Orchestrator(bus)
reasoning_engine = ReasoningEngine(bus)
response_handler = ResponseHandler(bus)
tool_resolver = ToolResolver(bus)
memory_manager = MemoryManager(bus)
automation_engine = AutomationEngine(bus)
environment_service = EnvironmentService(bus)
policy_engine = PolicyEngine(bus)

# ── Expose shared state for route handlers ────────────────────────────────────
app.state.bus = bus
app.state.response_handler = response_handler

# ── API routes ────────────────────────────────────────────────────────────────
app.include_router(router)


if __name__ == "__main__":
    _cfg = get_config()
    uvicorn.run(
        "ambient_assistant.main:app",
        host=_cfg.HOST,
        port=_cfg.PORT,
        reload=True,
    )
