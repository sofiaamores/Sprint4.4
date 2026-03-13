from agents import Runner
from agents import set_default_openai_key

import os
from dotenv import load_dotenv

from agents.main_agent import main_agent
from .conversation import ConversationManager


load_dotenv()

set_default_openai_key(os.getenv("OPENAI_API_KEY"))


from agents import Runner
from agents.main_agent import main_agent

from .conversation import ConversationManager


class Chatbot:

    def __init__(self):
        self.conversation = ConversationManager()

    def process_user_input(self, user_input):

        self.conversation.add_user_message(user_input)

        print("Agente analizando la solicitud...")

        result = Runner.run_sync(main_agent, user_input)

        response = result.final_output

        self.conversation.add_assistant_message(response)

        return response
