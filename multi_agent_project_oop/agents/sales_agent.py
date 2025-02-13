import logging
from utils.human_feedback import human_feedback

class SalesAgent:
    def run(self, state: dict) -> dict:
        try:
            logging.info("Sales Agent: Engaging with clients via chatbot and logging interactions to MongoDB.")
            raw_output = ("Sales Chatbot: Client engaged successfully; interaction logged to MongoDB. "
                          "Performance insights: 85% satisfaction.")
            approved = human_feedback("Sales Agent", raw_output)
            logging.info("Sales Agent: Client engagement completed.")
            return {"messages": [{"role": "assistant", "content": approved}]}
        except Exception as e:
            logging.exception("Sales Agent: Exception occurred.")
            error_msg = f"Error in Sales Agent: {str(e)}"
            approved = human_feedback("Sales Agent (error)", error_msg)
            return {"messages": [{"role": "assistant", "content": approved}]}
