Hunter DeGroot and Zack Bilderback

TEST vuln-13.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Injection Flaws => Log Spoofing (vuln-13) exists.

It will return a
 - 1 (error) if the vulnerability is present
 - 0 (success) if the vulnerability is fixed (aka not present)

This test assumes 3 things:

(jerry-curl maybe not required)
(1) That jerry-curl and jq are installed and available on the $PATH and uses the generic command-line attack.  To install these run the following command on Debian-based systems aka those using .deb packages.

```
$ sudo apt-get install owasp-wte-jerry-curl owasp-wte-jq
```

This assumes you have the OWASP WTE repo setup on the computer running Gauntlt.  If not, it can be added with:

```
$ sudo echo "deb http://appseclive.org/apt/14.04 trusty main" > /etc/apt/sources.list.d/owasp-wte.list
$ sudo wget -q -O - http://appseclive.org/apt/owasp-wte.gpg.key | apt-key add -
```

(2) There is a local proxy running on 127.0.0.1:8888

(3) Have python requests

apt-get install python-pip

pip install requests
