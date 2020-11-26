
## interactive_form_story_1
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
    - slot{"requested_slot": "cpf"}
* inform{"cep": "04537070"}
    - utter_unexpected_cep
    - update_phone_number_form
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567890"}
    - form: update_phone_number_form
    - slot{"cpf": "01234567890"}
    - slot{"requested_slot": "phone_number"}
* form: inform{"phone_number": "55 11 953755714"}
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

## interactive_form_story_2
* update_phone_number
    - update_email_form
    - form{"name": "update_email_form"}
    - slot{"requested_slot": "cpf"}
* inform{"cep": "04537070"}
    - utter_unexpected_cep
    - update_email_form
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567890"}
    - form: update_phone_number_form
    - slot{"cpf": "01234567890"}
    - slot{"requested_slot": "email"}
* form: inform{"email": "email@example.com"}
    - form: update_phone_number_form
    - slot{"phone_number": "email@example.com"}
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

## interactive_form_story_3
* get_power_outage_information
    - provide_power_supply_info_form
    - form{"name": "provide_power_supply_info_form"}
    - slot{"supplying_info": false}
    - slot{"requested_slot": "cep"}
* inform{"cpf": "48396334870"}
    - utter_unexpected_cpf
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}

## interactive_form_story_4
* supply_power_outage_information
    - provide_power_supply_info_form
    - form{"name": "provide_power_supply_info_form"}
    - slot{"supplying_info": true}
    - slot{"requested_slot": "cep"}
* inform{"cpf": "48396334870"}
    - utter_unexpected_cpf
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}

## interactive_form_story_5
* get_power_outage_information
    - provide_power_supply_info_form
    - form{"name": "provide_power_supply_info_form"}
    - slot{"supplying_info": false}
    - slot{"requested_slot": "cep"}
* inform{"phone_number": "55 11 953755714"}
    - utter_unexpected_phone_number
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}

## interactive_form_story_6
* supply_power_outage_information
    - provide_power_supply_info_form
    - form{"name": "provide_power_supply_info_form"}
    - slot{"supplying_info": true}
    - slot{"requested_slot": "cep"}
* inform{"cpf": "55 11 953755714"}
    - utter_unexpected_phone_number
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}

## interactive_form_story_7
* get_duplicate_bill
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"requested_slot": "cpf"}
* inform{"cep": "04537070"}
    - utter_unexpected_cep
    - issue_duplicate_form
    - slot{"requested_slot": "cpf"}

## interactive_story_8
* get_duplicate_bill{"month": "março"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 3}
    - slot{"requested_slot": "cpf"}
* inform{"cep": "78945651"}
    - utter_unexpected_cep
    - issue_duplicate_form
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567892"}
    - form: issue_duplicate_form
    - slot{"cpf": "01234567892"}
    - slot{"requested_slot": "year"}
* form: inform{"cpf": "48396334870"}
    - form: issue_duplicate_form
    - slot{"cpf": null}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567892"}
    - form: issue_duplicate_form
    - slot{"cpf": "01234567892"}
    - slot{"requested_slot": "year"}
* inform{"cep": "04537090"}
    - utter_unexpected_cep
    - issue_duplicate_form
    - slot{"requested_slot": "year"}
* form: inform{"year": "2018"}
    - form: issue_duplicate_form
    - slot{"year": 2018}
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

## interactive_story_9
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
    - slot{"requested_slot": "cpf"}
* inform{"month": "março"}
    - utter_unexpected_month
    - update_email_form
    - slot{"requested_slot": "cpf"}

## interactive_story_10
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
    - slot{"requested_slot": "cpf"}
* inform{"year": "2020"}
    - utter_unexpected_year
    - update_email_form
    - slot{"requested_slot": "cpf"}

## interactive_story_11
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
    - slot{"requested_slot": "cpf"}
* faq
    - form{"name": null}
    - respond_faq
    - utter_anything_else

## interactive_story_12
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
    - slot{"requested_slot": "cpf"}
* faq
    - form{"name": null}
    - respond_faq
    - utter_anything_else

## interactive_story_13
* get_duplicate_bill
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"requested_slot": "cpf"}
* faq
    - form{"name": null}
    - respond_faq
    - utter_anything_else