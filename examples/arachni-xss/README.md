# Challenge
Arachni is a powerful web application scanner written in ruby.  We will use it to test for cross site scripting (XSS) on a site.

# Hints
You need to have arachni installed on your machine.  It is a ruby gem, so you will need to add it to your Gemfile.

Get started with arachni to get familiar with the output
```
$ arachni --modules=xss --depth=1 --link-count=10 --auto-redundant=2 http://localhost:3000 
```
Once you feel good with working with the arachni output, check the `challenge_arachni-xss.attack` to get started. 

# Solution
Check `final_arachni-xss.attack` for a working solution answer.
