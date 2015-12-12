TEST vuln-20.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Injection Flaws => Database Backdoors (vuln-20) exists.

It will return a

1 (error) if the vulnerability is present or attack is unable to execute due to HTTP errors
0 (success) if the vulnerability is fixed (aka not present)
This test assumes 3 things:

(1) Requests library for python is installed. The simplest way to do this is to first install pip.

$ sudo apt-get install python-pip
$ sudo pip install requests

(2) The script ./webgoat/vuln-20/vuln-20-runner is in the path aka $PATH This can be done & confirmed with:

$ sudo cp webgoat/vuln-20/vuln-20-runner /usr/bin/
$ sudo chmod 775 /usr/bin/vuln-20-runner 
$ which vuln-20-runner
/usr/bin/vuln-20-runner

(3) There is a local proxy running on 127.0.0.1:8888

Testing vuln-20 can be done outside of Gauntlt by navigating to the webgoat/vuln-20 directory and running:

$ python exploit-vuln-20.py
