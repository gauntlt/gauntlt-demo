## Port checking with nmap
Gauntlt supports nmap.  Lets write a real simple port check attack.

To get started with this, go to `examples/port_check` and open up `challenge_port-check.attack`.  Besides using `Background` there is one new concept that we are using in this challenge.  We use the `And the following profile:` which is the same as saying `Given the following profile:`.

### Profiles
Gauntlt uses profiles in setup steps to pass in values to the subsequent steps.  These profiles must start with the first line of `| name | value |` but after that you can assign names and values as you see fit.  Once we work with attack aliases we will see why that is important.

### Try the challenge
Edit the `challenge_port-check.attack` and try to test to see if port 8008 is open.  You can run `$ bundle exec gauntlt challenge_port-check.attack` to see if your solution works. Check the README.md in `examples/port_check` for hints.

### Solution 
The answer is in `final_port-check.attack` and you can compare it to your solution.  Run `$ bundle exec gauntlt final_port-check.attack` and you should see the following output:

```
@final @slow
Feature: check to make sure the right ports are open on our server

  Background:                  # port_check/final_port-check.attack:4
    Given "nmap" is installed  # gauntlt-1.0.6/lib/gauntlt/attack_adapters/nmap.rb:4
    And the following profile: # gauntlt-1.0.6/lib/gauntlt/attack_adapters/gauntlt.rb:9
      | name | value     |
      | host | localhost |

  Scenario: Verify server is open on expected ports # port_check/final_port-check.attack:10
    When I launch an "nmap" attack with:            # gauntlt-1.0.6/lib/gauntlt/attack_adapters/nmap.rb:8
      """
      nmap -F <host>
      """
    Then the output should contain:                 # aruba-0.5.3/lib/aruba/cucumber.rb:113
      """
      8008
      """

1 scenario (1 passed)
4 steps (4 passed)
```
