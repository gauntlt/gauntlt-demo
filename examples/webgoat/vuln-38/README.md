TEST vuln-38.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Authentication Flaws => Forgot Password (vuln-38) exists.

It will return a
 - 1 (error) if the vulnerability is present
 - 0 (success) if the vulnerability is fixed (aka not present)

This test assumes 3 things:

(1) That python and python-requests are installed and available on the $PATH and uses the generic command-line attack.  To install these run the following command on Debian-based systems aka those using .deb packages.

```
$ sudo apt-get install python python-requests
```

This assumes you have the OWASP WTE repo setup on the computer running Gauntlt.  If not, it can be added with:

```
$ sudo echo "deb http://appseclive.org/apt/14.04 trusty main" > /etc/apt/sources.list.d/owasp-wte.list
$ sudo wget -q -O - http://appseclive.org/apt/owasp-wte.gpg.key | apt-key add -
```

(2) The python attack file and the text files for the usernames and colors ./webgoat/vuln-38/attack.py is in the path aka $PATH  This can be done & confirmed with:

```
$ sudo cp webgoat/vuln-38/attack.py /usr/bin/
$ sudo chmod 775 /usr/bin/attack.py
$ which attack.py
/usr/bin/attack.py

$ sudo cp webgoat/vuln-38/usernames.txt /usr/bin/
$ sudo chmod 775 /usr/bin/usernames.txt
$ which usernames.txt
/usr/bin/usernames.txt

$ sudo cp webgoat/vuln-38/color.txt /usr/bin/
$ sudo chmod 775 /usr/bin/color.txt
$ which color.txt
/usr/bin/color.txt

```

(3) There is a local proxy running on 127.0.0.1:8080

Testing vuln-38 can be done outside of Gauntlt by navigating to the webgoat/vuln-38 directory and running:

```
$ python attack.py
```

This Gauntlt test was written by Nick Kantor and Tanner Harper
