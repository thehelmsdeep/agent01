from .brain import LLMBrain
from .context import ContextBuilder
from .memory import MessageMemory, UserMemory, AgentMemory
from .tools.registry import ToolRegistry


class Agent:
    def __init__(self, brain: LLMBrain, tools: ToolRegistry) -> None:
        self.brain = brain
        self.tools = tools

        self.memory = MessageMemory()
        self.user_memory = UserMemory()
        self.agent_memory = AgentMemory()
        self.context_builder = ContextBuilder()

    def run_once(self, user_input: str) -> str:
        self.memory.add("user", user_input)

        context = self.context_builder.build(
            self.memory,
            self.user_memory,
            self.agent_memory,
        )

        response = self.brain.respond(context)

        self.memory.add("assistant", response)
        self.agent_memory.remember(f"handled: {user_input}")

        return response
