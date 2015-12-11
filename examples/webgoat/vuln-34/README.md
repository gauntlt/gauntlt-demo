TEST vuln-34.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Web Services => Web Services SAX injection (vuln-34) exists.

It will return a
 - Vuln-34 Present if the vulnerability is present
 - No Vulnerability if the vulnerability is fixed (aka not present)

This test assumes 2 things:

(1) The python requests library is installed.

You can do this with pip
```
$ pip install requests
```

(2) There is a local proxy running on 127.0.0.1:8080

Testing vuln-34 can be done outside of Gauntlt by navigating to the webgoat/vuln-34 directory and running:

```
$ python exploit-vuln34.py
```

This Gauntlt test was written by Andy Medina and Dinh Hyu on Thu, 10 Dec 2015 20:00:00

