import requests

s = requests.Session()

r = s.post("http://localhost:8080/WebGoat/j_spring_security_check", data={"username": "webgoat", "password": "webgoat"})

#print r.headers
#print r.text
#print r
#print r.cookies
#print s.cookies

#print s.get("http://localhost:8080/WebGoat/").text

inject = None

for high in s.get("http://localhost:8080/WebGoat/service/lessonmenu.mvc").json():
    if high['name'] == "Injection Flaws":
        inject = high
        break
#print high
#    print high['name']

blah = None

for next in inject['children']:
    #print next
    if next['name'] == "LAB: SQL Injection":
        blah = next

#print blah

#print inject

attack_loc = blah['link'] + "&stage=3"

#print attack_loc

s.get("http://localhost:8080/WebGoat/{}".format(attack_loc))
r2 = s.post("http://localhost:8080/WebGoat/{}".format(attack_loc), data={"employee_id": 112, "password": "smith' OR '1' = '1", "action": "Login"}, cookies = r.cookies)

#print r2

#print r2.text

if "Welcome Back" in r2.text and "Neville" in r2.text:
    print "FAIL"
else:
    print "PASS"
