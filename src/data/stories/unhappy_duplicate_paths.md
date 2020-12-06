
## interactive_story_1
* get_duplicate_bill{"month": "agosto"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 8}
    - slot{"year": 2020}
    - slot{"requested_slot": "cpf"}
* affirm
    - utter_continue
* affirm
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
* affirm
    - utter_what_do_you_want

## interactive_story_1
* get_duplicate_bill{"month": "setembro"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 9}
    - slot{"year": 2020}
    - slot{"requested_slot": "cpf"}
* deny
    - utter_continue
* affirm
    - issue_duplicate_form
    - slot{"requested_slot": "cpf"}
* inform{"cep": "04537070"}
    - utter_unexpected_cep
    - issue_duplicate_form
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567898"}
    - form: issue_duplicate_form
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
* get_duplicate_bill
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567986"}
    - form: issue_duplicate_form
    - slot{"cpf": null}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567893"}
    - form: issue_duplicate_form
    - slot{"cpf": "01234567893"}
    - slot{"requested_slot": "month"}
* inform{"email": "exemplo@mailc.om"}
    - utter_unexpected_email
    - issue_duplicate_form
    - slot{"requested_slot": "month"}
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
* form: inform{"cpf": "01234567894"}
    - form: update_phone_number_form
    - slot{"cpf": "01234567894"}
    - slot{"requested_slot": "phone_number"}
* inform{"email": "bola@email.com"}
    - utter_unexpected_email
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"cpf": "01234567894"}
    - slot{"requested_slot": "month"}
* affirm
    - utter_continue
* affirm
    - issue_duplicate_form
    - slot{"requested_slot": "month"}
* form: inform{"month": "janeiro"}
    - form: issue_duplicate_form
    - slot{"month": 1}
    - slot{"year": 2020}
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
* get_duplicate_bill
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
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
* form: inform{"cpf": "01234567895"}
    - issue_duplicate_form
    - slot{"cpf": "01234567895"}
    - slot{"requested_slot": "month"}
* form: inform{"month": "maio", "year": "2019"}
    - form: issue_duplicate_form
    - slot{"year": 2019}
    - slot{"month": 5}
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
* get_duplicate_bill
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"requested_slot": "cpf"}
* deny
    - utter_continue
* affirm
    - issue_duplicate_form
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
* get_duplicate_bill{"month": "abril"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 4}
    - slot{"year": 2020}
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
* get_duplicate_bill{"month": "janeiro"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 1}
    - slot{"year": 2020}
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
* get_duplicate_bill{"month": "dezembro"}
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"month": 12}
    - slot{"year": 2020}
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