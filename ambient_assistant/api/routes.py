from __future__ import annotations

import asyncio
import logging

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

from ambient_assistant.events.envelope import EventEnvelope

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/assistant", tags=["assistant"])


class MessageRequest(BaseModel):
    content: str


class MessageResponse(BaseModel):
    correlation_id: str
    response: str


@router.post("/message", response_model=MessageResponse)
async def post_message(body: MessageRequest, request: Request) -> MessageResponse:
    """Accept a user message, route it through the event bus, and return the reply.

    Flow:
        POST /assistant/message
            → message.received (bus)
            → orchestrator
            → reasoning.requested (bus)
            → reasoning engine / OpenAI
            → reasoning.completed (bus)
            → response handler (resolves future)
            → HTTP response
    """
    bus = request.app.state.bus
    response_handler = request.app.state.response_handler

    envelope = EventEnvelope(
        event_type="message.received",
        payload={"content": body.content},
        source="api",
    )

    future = response_handler.create_future(envelope.correlation_id)
    await bus.publish(envelope)

    try:
        reply = await asyncio.wait_for(future, timeout=30.0)
    except asyncio.TimeoutError:
        logger.error("Timeout waiting for response to %s", envelope.correlation_id)
        raise HTTPException(status_code=504, detail="Assistant response timed out.")

    return MessageResponse(correlation_id=envelope.correlation_id, response=reply)
