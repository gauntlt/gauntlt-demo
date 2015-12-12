vuln-45 AJAX ==> DOM Injection

This vulnerability is done under the assumption that WebGoat and Gauntlt have both been successfully installed. 

In order to check this, you can go ahead and run the following commands: 

which gauntlt
source .rvm/scripts/rvm
which gauntlt

The above commands double check a successful installation of gauntlt. 

Performing the vulnerability assessment requires a few additional packages. Below are the Programs/Packages requred and also the commands to type if using a command line interface. (one caviat is that get-pip.py must be installed from the website first). The last thing required is a request library provided to python which makes the session handling phenomenally easier. 

python: 
[hacker@console] [~/]$ sudo apt-get install python (on Debian32 Machine)

pip:
[hacker@console] [~/]$ python get-pip.py (performed in same working directory as downloaded file

requests library: 
[hacker@console] [~/]$ pip install requests

With all of the above installed, we assume that the vulnerable application is currently running. In our instance, WebGoat. 

In order to execute the python attack alone, it is done with the following command (must be in current directory of python script) : 

[hacker@console] [~/]$ python vuln-45.py

Synching the phython script into the gaunlt attack file requires manually pointing to that script within the .attack file. 

Running the phython script within the attack file utilizing gauntlt requires the following command: 

[hacker@console] [~/]$ gauntlt vuln-45.attack
