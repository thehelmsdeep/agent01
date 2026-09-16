import json


class ToolSelector:
    """Converts an agent decision into an executable tool action."""

    def select(self, response: str) -> dict:
        try:
            data = json.loads(response)
            if "tool" in data:
                return data
        except json.JSONDecodeError:
            pass

        return {}
