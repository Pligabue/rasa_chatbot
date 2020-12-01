
## interactive_story_1
* get_power_outage_information
    - provide_power_supply_info_form
    - form{"name": "provide_power_supply_info_form"}
    - slot{"supplying_info": false}
    - slot{"requested_slot": "cep"}
* inform{"cpf": "48396334870"}
    - utter_unexpected_cpf
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}
* deny
    - utter_continue
* affirm
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}
* form: inform{"cep": "04387080"}
    - form: provide_power_supply_info_form
    - slot{"cep": "04387080"}
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
