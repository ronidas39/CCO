# Multi-Agent LangGraph Project (OOP Version)

This project demonstrates a multi-agent workflow using LangGraph in an object-oriented style. It implements the following agents:

1. **CEO Agent:** Orchestrates and validates outputs from subordinate agents.
2. **Research Agent:** Conducts research using GPT‑4o (simulated).
3. **Ad Copy Agent:** Retrieves ad templates (simulated) and drafts ad copy.
4. **Content Writing Agent:** Generates detailed advertisement content.
5. **Marketing Agent:** Simulates scheduling and posting ads on social media.
6. **Sales Agent:** Simulates client engagement and logs interactions.

Each agent class uses human-in-the-loop feedback and includes error handling. A FastAPI web app (in `app.py`) exposes an endpoint to run the workflow.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
