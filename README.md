# agent01

A Windows AI agent foundation built around an LLM API, explicit tools, memory, and an execution loop.

## Architecture

```text
User
  |
  v
Agent Core
  |
  +--> Memory
  |
  +--> LLM Brain
  |       |
  |       v
  |    Tool Decision
  |
  +--> Tool Registry
          |
          v
      Windows Actions
```

The LLM is the reasoning layer. The agent, not the model, owns execution, tool permissions, state, and the loop that observes results and sends the next context back to the model.

## Project layout

```text
agent01/
├── src/
│   ├── agent.py          # agent execution loop
│   ├── brain.py          # LLM API adapter
│   ├── config.py         # environment configuration
│   ├── memory.py         # short-term conversation memory
│   ├── main.py           # CLI entry point
│   └── tools/
│       ├── base.py       # tool contract
│       └── registry.py   # tool registration/lookup
├── tests/
│   └── test_smoke.py
├── .env.example
├── .gitignore
└── requirements.txt
```

## Setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and configure the LLM API key and model.

## Run

```powershell
python -m src.main
```

Without an API key, the project can still be imported and the core components can be tested, but an LLM-backed response requires a configured provider.

## Roadmap

1. LLM-backed planning
2. Structured tool calls
3. Windows observation tools
4. Safe tool permissions and confirmations
5. Execution/observation loop
6. Persistent memory
7. Browser and desktop automation
