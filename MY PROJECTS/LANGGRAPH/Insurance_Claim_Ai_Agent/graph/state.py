from typing import TypedDict


class AgentState(TypedDict):
    image_path: str
    vision_output: dict
    cost_estimation: dict
    policy_answer: str
    final_decision: dict