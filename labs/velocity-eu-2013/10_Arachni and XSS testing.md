## XSS Testing with Arachni

### Installation
Check `examples/arachni-xss/README.md` for installation instructions and details.  Arachni is a rubygem and is added to the Gemfile for the gauntlt-demo repo so when you ran bundle it should have been setup.

### Challenge
Start with the `README.md` in `examples/arachni-xss` to get started.  Edit `examples/arachni-xss/challenge_arachni-xss.attack` and get started.

### Solution
You should notice that the final solution uses gauntlt attack aliases.  For arachni, you can use "arachni-simple_xss" and "arachni-full_xss" in your attack.  Currently, gauntlt doesnt expose attack aliases and to see what is available, you can consult [the source](https://github.com/gauntlt/gauntlt/blob/master/lib/gauntlt/attack_aliases/arachni.json).

You should get the following output:
```
@slow @final
Feature: Look for cross site scripting (xss) using arachni against a URL

  Scenario: Using arachni, look for cross site scripting and verify no issues are found # final_arachni-xss.attack:4
    Given "arachni" is installed                                                        # gauntlt-1.0.6/lib/gauntlt/attack_adapters/arachni.rb:1
    And the following profile:                                                          # gauntlt-1.0.6/lib/gauntlt/attack_adapters/gauntlt.rb:9
      | name | value                 |
      | url  | http://localhost:3000 |
    When I launch an "arachni" attack with:                                             # gauntlt-1.0.6/lib/gauntlt/attack_adapters/arachni.rb:5
      """
      arachni --modules=xss --depth=1 --link-count=10 --auto-redundant=2 <url>
      """
    Then the output should contain "0 issues were detected."                            # aruba-0.5.3/lib/aruba/cucumber.rb:97

  Scenario: Using arachni, look for cross site scripting and verify no issues are found # final_arachni-xss.attack:15
    Given "arachni" is installed                                                        # gauntlt-1.0.6/lib/gauntlt/attack_adapters/arachni.rb:1
    And the following profile:                                                          # gauntlt-1.0.6/lib/gauntlt/attack_adapters/gauntlt.rb:9
      | name | value                 |
      | url  | http://localhost:3000 |
Running a arachni-simple_xss attack. This attack has this description:
 This is a scan for cross site scripting (xss) that only runs the base xss module in arachni.  The scan only crawls one level deep which makes it faster.  For more depth, run the gauntlt attack alias 'arachni-simple_xss_with_depth' and specifiy depth.
The arachni-simple_xss attack requires the following to be set in the profile:
 ["<url>"]
    When I launch an "arachni-simple_xss" attack                                        # gauntlt-1.0.6/lib/gauntlt/attack_adapters/arachni.rb:9
    Then the output should contain "0 issues were detected."                            # aruba-0.5.3/lib/aruba/cucumber.rb:97

  Scenario: On the signup page, use arachni to look for cross site scripting and verify no issues are found # final_arachni-xss.attack:23
    Given "arachni" is installed                                                                            # gauntlt-1.0.6/lib/gauntlt/attack_adapters/arachni.rb:1
    And the following profile:                                                                              # gauntlt-1.0.6/lib/gauntlt/attack_adapters/gauntlt.rb:9
      | name | value                        |
      | url  | http://localhost:3000/signup |
Running a arachni-full_xss attack. This attack has this description:
 This is a scan for cross site scripting (xss) that only runs all the xss modules in arachni.  The scan only crawls one level deep, which makes it faster.  For more depth, run the gauntlt attack alias 'arachni-full_xss_with_depth' and specifiy depth.
The arachni-full_xss attack requires the following to be set in the profile:
 ["<url>"]
    When I launch an "arachni-full_xss" attack                                                              # gauntlt-1.0.6/lib/gauntlt/attack_adapters/arachni.rb:9
    Then the output should contain "0 issues were detected."                                                # aruba-0.5.3/lib/aruba/cucumber.rb:97

3 scenarios (3 passed)
12 steps (12 passed)
```