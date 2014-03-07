## Hello World
From the `gauntlt-demo` directory, run the following
```
# This should be run from the top-level of `gauntlt-demo`
# and not in labs/sxsw-2014
$ bundle exec gauntlt ./examples/hello_world/hello_world.attack
```

If all succeeded, you should see the resulting output
```
@final
Feature: hello world with gauntlt using the generic command line attack

  Scenario:                                # ./examples/hello_world/hello_world.attack:3
    When I launch a "generic" attack with: # gauntlt-1.0.8/lib/gauntlt/attack_adapters/generic.rb:1
      """
      cat /etc/passwd
      """
    Then the output should contain:        # aruba-0.5.3/lib/aruba/cucumber.rb:113
      """
      root
      """

1 scenario (1 passed)
2 steps (2 passed)
0m0.175s
```

Notice how we used `Feature` and `Scenario` here.  We could have created a `Background` if we had any setup steps that needed to be run before each `Scenario`.
