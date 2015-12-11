TEST vuln-34.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Web Services => Web Services SAX injection (vuln-34) exists.

It will return a
 - 1 (error) if the vulnerability is present
 - 0 (success) if the vulnerability is fixed (aka not present)

This test assumes 3 things:

(1) That jerry-curl and jq are installed and available on the $PATH and uses the generic command-line attack.  To install these run the following command on Debian-based systems aka those using .deb packages.

```
$ sudo apt-get install owasp-wte-jerry-curl owasp-wte-jq
```

This assumes you have the OWASP WTE repo setup on the computer running Gauntlt.  If not, it can be added with:

```
$ sudo echo "deb http://appseclive.org/apt/14.04 trusty main" > /etc/apt/sources.list.d/owasp-wte.list
$ sudo wget -q -O - http://appseclive.org/apt/owasp-wte.gpg.key | apt-key add -
```

(2) The script ./webgoat/vuln-34/vuln-34-runner is in the path aka $PATH  This can be done & confirmed with:

```
$ sudo cp webgoat/vuln-00/vuln-00-runner /usr/bin/
$ sudo chmod 775 /usr/bin/vuln-00-runner 
$ which vuln-00-runner
/usr/bin/vuln-00-runner
```

(3) There is a local proxy running on 127.0.0.1:8888

Testing vuln-34 can be done outside of Gauntlt by navigating to the webgoat/vuln-34 directory and running:

```
$ ./exploit-vuln-00.bash
```

This Gauntlt test was written by Andy Medina and Dinh Hyu on Thu, 10 Dec 2015 20:00:00

