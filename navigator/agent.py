# Google Cloud
# Agentic AI Hackatho
# XE GenAI UK

""" Agent for navigating and managing travel itineraries."""

from google.adk.agents import Agent
from navigator import prompt

from navigator.sub_agents.health_adviser.agent import health_adviser_agent
from navigator.sub_agents.place_finder.agent import place_finder_agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A Navigator using the services of a multi-agent EV assistant system.",
    instruction=prompt.ROOT_AGENT_PROMPT,
    sub_agents=[
        health_adviser_agent,
        place_finder_agent,
    ],
)  