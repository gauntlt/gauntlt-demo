UT CS 361 Fall 2015
Team: Team Name Not Found

TEST webgoat_http.attack - Vuln-04

This is a Gauntlt test to check if the vulnerability in WebGoat located at Code Quality => Discover Clues in the HTML (vuln-04) exists.

It will return:
	- 'Vulnerability Exploited' (1) if the vulnerability was able to be exploited by the python script
	- 'Success' (0) if no vulnerabilities were exploited and the web application is secure.

This assumes that:

1. Gauntlt is installed. This can be done through

```
curl -sSL http://bit.ly/1MJ3qNp | bash
```

The rvm script should also be sourced so that Gauntlt is in your path
```
source .rvm/scripts/rvm
```


2. WebGoat is installed and running on 127.0.0.1:8888. WebGoat should be installed with the previous command as well.

4. Two python libraries were used in the script, and should be installed and usable with pip. 

```
apt-get install python pip
pip install requests
```


This Gauntlt test was written by Kelly Wilson and Michael Kloc on Mon, 09 Dec 2015