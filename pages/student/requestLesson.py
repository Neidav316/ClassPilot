import json

import click
import streamlit as st
import pandas as pd


def get_finished_subjects(filter=None):
    f_data = open("utils/data/lesson_content.json")
    f_config = open("utils/data/slide_config.json")
    lesson_data = json.load(f_data)
    config = json.load(f_config)
    ready_subjects = {"subjects":[]}
    for subject in lesson_data["subjects"]:
        for config_subject in config["subjects"]:
            if subject["subject"] == config_subject["subject"]:
                ready_subjects["subjects"].append(subject)
                break

    return ready_subjects


data = get_finished_subjects()
# st.write(data)
df = pd.DataFrame({
    "Main Subject": [subject_content["subject"] for subject_content in data["subjects"]],
    "Link Lesson": ['Start Lesson' for _ in data["subjects"]],
    "Link Bot": ["Chat with bot" for _ in data["subjects"]]
})

st.header("Lesson Requester")
st.write(f"You are logged in as {st.session_state.role}.")

for index, row in df.iterrows():
    col1, col2, col3 = st.columns([1,1,5])
    with col1:
        st.write(row["Main Subject"].capitalize())
    with col2:
        if st.button(row["Link Lesson"], key=f"lesson{index}"):
            if "subject_content" not in st.session_state:
                st.session_state.subject_content = "Python"
            st.session_state.subject_content = row["Main Subject"]
            st.switch_page("pages/student/lessonPresenter.py")
    with col3:
        if st.button(row["Link Bot"], key=f"bot{index}"):
            if "subject_content" not in st.session_state:
                st.session_state.subject_content = "Python"
            st.session_state.subject_content = row["Main Subject"]
            st.switch_page("pages/student/chatBot.py")


def main():
    pass


if __name__ == "__main__":
    main()
