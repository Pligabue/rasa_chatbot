from typing import Dict, Text, Any, List, Union
import re

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

from db import session, User

import phonenumbers


class UpdatePhoneNumberForm(FormAction):

    def name(self) -> Text:
        return "update_phone_number_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cpf", "phone_number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cpf": [self.from_entity(entity="cpf", intent="inform")],
            "phone_number": [self.from_entity(entity="phone_number", intent="inform")]
        }

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        
        cpf = tracker.get_slot("cpf")
        phone_number = tracker.get_slot("phone_number")

        user = (session.query(User)
                .filter(User.document == cpf)
                .one_or_none())

        user.phone_number = phone_number

        session.commit()
        
        return []

    def validate_cpf(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Dict[Text, Any]:

        cpf = re.sub(r"[^\d]", "", value)

        user = (session.query(User)
                .filter(User.document == cpf)
                .one_or_none())
            
        if user is None:
            if len(cpf) == 11:
                dispatcher.utter_message(template="utter_no_document_match")
            else:
                dispatcher.utter_message(template="utter_invalid_cpf")
            return {"cpf": None}
        else:
            return {"cpf": cpf}

    def validate_phone_number(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Dict[Text, Any]:

        phone_number = "+" + re.sub(r"[^\d]", "", value)

        parsed_number = phonenumbers.parse(phone_number)

        if phonenumbers.is_valid_number(parsed_number):
            return {"phone_number": phone_number}
        else:
            dispatcher.utter_message(template="utter_invalid_phone_number")
            return {"phone_number": None}
            