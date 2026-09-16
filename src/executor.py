from .tools.registry import ToolRegistry


class ToolExecutor:
    """Executes tools selected by the agent."""

    def __init__(self, tools: ToolRegistry) -> None:
        self.tools = tools

    def execute(self, action: dict) -> str:
        tool_name = action.get("tool")
        args = action.get("args", {})

        if not tool_name:
            return "No tool selected"

        tool = self.tools.get(tool_name)
        return tool.run(**args)
