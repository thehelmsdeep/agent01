from .brain import LLMBrain
from .memory import MessageMemory, UserMemory, AgentMemory
from .tools.registry import ToolRegistry


class Agent:
    def __init__(self, brain: LLMBrain, tools: ToolRegistry) -> None:
        self.brain = brain
        self.tools = tools

        # Human conversation history
        self.memory = MessageMemory()

        # Separate memories
        self.user_memory = UserMemory()
        self.agent_memory = AgentMemory()

    def run_once(self, user_input: str) -> str:
        self.memory.add("user", user_input)

        context = self.memory.recent()
        response = self.brain.respond(context)

        self.memory.add("assistant", response)
        self.agent_memory.remember(f"handled: {user_input}")

        return response
