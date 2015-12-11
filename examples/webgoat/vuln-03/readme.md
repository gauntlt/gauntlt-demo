#Authentication Flaws > Mutli Level Login 2

This is a Gauntlt test to written to pass if the WebGoat vulnerability "Authenticat Flaws > Multi Level Login 2" cannot be exploited via the `hidden_user` POST parameter during authentication.

Success: No vunerability
Failure: Vunerability exploited

Place this repo at `/home/hacker/` for out of the box functionality or edit the path in vuln-03.attack.

###Requirements:

#####[pip](https://github.com/pypa/pip) if necessary

as root:

`$ python get-pip.py`

#####[requests](http://docs.python-requests.org/en/latest/)

again in a root terminal:

`pip install requests`

#####[WebGoat](https://github.com/WebGoat/WebGoat) server at 127.0.0.1:8080




