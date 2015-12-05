TEST vuln-03.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at General => Http Basics (vuln-03) exists using an attack script file in attack.py.

It will return a
1 (error) if the vulnerability is present
0 (success) if the vulnerability is fixed

requirements:
(1) The script ./webgoat/vuln-03/attack.py is in the path aka $PATH This can be done & confirmed with:

(2) requests 
$ sudo pip install requests

(3) Webgoat is being hosted at 127.0.0.1:8080

Testing vuln-00 can be done outside of Gauntlt by navigating to the webgoat/vuln-03 directory and running:
$ ./attack.py
