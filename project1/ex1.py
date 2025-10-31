# from itertools import chain
import langchain
from langchain_classic.chains.sequential import SequentialChain
from constants import GOOGLE_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains.llm import LLMChain
# from langchain.tools import 
from langchain_core.prompts import PromptTemplate
# from langchain_core.runnables import RunnableSequence
import streamlit as st
import os

# Set the API key in environment if not already set
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

print("starting server")
input_text = st.text_input("Celebrity Search Results")

first_input = PromptTemplate(
    input_variables=["name"],
    template="Tell me about celebrity {name}"
)

second_input = PromptTemplate(
    input_variables=["person"],
    template="When was {person} born"
)

if not GOOGLE_API_KEY:
    print("Google API Key is missing. Please set your API key in constants.py.")
else:
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            api_key=GOOGLE_API_KEY,
            temperature=0.7
        )

        # chain1: prompt about celebrity -> LLM
        # chain2: prompt about birth using output of chain1 -> LLM
        chain1 = LLMChain(llm=llm , prompt=first_input , verbose=True , output_key='person')
        chain2 = LLMChain(llm=llm , prompt=second_input , verbose=True , output_key='dob')
        
        parent_chain = SequentialChain(chains=[chain1,chain2] , verbose=True)
        

        # Sequence: output of chain1 feeds as 'person' to chain2
        

        if input_text:
            result = parent_chain.invoke({"name": input_text})
            st.write(result.content if hasattr(result, "content") else result)
    except Exception as e:
        print(e)