TEST vuln-38.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at AJAX => XML Injection (vuln-36) exists.

It will return a
 - 1 (error) if the vulnerability is present
 - 0 (success) if the vulnerability is fixed (aka not present)
 
This test assumes 3 things:

(1) That the path to this directory looks like /home/hacker/gauntlt-demo/examples/webgoat/vuln-36. This can be confirmed with:

```
$ pwd
```

This Gauntlt test was written by Nick Kasprzak and Timothy Kwan on Tue, 8 Dec 2015
