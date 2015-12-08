import requests
import pprint



url = 'http://127.0.0.1:8080/WebGoat'
values = {'username': 'guest',
        'password': 'guest'}

#r = requests.post(url + '/j_spring_security_check' , values)


with requests.Session() as s:
    # Request login page
    #Log into WebGoat

    r = s.post(url+'/j_spring_security_check', values)
    print (r.content)

# Figure out which menu item is "Http Basics"

# Request the lesson for General => Http Basics

# Submit the attack to the General => Http Basics page

# Purposefully fail for testing purposes

#if successfull, say so otherwise don't #logic
pprint.pprint("Attack Successfull")
