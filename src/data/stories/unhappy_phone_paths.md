
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
    - utter_give_feedback
    - utter_anything_else
* affirm
    - utter_what_do_you_want
