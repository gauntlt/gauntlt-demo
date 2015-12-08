Vulnerability-33, Web Services SQL Injection

The python script uses the requests library, which needed to be installed. Before the requests library was installed however pip first needed to be installed. This was done in root terminal (Superuser) via: python get-pip.py Once pip was installed, the requests library was installed via root terminal using: pip install requests

The path of the Python script must be included in the attack file. The contents of the attack file include the following path: python /home/hacker/test-gauntlt/injection-test/sql-injection2.py

Once both the Python script and the attack file are in the same directory, use gauntlt vuln-33.attack to run.

If an error occurs while running, repeat the install directions: source .rvm/scripts/rvm Then type: which gauntlt in order to ensure that gems is installed.
