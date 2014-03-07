## Garmr and Web Security Policies

### Install
If you are using the Vagrant box provided, you should be all set.  If you need to install Garmr for your OS, please check `vendor/Garmr/README.md` to see how to install it.  Also the `README.md` in `examples/garmr/README.md` has some tips for installing on ubuntu.

### Challenge
Garmr is a tool built my Mozilla that checks webpages to meet their security requirements.  Some of the things it detects are trivial and some are more important.  Since we are using this tool against vulnerable web applications and servers we aren't going to require that it passes all tests.  In your environment you can assess what is important for a failure or a pass.  This is one of the nice features behind gauntlt--you get to decide what is good or bad on a per application basis.

The challenge is to run garmr and parse the output.

Start with `examples/garmr/challenge_garmr.attack`

### Solution

```
@final @slow
Feature: Run a Garmr scan on a single URL

  Scenario: Use Garmr to scan a website for basic security requirements # ./examples/garmr/final_garmr.attack:4
    Given "garmr" is installed                                          # gauntlt-1.0.6/lib/gauntlt/attack_adapters/garmr.rb:1
    And the following profile:                                          # gauntlt-1.0.6/lib/gauntlt/attack_adapters/gauntlt.rb:9
      | name       | value                 |
      | target_url | http://localhost:3000 |
    When I launch a "garmr" attack with:                                # gauntlt-1.0.6/lib/gauntlt/attack_adapters/garmr.rb:5
      """
      garmr -u <target_url> -o my_garmr_output.xml
      """
    Then it should pass with:                                           # aruba-0.5.3/lib/aruba/cucumber.rb:162
      """
      [Garmr.corechecks.WebTouch] Pass The request returned an HTTP 200 response
      """
    And the file "my_garmr_output.xml" should not contain XML:          # gauntlt-1.0.6/lib/gauntlt/attack_adapters/gauntlt.rb:21
      | css                                   |
      | testcase[name="Http200Check"] failure |
    And the file "my_garmr_output.xml" should contain XML:              # gauntlt-1.0.6/lib/gauntlt/attack_adapters/gauntlt.rb:15
      | css                               |
      | testcase[name="InlineJS"] failure |

1 scenario (1 passed)
6 steps (6 passed)
```