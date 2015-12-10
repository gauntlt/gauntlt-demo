TEST vuln-15.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at General => Http Basics (vuln-15) exists.

It will return a
  - 1 (error) if the vulnerability is not present
  - 0 (success) if the vulnerability is present

The test assumes:
  1)  the Requests module for python is installed
      (our team used pip to install requests)
  2)  there is a local proxy running on 127.0.0.1:8888 
      testing vuln-15 can be done outside of Gauntlt by navigating to the webgoat/vuln-15 directory and running: 'python vuln-15.py'

This Gauntlt test was written by team Natalie/Heng.
