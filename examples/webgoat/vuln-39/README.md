#TEST vuln-39.attack

This is a [Gauntlt](http://gauntlt.org/) test to check if the vulnerability in WebGoat located at AJAX Security => Insecure Client Storage (vuln-39) exists.

It will return a
 - Vulnerable: (error) if the vulnerability is present
 - No Vulnerability: (success) if the vulnerability is fixed (aka not present)

This test assumes 3 things:

(1) Environment

- This test assumes the test is being run in HackingLab with Gauntlt and WebGoat on it. If not installed, via root terminal run:

```
$ curl -sSL http://bit.ly/1MJ3qNp | bash
```

- Then in a not root terminal run:

```
$ source .rvm/scripts/rvm
```
 
- It also assumes that Python (at least v. 2.7.3) is installed. This is included in HackingLab.
- That pip is installed. Pip can be installed via terminal

```
$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv 
```

- That the request and json libraries are installed
```
$ pip install requests
$ pip install json
```

(2) That the gauntlt/gauntlt-demo has been cloned

```
$ git clone https://github.com/gauntlt/gauntlt-demo.git
```

(3) There is a local proxy running on 127.0.0.1:8000

Testing vuln-39 can be done by navigating to the gauntlt-demo/examples/webgoat/vuln-39 directory and running:

```
$ gauntlt
```

This Gauntlt test was written by Cynthia Ibarra and Mauricio Amezcua 
