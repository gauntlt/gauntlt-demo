# TEST Vuln-40

#### What is being tested

This is a Gauntlt test to check if the vulnerability in WebGoat located at AJAX Security => LAB: DOM-Based cross-site scripting (vuln-40) exists.

#### What is being returned

It will return a
- 1 (error) exit code if the vulnerability is present and will print out the phrase "Vulnerable"
- 0 (success) exit code if the vulnerability is fixed (aka not present) and will print out the phrase "Safe"

## Test Requirements

- Ensure ruby, ruby gems, gauntlt, and WebGoat are installed properly and that WebGoad is listening on port 8080
- Ensure that xvfb is installed
```
sudo apt-get install xvfb
```
- Ensure that the watir-webdriver and headless gems are installed
```
gem install watir-webdriver
gem install headless
```

## Test Assumptions

- This test assumes that the vuln-40.rb file has executable permissions
- This test assumes that the default time limit for the aruba gem is extended. To do this, run the following command (changing the path as necessary to account for your account name):
```
vim +355 /home/hacker/.rvm/gems/ruby-2.2.1/gems/aruba-0.5.4/lib/aruba/api.rb
```
and change `DEFAULT_TIMEOUT_SECONDS = 3` to `DEFAULT_TIMEOUT_SECONDS = 30`

- The path to `vuln-40.rb` is assumed to be `/home/hacker/gauntlt-demo/examples/Vuln-40/vuln-40.rb`. If this path differs, make the appropriate changes to the `vuln-40.attack` file in the `When I launch a "generic" attack with:` section

## Running the test

To run the test, run the following command
```
gauntlt /path/to/vuln-40.attack
```