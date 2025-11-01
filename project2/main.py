from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.llm import LLMChain
# from langchain_classic.memory.buffer import ConversationBufferMemory


template = PromptTemplate(
    input_variables=["tone", "topic"],
    template="Write a {tone} paragraph explaining {topic} to a 10-year-old"
)

# prompt = template.format(tone="friendly" , topic="the concept of AI")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", api_key = os.getenv("GOOGLE_API_KEY"))

# memory = ConversationBufferMemory()

# print(prompt)

chain = LLMChain(llm=llm , prompt=template)

result = chain.invoke({"tone":"friendly" , "topic":"the concept of AI"})

print(result['text'])