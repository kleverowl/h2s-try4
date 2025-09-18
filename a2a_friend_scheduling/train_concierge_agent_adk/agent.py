import random
from datetime import date, datetime, timedelta

from google.adk.agents import LlmAgent


def search_trains(origin_station_code: str, destination_station_code: str, travel_date: str) -> str:
    """Searches for all available trains on a given route and date."""
    # Fallback Strategy
    return f"Automated train search is unavailable. I recommend the user check the official IRCTC website for train options between {origin_station_code} and {destination_station_code}."

def check_seat_availability(train_number: str, travel_class: str, date: str) -> str:
    """Checks the number of available seats for a specific train."""
    # Fallback Strategy
    return "Automated train search is unavailable. I recommend the user check the official IRCTC website for train options."


def create_agent() -> LlmAgent:
    """Constructs the ADK agent for train_concierge."""
    return LlmAgent(
        model="gemini-2.5-flash",
        name="train_concierge",
        instruction="""
            **Role:** You are an Indian Railways Travel Specialist.
            **Goal:** Find and manage train travel options within India.
            **Backstory:** You are an expert in navigating the Indian Railways system. You are adept at finding trains, checking seat availability, and understanding the different travel classes. You always prioritize direct routes and convenient timings.
        """,
        tools=[search_trains, check_seat_availability],
    )
