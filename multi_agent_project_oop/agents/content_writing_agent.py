import logging
from utils.human_feedback import human_feedback

class ContentWritingAgent:
    def run(self, state: dict) -> dict:
        try:
            logging.info("Content Writing Agent: Generating detailed ad content using GPT-4o.")
            raw_output = ("Ad Content: Introducing our cutting-edge product that redefines excellence "
                          "and innovation, crafted with passion and precision.")
            approved = human_feedback("Content Writing Agent", raw_output)
            logging.info("Content Writing Agent: Ad content generated.")
            return {"messages": [{"role": "assistant", "content": approved}]}
        except Exception as e:
            logging.exception("Content Writing Agent: Exception occurred.")
            error_msg = f"Error in Content Writing Agent: {str(e)}"
            approved = human_feedback("Content Writing Agent (error)", error_msg)
            return {"messages": [{"role": "assistant", "content": approved}]}
