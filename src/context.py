from .memory import MessageMemory, UserMemory, AgentMemory


class ContextBuilder:
    """Builds the context sent to the LLM.

    The LLM should not own memory. The agent collects the required
    context from its own memory layers and sends it to the model.
    """

    def build(
        self,
        messages: MessageMemory,
        user_memory: UserMemory,
        agent_memory: AgentMemory,
    ) -> list[dict[str, str]]:
        context = []

        if user_memory.data:
            context.append(
                {
                    "role": "system",
                    "content": f"User memory: {user_memory.data}",
                }
            )

        if agent_memory.events:
            context.append(
                {
                    "role": "system",
                    "content": f"Agent memory: {agent_memory.recent()}",
                }
            )

        context.extend(messages.recent())
        return context
