import requests

#makes a call to the page
r = requests.get('http://127.0.0.1:8080/WebGoat/')
dict =  r.headers
cookie = dict['Set-Cookie']
print cookie
sessionID = cookie[11:43]
print sessionID
print r.cookies

the_url = "http://127.0.0.1:8080/WebGoat/j_spring_security_check/jsessionid=" + sessionID
print the_url

#log into WebGoat
r = requests.post(the_url, data = {"username":"guest", "password":"guest"})
print r.headers

#Click on menu item and complete transactions
r = requests.get("http://127.0.0.1:8080/WebGoat/attack?Screen=146&menu=400&from=ajax&newAccount=1337&amount=12345&confirm=Confirm")

try:
	print r
except Exception as e:
	print e
