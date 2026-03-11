from __future__ import annotations

import logging

from ambient_assistant.events.bus import EventBus
from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)

_EVENT_IN = "message.received"
_EVENT_OUT = "reasoning.requested"


class Orchestrator:
    """Receives user messages and orchestrates the assistant pipeline.

    Listens for ``message.received`` events and forwards them as
    ``reasoning.requested`` events for the :class:`ReasoningEngine`.
    """

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        bus.subscribe(_EVENT_IN, self.handle)

    async def handle(self, envelope: EventEnvelope) -> None:
        logger.info("Orchestrator received %r", envelope)
        await self._bus.publish(
            EventEnvelope(
                event_type=_EVENT_OUT,
                payload=envelope.payload,
                correlation_id=envelope.correlation_id,
                source="orchestrator",
            )
        )
