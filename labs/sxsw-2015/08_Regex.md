## Regex with Gauntlt

### Challenge
This is not really a networking problem, but we thought this would be a good place to look at regex and output parsing with gauntlt. One popular network scanning tool, nmap, pads its output with spaces so it can make it difficult to parse the output reliably. Start with `challenge_regex.attack` and customize it so that you parse the output using regex.

### Try the challenge
Start with with the `README.md` in `examples/regex` and check the hints section.

### Solution
Check `final_regex.attack` for a working solution answer.

Run `$ bundle exec gauntlt final_regex.attack` and you should get the below output:

```
@final @slow
Feature: check to make sure the right ports are open on our server

  Background:                  # final_regex.attack:4
    Given "nmap" is installed  # gauntlt-1.0.6/lib/gauntlt/attack_adapters/nmap.rb:4
    And the following profile: # gauntlt-1.0.6/lib/gauntlt/attack_adapters/gauntlt.rb:9
      | name | value     |
      | host | localhost |

  Scenario: Verify server is open on expected ports    # final_regex.attack:10
    When I launch an "nmap" attack with:               # gauntlt-1.0.6/lib/gauntlt/attack_adapters/nmap.rb:8
      """
      nmap -F <host>
      """
    Then the output should match:                      # aruba-0.5.3/lib/aruba/cucumber.rb:141
      """
      3000\/tcp\s+open
      """
    Then the output should not match /3001.tcp\s+open/ # aruba-0.5.3/lib/aruba/cucumber.rb:146

1 scenario (1 passed)
5 steps (5 passed)
```
