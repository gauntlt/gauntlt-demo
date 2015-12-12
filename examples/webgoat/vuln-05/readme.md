Report by Alexandra Martinez and Jacob Walsh

UT CS 361 Fall 2015

Team: cs361_team

Phishing login credentials by XSS


Changes to Hacking Lab VM needed for testing:


$ sudo apt-get install python3

$ sudo apt-get install python3-requests


The attack assumes the python file, attack05.py, is in directory

~/casestudy/gauntlt-demo/examples/webgoat/vuln-05/




and the script vuln-05-runner is in the path

This can be confirmed with:

$ sudo cp casestudy/gauntlt-demo/examples/webgoat/vuln-05/vuln-05-runner /usr/bin/

$ sudo chmod 775 /usr/bin/vuln-05-runner 

$ which vuln-05-runner

/usr/bin/vuln-05-runner






Gauntlt will call the vuln-05-runner script which in turn will run our python attack.

Goal of Attack
This attack takes advantage of a Cross-Site Scripting (XSS) vulnerability 
where we generate a fake login page.  This page is set to phish the login credentials
that are entered and sent to a location of our choice.  Our attack preforms this injection,
submits credentials and utilizes webgoats system to confirm that the attack worked.


