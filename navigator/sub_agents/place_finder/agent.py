# Google Cloud
# Agentic AI Hackatho
# XE GenAI UK

"""Place Finder Agent for the Navigator system.
This agent assists users with location-based queries, such as finding specific places (e.g., EV charging stations, restaurants, landmarks).
It uses the Google Maps Platform tools to find places based on user queries and provides relevant information about those places.
"""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from navigator.shared_libraries.types import DestinationIdeas, POISuggestions, json_response_config
from navigator.sub_agents.place_finder import prompt
from navigator.tools.places import map_tool

place_finder_agent = Agent(
    model="gemini-2.5-flash",
    name="place_finder_agent",
    description="An agent that assists users with location-based queries, such as finding specific places (e.g., EV charging stations, restaurants, landmarks).",
    instruction=prompt.PLACE_FINDER_PROMPT,
    tools=[map_tool],
)

