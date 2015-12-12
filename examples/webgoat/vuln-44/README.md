TEST vuln-44.attack

This test checks for the vulnerability in webgoat titled Off-by-One Overflows under the Buffer Overflows section.

It will return a
 - 1 (error) if the vulnerability is present
 - 0 (success) if the vulnerability is fixed (aka not present)

  This test assumes 3 things:

  (1) That the python package Requests is installed 
  ```
  $ sudo apt-get install python-pip; sudo pip install requests
  ```

  (2) Gauntlt is being run from the base of the repo. For example, if you cloned the repo into /home/hacker, 
      the current working directory when running gauntlet should be /home/hacker/gauntlt-demo/ 

  (3) There is a local proxy running on 127.0.0.1:8888

  Testing vuln-44 can be done outside of Gauntlt by navigating to the webgoat/vuln-44 directory and running:

  ```
  $ python attack.py 
  ```

  This Gauntlt test was written by Patrick Aupperle and Ousek Son from team Admin on Thu, 10 Dec 2015 
