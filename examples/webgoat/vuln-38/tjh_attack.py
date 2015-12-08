#!/usr/bin/python

import StringIO
import cStringIO
import urllib2
import sys
import logging
import re
import mechanize
import cookielib

host_ip = "127.0.0.1"     #WebGoat runs at this IP (localhost)
port = 8080   #default port for WebGoat socket
menu = "500"   #menu number in which "Forgot Password" appears. Menu number is static and so it is safe to explicitly state
Username = "guest"
Password = "guest" 
response = ""
webGoatURL = "http://127.0.0.1:8080/WebGoat"

attackURL = webGoatURL + "/attack?ScreenXXX&menu" + menu

browser = mechanize.Browser() #create an "instance" of a web browser

#initialize browser options
browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)
browser.set_debug_responses(True)

#make sure it prints out the responses info
logger = logging.getLogger("mechanize")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)


browser.add_password(webGoatURL + "/login.mvc", Username , Password) #store login credentials
webGoat = browser.open(webGoatURL + "/login.mvc") #create "webgoat" browser & start at login page

cookie = cookielib.LWPCookieJar() #initialize cookiejar

browser.set_cookiejar(cookie) #link cookiejar wit browser



#html = webGoat.read()  #read html from webGoat and store in string called html

#print html   #print html
print "\n\n\n\n\n\n\n\n"
webGoat = browser.open(webGoatURL + "/attack?Screen=141&menu=500")
#json = webGoat.response().read()
#print json


# <MAY NOT NEED> s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initialize network socket
# <MAY NOT NEED> print("Socket successfully created!\n")
  

# <MAY NOT NEED> s.connect((host_ip,port))
# <MAY NOT NEED> print("Socket has successfully connected to WebGoat, IP:port %s%d", host_ip, port)


