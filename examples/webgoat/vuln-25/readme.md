TEST vuln-25.attack 

This is a Gauntlt test to check of the vulnerability in WebGoat located at Insecure Configuration => Forced Browsing (vuln-25) exists. 

It will print:

	"vuln-25 present" if the vulnerability is present
	"vuln-25 not present" if the vulnerability is fixed (not present)

This test assumes 3 things:

(1) That pip is installed on the machine so that you can run sudo pip install requests to install the requests python library


(2) That the machine has Gauntlt and WebGoat installed and both are configured properly


(3) There is a local proxy running on 127.0.0.1:8888 and that FoxyProxy in Iceweasel needs to be updated to have ZAP on 8888


(4) The script ./webgoat/vuln-25/vuln-25-runner is in the path aka $PATH. This can be done and confirmed with:
	
	$ sudo cp webgoat/vuln-25/vuln-25-runner /usr/bin/
	$ sudo chmod 775 /usr/bin/vuln-25-runner 
	$ which vuln-25-runner
	/usr/bin/vuln-25-runner
Testing vuln-25 can be done outside of Gauntlt by navigating to the webgoat/vuln-25 directory and running:
	$ ./exploit-vuln-25.py

(5) Make sure that the correct environment variables for rvm are setup correctly. We used:

	[~/]$ source /home/hacker/.rvm/scripts/rvm
	[~/]$ echo "source /home/hacker/.rvm/scripts/rvm/" >> /home/hacker/.bashrc

(6) To run our Gauntlt attack when we placed it in the gauntlt-demo clone we ran the following command:

	[~/]$ gauntlt gauntlt-demo/examples/webgoat/vuln-25/vuln-25.attack

    We had to do this because if we navigated to where our attack file was, the gauntlt command wasn't recognized
    but running the command above allowed us to run our attack file from where it was in the gauntlt-demo clone

    Also note that in our runner file we have the path set to 
	
	/home/hacker/gauntlt-demo/examples/webgoat/vunl-25/


UT CS 361 Fall 2015
Team name: blues
Team members: Stormy Emery, Bikranta Malla 

Team member:Bikranta Malla 
This Gauntlt test was written by Stormy Emery and Bikranta Malla on Sunday, 06 Dec 2015


