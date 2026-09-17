# Agent01

A Windows personal AI agent foundation built around a browser-based LLM brain, tools, memory, and an execution loop.

## Main Architecture

Agent01 uses **ChatGPT Web through the user's existing Chrome session** as the LLM brain.

No OpenAI API key is required for the default workflow.

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
          Browser Brain
                  |
                  v
        Chrome (User Profile)
                  |
                  v
          Logged-in ChatGPT Web
                  |
                  v
          Response / Reasoning
                  |
                  v
          Tool Executor
                  |
                  v
        Windows Actions
```

## Browser Brain

Browser Brain is the primary brain provider.

Flow:

```text
Agent01
   |
   v
Chrome Manager
   |
   v
Existing Chrome Profile
   |
   v
ChatGPT Web Session
   |
   v
Question -> Answer
```

The agent uses the user's already logged-in browser session instead of creating a separate API connection.

## Important

This project is NOT designed around:

- OpenAI API calls as the main brain
- API keys
- External LLM providers by default

The LLM interaction happens through the browser.

## Memory

Agent01 keeps two memory layers:

- User Memory: user preferences and long-term context.
- Agent Memory: internal execution state, decisions, and history.

## Project Layout

```text
agent01/
├── src/
│   ├── agent.py
│   ├── browser_brain.py      # ChatGPT Web integration
│   ├── chrome_manager.py     # Chrome startup/session handling
│   ├── brain.py              # Optional API brain adapter
│   ├── config.py
│   ├── memory.py
│   ├── context.py
│   ├── planner.py
│   ├── executor.py
│   ├── observation.py
│   └── main.py
```

## Roadmap

1. Context builder
2. Planning layer
3. Structured tool calls
4. Observation loop
5. Persistent memory
6. Browser Brain integration
7. ChatGPT response extraction
8. Windows automation tools
9. Safe permissions
10. Desktop agent capabilities
