class ChatBotFile:
    OLLAMA_MODEL = "llama3"
    PLAIN_TEXT_FILE = """FROM {}\n# set the system prompt\nSYSTEM \"\"\"\n{}\n\"\"\""""

    def __init__(self, chatbot_name, prompt):
        self.chatbot_name = chatbot_name
        self.prompt = prompt

    def plain_text(self):
        return self.PLAIN_TEXT_FILE.format(self.OLLAMA_MODEL, self.prompt)
