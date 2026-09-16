import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    api_key: str = os.getenv("LLM_API_KEY", "")
    base_url: str | None = os.getenv("LLM_BASE_URL") or None
    model: str = os.getenv("LLM_MODEL", "gpt-4o-mini")


settings = Settings()
