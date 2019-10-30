from rasa_sdk import Action
from rasa.core.events import Restarted


class ActionRestarted(Action):
    """ This is for restarting the chat"""
    def name(self):
        return "action_chat_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]
