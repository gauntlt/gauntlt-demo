TEST vuln-10.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Improper Error Handling => Fail Open Authentication Scheme (vuln-10) exists. You can run the specific attack file by switching to /home/hacker/Desktop/gauntlt-demo/examples/webgoat/vuln-10/ and running gauntlt in the directory. 

It will return a
 - 1 and print "Attack Successful" if the vulnerability is present
 - 0 and print "vuln-10 not present" if the vulnerability is fixed (aka not present)

This test assumes 3 things:
(1) Requests for python is installed (can be done using pip). 

you can do this in the Hacking vm with the following commands:

$ curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | python
$ pip install requests

(2) gauntlt-demo is cloned to the desktop so that the directories line up to the attack script

The attack script assumes the exploit python file is saved in the following directory:
/home/hacker/Desktop/gauntlt-demo/examples/webgoat/vuln-10/exploit-vuln-10.py
 
(3) Webgoat is up and running

This can be done using the following command:

$ webgoat start


