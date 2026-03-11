from __future__ import annotations

import logging

from ambient_assistant.events.bus import EventBus
from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)


class PolicyEngine:
    """Enforces policy rules on assistant actions before they are executed."""

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        bus.subscribe("policy.check", self.handle)

    async def handle(self, envelope: EventEnvelope) -> None:
        logger.info("PolicyEngine received %r", envelope)
