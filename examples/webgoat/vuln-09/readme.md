TEST vuln-09.attack

This test is related with Cross-Site Scripting (XSS) => HttpOnly Test.
This is a Gauntlt test to check that the WebGoat page is setting correctly the HttpOnly flag for unique2u cookie. The original test involved checking that the browser interprets the flag, but it didn't fit very well the gauntlt testing pattern, so the professor decided to have it test whether the site sets the cookie correctly and process it when it receives it back.

It will return a
1 (error) if WebGoat doesn't set the HttpOnly flag for cookie unique2u after pressing the Read Cookie button or if it doesn't print "SUCESS" after the Write Button is pressed afterwards.
0 (success) otherwise

This test assumes:
-The attack files (incliding .py) need to be in /home/hacker/cs361/gauntlt-demo/examples/webgoat/vuln-09
-python's requests library must be installed
-WebGoat is running on 127.0.0.1:8080

To install Python's requests library:
as root:
# apt-get install python-pip
# pip install requests

This Gauntlt test was written by Andy Ruiz Cabrera (ar48299) as part of the team Frostbyte
