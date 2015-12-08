import requests

s = requests.Session()
r = s.get('http://127.0.0.1:8080/WebGoat/login.mvc')
session1 = r.headers['Set-Cookie']
print session1

r = s.post('http://127.0.0.1:8080/WebGoat/j_spring_security_check;jsessionid=' + session1, data={"username":"guest","password":"guest"})
session2 =  r.request.headers['Cookie']
print session2

#for property, value in vars(r2.history[0].request.iteritems():
#	print property, ': ', value
