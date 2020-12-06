
## interactive_story_1
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
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
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
    - slot{"requested_slot": "cpf"}
* inform{"cep": "04537070"}
    - utter_unexpected_cep
    - update_phone_number_form
    - slot{"requested_slot": "cpf"}
* inform{"month": "março"}
    - utter_unexpected_month
    - update_phone_number_form
    - slot{"requested_slot": "cpf"}
* inform{"year": "2020"}
    - utter_unexpected_year
    - update_phone_number_form
    - slot{"requested_slot": "cpf"}
* inform{"email": "email@globo.com"}
    - utter_unexpected_email
    - update_phone_number_form
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567895"}
    - form: update_phone_number_form
    - slot{"cpf": "01234567895"}
    - slot{"requested_slot": "phone_number"}
* form: inform{"phone_number": "55 11 953755714"}
    - form: update_phone_number_form
    - slot{"phone_number": "5511953755714"}
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
* deny
    - utter_give_feedback
    - utter_bye

## interactive_story_1
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
    - slot{"requested_slot": "cpf"}
* deny
    - utter_continue
* affirm
    - update_phone_number_form
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
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
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
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
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
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
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

