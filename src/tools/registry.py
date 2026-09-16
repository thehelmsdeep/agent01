from typing import Any

from .base import Tool
from .calculator import CalculatorTool


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}
        self.register(CalculatorTool())

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        return self._tools[name]

    def names(self) -> list[str]:
        return list(self._tools)

    def descriptions(self) -> list[dict[str, Any]]:
        return [
            {"name": tool.name, "description": tool.description}
            for tool in self._tools.values()
        ]
