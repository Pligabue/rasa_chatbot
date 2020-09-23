from typing import Dict, Text, Any, List, Union, Optional
import re
import datetime
import difflib

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.executor import CollectingDispatcher

from db import Session, User

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

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        document = tracker.get_slot("cpf")
        month = tracker.get_slot("month")
        year = tracker.get_slot("year")

        session = Session()

        user = session.query(User).filter(User.document == document).one_or_none()
        if user is None:
            dispatcher.utter_message(template="utter_no_document_match")
            return []

        bills = filter(lambda bill: (bill.due_date.month == month and bill.due_date.year == year), user.bills)
        if not bills:
            dispatcher.utter_message(template="utter_no_bills")
            return []

        for bill in bills:
            is_past = bill.due_date < datetime.date.today()
            paid = bill.paid
            template = f"utter_{'past' if is_past else 'future'}_{'paid' if paid else 'unpaid'}_bill"
            amount = f"{bill.value:_.2f}".replace(".", ",").replace("_", ".")
            date = f"{bill.due_date.strftime('%d/%m/%Y')}"
            dispatcher.utter_message(template=template, amount=amount, date=date)      
        return []

    def validate_cpf(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print(f"CPF IS {value}")
        cpf = re.sub(r"[^\d]", "", value)
        if len(cpf) == 11:
            return { "cpf": cpf }
        else:
            dispatcher.utter_message(template="utter_invalid_cpf")
            return { "cpf": None }

    def validate_month(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        month_name = value.lower()    
        months = ["janeiro", "fevereiro", "março", 
                  "abril", "maio", "junho",
                  "julho", "agosto", "setembro", 
                  "outubro", "novembro", "dezembro"]
        matches = difflib.get_close_matches(month_name, months)
        if not matches:
            return { "month": None }
        print(f"match is {months.index(matches[0])}")
        month_num = months.index(matches[0]) + 1
        print(f"month is {month_num}")
        return { "month": month_num }

    def validate_year(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        try:
            year = int(value)    
            if year > 2000:
                return { "year": year }
            return { "year": None }
        except ValueError:
            return { "year": None }
