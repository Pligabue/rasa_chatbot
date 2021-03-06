from typing import Dict, Text, Any, List, Union
import re

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

from phonenumbers import parse, is_valid_number, format_number
from phonenumbers import phonenumberutil, PhoneNumberFormat

from db import session, User
from .cpf_validation import CPFValidation


class UpdatePhoneNumberForm(FormAction, CPFValidation):

    def name(self) -> Text:
        return "update_phone_number_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cpf", "phone_number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cpf": [self.from_entity(entity="cpf", intent="inform")],
            "phone_number": [self.from_entity(entity="phone_number",
                                              intent=["inform", "update_phone_number"])]
        }

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        cpf = tracker.get_slot("cpf")
        phone_number = tracker.get_slot("phone_number")

        user = User.where(User.document == cpf).first()

        user.phone_number = phone_number

        session.commit()

        return []

    def validate_phone_number(self,
                              value: Text,
                              dispatcher: CollectingDispatcher,
                              tracker: Tracker,
                              domain: Dict[Text, Any]) -> Dict[Text, Any]:

        striped_phone_number = re.sub(r"[^\d]", "", value)
        phone_number = "+" + striped_phone_number

        cpf = tracker.get_slot("cpf")
        user = User.where(User.document == cpf).first()
        formatted_current_number = ""
        if user is not None:
            try:
                parsed_current_number = parse("+" + user.phone_number)
                formatted_current_number = " " + format_number(parsed_current_number, PhoneNumberFormat.INTERNATIONAL)
            except phonenumberutil.NumberParseException:
                pass

        try:
            parsed_number = parse(phone_number)
            if is_valid_number(parsed_number):
                formatted_new_number = format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)  
                dispatcher.utter_message(
                    text=f"Seu telefone atual{formatted_current_number} será trocado por {formatted_new_number}")
                return {"phone_number": striped_phone_number}
        except phonenumberutil.NumberParseException:
            pass

        dispatcher.utter_message(template="utter_invalid_phone_number")
        return {"phone_number": None}
