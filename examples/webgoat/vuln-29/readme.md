# TEST vuln-29.attack
This is a Gauntlt test to check if the vulnerability in WebGoat located at General => Http Basics (vuln-29) exists.

It will return a

1 (Vulnerability present) if the vulnerability is present
0 (No Vulnerability present) if the vulnerability is fixed 

This test assumes 3 things:


(1)The script ./webgoat/vuln-29/vuln-29.py is in the path aka $PATH This can be done & confirmed with:
```
$ sudo cp webgoat/vuln-29/vuln-29.py /usr/bin/
$ sudo chmod 775 /usr/bin/vuln-29.py 
$ which vuln-29.py
/usr/bin/vuln-29.py
```

(2)Pip needs to be installed. If not installed, it can be done with the following command

```
curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | python
```
Once pip is installed, install the requests,which  are necessary for the script to run
```
pip install requests 
```


(3) The gauntlt-demo repo is cloned in home/hacker/ directory. Vuln-29.py works if folder
	is moved to external location home/hacker/test-gauntlt. Gauntlt needs to be called from
	here. 

This Gauntlt test was written by Juan Villegas and Hannah Grounds on Thurs, 10 Dec 2015 