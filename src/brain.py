from openai import OpenAI

from .config import settings


SYSTEM_PROMPT = """You are the reasoning layer of a Windows AI agent.
Decide what the agent should do next. Do not execute operating-system actions yourself.
The agent core owns tools, permissions, execution, and observations.
"""


class LLMBrain:
    def __init__(self) -> None:
        if not settings.api_key:
            raise RuntimeError("LLM_API_KEY is not configured")

        kwargs = {"api_key": settings.api_key}
        if settings.base_url:
            kwargs["base_url"] = settings.base_url
        self.client = OpenAI(**kwargs)

    def respond(self, messages: list[dict[str, str]]) -> str:
        response = self.client.chat.completions.create(
            model=settings.model,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}, *messages],
        )
        return response.choices[0].message.content or ""
