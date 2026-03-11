from __future__ import annotations

import asyncio
import logging

from ambient_assistant.events.bus import EventBus
from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)

_EVENT_IN = "reasoning.completed"


class ResponseHandler:
    """Receives completed reasoning results and resolves pending API futures.

    The API layer registers a :class:`asyncio.Future` per correlation ID
    via :meth:`create_future` before publishing the initial event.  When
    ``reasoning.completed`` arrives this handler resolves that future so
    the HTTP response can be returned to the caller.
    """

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        self._pending: dict[str, asyncio.Future[str]] = {}
        bus.subscribe(_EVENT_IN, self.handle)

    def create_future(self, correlation_id: str) -> asyncio.Future[str]:
        """Register and return a future that will be resolved with the reply."""
        future: asyncio.Future[str] = asyncio.get_event_loop().create_future()
        self._pending[correlation_id] = future
        return future

    async def handle(self, envelope: EventEnvelope) -> None:
        logger.info("ResponseHandler received %r", envelope)
        future = self._pending.pop(envelope.correlation_id, None)
        if future and not future.done():
            future.set_result(envelope.payload.get("content", ""))
        else:
            logger.warning(
                "No pending future for correlation_id=%s", envelope.correlation_id
            )
