## test duplicate bill
* greet: olá
  - utter_greet
* get_duplicate_bill: gostaria da segunda via de uma conta
  - issue_duplicate_form
  - slot{"cpf": "01234567890"}
  - slot{"month": 5}
  - slot{"year": 2020}
  - action_clear_temp_slots
  - utter_anything_else
* deny: nao
  - utter_give_feedback
  - utter_bye
* bye: adeus
  - action_restart