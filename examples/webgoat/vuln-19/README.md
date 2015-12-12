TEST vuln-19.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Injection Flaws => Add Data with SQL Injection exists.

It will return a
	1 (error) if the vulnerability is present
	0 (success) if the vulnerability is fixed (aka not present)

This test assumes 3 things:

(1) First, it assumes that the path of the WebGoat vulnerabilities to be tested is:
```
/home/hacker/gauntlt-demo/examples/webgoat/
```
This should be true if the gauntlt demo directory was created by cloning the
repo off of github into the home directory of the hacking-lab VM.

(2) Second, it assumes that the Python package manager pip, and the Python module "Requests" are both
installed on the running machine.
If these are not, then they can be installed by running the following two commands on a Debian distro:
```
$ sudo apt-get install python-pip
$ sudo pip install requests
```
(3) Third, this test assumes that WebGoat is setup and running on localhost:8080, equivalent to 127.0.0.1:8080.

Testing this vulnerability can be done outside of Gauntlt by navigating to the webgoat/vuln-19 directory and running
```
$ python attack.py
```

If executed this way and the script returns silently, then there is no vulnerability. Otherwise, it will output
that there exists a vulnerability.

This attack script written by Barry Luther, EID: BBL345
