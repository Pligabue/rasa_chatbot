# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Dict, Text, Any, List, Union, Optional
import re

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.executor import CollectingDispatcher

class PersonalInfoForm(FormAction):

    def name(self) -> Text:
        return "personal_info_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cpf", "name"]

    def slot_mappings(self):
        return {
            "cpf": self.from_entity(entity="cpf", intent="provide_cpf"),
            "name": self.from_entity(entity="name", intent="provide_name")
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit")
        return []

    def validate_cpf(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        cpf = re.sub(r"[^\d]", "", value)
        if len(cpf) == 11:
            return { "cpf": cpf }
        else:
            dispatcher.utter_message(template="utter_invalid_cpf")
            return { "cpf": None}

