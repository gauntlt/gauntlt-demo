import requests
import json
import sys

base_url = "http://127.0.0.1:8080/WebGoat/"

#Creates a new session, logs into the server.
sess = requests.Session()
login = {'username': 'guest', 'password': 'guest'}
resp = sess.post(base_url + "j_spring_security_check", data=login)

resp = sess.get(base_url + "service/lessonmenu.mvc")
directory = json.loads(resp.text)
#Gets the url of our target page from the directory sidebar
target_uri = directory[10]['children'][7]['link']
target_url = base_url + target_uri

#Gets the target page
resp = sess.get(target_url)

#Forming the malicious response
mal_data = {"userid": "jsmith'; INSERT INTO salaries VALUES ('test',9999);--", "SUBMIT": "Go!"}
sess.post(target_url, data=mal_data)

#If attack was successful, we should then be able to request the inserted data
req_mal_data = {"userid": "test", "SUBMIT": "Go!"}
resp = sess.post(target_url, data=req_mal_data)

if 'test' in resp.text and '9999' in resp.text:
	print("Site is vulnerable to SQL Data Injection")
	print("Vulnerability test 19 failed.")
	sys.exit(1)
else:
	sys.exit(0)

