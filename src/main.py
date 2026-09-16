import os

from .agent import Agent
from .brain import LLMBrain
from .browser_brain import BrowserBrain
from .browser_session import BrowserSessionManager
from .tools.registry import ToolRegistry


def create_brain():
    provider = os.getenv("BRAIN", "api").lower()

    if provider == "browser":
        session = BrowserSessionManager()
        if not session.is_available():
            raise RuntimeError(
                "Chrome remote session is not available. Start Chrome with remote debugging on port 9222."
            )
        return BrowserBrain()

    return LLMBrain()


def main() -> None:
    agent = Agent(create_brain(), ToolRegistry())
    print("agent01 ready. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break
        if not user_input:
            continue

        try:
            print(f"Agent: {agent.run_once(user_input)}")
        except Exception as exc:
            print(f"Agent error: {exc}")


if __name__ == "__main__":
    main()
