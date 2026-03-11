from __future__ import annotations

import logging

from ambient_assistant.events.bus import EventBus
from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)


class EnvironmentService:
    """Provides ambient environment context (sensors, device state, etc.)."""

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        bus.subscribe("environment.query", self.handle)

    async def handle(self, envelope: EventEnvelope) -> None:
        logger.info("EnvironmentService received %r", envelope)
