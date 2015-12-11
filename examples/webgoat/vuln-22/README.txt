Vuln-22 Blind String SQL Injection

Install WebGoat and Gauntlt through a root terminal using the command:

curl -sSL http://bit.ly/1MJ3qNp | bash

Next check to see that Gauntlt installed without problems by opening a normal terminal and running these three commands in succession from the home directory:

which gauntlt
source .rvm/scripts/rvm
which gauntlt

This is done in the home directory because this ensures that the rvm script will always be in the path of the python script and attack file.

In order to run the python script, parse.py, correctly, it is necessary to download the pip package management system because the python requests library is used for the .Session(), .get, and .post functions. To install pip on the virtual machine using a root terminal, use the command:

python get-pip.py

Then to install the requests library, use the command:

pip install requests

From here, given that the WebGoat application is up and running, the python script should run with the simple command:

python parse.py

In order to run the python script in conjunction with the attack file, Vuln-22.attack, the absolute path of the python script must be included, or else gaunlt will not be able to find the script.

Finally, in order to run the python script and attack file together, input, in a normal terminal, the command:

gauntlt Vuln-22.attack
