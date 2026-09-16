from .brain import LLMBrain
from .memory import MessageMemory
from .tools.registry import ToolRegistry


class Agent:
    def __init__(self, brain: LLMBrain, tools: ToolRegistry) -> None:
        self.brain = brain
        self.tools = tools
        self.memory = MessageMemory()

    def run_once(self, user_input: str) -> str:
        self.memory.add("user", user_input)
        response = self.brain.respond(self.memory.recent())
        self.memory.add("assistant", response)
        return response
