from __future__ import annotations

import logging
from collections import defaultdict
from typing import Awaitable, Callable

from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)

Handler = Callable[[EventEnvelope], Awaitable[None]]


class EventBus:
    """In-process asyncio event bus.

    Subsystems must not call each other directly; all communication must
    go through this bus.  Handlers are awaited in subscription order.
    Use ``event_type="*"`` to receive every event (e.g. for logging).
    """

    def __init__(self) -> None:
        self._handlers: dict[str, list[Handler]] = defaultdict(list)
        self._wildcard_handlers: list[Handler] = []

    def subscribe(self, event_type: str, handler: Handler) -> None:
        """Register *handler* for *event_type*, or ``'*'`` for all events."""
        if event_type == "*":
            self._wildcard_handlers.append(handler)
        else:
            self._handlers[event_type].append(handler)
        logger.debug("Subscribed %s → '%s'", handler.__qualname__, event_type)

    async def publish(self, envelope: EventEnvelope) -> None:
        """Publish *envelope* and await all matching handlers."""
        logger.debug("Publishing %r", envelope)
        for handler in self._handlers.get(envelope.event_type, []):
            await handler(envelope)
        for handler in self._wildcard_handlers:
            await handler(envelope)
