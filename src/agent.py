from .brain import LLMBrain
from .context import ContextBuilder
from .memory import MessageMemory, UserMemory, AgentMemory
from .storage import MemoryStorage
from .user_storage import UserMemoryStorage
from .tools.registry import ToolRegistry


class Agent:
    def __init__(self, brain: LLMBrain, tools: ToolRegistry, user_id: str = "default") -> None:
        self.brain = brain
        self.tools = tools
        self.user_id = user_id

        self.memory = MessageMemory()
        self.user_memory = UserMemory()
        self.agent_memory = AgentMemory()
        self.context_builder = ContextBuilder()

        self.storage = MemoryStorage()
        self.user_storage = UserMemoryStorage()

        self.load_memory()

    def load_memory(self) -> None:
        data = self.storage.load()
        user_data = self.user_storage.load(self.user_id)

        self.user_memory.data.update(user_data)
        self.agent_memory.events.extend(data.get("agent_memory", []))
        self.memory.messages.extend(data.get("messages", []))

    def save_memory(self) -> None:
        self.storage.save({
            "messages": self.memory.messages,
            "agent_memory": self.agent_memory.events,
        })
        self.user_storage.save(self.user_id, self.user_memory.data)

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

        self.save_memory()

        return response
