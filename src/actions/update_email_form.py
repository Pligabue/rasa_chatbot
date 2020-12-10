from typing import Dict, Text, Any, List, Union
import re

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

from db import session, User
from .cpf_validation import CPFValidation


class UpdateEmailForm(FormAction, CPFValidation):

    def name(self) -> Text:
        return "update_email_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cpf", "email"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cpf": [self.from_entity(entity="cpf", intent="inform")],
            "email": [self.from_entity(entity="email", intent=["inform", "update_email"])]
        }

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        cpf = tracker.get_slot("cpf")
        email = tracker.get_slot("email")

        user = User.where(User.document == cpf).first()

        user.email = email

        session.commit()

        return []

    def validate_email(self,
                       value: Text,
                       dispatcher: CollectingDispatcher,
                       tracker: Tracker,
                       domain: Dict[Text, Any]) -> Dict[Text, Any]:

        email = re.sub(r"[^a-zA-Z@\.]", "", value)

        cpf = tracker.get_slot("cpf")
        user = User.where(User.document == cpf).first()
        current_email = ""
        if user is not None:
            current_email = " " + user.email

        if re.match(r"^.+@.+\..+$", email):
            dispatcher.utter_message(text=f"Seu email atual{current_email} será trocado por {email}")
            return {"email": email}
        else:
            dispatcher.utter_message(template="utter_invalid_email")
            return {"email": None}
