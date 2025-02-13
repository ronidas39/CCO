import logging
from utils.human_feedback import human_feedback

class ResearchAgent:
    def run(self, state: dict) -> dict:
        try:
            logging.info("Research Agent: Conducting research using GPT-4o.")
            query = state["messages"][0].get("content", "")
            raw_output = f"Research Insight for '{query}': Comprehensive analysis and findings using GPT-4o."
            approved = human_feedback("Research Agent", raw_output)
            logging.info("Research Agent: Research completed.")
            return {"messages": [{"role": "assistant", "content": approved}]}
        except Exception as e:
            logging.exception("Research Agent: Exception occurred.")
            error_msg = f"Error in Research Agent: {str(e)}"
            approved = human_feedback("Research Agent (error)", error_msg)
            return {"messages": [{"role": "assistant", "content": approved}]}
