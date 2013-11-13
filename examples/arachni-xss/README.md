# Challenge
Arachni is a powerful web application scanner written in ruby.  We will use it to test for cross site scripting (XSS) on a site.

# Hints
You need to have arachni installed on your machine.  It is a ruby gem, so you will need to add it to your Gemfile.

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
