import json

MAIN_DATA_PATH = "utils/data/"
SUBJECTS_PATH = "lesson_content.json"
STUDENT_DATA_PATH = "student_data.json"
LESSON_CONTENT_PATH = "lesson_content.json"
SECRET_KEYS = "secret_keys.json"
USERS_PATH = "users.json"
SLIDE_CONFIG_PATH = "slide_config.json"

def get_data_from_path(path):
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return {}
def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)