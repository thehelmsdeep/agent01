from dataclasses import dataclass, field


@dataclass
class MessageMemory:
    messages: list[dict[str, str]] = field(default_factory=list)

    def add(self, role: str, content: str) -> None:
        self.messages.append({"role": role, "content": content})

    def recent(self, limit: int = 20) -> list[dict[str, str]]:
        return self.messages[-limit:]


@dataclass
class UserMemory:
    """Long term memory belonging to the human user."""
    data: dict[str, str] = field(default_factory=dict)

    def set(self, key: str, value: str) -> None:
        self.data[key] = value

    def get(self, key: str, default=None):
        return self.data.get(key, default)


@dataclass
class AgentMemory:
    """Internal memory of agent actions and state."""
    events: list[str] = field(default_factory=list)

    def remember(self, event: str) -> None:
        self.events.append(event)

    def recent(self, limit: int = 20) -> list[str]:
        return self.events[-limit:]
