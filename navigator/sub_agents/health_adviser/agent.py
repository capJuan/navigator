# Google Cloud
# Agentic AI Hackatho
# XE GenAI UK

""" Search for relevant information about health consideration to particular symptoms """

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from navigator.tools.search import google_search_grounding
from navigator.sub_agents.health_adviser import prompt


health_adviser_agent = Agent(
    model="gemini-2.5-flash",
    name="health_adviser_agent",
    description="Given a medical condition or symptoms, this agent provides the best course of action to keep the driver safe",
    instruction=prompt.HEALTH_ADVISER_AGENT_PROMPT,
    tools=[google_search_grounding],
)
