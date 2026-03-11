from __future__ import annotations

import logging

from ambient_assistant.events.bus import EventBus
from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)


class EventLogger:
    """Logs every event that passes through the bus.

    Subscribes with the wildcard ``'*'`` so it receives all events
    regardless of type, providing a full audit trail.
    """

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        bus.subscribe("*", self.handle)

    async def handle(self, envelope: EventEnvelope) -> None:
        logger.info(
            "[EVENT] type=%-30s correlation_id=%s source=%s",
            envelope.event_type,
            envelope.correlation_id,
            envelope.source,
        )
