## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* affirm
    - utter_continue
* affirm
    - issue_debt_info_form
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567895"}
    - form: issue_debt_info_form
    - slot{"cpf": "01234567895"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - utter_anything_else
* affirm
    - utter_what_do_you_want

## interactive_story_1
* get_debt_info{"month": "setembro"}
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* deny
    - utter_continue
* affirm
    - issue_debt_info_form
    - slot{"requested_slot": "cpf"}
* inform{"cep": "04537070"}
    - utter_unexpected_cep
    - issue_debt_info_form
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567898"}
    - form: issue_debt_info_form
    - slot{"cpf": "01234567898"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - utter_anything_else
* deny
    - utter_give_feedback
    - utter_bye

## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* inform{"email": "exemplo@mail.com"}
    - utter_unexpected_email
    - issue_debt_info_form
    - slot{"requested_slot": "cpf"}
* deny
    - utter_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - utter_anything_else
* affirm
    - utter_what_do_you_want

## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* inform{"cep": "04537080"}
    - utter_unexpected_cep
    - issue_duplicate_form
    - slot{"requested_slot": "cpf"}
* inform{"email": "email@globo.com"}
    - utter_unexpected_email
    - issue_duplicate_form
    - slot{"requested_slot": "cpf"}
* inform{"phone_number": "55 11 95375 5714"}
    - utter_unexpected_phone_number
    - issue_duplicate_form
    - slot{"requested_slot": "cpf"}
* form: inform{"month": "maio"}
    - utter_unexpected_month
    - issue_duplicate_form
    - slot{"requested_slot": "cpf"}
* form: inform{"year": "2019"}
    - utter_unexpected_year
    - issue_duplicate_form
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567895"}
    - form: issue_duplicate_form
    - slot{"cpf": "01234567895"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - utter_anything_else

## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* deny
    - utter_continue
* affirm
    - issue_debt_info_form
    - slot{"requested_slot": "cpf"}
* deny
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - utter_anything_else
    
## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* faq
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - respond_faq
    
## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* update_cep
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - utter_update_unavailable
    - utter_ask_any_other_data
* deny
  - utter_what_do_you_want

## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* update_cpf
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - utter_update_unavailable
    - utter_ask_any_other_data
* affirm
  - utter_ask_which_data

## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* update_email
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - update_email_form
    - form{"name": "update_email_form"}
    - slot{"requested_slot": "cpf"}

## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* get_power_outage_information
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - provide_power_supply_info_form
    - form{"name": "provide_power_supply_info_form"}
    - slot{"requested_slot": "cep"}

## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* get_duplicate_bill
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - issue_debt_info_form
    - form{"name": "issue_duplicate_form"}
    - slot{"requested_slot": "cpf"}

## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* supply_power_outage_information
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - provide_power_supply_info_form
    - form{"name": "provide_power_supply_info_form"}
    - slot{"requested_slot": "cep"}

## interactive_story_1
* get_debt_info
    - issue_debt_info_form
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}
* update_phone_number
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
    - slot{"requested_slot": "cpf"}