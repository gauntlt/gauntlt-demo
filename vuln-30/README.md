TEST vuln-30.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Parameter Tampering => Bypass Client Side JavaScript Validation (vuln-30) exists.

It will return 

* `vuln-30 is present` if the vulnerability is present

* `vuln-30 not present` (success) if the vulnerability is fixed (aka not present)

This test assumes 4 things:

(1) The Python library Requests is installed

`$ pip install requests`

(2) There is a local proxy running on 127.0.0.1:8888

Testing vuln-30 can be done outside of Gauntlt by navigating to the webgoat/vuln-30 directory and running:

`$ python exploit-vuln-30.py`

(3) Gauntlt is installed

(4) The files are all located in the path

`/home/hacker/vuln-30/`

This Gauntlt test was written by Hao-Hsiang Chi and Tarequl Alam from team Anthing Man on Tuesday, 8 Dec 2015
