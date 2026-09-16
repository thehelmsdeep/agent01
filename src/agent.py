from .brain import LLMBrain
from .context import ContextBuilder
from .memory import MessageMemory, UserMemory, AgentMemory
from .storage import MemoryStorage
from .planner import Planner
from .executor import ToolExecutor
from .tools.registry import ToolRegistry


class Agent:
    """Personal single-user AI Agent core."""

    def __init__(self, brain: LLMBrain, tools: ToolRegistry) -> None:
        self.brain = brain
        self.tools = tools
        self.planner = Planner()
        self.executor = ToolExecutor(tools)

        self.memory = MessageMemory()
        self.user_memory = UserMemory()
        self.agent_memory = AgentMemory()
        self.context_builder = ContextBuilder()

        self.storage = MemoryStorage()

        self.load_memory()

    def load_memory(self) -> None:
        data = self.storage.load()

        self.user_memory.data.update(data.get("user_memory", {}))
        self.agent_memory.events.extend(data.get("agent_memory", []))
        self.memory.messages.extend(data.get("messages", []))

    def save_memory(self) -> None:
        self.storage.save({
            "messages": self.memory.messages,
            "user_memory": self.user_memory.data,
            "agent_memory": self.agent_memory.events,
        })

    def run_once(self, user_input: str) -> str:
        self.memory.add("user", user_input)

        plan = self.planner.create_plan(user_input)
        self.agent_memory.remember({"plan": plan})

        context = self.context_builder.build(
            self.memory,
            self.user_memory,
            self.agent_memory,
        )

        response = self.brain.respond(context)

        self.memory.add("assistant", response)
        self.agent_memory.remember(f"handled: {user_input}")

        self.save_memory()

        return response
