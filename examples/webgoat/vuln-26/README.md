In vulnerability 26, we carry out a malicious file execution.

We return "The site is secure." if the vulnerability is not present.
We return "The site is vulnerable." otherwise.

Installation assumptions:

We assume that requests is installed.
To install, use:
sudo apt-get install python-pip
sudo pip install requests

We assume that the gauntlt-demo folder is on the hacker's desktop.
Thus we run gauntlt from:
/home/hacker/Desktop/gauntlt-demo/examples/webgoat/vuln-26/vuln-26.attack

Finally, we make the class-wide assumptions about the setup of
gauntlt and webgoat.
That is, jerry-curl and jq must be installed, and the OWASP WTE repo
must be setup.
