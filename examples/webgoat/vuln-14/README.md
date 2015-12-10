#vuln-14.attack

This is a [Gauntlt](http://gauntlt.org/) test to check if the vulnerability in Webgoat located at Injection Flaws => XPATH Injection (vuln-14) exists.

It will return the following:
 - 1 (error): if the vulnerability is present within the web application
 - 0 (success): if the vulnerability is fixed (not present within the web application)

**Note:** This vulnerability tests only a single user: Mike.

# How to set up WebGoat 
* Start up your virtual machine and open up a root terminal.
* Run the following curl-bash script to install WebGoat and Gauntlt
```
$ curl -sSL http://bit.ly/1MJ3qNp | bash
```
* Check to make sure WebGoat installed without problems. To do so, you can use WebGoat START to launch WebGoat. This can be found under Applications/Other/WebGoat START or under Applications/Hacking-Lab/WebGoat START.

![Screen](https://raw.githubusercontent.com/aseal134/gauntlt-demo/master/examples/webgoat/vuln-14/Screenshots/HL-Launch-WebGoat.png)
* Check that Gauntlt installed without problems. 
Launch a terminal (normal, not the root terminal) - the normal terminal is under Applications => Accessories => Terminal.  Make sure to source the rvm script so Gauntlt will be in your path or else the Gauntlt won't be in your path.
![Screen 2](https://raw.githubusercontent.com/aseal134/gauntlt-demo/master/examples/webgoat/vuln-14/Screenshots/HL-Source-rvm.png)
* Create a file called gauntlt-test.attack in the initial-test directory with the following contents:
![Screen 3](https://raw.githubusercontent.com/aseal134/gauntlt-demo/master/examples/webgoat/vuln-14/Screenshots/HL-test-attack2.png)
* Close the editor and run the attack like:
![Screen 4](https://raw.githubusercontent.com/aseal134/gauntlt-demo/master/examples/webgoat/vuln-14/Screenshots/HL-gauntlt-test.png)

You now have an environment running WebGoat and Gauntlt.

If you receive a "no such file or directory error when running the following command: 
```
$ source .rvm/scripts/rvm
```
You can remedy this by running the following commands:
```
$ wget -O rvm.key http://pgp.key-server.io/download/0x3804BB82D39DC0E3
$ gpg --import rvm.key
$ curl -sSL https://get.rvm.io | bash -s stable --ruby
$ source /home/hacker/.rvm/scripts/rvm && cd /home/hacker && gem install gauntlt
```
You can then go back and check that you have Gauntlt working on your machine.

##Executing the Attack
* The attack script is written in Python and requires **requests** and **json** libraries. To install these libraries, execute the following commands in your terminal:
```
$ sudo pip install requests
$ sudo pip install simplejson
```
* You may then clone the repository onto your Desktop for testing purposes.
* To execute the gauntlt attack, execute the following command:
```
$ gauntlt
```
* To execute the attack on the WebGoat application to exploit the Injection Flaws: XPATH injection vulnerability, execute the following:
```
$ cd /home/hacker/Desktop/gauntlt-demo/examples/webgoat/vuln-07
$ python attack.py
```

# Other Assumptions
(1) That jerry-curl and jq are installed and available on the $PATH and uses the generic command-line attack.  To install these run the following command on Debian-based systems aka those using .deb packages.

```
$ sudo apt-get install owasp-wte-jerry-curl owasp-wte-jq
```

This assumes you have the OWASP WTE repo setup on the computer running Gauntlt.  If not, it can be added with:

```
$ sudo echo "deb http://appseclive.org/apt/14.04 trusty main" > /etc/apt/sources.list.d/owasp-wte.list
$ sudo wget -q -O - http://appseclive.org/apt/owasp-wte.gpg.key | apt-key add -
```

