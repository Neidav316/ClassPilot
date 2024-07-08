import streamlit as st
from langchain_community.chat_models import ChatOllama
import ollama

st.header("Chatbot")
st.write(f"You are logged in as {st.session_state.role}.")

client_ollama = ollama.Client()

if "model_chat" not in st.session_state:
    st.session_state["model_chat"] = "llama3"

if "messages_chat" not in st.session_state:
    st.session_state.messages_chat = []
for message in st.session_state.messages_chat:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Say something")
if prompt:
    st.session_state.messages_chat.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        stream = client_ollama.chat.completions.create(
            model=st.session_state["model_chat"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages_chat
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages_chat.append({"role": "assistant", "content": response})


def main():
    pass


if __name__ == "__main__":
    main()
