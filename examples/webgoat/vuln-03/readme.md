TEST vuln-03.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Authentication Flaws => Multi Level Login 2 (vuln-03) exists using (attack.py)

It will return a
1 (error) if the vulnerability is present
0 (success) if the vulnerability is fixed

requirements:
(1) requests 
$ sudo pip install requests

(2) Webgoat is being running at 127.0.0.1:8080

Testing vuln-03 can be done outside of Gauntlt by navigating to the webgoat/vuln-03 directory and running:
$ ./attack.py
