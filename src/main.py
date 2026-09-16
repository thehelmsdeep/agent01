import os

from .agent import Agent
from .brain import LLMBrain
from .browser_brain import BrowserBrain
from .tools.registry import ToolRegistry


def create_brain():
    provider = os.getenv("BRAIN", "api").lower()

    if provider == "browser":
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
