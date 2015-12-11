TEST vuln-12.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Injection Flaws => Numeric SQL Injection (vuln-12) exists.

It will return a

 - False (error) if the vulnerability is present
 - True (success) if the vulnerability is fixed (aka not present)

This test assumes 2 things:

(1) That the requests library for python is installed as outlined in this guide: http://docs.python-requests.org/en/latest/user/install/#install

```
$ pip install requests
```

(2) The clone is located home/hacker/ (the default directory you get when opening a terminal)

Test written by Blake Henry and Misty Francis
Team: SKT-T1


