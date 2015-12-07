TEST vuln-43.attack
TEST vuln-00.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Concurrency => Shopping Cart Concurrency Flaw (vuln-43) exists.

It will return a
 - 1 (error) if the vulnerability is present, or if an error occurred trying to exploit it
 - 0 (success) if the vulnerability is fixed (aka not present)

This test assumes:

(1) That Python and the "requests" module are installed. "requests" can be installed with ```pip install requests```. If pip is not installed, use ```curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | python``` to install it.

(2) The script webgoat/vuln-43/vuln-43-runner is in the path ($PATH) and executable. This can be done with the following commands, which must be run from the vuln-43 directory, as the files' owner:

```
$ export PATH=$PATH:`pwd`
$ chmod 755 vuln-43-runner
```

(3) WebGoat is running on 127.0.0.1:8080/WebGoat/


Testing vuln-43 can be done outside of Gauntlt by navigating to the webgoat/vuln-43 directory and running:

```
$ chmod 755 vuln-43-runner
$ ./vuln-43-runner
```

This Gauntlt test was written by Sam Lauber and Mukund Rathi on Monday December 7 2015

