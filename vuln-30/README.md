TEST vuln-30.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Parameter Tampering => Bypass Client Side JavaScript Validation (vuln-30) exists.

It will return a

1 (error) if the vulnerability is present
0 (success) if the vulnerability is fixed (aka not present)

This test assumes 3 things:

(1) The Python library Requests is installed

(2) There is a local proxy running on 127.0.0.1:8888

Testing vuln-30 can be done outside of Gauntlt by navigating to the webgoat/vuln-30 directory and running:

`$ python exploit-vuln-30.py`

(3) Gauntlt is installed

This Gauntlt test was written by Hao-Hsiang Chi and Tarequl Alam from team Anthing Man on Tuesday, 8 Dec 2015
