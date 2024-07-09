import json

import click
import streamlit as st
import pandas as pd


def get_subjects(filter=None):
    f = open("utils/data/lesson_content.json")
    return json.load(f)


data = get_subjects()

df = pd.DataFrame({
    "Main Subject": [subject_content["subject"] for subject_content in data["subjects"]],
    "Link Lesson": ['Start Lesson' for _ in data["subjects"]],
    "Link Bot": ["Chat with bot" for _ in data["subjects"]]
})

st.header("Lesson Requester")
st.write(f"You are logged in as {st.session_state.role}.")

for index, row in df.iterrows():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(row["Main Subject"])
    with col2:
        if st.button(row["Link Lesson"], key=f"lesson{index}"):
            if "subject_content" not in st.session_state:
                st.session_state.subject_content = "Python"
            st.session_state.subject_content = row["Main Subject"]
            st.switch_page("pages/teacher/lessonPrepare.py")
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
