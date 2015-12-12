
#Bling SQL Injection	-		Case Study 	
TEST vuln-21.attack

This is a Gauntlt test to check if the vulnerability in WebGoat 
located at General => HTTP Basics (vuln-21) exists.

It will return a

1 (error) if the vulnerability is present

0 (success) if the vulnerability is fixed (aka not present)


#Set Up

This test assumes 3 things: that:

(1) WebGoat and Gauntl are installed on your VM

Run the following curl-bash script to do the install.  

	curl -sSL http://bit.ly/1MJ3qNp | bash


(2) Paths and vuln-21 directories are correctly set | 
Making sure the environment for WebGoat and Gauntlt are set 

You can check this respectively:

	$which ruby
	/home/hacker/.rvm/gems/ruby-2.2.1/bin/ruby

	$which gauntlt
	/home/hacker/.rvm/gems/ruby-2.2.1/bin/gauntlt


(3) There is a local proxy running on 127.0.0.1:8888

Testing vuln-00 can be done outside of Gauntlt by navigating to the webgoat/vuln-21 directory and running:

	$ ./exploit-vuln-21.bash

(4) Python-Pip is properly installed

You can achieve this with: 

	apt-get install python-pip

	pip insall request
	
	
(5)	(Optional) Install Geany to use as Editor for Python 

	apt-get install geany geany-plugins




This Gauntlt test was written by Patrizio Chiquini & Omar   on December 11th, 2015 
