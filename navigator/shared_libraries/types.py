# Google Cloud
# Agentic AI Hackatho
# XE GenAI UK

"""Common data schema and types for navigator agents."""

from pydantic import BaseModel, Field
from google.genai import types


class Destination(BaseModel):
    """A destination recommendation."""
    name: str = Field(description="A Destination's Name")
    country: str = Field(description="The Destination's Country Name")
    image: str = Field(description="verified URL to an image of the destination")
    highlights: str = Field(description="Short description highlighting key features")
    rating: str = Field(description="Numerical rating (e.g., 4.5)")


class DestinationIdeas(BaseModel):
    """Destinations recommendation."""
    places: list[Destination]

class POI(BaseModel):
    """A point of interest recommendation."""
    name: str = Field(description="A Point of Interest's Name")
    category: str = Field(description="The Category of the Point of Interest")
    location: str = Field(description="The Location of the Point of Interest")
    image: str = Field(description="verified URL to an image of the point of interest")
    rating: str = Field(description="Numerical rating (e.g., 4.5)")


class POISuggestions(BaseModel):
    """Points of interest recommendation."""
    places: list[POI]

# Convenient declaration for controlled generation.
json_response_config = types.GenerateContentConfig(
    response_mime_type="application/json"
)