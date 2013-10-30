[![build status](https://travis-ci.org/gauntlt/gauntlt-demo.png)](https://travis-ci.org/gauntlt/gauntlt-demo)

# Gauntlt Demo
This is a demo set of attacks that can be used to demo gauntlt and learn how to implement it. Each directory in `./examples` contains a specific type of attack that you might want to run.  Inside each example you will find a README.md which will have a challenge and some hints on how to solve it.  We recommend reading that first and then try to create an attack to solve the challenge.

## Installation
```
$ git clone https://github.com/gauntlt/gauntlt-demo
$ cd ./gauntlt-demo
$ git submodule update --init --recursive
$ bundle
```
## Start targets
This includes railsgoat as a target to pratice against and in the future we will bundle other services.  To start the default services (which is just railsgoat right now) run the following.
```
$ bundle exec start_services
```

You can also run the following to start individual targets which is still just railsgoat but more will be coming:
```
$ bundle exec start_services config/railsgoat.rb
```

## Run a Gauntlt attack
Once you have a target ready, you can start customizing attacks and testing them against the target.
```
$ cd ./examples
$ bundle exec gauntlt hello_world/hello_world.attack
```

