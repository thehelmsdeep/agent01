class Planner:
    """Simple planning layer for the personal agent."""

    def create_plan(self, user_input: str) -> list[str]:
        return [
            "understand_request",
            f"process: {user_input}",
            "generate_response",
        ]
