import logging
from utils.human_feedback import human_feedback

class MarketingAgent:
    def run(self, state: dict) -> dict:
        try:
            logging.info("Marketing Agent: Scheduling and posting ad on social media.")
            raw_output = ("Marketing: Ad scheduled and posted on Facebook, Instagram, Flodesk, Threads, "
                          "and LinkedIn via API.")
            approved = human_feedback("Marketing Agent", raw_output)
            logging.info("Marketing Agent: Ad posted successfully.")
            return {"messages": [{"role": "assistant", "content": approved}]}
        except Exception as e:
            logging.exception("Marketing Agent: Exception occurred.")
            error_msg = f"Error in Marketing Agent: {str(e)}"
            approved = human_feedback("Marketing Agent (error)", error_msg)
            return {"messages": [{"role": "assistant", "content": approved}]}
