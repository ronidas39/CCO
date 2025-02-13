import logging
from utils.human_feedback import human_feedback

class AdCopyAgent:
    def run(self, state: dict) -> dict:
        try:
            logging.info("Ad Copy Agent: Retrieving ad templates from Chroma DB.")
            raw_output = ("Ad Template: Retrieved templates from Chroma DB. Draft ad copy: "
                          "'Experience innovation at its finest!'")
            approved = human_feedback("Ad Copy Agent", raw_output)
            logging.info("Ad Copy Agent: Draft ad copy created.")
            return {"messages": [{"role": "assistant", "content": approved}]}
        except Exception as e:
            logging.exception("Ad Copy Agent: Exception occurred.")
            error_msg = f"Error in Ad Copy Agent: {str(e)}"
            approved = human_feedback("Ad Copy Agent (error)", error_msg)
            return {"messages": [{"role": "assistant", "content": approved}]}
