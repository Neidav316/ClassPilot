import streamlit as st
from groq import Groq
from utils.Prompts import prompts
import json

with open("utils/data/secret_keys.json") as f:
    keys = json.load(f)["Keys"]
    for key in keys:
        if key["Api Name"] == "ChatGroq":
            chatGroq_key = key["Key"]

st.header("Questioner")
st.write(f"You are logged in as {st.session_state.role}.")


# Model init
if chatGroq_key is None:
    print("Error loading the api key")
    client_questioner = None
else:
    client_questioner = Groq(api_key=chatGroq_key)

if "model_questioner" not in st.session_state:
    st.session_state["model_questioner"] = "llama3-70b-8192"

# Need to extract data from database
# Get system prompt for model to generate questions
# Get lesson plan content for generating questions
initial_prompt = prompts.prompt_questioner
if "subject_content" in st.session_state:
    with open("utils/data/lesson_plans.json") as f:
        content = json.load(f)
        for subject in content["subjects"]:
            if subject["subject"] == st.session_state.subject_content:
                prompt = initial_prompt + json.dumps(subject)
                system_prompt = {"role": "system", "content": prompt}


    with st.chat_message("assistant"):
        response = client_questioner.chat.completions.create(
            model=st.session_state["model_questioner"],
            messages=[system_prompt, {"role": "user", "content": "give me a question"}],
            max_tokens=2048,
            stream=False
        ).choices[0].message.content
        st.write(response)




#

def main():
    pass


if __name__ == "__main__":
    main()
