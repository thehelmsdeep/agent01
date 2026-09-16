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
  |                |
  +----------------+
                   |
                   v
            Context Builder
                   |
                   v
          Reasoning / Brain Layer
                   |
        +----------+----------+
        |                     |
        v                     v
    API Brain          Browser Brain
                              |
                              v
                    Existing Chrome Session
                              |
                              v
                         ChatGPT Web
                   |
                   v
            Tool Decision
                   |
                   v
            Tool Executor
                   |
                   v
          Windows Actions
```

The LLM is the reasoning layer only. The agent owns execution, tool permissions, state, memory management, and the execution loop.

The project supports different brain providers:

- **API Brain**: uses an LLM API provider.
- **Browser Brain**: connects to an existing logged-in browser session and uses ChatGPT Web without requiring a separate API key.

The agent keeps two independent memory systems:

- **User Memory**: user preferences, profile information, and long-term user context.
- **Agent Memory**: internal agent state, completed tasks, decisions, and execution history.

This separation allows the agent to change its reasoning provider without losing user or agent context.

## Browser Brain Concept

The browser mode is designed for a personal agent workflow:

```text
Your Chrome
   |
   | Logged-in ChatGPT session
   |
   v
Browser Controller
   |
   v
Agent01
```

The agent does not need to create a new ChatGPT account session. It can work with an existing browser profile/session.

## Project layout

```text
agent01/
├── src/
│   ├── agent.py              # agent execution loop
│   ├── brain.py              # API LLM adapter
│   ├── browser_brain.py      # ChatGPT browser adapter
│   ├── config.py             # environment configuration
│   ├── memory.py             # conversation memory
│   ├── context.py            # context builder
│   ├── planner.py            # planning layer
│   ├── executor.py           # tool execution
│   ├── observation.py        # observation loop
│   ├── main.py               # CLI entry point
│   └── tools/
│       ├── base.py
│       └── registry.py
├── tests/
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
Context Builder
      |
      v
Brain Provider
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

Copy `.env.example` to `.env` and configure the selected brain provider.

## Run

```powershell
python -m src.main
```

## Roadmap

1. Context builder ✅
2. Planning layer ✅
3. Structured tool calls ✅
4. Observation and reasoning loop ✅
5. Persistent memory storage ✅
6. Browser Brain integration 🚧
7. Browser response extraction
8. Windows observation tools
9. Safe tool permissions and confirmations
10. Desktop automation
