from src.memory import MessageMemory
from src.tools.base import ToolResult
from src.tools.registry import ToolRegistry


def test_memory():
    memory = MessageMemory()
    memory.add("user", "hello")
    assert memory.recent() == [{"role": "user", "content": "hello"}]


def test_registry():
    class PingTool:
        name = "ping"
        description = "Return a ping result."

        def run(self, **kwargs):
            return ToolResult(True, "pong")

    registry = ToolRegistry()
    registry.register(PingTool())
    assert registry.names() == ["ping"]
