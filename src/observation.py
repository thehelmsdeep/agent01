class ObservationLoop:
    """Stores tool results as observations for the agent loop."""

    def observe(self, action: dict, result: str) -> dict:
        return {
            "action": action,
            "result": result,
        }
