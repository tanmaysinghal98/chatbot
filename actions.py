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
from PyDictionary import PyDictionary
import urllib.request

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.forms import FormAction

logger = logging.getLogger(__name__)

class ActionLs(Action):
    def name(self):
        return "action_ls"

    def run(self, dispatcher, tracker, domain):
        current_path = tracker.slots['current_path']
        dirs = os.listdir(current_path)
        for file in dirs:
            if not file.startswith('.'):
                if os.path.isfile(os.path.join(current_path, file)):
                    dispatcher.utter_message(file + " # File")

                if os.path.isdir(os.path.join(current_path, file)):
                    dispatcher.utter_message(file + " # Directory")

        return []

class GitPushForm(FormAction):
   def name(self):
       return "gitpush_form"

   @staticmethod
   def required_slots(tracker):
       current_path = tracker.slots['current_path']
       dirs = os.listdir(current_path)
       flag = 0
       for file in dirs:
           if file == '.git':
               flag = 1
               break

       if flag == 0:
           return ["url"]
       else:
           return []

       return []

   def slot_mappings(self):
       return {"url": [self.from_entity(entity="url", intent=["get_url"])]}

   def submit(self, dispatcher, tracker, domain):
       # dispatcher.utter_message("# HI")
       current_path = tracker.slots['current_path']
       dirs = os.listdir(current_path)
       flag = 0
       for file in dirs:
           if file == '.git':
               flag = 1
               break

       if flag == 0:
           dispatcher.utter_message(tracker.get_slot('url'))
           os.system('git --git-dir=' + current_path + '.git --work-tree=' + current_path + ' init')
           os.system('git --git-dir=' + current_path + '.git --work-tree=' + current_path + ' remote add origin ' + tracker.get_slot('url'))

       os.system('git --git-dir=' + current_path + '.git --work-tree=' + current_path + ' add -A')
       os.system('git --git-dir=' + current_path + '.git --work-tree=' + current_path + ' commit -m "Commit from CODA"')
       os.system('git --git-dir=' + current_path + '.git --work-tree=' + current_path + ' push origin ' + out)
       dispatcher.utter_message("Done!")


       return [SlotSet("url", None)]

class GitPullForm(FormAction):
   def name(self):
       return "gitpull_form"

   @staticmethod
   def required_slots(tracker):
       current_path = tracker.slots['current_path']
       dirs = os.listdir(current_path)
       flag = 0
       for file in dirs:
           if file == '.git':
               flag = 1
               break

       if flag == 0:
           return ["url"]
       else:
           return []

       return []

   def slot_mappings(self):
       return {"url": [self.from_entity(entity="url", intent=["get_url"])]}

   def submit(self, dispatcher, tracker, domain):
       # dispatcher.utter_message("# HI")
       current_path = tracker.slots['current_path']
       dirs = os.listdir(current_path)
       flag = 0
       for file in dirs:
           if file == '.git':
               flag = 1
               break

       if flag == 0:
           dispatcher.utter_message(tracker.get_slot('url'))
           os.system('git --git-dir=' + current_path + '.git --work-tree=' + current_path + ' init')
           os.system('git --git-dir=' + current_path + '.git --work-tree=' + current_path + ' remote add origin ' + tracker.get_slot('url'))

       os.system('git --git-dir=' + current_path + '.git --work-tree=' + current_path + ' pull')
       # os.system('git --git-dir=' + current_path + '.git --work-tree=' + current_path + ' commit -m "Commit from CODA"')
       # os.system('git --git-dir=' + current_path + '.git --work-tree=' + current_path + ' push origin master')
       dispatcher.utter_message("Done!")


       return [SlotSet("url", None)]

class GitCloneForm(FormAction):
   def name(self):
       return "gitclone_form"

   @staticmethod
   def required_slots(tracker):
       return ['url']

   def slot_mappings(self):
       return {"url": [self.from_entity(entity="url", intent=["get_url", "git_clone"])]}

   def submit(self, dispatcher, tracker, domain):
       current_path = tracker.slots['current_path']
       url = tracker.get_slot('url')
       current_path += url[url.rfind('/') : url.rfind('.')] + "/"
       msg = 'git clone ' + tracker.get_slot('url') + " " + current_path
       dispatcher.utter_message(msg)
       os.system(msg)
       dispatcher.utter_message("Done!")
       return [SlotSet("url", None)]

class ActionCd(Action):
    def name(self):
        return "action_cd"

    def run(self, dispatcher, tracker, domain):
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
        return "action_back"

    def run(self, dispatcher, tracker, domain):
        current_path = tracker.slots['current_path']
        if current_path != '/':
            current_path = current_path[:current_path.rfind('/')]
            current_path = current_path[:current_path.rfind('/')]
            current_path = current_path + '/'

        return [SlotSet("current_path", current_path)]

class ActionPwd(Action):
    def name(self):
        return "action_pwd"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(tracker.get_slot('current_path'))
        return []

class ActionSpeedtest(Action):
    def name(self):
        return "action_speedtest"

    def run(self, dispatcher, tracker, domain):
        speed = subprocess.run(['speedtest-cli', '--simple'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
        dispatcher.utter_message(speed[0])
        dispatcher.utter_message(speed[1])
        dispatcher.utter_message(speed[2])
        return []

class ActionNews(Action):
    def name(self):
        return "action_news"

    def run(self, dispatcher, tracker, domain):
        newsapi = NewsApiClient(api_key='9ff5b27932fc4787b1c06c9a4f26ea18')
        top_headlines = newsapi.get_top_headlines(country='in', language='en', category='technology')
        for i in range(0,5):
            dispatcher.utter_message(top_headlines['articles'][i]['title'])
        return []

class MkdirForm(FormAction):
   def name(self):
       return "mkdir_form"

   @staticmethod
   def required_slots(tracker):
       return ["new_folder"]

   def slot_mappings(self):
       return {"new_folder": [self.from_entity(entity="new_folder", intent=["mkdir", "new_folder_mkdir"]), self.from_text(intent="inform")]}

   def submit(self, dispatcher, tracker, domain):
       message = 'mkdir ' + tracker.get_slot('current_path') + tracker.get_slot('new_folder')
       dispatcher.utter_message(message)
       os.system(message)
       dispatcher.utter_message('Folder Created')
       return [SlotSet("new_folder", None)]

class CpForm(FormAction):
   def name(self):
       return "cp_form"

   @staticmethod
   def required_slots(tracker):
       return ["from", "to"]

   def slot_mappings(self):
       return {"from": [self.from_entity(entity="from", intent=["cp"]), self.from_text(intent="inform")],
                "to": [self.from_entity(entity="to", intent=["cp", "cp_to"]), self.from_text(intent="inform")]}

   def submit(self, dispatcher, tracker, domain):
       file = tracker.get_slot('from')
       to = tracker.get_slot('to')

       cmd = 'find /Users/tanmaysinghal -name "*' + file + '*" -not -path "/Users/tanmaysinghal/Library/*"'
       out = subprocess.check_output(cmd , shell=True).decode('utf-8').split('\n')
       out = out[0]
       if(out == ''):
           cmd = 'find /Users/tanmaysinghal -name "*' + file.capitalize() + '*" -not -path "/Users/tanmaysinghal/Library/*"'
           out = subprocess.check_output(cmd , shell=True).decode('utf-8').split('\n')
           out = out[0]
           if(out == ''):
               dispatcher.utter_message("Directory or file not found")
               return [SlotSet("from", None), SlotSet("to", None)]

       cmd = 'find /Users/tanmaysinghal -type d -name "*' + to + '*" -not -path "/Users/tanmaysinghal/Library/*"'
       fpath = subprocess.check_output(cmd , shell=True).decode('utf-8').split('\n')
       fpath = fpath[0]
       if(fpath == ''):
           cmd = 'find /Users/tanmaysinghal -name "*' + to.capitalize() + '*" -not -path "/Users/tanmaysinghal/Library/*"'
           fpath = subprocess.check_output(cmd , shell=True).decode('utf-8').split('\n')
           fpath = fpath[0]
           if(fpath == ''):
               dispatcher.utter_message("Directory or file not found")
               return [SlotSet("from", None), SlotSet("to", None)]

       os.system("cp -r " + out + " " + fpath)
       dispatcher.utter_message("Copied")
       return [SlotSet("from", None), SlotSet("to", None)]

class MvForm(FormAction):
   def name(self):
       return "mv_form"

   @staticmethod
   def required_slots(tracker):
       return ["fromm", "tom"]

   def slot_mappings(self):
       return {"fromm": [self.from_entity(entity="fromm", intent=["mv"]), self.from_text(intent="inform")],
                "tom": [self.from_entity(entity="tom", intent=["mv", "mv_to"]), self.from_text(intent="inform")]}

   def submit(self, dispatcher, tracker, domain):

       file = tracker.get_slot('fromm')
       to = tracker.get_slot('tom')

       cmd = 'find /Users/tanmaysinghal -name "*' + file + '*" -not -path "/Users/tanmaysinghal/Library/*"'
       out = subprocess.check_output(cmd , shell=True).decode('utf-8').split('\n')
       out = out[0]
       if(out == ''):
           cmd = 'find /Users/tanmaysinghal -name "*' + file.capitalize() + '*" -not -path "/Users/tanmaysinghal/Library/*"'
           out = subprocess.check_output(cmd , shell=True).decode('utf-8').split('\n')
           out = out[0]
           if(out == ''):
               dispatcher.utter_message("Directory or file not found")
               return [SlotSet("from", None), SlotSet("to", None)]

       cmd = 'find /Users/tanmaysinghal -type d -name "*' + to + '*" -not -path "/Users/tanmaysinghal/Library/*"'
       fpath = subprocess.check_output(cmd , shell=True).decode('utf-8').split('\n')
       fpath = fpath[0]
       if(fpath == ''):
           cmd = 'find /Users/tanmaysinghal -name "*' + to.capitalize() + '*" -not -path "/Users/tanmaysinghal/Library/*"'
           fpath = subprocess.check_output(cmd , shell=True).decode('utf-8').split('\n')
           fpath = fpath[0]
           if(fpath == ''):
               dispatcher.utter_message("Directory or file not found")
               return [SlotSet("from", None), SlotSet("to", None)]

       os.system("mv " + out + " " + fpath)
       dispatcher.utter_message("Moved")
       return [SlotSet("fromm", None), SlotSet("tom", None)]

class ActionMean(Action):
    def name(self):
        return "action_mean"

    def run(self, dispatcher, tracker, domain):
        dictionary = PyDictionary()
        word = tracker.get_slot('meaning')
        for key, value in dictionary.meaning(word).items():
            dispatcher.utter_message(key + ':')
            for x in dictionary.meaning(word)[key]:
                dispatcher.utter_message(x)
        return [SlotSet("meaning", None)]

class ActionWeather(Action):
    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        url = 'http://wttr.in/' + tracker.get_slot('location') + '?0pq_T_A'
        r = urllib.request.urlopen(url)
        resp = r.read().decode(r.info().get_param('charset') or 'utf-8')
        resp = resp.split('\n')
        for i in range(0, len(resp)):
            dispatcher.utter_message(resp[i])
        return []

class ActionRm(Action):
    def name(self):
        return "action_rm"

    def run(self, dispatcher, tracker, domain):
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
                        dispatcher.utter_message("Removed")
                        os.system("rm -rf " + current_path + directory)

                    if file == directory.capitalize():
                        flag = 1
                        dispatcher.utter_message("Removed")
                        os.system("rm -rf " + current_path + directory.capitalize())

                else:
                    if file == directory:
                        flag = 1
                        dispatcher.utter_message("Removed")
                        os.system("rm " + current_path + directory)

                    if file == directory.capitalize():
                        flag = 1
                        dispatcher.utter_message("Removed")
                        os.system("rm " + current_path + directory.capitalize())

        if flag == 0:
            dispatcher.utter_message("Directory or File not found")

        return [SlotSet("directory", None)]
