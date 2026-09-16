from typing import Any

from .base import Tool, ToolResult


class CalculatorTool(Tool):
    name = "calculator"
    description = "Evaluate simple arithmetic expressions."

    def run(self, expression: str, **kwargs: Any) -> ToolResult:
        allowed = set("0123456789+-*/(). ")

        if not expression or any(ch not in allowed for ch in expression):
            return ToolResult(False, "Invalid expression")

        try:
            result = eval(expression, {"__builtins__": {}}, {})
            return ToolResult(True, str(result))
        except Exception as exc:
            return ToolResult(False, str(exc))
