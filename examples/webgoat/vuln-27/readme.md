TEST vuln-27.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Parameter Tampering => Bypass HTML Field Restrictions (vuln-27) exists.

It will return a
 - 1 (error) if the vulnerability is present
 - 0 (success) if the vulnerability is fixed (aka not present)

This test assumes 4 things:

(1) That the python requests, json, and sys modules are all installed. The json and sys modules should both be included with python as of version 2.6 and later.

```
$ pip install requests
```

If pip is not installed, it can be installed with

```
$ sudo apt-get install python-pip
```

(2) WebGoat is running on http://127.0.0.1:8080/WebGoat/

(3) Both files (vuln-27.py and vuln-27.attack) exist in the same directory. They currently do, and should not be separated.

(4) That Gauntlt's running structure and present working directory do not change. Gauntlt must run from tmp/aruba/, two directories down from the directory of the attack file.

Testing vuln-27 can be done outside of Gauntlt by navigating to the examples/webgoat/vuln-27/ directory and running:

```
$ python vuln-27.py
```

This Gauntlt test was written by Kyle DeHolton and Bryant Peng on Tues, December 8, 2015.
