from typing import Dict, Text, Any, List, Union
import datetime
import difflib

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

from db import User
from .cpf_validation import CPFValidation


class IssueDuplicateForm(FormAction, CPFValidation):
    def name(self) -> Text:
        return "issue_duplicate_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cpf", "month", "year"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cpf": self.from_entity(entity="cpf", intent="inform"),
            "month": self.from_entity(entity="month"),
            "year": self.from_entity(entity="year"),
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
                 if (bill.due_date.month == month
                     and bill.due_date.year == year)]

        if not bills:
            dispatcher.utter_message(template="utter_no_bills",
                                     month=f"{month:02}",
                                     year=str(year)[-2:])
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
        month = months.index(matches[0]) + 1 if matches else None

        year = next(tracker.get_latest_entity_values("year"), None)

        if year is not None:
            return {"month": month}
        else:
            return {"month": month, "year": datetime.date.today().year}

    def validate_year(self,
                      value: Text,
                      dispatcher: CollectingDispatcher,
                      tracker: Tracker,
                      domain: Dict[Text, Any]) -> Dict[Text, Any]:
        try:
            year = int(value)
            if year < 2000:
                year = None
                dispatcher.utter_message(template="utter_invalid_year", min_year=2000)
        except ValueError:
            year = None
            dispatcher.utter_message(template="utter_invalid_year", min_year=2000)

        return {"year": year}
