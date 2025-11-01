from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import initialize_agent, AgentType
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Solution: the agent tool must take a single string input argument.
# We'll parse this string (format: "<value> <from_unit> to <to_unit>") in the tool.

@tool("convert_temp")
def convert_temp(input: str) -> str:
    """
    Convert temperature from one unit to another.
    Input format: "<value> <from_unit> to <to_unit>", e.g. "25 celsius to fahrenheit"
    """
    try:
        # Split input string such as "25 celsius to fahrenheit"
        parts = input.lower().split()
        if "to" not in parts or len(parts) < 4:
            return "Invalid input format. Please use '<value> <from_unit> to <to_unit>'."
        to_index = parts.index("to")
        value = float(parts[0])
        from_unit = parts[1]
        to_unit = parts[to_index + 1]
        if from_unit == to_unit:
            return f"{value} {from_unit.capitalize()} is already {value} {to_unit.capitalize()}"
        if from_unit == "celsius" and to_unit == "fahrenheit":
            result = value * 9 / 5 + 32
            return f"{value} Celsius is {result} Fahrenheit"
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            result = (value - 32) * 5 / 9
            return f"{value} Fahrenheit is {result} Celsius"
        else:
            return "Unsupported unit conversion. Supported: Celsius <-> Fahrenheit."
    except Exception as e:
        return f"Error: {e}"

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", api_key=api_key)

tools = [convert_temp]

agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

response = agent.run("Convert 25 celsius to fahrenheit")
print("\nAnswer:", response)