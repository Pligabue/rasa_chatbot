from typing import Dict, Text, Any
import re

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from db import User


class CPFValidation:

    def validate_cpf(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Dict[Text, Any]:

        cpf = re.sub(r"[^\d]", "", value)

        user = User.where(User.document == cpf).first()

        if user is None:
            if len(cpf) == 11:
                dispatcher.utter_message(template="utter_no_document_match")
            else:
                dispatcher.utter_message(template="utter_invalid_cpf")
            return {"cpf": None}
        else:
            return {"cpf": cpf}