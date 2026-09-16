class ReasoningLoop:
    """Simple iterative reasoning controller for the agent."""

    def __init__(self, max_steps: int = 3) -> None:
        self.max_steps = max_steps

    def should_continue(self, step: int, observation: str | None = None) -> bool:
        if step >= self.max_steps:
            return False

        return bool(observation)
