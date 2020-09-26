from typing import Dict, Text, Any, List, Union, Optional
import re
import datetime
import difflib

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.executor import CollectingDispatcher

from db import session, User, PowerSupply, Occurrence

from helpers.user_power_supply import get_user_power_supply

class ProvidePowerSupplyInfoForm(FormAction):

    def name(self) -> Text:
        return "provide_power_supply_info_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cpf"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cpf": self.from_entity(entity="cpf", intent="inform")
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        document = tracker.get_slot("cpf")

        user = session.query(User).filter(User.document == document).one_or_none()
        if user is None:
            dispatcher.utter_message(template="utter_no_document_match")
            return []

        power_supply = get_user_power_supply(user)
        occurrence = power_supply.occurrences.first()

        dispatcher.utter_message(
            template="utter_power_supply_info",
            status=("não está funcionando momentaneamente" if power_supply.down() 
                    else "funcionando normalmente"))

        category = ("Uma manutenção" if occurrence.category_is("maintenance") else 
                    "Uma queda de energia" if occurrence.category_is("power_outage") else
                    "Um problema")
        status = ("está sendo feita" if occurrence.status_is("in_progress") and occurrence.category_is("maintenance") else
                  "está pendente" if occurrence.status_is("pending") and occurrence.category_is("maintenance") else
                  "está sendo investigada" if occurrence.status_is("in_progress") and occurrence.category_is("power_outage") else 
                  "ocorreu")
        if occurrence.has_estimation():
            hours_until_estimation = occurrence.time_until_estimation().total_seconds()//3600
            if hours_until_estimation < 1:
                estimation = f"A operação deve ser normalizada em menos de uma hora"
            else:
                estimation = f"A operação deve ser normalizada dentro de {hours_until_estimation} hora{'s' if hours_until_estimation == 1 else ''}"
        else:
            estimation = "Ainda não há previsão de conclusão"
        additional_comments = f"Para acompanhar o status da ocorrência, acesse sitegenerico.com/ocorrencia/{occurrence.id}."

        if power_supply.down():
            dispatcher.utter_message(
                template="utter_occurrence_status",
                category=category,
                status=status,
                estimation=estimation,
                additional_comments=additional_comments)
         
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
            return { "cpf": None}
