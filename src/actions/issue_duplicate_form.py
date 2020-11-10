from typing import Dict, Text, Any, List, Union, Optional
import re
import datetime
import difflib

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.executor import CollectingDispatcher

from db import session, User


class IssueDuplicateForm(FormAction):

    def name(self) -> Text:
        return "issue_duplicate_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cpf", "month", "year"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cpf": self.from_entity(entity="cpf", intent="inform"),
            "year": self.from_entity(entity="year"),
            "month": self.from_entity(entity="month"),
        }

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        document = tracker.get_slot("cpf")
        month = tracker.get_slot("month")
        year = tracker.get_slot("year")

        user = (session.query(User)
                .filter(User.document == document)
                .one_or_none())

        if user is None:
            dispatcher.utter_message(template="utter_no_document_match")
            return []

        bills = [bill for bill in user.bills
                 if (bill.due_date.month == month and bill.due_date.year)]

        if not bills:
            dispatcher.utter_message(template="utter_no_bills")
            return []

        for bill in bills:
            is_past = bill.due_date < datetime.date.today()
            amount = f"{bill.value:_.2f}".replace(".", ",").replace("_", ".")
            date = f"{bill.due_date.strftime('%d/%m/%Y')}"
            template = (f"utter_{'past' if is_past else 'future'}_"
                        f"{'' if bill.paid else 'un'}paid_bill")

            dispatcher.utter_message(template=template,
                                     amount=amount,
                                     date=date)

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

    def validate_month(self,
                       value: Text,
                       dispatcher: CollectingDispatcher,
                       tracker: Tracker,
                       domain: Dict[Text, Any]) -> Dict[Text, Any]:

        months = ["janeiro", "fevereiro", "março",
                  "abril", "maio", "junho",
                  "julho", "agosto", "setembro",
                  "outubro", "novembro", "dezembro"]

        matches = difflib.get_close_matches(value.lower(), months)

        if not matches:
            return {"month": None}

        month_num = months.index(matches[0]) + 1
        return {"month": month_num}

    def validate_year(self,
                      value: Text,
                      dispatcher: CollectingDispatcher,
                      tracker: Tracker,
                      domain: Dict[Text, Any]) -> Dict[Text, Any]:
        try:
            year = int(value)
            if year > 2000:
                return {"year": year}

        except ValueError:
            return {"year": None}

        return {"year": None}
