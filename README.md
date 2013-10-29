![build status](https://travis-ci.org/gauntlt/gauntlt-demo.png)


Gauntlt Demo
============
This is a demo set of attacks that can be used to demo gauntlt and learn how to implement it.

Installation
============

```
$ git clone https://github.com/gauntlt/gauntlt-demo
$ cd ./gauntlt-demo
$ bundle
```
Start targets
=============
This includes railsgoat as a target to pratice against.  To start railsgoat run the following.
```
$ bundle exec start_services
```

Run a Gauntlt attack
====================
```
$ cd ./examples
$ bundle exec gauntlt network.attack
```

