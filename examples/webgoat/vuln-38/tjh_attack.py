#!/usr/bin/python

import urllib2
import sys
import re
import mechanize
import cookielib

host_ip = "127.0.0.1"     #WebGoat runs at this IP (localhost)
port = 8080   #default port for WebGoat socket
menu = 500   #menu number in which "Forgot Password" appears. Screen number isn't saved because screen number is NOT static.


browser = mechanize.Browser() #create an "instance" of a web browser

#initialize browser options
browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)

webGoat = browser.open('http://127.0.0.1:8080/WebGoat/login.mvc') #create "webgoat" browser & start at login page

cookie = cookielib.LWPCookieJar() #initialize cookiejar

browser.set_cookiejar(cookie) #link cookiejar wit browser

browser.add_password('http://127.0.0.1:8080/WebGoat', 'guest' , 'guest') #store login credentials

html = webGoat.read()  #read html from webGoat and store in string called html

print html   #print html


# <MAY NOT NEED> s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initialize network socket
# <MAY NOT NEED> print("Socket successfully created!\n")
  

# <MAY NOT NEED> s.connect((host_ip,port))
# <MAY NOT NEED> print("Socket has successfully connected to WebGoat, IP:port %s%d", host_ip, port)


