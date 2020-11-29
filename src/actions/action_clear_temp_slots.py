from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from typing import Dict, Text, Any, List


class ClearTempSlots(Action):
    def name(self) -> Text:
        return "action_clear_temp_slots"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [
            SlotSet("month", None),
            SlotSet("year", None),
            SlotSet("phone_number", None),
            SlotSet("email", None),
            SlotSet("cep", None)
        ]
