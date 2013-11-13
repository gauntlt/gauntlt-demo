@reallyslow
Feature: Run all the gauntlt tests inside of cucumber.  This could be chained with any other test framework you have.

  Scenario: Go to the examples directory and run all the attacks
    Given I copy the attack files from the "examples" directory
    When I run `bundle exec gauntlt --tags @final`
    Then the output should not match /(\d+) failed/
    Then the output should match /(\d+) passed/

