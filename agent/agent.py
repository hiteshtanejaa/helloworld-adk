from google.adk.agents import Agent

def say_hello(name: str) -> str:
    """
    Greets the user by name.
    
    Args:
        name: The name of the person to greet.
    Returns:
        A greeting string.
    """
    return f"Hello, {name}! I am a deployed ADK agent."

def get_status() -> str:
    """
    Returns the operational status of the agent.
    
    Returns:
        A status confirmation string.
    """
    return "Agent is operational and ready to assist."

root_agent = Agent(
    name="hello_world_agent",
    model="gemini-2.5-flash",
    description="A simple hello world ADK agent.",
    instruction="""
        You are a friendly assistant.
        When a user gives you their name, use say_hello to greet them.
        When asked about your status, use get_status.
        Keep responses concise.
    """,
    tools=[say_hello, get_status],
)

