from typing import Dict, Text, Any, List, Union
import re
import datetime
import difflib

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

from db import User


class IssueDuplicateForm(FormAction):

    def name(self) -> Text:
        return "issue_debt_info_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cpf"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cpf": self.from_entity(entity="cpf", intent="inform")
        }

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        document = tracker.get_slot("cpf")

        user = User.where(User.document == document).first()

        if user is None:
            dispatcher.utter_message(template="utter_no_document_match")
            return []

        bills = [bill for bill in user.bills if bill.paid is False]

        if not bills:
            dispatcher.utter_message(template="utter_no_debt")
            return []

        total_amount = 0.0
        bills_message = f"Você tem {len(bills)} contas não pagas:\n"
        for bill in bills:
            due_date = bill.due_date.strftime('%d/%m/%Y')
            amount = f"{bill.value:_.2f}".replace(".", ",").replace("_", ".")
            total_amount += bill.value
            bills_message += f"- Conta de {due_date} no valor de R${amount}\n"

        dispatcher.utter_message(text=bills_message)

        total_amount_msg = f"{total_amount:_.2f}"
        total_amount_msg = total_amount_msg.replace(".", ",").replace("_", ".")
        dispatcher.utter_message(
            text=f"No total, você deve R${total_amount_msg}")

        return []

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
