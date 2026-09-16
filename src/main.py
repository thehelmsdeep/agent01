from .agent import Agent
from .brain import LLMBrain
from .tools.registry import ToolRegistry


def main() -> None:
    agent = Agent(LLMBrain(), ToolRegistry())
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
