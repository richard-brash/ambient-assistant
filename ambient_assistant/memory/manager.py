from __future__ import annotations

import logging

from ambient_assistant.events.bus import EventBus
from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)


class MemoryManager:
    """Manages short- and long-term memory for the assistant."""

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        bus.subscribe("memory.store", self.handle_store)
        bus.subscribe("memory.retrieve", self.handle_retrieve)

    async def handle_store(self, envelope: EventEnvelope) -> None:
        logger.info("MemoryManager store %r", envelope)

    async def handle_retrieve(self, envelope: EventEnvelope) -> None:
        logger.info("MemoryManager retrieve %r", envelope)
