from typing import Dict, Text, Any, List, Union, Optional
import re
from datetime import datetime

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.executor import CollectingDispatcher

from db import session, User, PowerSupply, Occurrence, Address

from helpers.address_power_supply import get_postal_code_power_supply
from helpers.occurrence_messages import get_occurrence_messages

from services.dispatch_team import dispatch_team


class UpdateEmailForm(FormAction):

    def name(self) -> Text:
        return "update_email_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cpf", "email"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cpf": [self.from_entity(entity="cpf", intent="inform")],
            "email": [self.from_entity(entity="email", intent="inform")]
        }

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        
        cpf = tracker.get_slot("cpf")
        email = tracker.get_slot("email")

        user = (session.query(User)
                .filter(User.document == cpf)
                .one_or_none())

        user.email = email
        
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

    def validate_email(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Dict[Text, Any]:

        email = re.sub(r"[^a-zA-Z@\.]", "", value)

        if re.match(r"^.+@.+\..+$", email):
            return {"email": email}
        else:
            return {"email": None}