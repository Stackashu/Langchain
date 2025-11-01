from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# Memory
memory = ConversationBufferMemory()

# Conversation chain
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

# Start chatting
conversation.predict(input="Hey, I’m Stackashu.")
conversation.predict(input="What did I just tell you?")
