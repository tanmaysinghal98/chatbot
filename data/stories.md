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


## Generated Story 576413129006021089
* mkdir
    - mkdir_form
    - form{"name": "mkdir_form"}
    - slot{"requested_slot": "new_folder"}
* form: inform{"new_folder": "madarchod"}
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

##story_directnew_folder_mkdir
* new_folder_mkdir
 - utter_default

##story_direct_inform
* inform
  - utter_default

##story_cp
  * cp
    - cp_form
    - form{"name": "cp_form"}
    - form{"name": "null"}

##story_gitpush
 * git_push
  - gitpush_form
  - form{"name": "gitpush_form"}
  - form{"name": "null"}

##story_gitpull
   * git_pull
    - gitpull_form
    - form{"name": "gitpull_form"}
    - form{"name": "null"}

##story_gitclone
  * git_clone
    - gitclone_form
    - form{"name": "gitclone_form"}
    - form{"name": "null"}


##story_mv
 * mv
  - mv_form
  - form{"name": "mv_form"}
  - form{"name": "null"}


##story_direct_cp_to
* cp_to
  - utter_default

##story_direct_get_url
  * get_url
    - utter_default

##story_direct_mv_to
  * mv_to
    - utter_default

## story_rm
* rm
 - action_rm
 - action_ls


## Generated Story -8210409641556309922
* cp{"from": "pagal", "to": "music"}
    - slot{"from": "pagal"}
    - slot{"to": "music"}
    - cp_form
    - form{"name": "cp_form"}
    - slot{"from": "pagal"}
    - slot{"to": "music"}
    - slot{"from": null}
    - slot{"to": null}
    - form{"name": null}
    - slot{"requested_slot": null}


## Generated Story 7296060556714048204
* cp{"from": "music", "to": "downloads"}
    - slot{"from": "music"}
    - slot{"to": "downloads"}
    - cp_form
    - form{"name": "cp_form"}
    - slot{"from": "music"}
    - slot{"to": "downloads"}
    - slot{"from": null}
    - slot{"to": null}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story 7690714786894624662
* mv{"fromm": "pagal", "tom": "music"}
    - slot{"fromm": "pagal"}
    - slot{"tom": "music"}
    - mv_form
    - form{"name": "mv_form"}
    - slot{"fromm": "pagal"}
    - slot{"tom": "music"}
    - slot{"from": null}
    - slot{"to": null}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -7088158622873961935
* cp
    - cp_form
    - form{"name": "cp_form"}
    - slot{"requested_slot": "from"}
* form: cp{"from": "sjhbd"}
    - slot{"from": "sjhbd"}
    - form: cp_form
    - slot{"from": "sjhbd"}
    - slot{"requested_slot": "to"}
* form: cp_to{"to": "fsddfb"}
    - slot{"to": "fsddfb"}
    - form: cp_form
    - slot{"to": "fsddfb"}
    - slot{"from": null}
    - slot{"to": null}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -2118088312163187205
* mv
    - mv_form
    - form{"name": "mv_form"}
    - slot{"requested_slot": "fromm"}
* form: mv{"fromm": "jdsbjs"}
    - slot{"fromm": "jdsbjs"}
    - form: mv_form
    - slot{"fromm": "jdsbjs"}
    - slot{"requested_slot": "tom"}
* form: mv_to{"tom": "jshdf"}
    - slot{"tom": "jshdf"}
    - form: mv_form
    - slot{"tom": "jshdf"}
    - slot{"from": null}
    - slot{"to": null}
    - form{"name": null}
    - slot{"requested_slot": null}
## Generated Story 3530304765317168321
* cp{"from": "shantanu", "to": "tanmay"}
    - slot{"from": "shantanu"}
    - slot{"to": "tanmay"}
    - cp_form
    - form{"name": "cp_form"}
    - slot{"from": "shantanu"}
    - slot{"to": "tanmay"}
    - slot{"from": null}
    - slot{"to": null}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story 3184962036316840253
* cp{"from": "shantanu", "to": "madarchod"}
    - slot{"from": "shantanu"}
    - slot{"to": "madarchod"}
    - cp_form
    - form{"name": "cp_form"}
    - slot{"from": "shantanu"}
    - slot{"to": "madarchod"}
    - slot{"from": null}
    - slot{"to": null}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -5045554307600360606
* mv{"fromm": "madarchod", "tom": "shantanu"}
    - slot{"fromm": "madarchod"}
    - slot{"tom": "shantanu"}
    - mv_form
    - form{"name": "mv_form"}
    - slot{"fromm": "madarchod"}
    - slot{"tom": "shantanu"}
    - slot{"fromm": null}
    - slot{"tom": null}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -264160495058568725
* mv
    - mv_form
    - form{"name": "mv_form"}
    - slot{"requested_slot": "fromm"}
* form: mv{"fromm": "shantanu"}
    - slot{"fromm": "shantanu"}
    - form: mv_form
    - slot{"fromm": "shantanu"}
    - slot{"requested_slot": "tom"}
* form: mv_to{"tom": "lund"}
    - slot{"tom": "lund"}
    - form: mv_form
    - slot{"tom": "lund"}
    - slot{"fromm": null}
    - slot{"tom": null}
    - form{"name": null}
    - slot{"requested_slot": null}
