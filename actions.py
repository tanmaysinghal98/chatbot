# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
import os
import subprocess
from newsapi import NewsApiClient

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

logger = logging.getLogger(__name__)

class ActionLs(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_ls"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        current_path = tracker.slots['current_path']
        dirs = os.listdir(current_path)

        # This would print all the files and directories
        for file in dirs:
            if not file.startswith('.'):
                if os.path.isfile(os.path.join(current_path, file)):
                    dispatcher.utter_message(file + " # File")# file
                if os.path.isdir(os.path.join(current_path, file)):
                    dispatcher.utter_message(file + " # Directory")# folder

        return []



class ActionCd(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_cd"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        current_path = tracker.get_slot('current_path')
        directory = tracker.get_slot('directory')
        dispatcher.utter_message(directory)

        dirs = os.listdir(current_path)
        flag = 0
        for file in dirs:
            if not file.startswith('.') and directory is not None:
                if os.path.isdir(os.path.join(current_path, file)):
                    if file == directory:
                        flag = 1
                        current_path = current_path + directory + "/"
                        return [SlotSet("current_path", current_path)]

                    if file == directory.capitalize():
                        flag = 1
                        current_path = current_path + directory.capitalize() + "/"
                        return [SlotSet("current_path", current_path), SlotSet("directory", None)]

        if flag == 0:
            dispatcher.utter_message("Directory not found")

        return [SlotSet("directory", None)]



class ActionBack(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_back"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        current_path = tracker.slots['current_path']
        if current_path != '/':
            current_path = current_path[:current_path.rfind('/')]
            current_path = current_path[:current_path.rfind('/')]
            current_path = current_path + '/'

        return [SlotSet("current_path", current_path)]



class ActionPwd(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_pwd"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        dispatcher.utter_message(tracker.get_slot('current_path'))
        return []


class ActionSpeedtest(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_speedtest"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #dispatcher.utter_message("Performing SpeedTest")
        speed = subprocess.run(['speedtest-cli', '--simple'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
        dispatcher.utter_message(speed[0])
        dispatcher.utter_message(speed[1])
        dispatcher.utter_message(speed[2])
        return []

class ActionNews(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_news"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #dispatcher.utter_message("Performing SpeedTest")
        newsapi = NewsApiClient(api_key='9ff5b27932fc4787b1c06c9a4f26ea18')
        top_headlines = newsapi.get_top_headlines(country='in', language='en', category='technology')
        for i in range(0,5):
            dispatcher.utter_message(top_headlines['articles'][i]['title'])
            # top_headlines['articles'][0]['title']
        return []
