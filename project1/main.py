from constants import GOOGLE_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os

# Set the API key in environment if not already set
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

st.title("Langchain + Google Gemini Demo")
print("starting server")

input_text = st.text_input("Enter what do you want to ask")

# Check if Google API key is present
if not GOOGLE_API_KEY:
    print("Google API Key is missing. Please set your API key in constants.py.")
else:
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            api_key=GOOGLE_API_KEY,
            temperature=0.7
        )
        if input_text:
            response = llm.invoke(input_text)
            # print(response)
            st.write(response.content)
            
    except Exception as e:
        st.error(f"Error: {e}")
        print(e)