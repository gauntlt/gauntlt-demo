## Multi Level Authentication 1
This is a test to check if the vulnerability in the multi level authentication of Web Goat exists.

It will return a
 - 1 (error) if the vulnerability is present, It will also print ‘vulnerable’
 - 0 (success) if the vulnerability is fixed (aka not present)

This test assumes 3 things:

1. That python and a few libraries are installed. This includes requests, re, json, and some system libraries installed with python. If any of these are missing, the pip installer can help with the installation process.

See https://pip.pypa.io/en/stable/installing/ for details about pip installation.

Following the installation of pip, install any missing packages with a command formatted like the following:

```
pip install requests
```

2. We also assume that you have Gauntlt running.  If not, the directions are on their site at http://gauntlt.org/.

The attack file vuln-02.attack needs to know the absolute path to the vuln-02.py file in order to run it successfully.
There is a local proxy running on 127.0.0.1:8888 if you run the script with the -d flag.

You can also test the vulnerability with the python script outside of gauntlt by navigating to the folder containing vuln-02.py and running the following command. If you use the -d flag it will use the proxy running at 127.0.0.1:8888

```
$ python vuln-02.py -d
```
3. We lastly assume that you are using the Hacking Lab OS. The gauntlt demo was placed in the home directory of hacker. To run the python exploit script with gauntlt python script should be placed in the following location:
```
/home/hacker/gauntlt-demo/vuln-02/vuln-02.py
```

This Gauntlt test was written by Taylor Smith and Jeremy Wenzel

