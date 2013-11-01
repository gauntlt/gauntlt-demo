# Challenge
Garmr is a tool built my Mozilla that checks webpages to meet their security requirements.  Some of the things it detects are trivial and some are more important.  Since we are using this tool against vulnerable web applications and servers we aren't going to require that it passes all tests.  In your environment you can assess what is important for a failure or a pass.  This is one of the nice features behind gauntlt--you get to decide what is good or bad on a per application basis.

The challenge is to run garmr and parse the output.

# Hints
You need to have Garmr installed on your machine.  For your convenience, we have added the Garmr repo in our vendor directory. To install it, run:
```
# On Ubuntu you might need this package
$ sudo apt-get install python-setuptools
$ cd vendor/Garmr && sudo python setup.py install && cd ../../
```
Get started with Garmr to get familiar with the output
```
$ garmr -u http://localhost:3000 
$ garmr -u http://localhost:3000 -o garmr-out.xml 
```
Once you feel good with working with the Garmr output, check the `challenge_garmr.attack` to get started. Since the app we are testing is vulnerable it might be a good idea to check for one of the lines that show 'Pass'

# Solution
Check `final_garmr.attack` for a working solution answer.
