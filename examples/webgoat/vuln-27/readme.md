TEST vuln-27.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Parameter Tampering => Bypass HTML Field Restrictions (vuln-27) exists.

It will return a
 - 1 (error) if the vulnerability is present
 - 0 (success) if the vulnerability is fixed (aka not present)

This test assumes 3 things:

(1) That the python requests, json, and sys modules are all installed. The json and sys modules should both be included with python as of version 2.6 and later.

```
$ pip install requests
```

(This pip command assumes that the user running it has permissions to write to the directory that pip is using. If there are permission errors, then it *can* be installed as root; however, **the authors do not vouch for anything in the requests library, and extreme caution should be taken when installing foreign libraries as root**.) If pip is not installed, it can be installed with

```
$ sudo apt-get install python-pip
```

(2) WebGoat is running on http://127.0.0.1:8080/WebGoat/

(3) The script examples/webgoat/vuln-27/vuln-27.py is in the path ($PATH). One possible way to remidy this problem is to ensure that the python script is executable and then copy it into /usr/bin/.

```
$ chmod a+x vuln-27.py
$ sudo cp vuln-27.py /usr/bin/
```

Testing vuln-27 can be done outside of Gauntlt by navigating to the examples/webgoat/vuln-27/ directory and running:

```
$ python vuln-27.py
```

This Gauntlt test was written by Kyle DeHolton and Bryant Peng on Tues, December 8, 2015.
