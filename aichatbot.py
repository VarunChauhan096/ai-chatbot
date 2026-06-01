import streamlit as st
from groq import Groq

st.title("AI CHATBOT 🤖")
st.write("Solution to Your Problems !")

api_key = st.text_input("Enter your API key here", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message here.....")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    if not api_key:
        st.warning("Please enter your Groq API key!")
        st.stop()
    else:
        client = Groq(api_key=api_key)
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.write(reply)