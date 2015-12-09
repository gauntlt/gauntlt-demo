TEST vuln-42.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at General => Concurrency (vuln-42) exists.

It will return a 

** 1 (error) if the vulnerability is present
** 0 (success) if the vulnerability is fixed (aka not present)

This test assumes that the Python requests library is installed:

** as root: ```apt-get install python-pip ```
** ```pip install requests```

NOTE: This test causes a TimeOut Error. There are two comments in attack.py to show how to shortcircuit the code. (Search for 'SHORTCIRCUIT')

This Gauntlt test was written by Alia Mancisidor and Martin Huang on 9 Dec 2015 
