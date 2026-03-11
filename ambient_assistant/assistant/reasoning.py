from __future__ import annotations

import logging

from openai import AsyncOpenAI

from ambient_assistant.config import get_config
from ambient_assistant.events.bus import EventBus
from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)

_EVENT_IN = "reasoning.requested"
_EVENT_OUT = "reasoning.completed"


class ReasoningEngine:
    """Calls the OpenAI API to produce a reply.

    Listens for ``reasoning.requested`` events, performs the LLM call,
    and publishes a ``reasoning.completed`` event carrying the reply.
    """

    def __init__(self, bus: EventBus) -> None:
        self._bus = bus
        config = get_config()
        self._client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)
        self._model = config.OPENAI_MODEL
        bus.subscribe(_EVENT_IN, self.handle)

    async def handle(self, envelope: EventEnvelope) -> None:
        logger.info("ReasoningEngine received %r", envelope)
        user_message = envelope.payload.get("content", "")
        reply = await self._call_openai(user_message)
        await self._bus.publish(
            EventEnvelope(
                event_type=_EVENT_OUT,
                payload={"content": reply},
                correlation_id=envelope.correlation_id,
                source="reasoning",
            )
        )

    async def _call_openai(self, user_message: str) -> str:
        response = await self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": "user", "content": user_message}],
        )
        return response.choices[0].message.content or ""
