TEST vuln-16.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Injection Flaws => LAB: SQL Injection => Stage 3: Numeric SQL Injection (vuln-16) exists.

It will return a
 - FAIL (error) if the vulnerability is present
 - PASS (success) if the vulnerability is fixed (aka not present)

This test assumes 3 things:

(1) That python and virtualenv are installed.  To install these run the following command on Debian-based systems aka those using .deb packages.

```
$ sudo apt-get install python virtualenv
```

(2) That gauntlt-demo is installed to the user's home directory (i.e. ~/gauntlt-demo)

(3) That the user's home directory is /home/tyler/

Testing vuln-16 can be done outside of Gauntlt by navigating to the webgoat/vuln-16 directory and running:

```
$ python vuln-16.py
```

This Gauntlt test was written by Tyler O'Meara (Tyler@TylerOMeara.com) on Sat, 5 Dec 2015 20:36:00 -0600
