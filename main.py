import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


model = ChatGoogleGenerativeAI(model='gemini-3.6-flash', google_api_key=api_key)


st.title("Basic chat bot")

user_input = st.chat_input("You:")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    output = model.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=output.content))

    st.write("You:", user_input)
    st.write("AI:", output.content[0]["text"])
