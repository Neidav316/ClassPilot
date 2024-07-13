import streamlit as st

from init_streamlit import init


init()
# Role initialize in session state and default value for role
# if "role" not in st.session_state:
#     st.session_state.role = None  # default = None, upon app activation, the user will sign in automatically as None
#
# if "subject_content" not in st.session_state:
#     st.session_state.subject_content = ""

role = st.session_state.role

# Logout and Settings pages
logout_page = st.Page("pages/auth/logout_page.py", title="Log out")
settings = st.Page("settings.py", title="Settings")

### Teacher Pages
lesson_planner_page = st.Page("pages/teacher/lessonCreator.py", title="Lesson Planner", default=(role == "Teacher"))
lesson_prepare_page = st.Page("pages/teacher/lessonPrepare.py", title="Lesson Prepare")
teacher_lesson_requester_page = st.Page("pages/teacher/requestLessonTeacher.py", title="Lesson List - Teacher")

### Student Pages
student_lesson_requester_page = st.Page("pages/student/requestLesson.py", title="Lesson List", default=(role == "Student"))
chatbot_page = st.Page("pages/student/chatBot.py", title="ChatBot Assistant")
lesson_presenter_page = st.Page("pages/student/lessonPresenter.py", title="Lesson Presenter")
questioner_page = st.Page("pages/student/questioner.py", title="Questioner")

admin_1 = st.Page("pages/admin/admin_1.py", title="Admin 1", default=(role == "Admin"))

# Sorting the pages according to relevancy, for neet side menu in navigation
account_pages = [settings, logout_page]
teacher_pages = [lesson_planner_page, lesson_prepare_page, teacher_lesson_requester_page]
student_pages = [student_lesson_requester_page, chatbot_page, lesson_presenter_page, questioner_page]
admin_pages = [admin_1]

# init the dict for the side menu display
page_dict = {}

if st.session_state.role in ["Teacher", "Admin"]:  # if user is role Admin or Teacher, it will add the pages to the dict
    page_dict["Teacher"] = teacher_pages
if st.session_state.role in ["Student", "Admin"]:  # if user is role Admin or Student, it will add the pages to the dict
    page_dict["Student"] = student_pages
if st.session_state.role == "Admin":  # if user is role Admin, it will add the pages to the dict
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:  # if dict is not empty, it will add the side menu navigation, and the default page that will
                        # be displayed will be according to role and the page that was set to default
    pg = st.navigation(page_dict | {"Account": account_pages})
else:  # if dict is empty, meaning role is None, it will navigate to log in page
    pg = st.navigation([st.Page("pages/auth/login_page.py")])
# Run the page
pg.run()

# def switch_page(filePath):
#     st.switch_page(filePath)