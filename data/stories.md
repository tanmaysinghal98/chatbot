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


## Generated Story 6917795793949540468
* greet
    - utter_greet
* ls
    - action_ls
* cd{"directory": "downloads"}
    - slot{"directory": "downloads"}
    - action_cd
    - slot{"current_path": "/Users/tanmaysinghal/Downloads/"}
    - slot{"directory": null}
    - action_ls
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
    
## Generated Story 6090548465607773557
* mkdir
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"requested_slot": "new_folder"}
* form: new_folder_mkdir{"new_folder": "madarchod"}
    - form: mkdir_form
    - slot{"new_folder": "madarchod"}
    - form{"name": null}
    - slot{"requested_slot": null}
## Generated Story 3650118840336526519
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

## Generated Story -4426602071370404037
* greet
    - utter_greet
* pwd
    - action_pwd
* goodbye
    - utter_goodbye

## Generated Story 8614332857277738178
* greet
    - utter_greet
* ls
    - action_ls
* cd{"directory": "hi"}
    - slot{"directory": "hi"}
    - action_cd
    - slot{"current_path": "/Users/tanmaysinghal/hi/"}
* mkdir{"new_folder": "tanmay"}
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"new_folder": "tanmay"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye

## Generated Story -4273105917470362637
* greet
    - utter_greet
* speedtest
    - action_speedtest
* news
    - utter_news
    - action_news
* ls
    - action_ls
* cd{"directory": "desktop"}
    - slot{"directory": "desktop"}
    - action_cd
    - slot{"current_path": "/Users/tanmaysinghal/Desktop/"}
    - slot{"directory": null}
    - action_ls
* mkdir{"new_folder": "lauda"}
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"new_folder": "lauda"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story 585072469833944631
* greet
    - utter_greet
* news
    - utter_news
    - action_news
* speedtest
    - utter_speedtest
    - action_speedtest
* ls
    - action_ls
* cd{"directory": "applications"}
    - slot{"directory": "applications"}
    - action_cd
    - slot{"current_path": "/Users/tanmaysinghal/Applications/"}
    - slot{"directory": null}
    - action_ls
* back
    - action_back
    - slot{"current_path": "/Users/tanmaysinghal/"}
    - action_ls
* mkdir{"new_folder": "sex"}
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"new_folder": "sex"}
    - form{"name": null}
    - slot{"requested_slot": null}
* ls
    - action_ls
* goodbye
    - utter_goodbye

## Generated Story 6180054716992161080
* greet
    - utter_greet
* ls
    - action_ls
* mkdir{"new_folder": "rushabh"}
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"new_folder": "rushabh"}
    - form{"name": null}
    - slot{"requested_slot": null}

