
## interactive_form_story_1
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
    - slot{"requested_slot": "cpf"}
* inform{"cep": "04537070"}
    - utter_unexpected_cep
    - update_phone_number_form
    - slot{"requested_slot": "cpf"}

## interactive_form_story_1_2
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
    - slot{"requested_slot": "cpf"}
* inform{"email": "email@exemplo.com"}
    - utter_unexpected_email
    - update_phone_number_form
    - slot{"requested_slot": "cpf"}

## interactive_form_story_2
* update_email
    - update_email_form
    - form{"name": "update_email_form"}
    - slot{"requested_slot": "cpf"}
* inform{"cep": "04537070"}
    - utter_unexpected_cep
    - update_email_form
    - slot{"requested_slot": "cpf"}

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
* inform{"phone_number": "55 11 953755714"}
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

## interactive_story_11
* update_phone_number
    - update_phone_number_form
    - form{"name": "update_phone_number_form"}
    - slot{"requested_slot": "cpf"}
* inform{"email": "email@exemple.com.br"}
    - utter_unexpected_email
    - update_phone_number_form
    - slot{"requested_slot": "cpf"}

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

