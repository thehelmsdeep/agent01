# agent01

A Windows AI agent foundation built around an LLM brain, explicit tools, separated memory layers, and an execution loop.

## Architecture

```text
User
  |
  v
Agent Core
  |
  +----------------+
  |                |
  v                v
User Memory     Agent Memory
  |
  +----------------+
                   |
                   v
            Context Builder
                   |
                   v
              LLM Brain
                   |
                   v
            Tool Decision
                   |
                   v
            Tool Registry
                   |
                   v
          Windows Actions
```

The LLM is the reasoning layer only. The agent owns execution, tool permissions, state, memory management, and the execution loop.

The agent keeps two independent memory systems:

- **User Memory**: user preferences, profile information, and long-term user context.
- **Agent Memory**: internal agent state, completed tasks, decisions, and execution history.

This separation allows the agent to use different LLM providers without losing user or agent context.

## Project layout

```text
agent01/
├── src/
│   ├── agent.py              # agent execution loop
│   ├── brain.py              # LLM adapter
│   ├── config.py             # environment configuration
│   ├── memory.py             # conversation memory
│   ├── user_memory.py        # user-specific memory
│   ├── agent_memory.py       # agent internal memory
│   ├── main.py               # CLI entry point
│   └── tools/
│       ├── base.py           # tool contract
│       └── registry.py       # tool registration/lookup
├── tests/
│   └── test_smoke.py
├── .env.example
├── .gitignore
└── requirements.txt
```

## Memory Flow

```text
User Message
      |
      v
Agent Core
      |
      +--> Conversation History
      |
      +--> User Memory
      |
      +--> Agent Memory
      |
      v
Context sent to LLM
      |
      v
Response + Tool Actions
```

## Setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and configure the LLM provider.

## Run

```powershell
python -m src.main
```

## Roadmap

1. Context builder
2. LLM-backed planning
3. Structured tool calls
4. Windows observation tools
5. Safe tool permissions and confirmations
6. Persistent memory storage
7. Browser and desktop automation
8. Multi-user agent sessions
