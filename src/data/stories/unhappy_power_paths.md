
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
    - utter_anything_else
* affirm
    - utter_what_do_you_want

## interactive_story_1
* supply_power_outage_information
    - provide_power_supply_info_form
    - form{"name": "provide_power_supply_info_form"}
    - slot{"supplying_info": true}
    - slot{"requested_slot": "cep"}
* inform{"cpf": "01234567896"}
    - utter_unexpected_cpf
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}
* inform{"month": "abril"}
    - utter_unexpected_month
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}
* inform{"year": "2017"}
    - utter_unexpected_year
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}
* inform{"email": "email@exemple.com.br"}
    - utter_unexpected_email
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}
* inform{"phone_number": "5511953755714"}
    - utter_unexpected_phone_number
    - provide_power_supply_info_form
    - slot{"requested_slot": "cep"}
* form: inform{"cep": "02420060"}
    - form: provide_power_supply_info_form
    - slot{"cep": "02420060"}
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
