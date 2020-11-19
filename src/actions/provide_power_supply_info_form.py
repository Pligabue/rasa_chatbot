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


class ProvidePowerSupplyInfoForm(FormAction):

    def name(self) -> Text:
        return "provide_power_supply_info_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["cep", "supplying_info"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cep": [self.from_entity(entity="cep", intent="inform")],
            "supplying_info": [
                self.from_trigger_intent(
                    intent="supply_power_outage_information",
                    value=True),
                self.from_trigger_intent(
                    intent="get_power_outage_information",
                    value=False)
            ]
        }

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        cep = tracker.get_slot("cep")
        supplying_info = tracker.get_slot("supplying_info")
        power_supply = get_postal_code_power_supply(cep)

        if power_supply is None:
            dispatcher.utter_message(template="utter_no_power_supply")
            
        elif power_supply.is_down():
            occurrence = power_supply.occurrences.first()
            dispatcher.utter_message(
                template="utter_power_supply_info",
                status=("não está funcionando momentaneamente"))

            messages = get_occurrence_messages(occurrence)
            dispatcher.utter_message(
                template="utter_occurrence_status",
                category=messages["category"],
                status=messages["status"],
                estimation=messages["estimation"],
                additional_comments=messages["additional_comments"])

        elif power_supply.is_up():
            if supplying_info:
                occurrence = Occurrence(power_supply=power_supply,
                                        category="power_outage",
                                        status="pending",
                                        start_time=datetime.now())

                power_supply.status = "pending"
                session.add(occurrence)
                session.commit()
                dispatcher.utter_message(template="utter_start_investigations")
            else:
                dispatcher.utter_message(
                    text="A enegia na sua região está funcionando normalmente.")

        elif power_supply.is_pending():
            if supplying_info:
                occurrence = power_supply.occurrences.first()
                occurrence.status = "in_progress"
                power_supply.status = "down"
                session.commit()
                dispatch_team(occurrence)
                dispatcher.utter_message(template="utter_team_on_the_way")
            else:
                dispatcher.utter_message(
                    text="Estamos verificando a situação na sua região. Por favor, aguarde mais desenvolvimentos.")
        return []

    def validate_cep(self,
                     value: Text,
                     dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Dict[Text, Any]:

        cep = re.sub(r"[^\d]", "", value)

        if len(cep) == 8:
            return {"cep": cep}
        else:
            dispatcher.utter_message(template="utter_invalid_cep")
            return {"cep": None}
