from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Dict, Text, Any, List

from helpers.generate_test_user import generate_test_user


class SetupTestUser(Action):
    def name(self) -> Text:
        return "action_setup_test_user"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        test_user_info = generate_test_user()
        cpf = test_user_info["cpf"]
        cep = test_user_info["cep"]
        start_date = test_user_info["oldest_bill"].strftime("%d/%m/%Y")
        stop_date = test_user_info["most_recent_bill"].strftime("%d/%m/%Y")

        formatted_cpf = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        formatted_cep = f"{cep[0:5]}-{cep[5:8]}"
        dispatcher.utter_message(
            text=f"Para realizar o teste, utilize as seguintes informações:\n" +
                 f"- CPF: {formatted_cpf}\n" +
                 f"- CEP: {formatted_cep}")
        dispatcher.utter_message(text=f"Você tem contas de luz de {start_date} até {stop_date}")

        return []
