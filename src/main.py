import os
import time

from .agent import Agent
from .brain import LLMBrain
from .browser_brain import BrowserBrain
from .browser_session import BrowserSessionManager
from .chrome_launcher import ChromeLauncher
from .tools.registry import ToolRegistry


def create_brain():
    # Browser ChatGPT is the primary brain.
    # API LLM is only an optional fallback.
    provider = os.getenv("BRAIN", "browser").lower()

    if provider == "api":
        return LLMBrain()

    session = BrowserSessionManager()

    if not session.is_available():
        launcher = ChromeLauncher()
        launcher.launch()

        for _ in range(15):
            time.sleep(1)
            if session.is_available():
                break
        else:
            raise RuntimeError(
                "Chrome remote session is not available after launch."
            )

    return BrowserBrain()


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
