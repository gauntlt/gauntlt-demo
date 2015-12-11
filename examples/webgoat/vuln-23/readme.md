TEST vuln-23.attack

This is a Gauntlt test to check if the vulnerability in WebGoat Denial of Service -> ZipBomb exists.

It will pass if 

The webpage contains the phrase "* File uploaded"
The webpage doesn't contain the phrase "* Congratulations"

This test assumes 3 things:

(1) That Easy Install, pip, the python requests module are installed and available on the $PATH and uses the generic command-line attack. To install these run the following command on Debian-based systems aka those using .deb packages.

$ sudo apt-get install python-setuptools
$ sudo easy_install pip
$ sudo pip install requests

(2) That the provided zipBomb.zip is in the same directory as the attack. The zipBomb is just a large txt file that contains all "1"s.

(3) There is a local proxy running on 127.0.0.1:8888

Testing vuln-00 can be done outside of Gauntlt by navigating to the webgoat/vuln-00 directory and running:

$ python exploit-vuln-23.py
