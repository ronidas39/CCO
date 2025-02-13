import logging
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from graph_builder import build_graph
from langgraph.graph.message import HumanMessage

# Configure logging.
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI(title="Multi-Agent LangGraph OOP DialogFlow API")

# Build the graph once.
graph = build_graph()

# In-memory session store.
sessions = {}

class DialogRequest(BaseModel):
    session_id: str = None  # Optional; if not provided, a new session is created.
    message: str

@app.post("/dialog", summary="Continue the dialogue")
async def continue_dialog(request: DialogRequest):
    try:
        # If session_id not provided, create one.
        session_id = request.session_id or str(uuid.uuid4())
        # Retrieve previous state or initialize a new state.
        if session_id in sessions:
            state = sessions[session_id]
            # Append the new user message.
            state["messages"].append({"role": "user", "content": request.message})
        else:
            state = {"messages": [{"role": "user", "content": request.message}]}
        
        # Invoke the graph with the updated state.
        result = graph.invoke(state)
        
        # Save the updated state for the session.
        sessions[session_id] = result
        
        # Return the session id and the new assistant message(s).
        response_messages = [msg for msg in result.get("messages", []) if msg.get("role") == "assistant"]
        return {"session_id": session_id, "messages": response_messages}
    except Exception as e:
        logging.exception("Error during dialogue execution")
        raise HTTPException(status_code=500, detail=str(e))
