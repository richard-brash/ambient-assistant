from __future__ import annotations

import logging

from ambient_assistant.events.bus import EventBus
from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)


class AutomationEngine:
    """Executes automation workflows triggered by assistant decisions."""

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        bus.subscribe("automation.triggered", self.handle)

    async def handle(self, envelope: EventEnvelope) -> None:
        logger.info("AutomationEngine received %r", envelope)
