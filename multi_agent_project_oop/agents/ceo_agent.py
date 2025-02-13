import logging
from utils.human_feedback import human_feedback

class CEOAgent:
    def run(self, state: dict) -> dict:
        try:
            logging.info("CEO Agent: Reviewing output from subordinate agent.")
            # For continuous dialogue, the CEO agent may review the latest agent output and optionally prompt for additional input.
            subordinate_output = state["messages"][-1].get("content", "")
            approved = human_feedback("CEO Agent", subordinate_output)
            logging.info("CEO Agent: Feedback approved.")
            return {"messages": [{"role": "assistant", "content": approved}]}
        except Exception as e:
            logging.exception("CEO Agent: Exception occurred.")
            error_msg = f"Error in CEO Agent: {str(e)}"
            approved = human_feedback("CEO Agent (error)", error_msg)
            return {"messages": [{"role": "assistant", "content": approved}]}
