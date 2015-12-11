This Gauntlt test was written by Alexandra Gibner (atg572) and Peter Ten Eyck (pwt249)

This is a Gauntlt test to check if the vulnerability located at Injection Flaws => Command Injection (vuln-11) exists in Webgoat.

It will return 
- "Attack Successful" if the vulnerability is present
- "vuln-11 not present" if the vulnerability is not present (aka fixed)

This test assumes 4 things:

(1) That Python 2.x is installed and available on the $PATH
```
#as root
$ sudo apt-get install python
```
(2) That the requests Python library is available
```
#as root
$ sudo apt-get install python-pip
$ sudo pip install requests
```
(3) There is a local proxy running at 127.0.0.1:8080

(4) There exists a copy of the python script (vuln-11-runner.py) at /home/hacker/webgoat/ 

Testing vuln-11 can be done outside of Gauntlt by navigating to the /home/hacker/webgoat/ directory and running 
```
./vuln-11-runner.py
```
