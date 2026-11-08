from langgraph.graph import StateGraph, END

from graph.state import AgentState

from agents.vision_agent import vision_agent
from agents.cost_agent import cost_agent
from agents.policy_agent import policy_agent
from agents.decision_agent import decision_agent


workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("Vision Agent", vision_agent)
workflow.add_node("Cost Agent", cost_agent)
workflow.add_node("Policy Agent", policy_agent)
workflow.add_node("Decision Agent", decision_agent)

# Flow
workflow.set_entry_point("Vision Agent")

workflow.add_edge("Vision Agent", "Cost Agent")
workflow.add_edge("Cost Agent", "Policy Agent")
workflow.add_edge("Policy Agent", "Decision Agent")
workflow.add_edge("Decision Agent", END)

# Compile
app = workflow.compile()