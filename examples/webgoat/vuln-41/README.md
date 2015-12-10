##TEST vuln-41.attack

This is a Gauntlt Test to check if the vulnerability in WebGoat located at AJAX Security  => Silent Transactions Attacks (vuln-41) exists.

It will return a 
- 1 (error) if a vulnerability exists
- 0 (success) if the vulnerability is fixed (aka not present)

##Setup

(1) The environment is set up correctly. This attack assumes you have a Hacking-Lab VM. Launch a root terminal and run:
```
$ curl -sSL http://bit.ly/1MJ3qNp | bash
```

Make sure WebGoat is installed without problems. Make sure FoxyProxy is disabled and open Applications => Other => WebGoatSTART.

Now make sure Gauntlt is installed without problems. Open Applications => Accessories => Terminal and run in the home directory:
```
$ which gauntlt
$ source .rvm/scripts/rvm
$ which gauntlt
```

(2) The Python Requests library is installed
```
$ git clone git://github.com/kennethreitz/requests.git
$ cd requests
$ python setup.py install
```

## Testing the Attack

(1) To run the gauntlt attack, go to examples/webgoat/vuln-41 and call:
```
$ gauntlt vuln-41.attack
```

It is written to pass when the vulnerability is fixed.

(2) To run our python script directly, go to examples/webgoat/vuln-41 and run:
```
$ python attack.py
``` 

Inside the gauntlt attack file, the absolute path of the python script must be included, otherwise gauntlt won't be able to find the script.
