from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
import operator

# Import agent classes.
from agents.ceo_agent import CEOAgent
from agents.research_agent import ResearchAgent
from agents.ad_copy_agent import AdCopyAgent
from agents.content_writing_agent import ContentWritingAgent
from agents.marketing_agent import MarketingAgent
from agents.sales_agent import SalesAgent

# Define the global state schema.
class State(TypedDict):
    messages: list

def build_graph():
    graph_builder = StateGraph(State)
    
    # Instantiate agents.
    ceo = CEOAgent()
    research = ResearchAgent()
    ad_copy = AdCopyAgent()
    content_writer = ContentWritingAgent()
    marketing = MarketingAgent()
    sales = SalesAgent()
    
    # Add nodes (each node calls the agent's run() method).
    graph_builder.add_node("ceo", lambda state: ceo.run(state))
    graph_builder.add_node("research", lambda state: research.run(state))
    graph_builder.add_node("ad_copy", lambda state: ad_copy.run(state))
    graph_builder.add_node("content_writing", lambda state: content_writer.run(state))
    graph_builder.add_node("marketing", lambda state: marketing.run(state))
    graph_builder.add_node("sales", lambda state: sales.run(state))
    
    # Define control flow.
    # For continuous dialogue, we assume each conversation turn is triggered by the CEO.
    graph_builder.add_edge(START, "ceo")
    graph_builder.add_edge("ceo", "research")
    graph_builder.add_edge("research", "ceo")
    graph_builder.add_edge("ceo", "ad_copy")
    graph_builder.add_edge("ad_copy", "ceo")
    graph_builder.add_edge("ceo", "content_writing")
    graph_builder.add_edge("content_writing", "ceo")
    graph_builder.add_edge("ceo", "marketing")
    graph_builder.add_edge("marketing", "ceo")
    graph_builder.add_edge("ceo", "sales")
    graph_builder.add_edge("sales", "ceo")
    # Instead of finishing the conversation, the CEO node will produce an output and then the workflow stops.
    graph_builder.add_edge("ceo", END)
    
    return graph_builder.compile()
