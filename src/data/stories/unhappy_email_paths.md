
## interactive_story_1
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567896"}
    - form: update_email_form
    - slot{"cpf": "01234567896"}
    - slot{"requested_slot": "email"}
* inform{"month": "abril"}
    - utter_unexpected_month
    - update_email_form
    - slot{"requested_slot": "email"}
* inform{"year": "2020"}
    - utter_unexpected_year
    - update_email_form
    - slot{"requested_slot": "email"}
* inform{"cep": "04537070"}
    - utter_unexpected_cep
    - update_email_form
    - slot{"requested_slot": "email"}
* form: inform{"email": "pliga@globo.com"}
    - form: update_email_form
    - slot{"email": "pliga@globo.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_clear_temp_slots
    - slot{"month": null}
    - slot{"year": null}
    - slot{"phone_number": null}
    - slot{"email": null}
    - slot{"cep": null}
    - utter_ask_any_more_data
* deny
    - utter_anything_else

## interactive_story_1
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "04567891325"}
    - form: update_email_form
    - slot{"cpf": null}
    - slot{"requested_slot": "cpf"}
* deny
    - utter_continue
* affirm
    - update_email_form
    - slot{"requested_slot": "cpf"}
* affirm
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

## interactive_story_1
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
    - slot{"requested_slot": "cpf"}
* deny
    - utter_continue
* affirm
    - update_email_form
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
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
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
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
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
* affirm
  - utter_ask_which_data

## interactive_story_1
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
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
* deny
  - utter_what_do_you_want

## interactive_story_1
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
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
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"requested_slot": "cpf"}

## interactive_story_1
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
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
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
    - slot{"requested_slot": "cpf"}
* get_debt_info
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
    - form{"name": "issue_debt_info_form"}
    - slot{"requested_slot": "cpf"}

## interactive_story_1
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
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
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
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