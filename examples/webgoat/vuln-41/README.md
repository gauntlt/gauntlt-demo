TEST vuln-41.attack

Installing Python Requests library
- git clone git://github.com/kennethreitz/requests.git
- cd requests
- python setup.py install

This is a Gauntlt Test to check if the vulnerability in WebGoat located at AJAX Security  => Silent Transactions Attacks (vuln-41) exists.

It will return a 
- 1 (error) if a vulnerability exists
- 0 (success) if the vulnerability is fixed (aka not present)
