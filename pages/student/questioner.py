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

# Get system prompt for model to generate questions
system_prompt = {"role": "system", "content": prompts.prompt_questioner}

# Get lesson plan content for generating questions
# Need to extract data from database



#

def main():
    pass


if __name__ == "__main__":
    main()
