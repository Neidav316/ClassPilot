import streamlit as st
import reveal_slides as rs
import json
from utils.Prompts import prompts



# NOTES FOR Reveal_Slides syntex
# For making new slides, at the end of some string,
# horizontal slide (left,right), input ---, for a vertical slide (up,down), input --
# For making slide progress the text,
# input at end of string <!-- .element: class="fragment" data-fragment-index="<some number, start from 0>" -->
# For highlight text, input before text ##
# For linking a website link, [chosen string](url link)
# For changing background,input at start of string of slide <!-- .slide: data-background-color="#COLORCODE" -->
def json_to_slides(json_file):
    sample_text = ""
    sample_text = sample_text + f"# Subject Matter: {json_file['subject']}" + '\n' + "Presentation By ClassPilot \n---\n"
    for lesson in json_file["lessons"]:
        sample_text = sample_text + f"## {lesson['title']}" + "\n---\n"
        for page in lesson["pages"]:
            sample_text = sample_text + "\n" + f"### {page['title']}" + "\n" + f"{page['content']}" + "\n---\n"

    sample_text = sample_text + "# End \n ## Good Luck!"

    return sample_text

def set_subject_content(subjects):
    if "subject_content" in st.session_state:
        for subject in subjects["subjects"]:
            if subject["subject"] == st.session_state.subject_content:
                return subject

def get_subject_config():
    with open("utils/data/slide_config.json") as f:
        subjects = json.load(f)["subjects"]
    for subject in subjects:
        if subject["subject"] == st.session_state.subject_content:
            return subject["config"]


st.header("Lesson Presenter")
if st.session_state.subject_content == "":
    st.error("No lesson was chosen, please go back to main page")
    st.stop()

with open("utils/data/lesson_content.json") as f:
    content = json.load(f)
    subject = set_subject_content(content)
    sample_markdown = json_to_slides(subject)

config = get_subject_config()
currState = rs.slides(sample_markdown,
                      height=config["height"],
                      theme=config["theme"],  # color and font style of text
                      config={
                          # add the css cutsom font size
                          "center": True
                      },
                      markdown_props={"data-separator-vertical": "^--$"},
                      key="foo")

st.page_link("pages/student/chatBot.py", label="Ask ChatBot")


def main():
    pass


if __name__ == "__main__":
    main()
