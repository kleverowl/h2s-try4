from datetime import date, datetime, timedelta

from google.adk.agents import LlmAgent


def search_trains(origin_station_code: str, destination_station_code: str, travel_date: str) -> str:
    """
    Searches for all available trains on a given route and date.

    Args:
        origin_station_code: The station code for the origin.
        destination_station_code: The station code for the destination.
        travel_date: The date of travel in YYYY-MM-DD format.

    Returns:
        A string with the search results.
    """
    # Mock data for train search
    return f"Found 3 trains from {origin_station_code} to {destination_station_code} on {travel_date}. Train numbers: 12345, 67890, 13579"


def check_seat_availability(train_number: str, travel_class: str, date: str) -> str:
    """
    Checks the number of available seats for a specific train.

    Args:
        train_number: The number of the train.
        travel_class: The class of travel (e.g., 'Sleeper', '3A', '2A', '1A').
        date: The date of travel in YYYY-MM-DD format.

    Returns:
        A string with the availability information.
    """
    # Mock data for seat availability
    return f"Availability for train {train_number} in {travel_class} on {date}: 100 seats available."


def create_agent() -> LlmAgent:
    """Constructs the ADK agent for the train_concierge."""
    return LlmAgent(
        model="gemini-2.5-flash",
        name="train_concierge",
        instruction="""
            **Role:** You are an Indian Railways Travel Specialist.
            Your sole responsibility is to find and manage train travel options within India.

            **Core Directives:**

            *   **Find Trains:** Use the `search_trains` tool to find all available trains on a given route and date.
            *   **Check Seat Availability:** Use the `check_seat_availability` tool to check the number of available seats for a specific train.
            *   **Prioritize Routes:** Always prioritize direct routes and convenient timings.
            *   **Polite and Concise:** Always be polite and to the point in your responses.
            *   **Stick to Your Role:** Do not engage in any conversation outside of train travel.
                    If asked other questions, politely state that you can only help with train travel inquiries.
        """,
        tools=[search_trains, check_seat_availability],
    )
