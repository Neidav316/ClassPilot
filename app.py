import streamlit as st

# Role initialize in session state and default value for role
if "role" not in st.session_state:
    st.session_state.role = "Admin"  # default = ADMIN, upon app activation, the user will sign in automatically as ADMIN

ROLES = [None, "Teacher", "Student", "Admin"]

role = st.session_state.role

# Page Configuration

st.set_page_config(page_title="ClassPilot AI", page_icon=":rocket:", layout="wide")
st.sidebar.title("ClassPilot AI")

# Logout and Settings pages
logout_page = st.Page("pages/auth/logout_page.py", title="Log out")
settings = st.Page("settings.py", title="Settings")

### Teacher Pages
lesson_planner = st.Page("pages/teacher/LessonPlanner.py", title="Lesson Planner", default=(role == "Teacher"))

### Student Pages
lesson_requester_page = st.Page("pages/student/requestLesson.py", title="Lesson Requester", default=(role == "Student"))
chatbot_page = st.Page("pages/student/chatBot.py", title="ChatBot Assistant")
lesson_presenter_page = st.Page("pages/student/lessonPresenter.py", title="Lesson Presenter")
questioner_page = st.Page("pages/student/questioner.py", title="Questioner")

admin_1 = st.Page("pages/admin/admin_1.py", title="Admin 1", default=(role == "Admin"))

# Sorting the pages according to relevancy, for neet side menu in navigation
account_pages = [settings, logout_page]
teacher_pages = [lesson_planner]
student_pages = [lesson_requester_page, chatbot_page, lesson_presenter_page, questioner_page]
admin_pages = [admin_1]

st.title("ClassPilot AI")

st.logo("images/app_Logo.jpg", icon_image="images/app_Logo.jpg")

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

def switch_page(filePath):
    st.switch_page(filePath)