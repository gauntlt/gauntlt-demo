# Challenge
Gauntlt can use environment variables. Lets use environment variables in attack script profiles. This is useful when the target hostname, paths, or other profile element, for a given attack script differs server-to-server or environment-to-environment.

For example, you want to run the same attack script in your development, test, and production environments. But the target hostname is different. Setting environment variables in the cucumber profile and using environment variables in the attack script allow you to sync identical attack scripts in all environments.

Lets revisit our simple port_check but this time use enviroment variables. Start in `challenge_env-vars.attack`

# Hints
Read this gauntlt wiki page to get started: [Using Cucumber Profiles and Environment Variables with Gauntlt](https://github.com/gauntlt/gauntlt/wiki/Using-Cucumber-Profiles-and-Environment-Variables-with-Gauntlt)

# Solution
Check `final_env-vars.attack` for a working solution answer. Try changing the environment variable to point to a different host like scanme.nmap.org and running again.
