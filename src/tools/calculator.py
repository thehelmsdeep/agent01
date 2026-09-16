from .base import ToolResult


class CalculatorTool:
    name = "calculator"
    description = "Evaluate simple arithmetic expressions."

    def run(self, expression: str, **kwargs) -> ToolResult:
        try:
            result = eval(expression, {"__builtins__": {}}, {})
            return ToolResult(True, str(result))
        except Exception as exc:
            return ToolResult(False, str(exc))
