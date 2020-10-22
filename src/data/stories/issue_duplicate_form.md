## get duplicate bill
* get_duplicate_bill
  - issue_duplicate_form
  - form{"name": "issue_duplicate_form"}
  - form{"name": null}
  - utter_anything_else

## interactive_story_1
* greet
    - utter_greet
* get_duplicate_bill
    - issue_duplicate_form
    - form{"name": "issue_duplicate_form"}
    - slot{"requested_slot": "cpf"}
* form: get_duplicate_bill{"month": "dezembro", "year": "2019"}
    - form: issue_duplicate_form
    - slot{"month": 12}
    - slot{"year": 2019}
    - slot{"requested_slot": "cpf"}
* form: inform{"cpf": "01234567890"}
    - form: issue_duplicate_form
    - slot{"cpf": "01234567890"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_anything_else
* deny
    - utter_bye
* bye
    - action_restart