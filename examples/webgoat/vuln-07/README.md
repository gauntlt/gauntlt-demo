#TEST vuln-07.attack

This is a [Gauntlt](http://gauntlt.org/) test to check whether there's a vulnerability in WebGoat located at Cross-Site Scripting (XSS) => LAB: Cross Site Scripting => Stage 5: Reflected XSS.

It will return the following:
 - 1 (error): if the vulnerability is present within the web application
 - 0 (success): if the vulnerability is fixed (not present within the web application)

**Note:** This vulnerability tests only a single user: Larry.

# Getting Started
## Setting up the Environment
* This attack assumes you have a HL virtual machine. Start up the HL VM and launch a Root terminal. There are multiple terminals within the VM, so make sure that you're using the Root terminal.
* Run the install script for WebGoat and Gauntlt
```
$ curl -sSL http://bit.ly/1MJ3qNp | bash
```
* Check to make sure WebGoat installed without problems. To do so, you can use WebGoat START to launch WebGoat. This can be found under Applications/Other/WebGoat START or under Applications/Hacking-Lab/WebGoat START.
* Check that Gauntlt installed without problems.
![Step 1](http://res.cloudinary.com/dx4at2j5f/image/upload/v1449532665/CaseStudy/Step2.png)
![Step 2](http://res.cloudinary.com/dx4at2j5f/image/upload/v1449532707/CaseStudy/Step1.png)
![Step 3](http://res.cloudinary.com/dx4at2j5f/image/upload/v1449532665/CaseStudy/Step3.png)

When running the following command: 
```
$ source .rvm/scripts/rvm
```
There will be instances in which you will receive the following error: "no such file or directory". In this case, run the following four commands:
```
$ wget -O rvm.key http://pgp.key-server.io/download/0x3804BB82D39DC0E3
$ gpg --import rvm.key
$ curl -sSL https://get.rvm.io | bash -s stable --ruby
$ source /home/hacker/.rvm/scripts/rvm && cd /home/hacker && gem install gauntlt
```
Afterwards, check to make sure that Gauntlt has installed successfully using the above instructions.

##Executing the Attack
* The attack script is written in Python and requires the following libraries: **requests**, **sys**, and **json**. Simply run the following commands to install these libraries.
```
$ pip install requests
$ pip install json
```
* Clone the REPO onto the Desktop for testing purposes.
* To execute the gauntlt attack, simply run:
```
$ gauntlt
```
* To execute an attack on the WebGoat application to exploit the Stage 5: Reflected XSS vulnerability, simply run:
```
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

