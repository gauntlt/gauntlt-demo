TEST Vulnerability 01- Bypassing an Path Based Access Control System

This is a Gauntlt test to see if a vulnerability is present in the Access Control Flaws->Bypass a Path Based Access Control Scheme page of the Webgoat App.

It will return an error and "Attack Successful" if the vulnerability is present and "Attack Failed, Vulnerability Not Present" if the vulnerability is not present or has been fixed.

This test assumes three things, that:

- The gauntlt-demo repo was cloned to /home/hacker/ with 
```
$ git clone https://github.com/gauntlt/gauntlt-demo.git
```
  from /home/hacker/
  
- That gauntlt is placed in the path using 
```
$ source .rvm/scripts/rvm
```
from /home/hacker/ as well.

- That pip and the python Requests library are installed, by running the following in Terminal as root:
```
$ apt-get install python-pip
$	pip install requests
```

This individual test can be run by executing gauntlt in this directory rather than the gauntlt-demo parent directory.


This Gauntlt test was written by Connor Mooney and Daniel Zhang on December 8th, 2015
