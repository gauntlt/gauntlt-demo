import requests

payload = {'username': 'guest', 'password': 'guest')
r = requests.get("http://127.0.0.1:8080/WebGoat/j_spring_security_check", params = payload)
r.text
