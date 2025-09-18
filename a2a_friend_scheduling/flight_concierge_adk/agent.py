from datetime import date, datetime, timedelta

from google.adk.agents import LlmAgent


def search_flights(
    origin_airport_code: str, destination_airport_code: str, travel_date: str
) -> str:
    """
    Searches for all available flights on a given route and date.

    Args:
        origin_airport_code: The airport code for the origin.
        destination_airport_code: The airport code for the destination.
        travel_date: The date of travel in YYYY-MM-DD format.

    Returns:
        A string with the search results.
    """
    # Mock data for flight search
    return f"Found 5 flights from {origin_airport_code} to {destination_airport_code} on {travel_date}. Flight numbers: UA123, DL456, AA789, WN012, AS345"


def create_agent() -> LlmAgent:
    """Constructs the ADK agent for the flight_concierge."""
    return LlmAgent(
        model="gemini-2.5-flash",
        name="flight_concierge",
        instruction="""
            **Role:** You are a Flight Booking Specialist.
            Your sole responsibility is to find and manage flight travel options.

            **Core Directives:**

            *   **Find Flights:** Use the `search_flights` tool to find all available flights on a given route and date.
            *   **Polite and Concise:** Always be polite and to the point in your responses.
            *   **Stick to Your Role:** Do not engage in any conversation outside of flight travel.
                    If asked other questions, politely state that you can only help with flight travel inquiries.
        """,
        tools=[search_flights],
    )
