from a2a.server import Server
from google.adk.agents import Agent

from .agent import create_agent


def _get_agent() -> Agent:
    return create_agent()


agent_executor = Server(agent=_get_agent(), port=10005)
