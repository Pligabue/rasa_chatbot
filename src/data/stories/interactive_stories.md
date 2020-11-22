## interactive_story_1
* greet
    - utter_greet
* get_duplicate_bill
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"requested_slot": "cpf"}
* form: get_duplicate_bill{"month": "dezembro", "year": "2019"}
    - form: issue_duplicate_form
    - slot{"month": 12}
    - slot{"year": 2019}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567890"}
    - form: issue_duplicate_form
    - slot{"cpf": "01234567890"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - action_clear_temp_slots
    - utter_anything_else
    - utter_give_feedback
* deny
    - utter_bye
* bye
    - action_restart

    
## interactive_story_2
* get_duplicate_bill{"month": "setembro", "year": "2019"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 9}
    - slot{"year": 2019}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "0123465789"}
    - form: issue_duplicate_form
    - slot{"cpf": null}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567890"}
    - form: issue_duplicate_form
    - slot{"cpf": "01234567890"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - utter_anything_else
    - utter_give_feedback
* deny
    - utter_bye

## interactive_story_3
* get_duplicate_bill{"month": "outubro", "year": "2019"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 10}
    - slot{"year": 2019}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567891"}
    - form: issue_duplicate_form
    - slot{"cpf": "01234567891"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - utter_anything_else
    - utter_give_feedback
* deny
    - utter_bye
* bye

## interactive_story_1
* get_duplicate_bill{"month": "agosto", "year": "2020"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 8}
    - slot{"year": 2020}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "09876543210"}
    - form: issue_duplicate_form
    - slot{"cpf": "09876543210"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - utter_anything_else
    - utter_give_feedback

## interactive_story_1
* get_duplicate_bill{"month": "junho"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 6}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567892"}
    - form: issue_duplicate_form
    - slot{"cpf": "01234567892"}
    - slot{"requested_slot": "year"}
* form: inform{"year": "2019"}
    - form: issue_duplicate_form
    - slot{"year": 2019}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - utter_anything_else
    - utter_give_feedback

## interactive_story_1
* get_duplicate_bill{"month": "outubro", "year": "2020"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 10}
    - slot{"year": 2020}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "98765432105"}
    - form: issue_duplicate_form
    - slot{"cpf": null}
    - slot{"requested_slot": "cpf"}
* bye
    - form{"name": null}
    - utter_bye

## interactive_story_1
* get_duplicate_bill
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567892"}
    - form: issue_duplicate_form
    - slot{"cpf": "01234567892"}
    - slot{"requested_slot": "month"}
* form: inform{"month": "agosto", "year": "2019"}
    - form: issue_duplicate_form
    - slot{"year": 2019}
    - slot{"month": 8}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - utter_anything_else
    - utter_give_feedback

## interactive_story_1
* get_power_outage_information
    - provide_power_supply_info_form
    - form{"name": "provide_power_supply_info_form"}
    - slot{"supplying_info": false}
    - slot{"requested_slot": "cep"}
* form: inform{"cep": "02308201"}
    - form: provide_power_supply_info_form
    - slot{"cep": "02308201"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - utter_anything_else
    - utter_give_feedback

## interactive_story_1
* get_power_outage_information
    - provide_power_supply_info_form
    - form{"name": "provide_power_supply_info_form"}
    - slot{"supplying_info": false}
    - slot{"requested_slot": "cep"}
* form: inform{"cep": "02807100"}
    - form: provide_power_supply_info_form
    - slot{"cep": "02807100"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - utter_anything_else
    - utter_give_feedback
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "66243987905"}
    - form: update_phone_number_form
    - slot{"cpf": "66243987905"}
    - slot{"requested_slot": "phone_number"}
* form: inform{"phone_number": "+55 (11) 95375-5714"}
    - form: update_phone_number_form
    - slot{"phone_number": "5511953755714"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_any_more_data
* deny
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - utter_anything_else
    - utter_give_feedback
