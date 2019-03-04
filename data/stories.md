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
