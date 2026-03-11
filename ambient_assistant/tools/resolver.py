from __future__ import annotations

import logging

from ambient_assistant.events.bus import EventBus
from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)


class ToolResolver:
    """Resolves and executes tools requested by the assistant."""

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        bus.subscribe("tool.requested", self.handle)

    async def handle(self, envelope: EventEnvelope) -> None:
        logger.info("ToolResolver received %r", envelope)
