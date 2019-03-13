## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. -->
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. -->
 - utter_greet <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' -->

## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks

## story_ls
* ls
 - action_ls

## story_cd
* cd{"directory" : "Applications"}
 - action_cd
 - action_ls

## story_back
* back
 - action_back
 - action_ls

## story_pwd
* pwd
 - action_pwd

## story_speedtest
* speedtest
 - utter_speedtest
 - action_speedtest

## story_news
* news
 - utter_news
 - action_news

## story_mkdir
* mkdir
 - mkdir_form
 - form{"name": "mkdir_form"}
 - form{"name": "null"}

## story_mean
* mean{"meaning": "car"}
 - action_mean

## story_weather
* weather{"location":"nagpur"}
 - action_weather


## Generated Story 6917795793949540468
* mkdir
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"requested_slot": "new_folder"}
* form: new_folder_mkdir{"new_folder": "pakistan"}
    - form: mkdir_form
    - slot{"new_folder": "pakistan"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -4699630783042895808
* mkdir
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"requested_slot": "new_folder"}
* form: new_folder_mkdir{"new_folder": "movies"}
    - form: mkdir_form
    - slot{"new_folder": "movies"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story 5764131290060210138
* mkdir
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"requested_slot": "new_folder"}
* form: new_folder_mkdir{"new_folder": "madarchod"}
    - form: mkdir_form
    - slot{"new_folder": "madarchod"}
    - form{"name": null}
    - slot{"requested_slot": null}


## Generated Story -7158987982550963462
* mkdir{"new_folder": "madarchod"}
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"new_folder": "madarchod"}
    - form{"name": null}
    - slot{"requested_slot": null}


## Generated Story 9178763216486222699
* greet
    - utter_greet
* ls
    - action_ls
* mkdir
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"requested_slot": "new_folder"}
* form: new_folder_mkdir{"new_folder": "lundd"}
    - form: mkdir_form
    - slot{"new_folder": "lundd"}
    - slot{"new_folder": null}
    - form{"name": null}
    - slot{"requested_slot": null}


## Generated Story 7107326189628707028
* greet
    - utter_greet
* ls
    - action_ls
* mkdir
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"requested_slot": "new_folder"}
* form: new_folder_mkdir{"new_folder": "rty"}
    - form: mkdir_form
    - slot{"new_folder": "rty"}
    - slot{"new_folder": null}
    - form{"name": null}
    - slot{"requested_slot": null}

## story_rm
* rm
 - action_rm
 - action_ls
