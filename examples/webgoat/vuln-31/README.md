**TEST vuln-31.attack**

This is a Gauntlt test to check if the vulnerability in WebGoat located at General => Http Basics (vuln-31 - Session Management Flaws => Spoof an Authentication Cookie) exists.

It will print out:

* __\*\*\*Vulnerability Present\*\*\*__ if the vulnerability is present
* __\*\*\*No Vulnerability\*\*\*__ if the vulnerability is fixed (i.e. not present)

1) You have to have requests installed. If you don't have requests installed on your machine, follow these steps to install it:
Clone the public repo:
		
	$ git clone git://github.com/kennethreitz/requests.git
		
Once you have the copy of the source, install it by issuing this command:
		
	$ python setup.py install
		

<br/><br/>
2) There is a local proxy running on 127.0.0.1:8888
Testing vuln-31 can be done outside of Gauntlt by navigating to the webgoat/vuln-31 directory and running:

	$ python exploit-vuln-31.py

<br/><br/>
3) Create a new directory called CaseStudyVuln31 and clone the gauntlt repo in that directory. The path to the script is like so. Running Guantlt will be safest if you are cd into this directory. 
		
	/home/hacker/CaseStudyVuln31/gauntlt/examples/webgoat/vuln-31/exploit-vuln-31.py
	

<br/><br/>
*This Gauntlt test was written by Tin Vo (tinnvo1101@gmail.com) and Uyviet Nguyen (uyviet.nguyen@utexas.edu) on 10 Dec 2015*
