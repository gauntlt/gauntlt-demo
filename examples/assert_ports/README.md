# Challenge
It is common to put service ports on web applications or add new services. Finding new services in your prod environment is usually a cause for concern and needs to be checked.  Lets write a gauntlt attack that helps us assert ports. We will check to make sure that only the ports you expect to be open are open and no other ports are open.

# Hints
Now that you have learned how to use regex in gauntlt, see if you can parse nmap output
```
$ nmap -F localhost
```
For help with this, use the gauntlt wiki article [Assert your network services from the outside in using gauntlt](https://github.com/gauntlt/gauntlt/wiki/Assert-your-network-services-from-the-outside-in-using-gauntlt).

# Solution
Check `final_assert-ports.attack` for a working solution answer.
