TEST vuln-28.attack

This is a Gauntlt test to check if the vulnerability in WebGoat located at Parameter Tampering => Exploit Hidden Fields (vuln-28) exists.

It will return a
 - 1 (error) if the vulnerability is present
 - 0 (success) if the vulnerability is fixed (aka not present)
 
This test assumes 3 things:

(1) That the path to this directory looks like /home/hacker/gauntlt-demo/examples/webgoat/vuln-28. This can be confirmed with:

```
$ pwd
```

(2) There is a local proxy running on 127.0.0.1:8888

This Gauntlt test was written by Kevin Bishop and Rachel Larios on Tue, 8 Dec 2015
