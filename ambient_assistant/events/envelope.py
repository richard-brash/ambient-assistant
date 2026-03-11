from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class EventEnvelope:
    """Wraps every event travelling through the bus."""

    event_type: str
    payload: dict[str, Any]
    correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    source: str = ""

    def __repr__(self) -> str:
        return (
            f"EventEnvelope(type={self.event_type!r}, "
            f"correlation_id={self.correlation_id!r}, "
            f"source={self.source!r})"
        )
