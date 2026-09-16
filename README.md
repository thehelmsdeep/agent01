# agent01

Windows AI Agent project.

## Goal

Build a local browser-based AI agent that can operate a browser environment while keeping the user's personal ChatGPT conversations separate from the agent session.

## Architecture

```
User
 |
 v
Agent Runtime
 |
 +--> Browser Controller (Playwright)
 |
 +--> Separate Browser Profile
 |
 +--> LLM Brain (future)
```

## Principles

- Separate agent browser profile
- Do not use user's personal chats/cookies
- Local-first architecture
- Modular components

## Current Stack

- Python
- Playwright
- Browser automation
- Environment configuration

## Setup

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

python -m playwright install chromium
```

## Project Status

Phase 1:
- Browser controller
- Dedicated profile
- Chat interface experiments

Future:
- Agent planner
- Tool system
- Memory layer
- Task execution
