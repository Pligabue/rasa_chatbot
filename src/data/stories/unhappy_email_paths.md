
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