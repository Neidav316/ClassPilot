import streamlit as st
import json
from utils.Prompts  import prompts

from pages.student.chatbot.ChatBot import ChatBot


def json_to_text(json_content):
    complete_text = f"Subject: {json_content['subject']} \n"
    for lesson in json_content["lessons"]:
        complete_text += f"Lesson Title: {lesson['title']} \n"
        for page in lesson["pages"]:
            complete_text += f"Subtitle: {page['title']} \n content: {page['content']}\n"

    return complete_text

# def main():
# Initialize role in session state and default value for role
if "role" not in st.session_state:
    st.session_state.role = "Student"  # default role is Student

st.header("Chatbot")
st.write(f"You are logged in as {st.session_state.role}.")

# Load lesson text if not already loaded
if "text_lesson" not in st.session_state:
    with open("utils/data/lesson_plans.json", "r", encoding='utf-8') as file:
        content = json.load(file)["subjects"][0]
        initial_prompt = prompts.prompt_chatbot
        text = initial_prompt + json_to_text(content)
        st.session_state.text_lesson = text

# Initialize chatbot if not already initialized
if "chatbot" not in st.session_state:
    model = "example_bot"
    st.session_state.chatbot = ChatBot(model, st.session_state.text_lesson)

# Display chat messages from session state
if "messages_chat" not in st.session_state:
    st.session_state.messages_chat = []

for message in st.session_state.messages_chat:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
prompt = st.chat_input("Say something")
if prompt:
    st.session_state.messages_chat.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from chatbot
    with st.chat_message("assistant"):
        stream = st.session_state.chatbot.send_message(prompt)
        response = st.session_state.chatbot.respond()
        st.markdown(response)

    # Append assistant's response to messages_chat
    st.session_state.messages_chat.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    # main()
    pass