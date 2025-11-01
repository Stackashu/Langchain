from dotenv import load_dotenv
import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import initialize_agent , AgentType, load_tools


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(mode="gemini-2.5-flash-lite" , api_key=api_key)

tools  = load_tools(["llm-math"],llm=llm)

agent = initialize_agent(tools,llm,agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION , verbose=True)


response = agent.run("If a car travels at 70 km/h for 4.5 hours, how far does it go?")
print("\nAnswer:", response)