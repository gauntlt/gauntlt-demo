TEST vuln-39.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at AJAX Security => Insecure Client Storage (vuln-39) exists.

It will return a
 - Vulnerability Present (error) if the vulnerability is present
 - No Vulnerability (success) if the vulnerability is fixed (aka not present)

This test assumes 3 things:

(1) That Python (at least v. 2.7.3) is installed. 
(2) That pip is installed. Pip can be installed via terminal

```
$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv 
```

This assumes you have the OWASP WTE repo setup on the computer running Gauntlt.  If not, it can be added with:

```
$ sudo echo "deb http://appseclive.org/apt/14.04 trusty main" > /etc/apt/sources.list.d/owasp-wte.list
$ sudo wget -q -O - http://appseclive.org/apt/owasp-wte.gpg.key | apt-key add -
```

(2) The script ./webgoat/vuln-00/vuln-00-runner is in the path aka $PATH  This can be done & confirmed with:

```
$ sudo cp webgoat/vuln-00/vuln-00-runner /usr/bin/
$ sudo chmod 775 /usr/bin/vuln-00-runner 
$ which vuln-00-runner
/usr/bin/vuln-00-runner
```

(3) There is a local proxy running on 127.0.0.1:8888

Testing vuln-39 can be done by navigating to the webgoat/vuln-39 directory and running:

```
$ gauntlt
```

This Gauntlt test was written by Matt Tesauro (matt.tesauro@owasp.org) on Mon, 23 Nov 2015 22:43:10 -0600
