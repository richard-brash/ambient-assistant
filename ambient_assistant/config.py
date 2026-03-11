from __future__ import annotations

import os
from dataclasses import dataclass, field

from dotenv import load_dotenv

# Load .env once, at import time.  All other modules must NOT call load_dotenv.
load_dotenv()


@dataclass
class Config:
    OPENAI_API_KEY: str = field(default_factory=lambda: os.environ.get("OPENAI_API_KEY", ""))
    OPENAI_MODEL: str = field(default_factory=lambda: os.environ.get("OPENAI_MODEL", "gpt-4o"))
    HOST: str = field(default_factory=lambda: os.environ.get("HOST", "0.0.0.0"))
    PORT: int = field(default_factory=lambda: int(os.environ.get("PORT", "8000")))


def get_config() -> Config:
    """Return a fresh Config instance populated from the environment."""
    return Config()
