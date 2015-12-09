TEST vuln-32.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Web Services => WSDL Scanning (vuln-32) exists.

The test will pass if the vulnerability is present, and fail otherwise.

This test assumes the following:

(1) The python "requests" library is installed

(2) The script ./webgoat/vuln-32/vuln-32.py is located at /home/hacker/attackScripts/vuln-32.py

Testing vuln-32 can be done by navigating to the webgoat/vuln-32 directory and running:

$ gauntlt
