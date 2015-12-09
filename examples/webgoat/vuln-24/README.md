TEST vuln-24.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Denial of Service => Denial of Service from Multiple Logins (vuln-24) exists.

It will print:

* "Attack Successful. vuln-24 is present" and fail the Gauntlt test if the vulnerability is present
* "Attack Failed. vuln-24 is not present" and pass the Gauntlt test if the vulnerability is fixed (aka not present)

This test assumes 5 things: 

1. The Python script is in /home/hacker/gauntlt-demo/examples/webgoat/vuln-24 and that this full path is listed on line 6 in the .attack file

2. The Python setuptools package is installed. To install this run the following command on Debian-based systems aka those using .deb packages.
```
$ sudo apt-get install python-setuptools
```

3. The Python pip package is installed. To install this run the following command on Debian-based systems aka those using .deb packages.
```
$ sudo easy_install pip
```

4. The Python requests package is installed. To install this run the following command on Debian-based systems aka those using .deb packages.
```
$ sudo pip install requests
```

5. The Python BeautifulSoup4 package is installed. To install this run the following command on Debian-based systems aka those using .deb packages.
```
$ sudo pip install beautifulsoup4
``` 