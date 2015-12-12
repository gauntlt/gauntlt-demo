#!/usr/bin/env python

import requests
import json

cookies = None
loginCreds = {"username":"guest", "password":"guest"}
url = "http://127.0.0.1:8080/WebGoat/"
link = ""
success = True

def printCookies():
	for cookie in cookies:
		print(cookie.name)
		print(cookie.value)
		print("HttpOnly" in cookie._rest)
		print("=========================")


def login(): 
	global link, cookies
	r1 = requests.get(url + "login.mvc")
	cookies = r1.cookies;
	r2 = requests.post(url + "j_spring_security_check", data = loginCreds, cookies = cookies)
	cookies.update(r2.history[0].cookies)
	r3 = requests.get(url + "service/lessonmenu.mvc", cookies=cookies)
	j = json.loads(r3.text)
	link = url + j[8]["children"][7]["link"]
	r4 = requests.get(link, cookies=cookies)
	cookies.update(r4.cookies)

def pressReadButton():
	global success
	data = {"httponly":"True", "httponly_value":"True","read_result":"", "action":"Read Cookie"}
	r1 = requests.post(link, data=data, cookies=cookies)
	r1.history
	cookies.update(r1.cookies)
	found = False
	for cookie in cookies:
		if (cookie.name == "unique2u"):
			found = True
			if ("HttpOnly" not in cookie._rest):
				success = False
	success = success and found

def pressWriteButton():
	global success
	data = {"httponly_value":"True","read_result":"", "action":"Write Cookie"}
	r1 = requests.post(link, data=data, cookies = cookies)
	success = success and (r1.text.find("* SUCCESS: Your browser enforced") > 0)

login()
pressReadButton()
pressWriteButton()
print(success)
 

