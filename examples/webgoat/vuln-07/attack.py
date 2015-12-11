import requests
import sys
import json

# WebGoat login page URL
URL = 'http://127.0.0.1:8080/WebGoat/j_spring_security_check'

def main():
    # Start a session so we can have persistant cookies
    session = requests.session(config={'verbose': sys.stderr})

    # WebGoat login information
    USERNAME = 'webgoat'
    PASSWORD = 'webgoat'

    # This is the form data that the page sends when logging in
    login_data = {
        'username': USERNAME,
        'password': PASSWORD
    }

	# Screen 1: Login Page
    r = session.get('http://127.0.0.1:8080/WebGoat/login.mvc')
    # print(r.text)
    print(requests.utils.dict_from_cookiejar(session.cookies)) # First cookie

    # Authenticate (Request login page, log into WebGoat using POST request)
    r = session.post(URL, data=login_data)
    print(requests.utils.dict_from_cookiejar(session.cookies)) # Second cookie (after POST authentication)

    # Since application menu is dynamic, must first parse JSON and get actual link of attack
    JSON_URL = 'http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc'
    r = session.get(JSON_URL)
    parsed_json = json.loads(r.text)
    menu_request_name = parsed_json[8]["children"][1]["children"][4]["name"]
    print(menu_request_name)
    menu_request_link = parsed_json[8]["children"][1]["children"][4]["link"]
    print(menu_request_link)

	# Request the lesson for Cross-Site Scripting (XSS) => Reflected XSS
    # We can do this now that we have the dynamic menu ID
    LESSON_URL = 'http://127.0.0.1:8080/WebGoat/' + menu_request_link
    r = session.get(LESSON_URL)
    #print(r.text)
  
    # Screen 1: 'Login' Information
    EMPLOYEE_ID = '101'
    ACTION = 'Login'
    PASSWORD = 'larry'

    login_data = {
        'employee_id' : EMPLOYEE_ID,
        'password' : PASSWORD,
        'action' : ACTION
    }
	
	# Screen 1: 'Login' POST request
    if (LESSON_URL.endswith('&stage=5')):
        LESSON_URL = LESSON_URL[:-8]

    r = session.post(LESSON_URL, data=login_data)

    # Screen 2: 'Search Staff' Information
    EMPLOYEE_ID = '101'
    ACTION = 'SearchStaff'

    login_data = {
        'employee_id' : EMPLOYEE_ID,
        'action' : ACTION
    }
    
    # Screen 2: 'Search Staff' POST request
    r = session.post(LESSON_URL, data=login_data)

    # Screen 3: 'Search User' Information
    #SEARCH_NAME = '"><script>alert(0)</script>'
    SEARCH_NAME = '%22%3E%3Cscript%3Ealert(0)%3C%2Fscript%3E&action=FindProfile'

    login_data = {
        'search_name' : SEARCH_NAME
    }
    
    # Screen 3: 'Search User' POST request
    r = session.post(LESSON_URL, data=login_data)


	# Purposefully fail for testing purposes

	# Set the correct exit code
	# It will return a
	# - 0 (error) if the vulnerability is present
	# - 1 (success) if the vulnerability is fixed (aka not present)

    if 'Stage 6: Block Reflected XSS' in r.text:
        print('1: vulnerability present') # vulnerability present
        exit(1)
    else:
        print('0: vulnerability not present') # vulnerability not present, it's been fixed!
        exit(0)

if __name__ == '__main__':
    main()
