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

        user = User.where(User.document == document).first()

        if user is None:
            dispatcher.utter_message(template="utter_no_document_match")
            return []

        bills = [bill for bill in user.bills
                 if (bill.due_date.month == month and bill.due_date.year == year)]

        if not bills:
            dispatcher.utter_message(template="utter_no_bills", month=f"{month:02}", year=str(year)[-2:])
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

        user = User.where(User.document == cpf).first()
            
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
            month = None
        else:
            month = months.index(matches[0]) + 1

        year = tracker.get_slot("year")
        if year is None:
            year = datetime.date.today().year
            
        return {"month": month, "year": year}

    def validate_year(self,
                      value: Text,
                      dispatcher: CollectingDispatcher,
                      tracker: Tracker,
                      domain: Dict[Text, Any]) -> Dict[Text, Any]:

        try:
            year = int(value)
            if year < 1900:
                year = None
                dispatcher.utter_template("utter_invalid_year")
        except ValueError:
            year = None
            dispatcher.utter_template("utter_invalid_year")

        return {"year": year}
