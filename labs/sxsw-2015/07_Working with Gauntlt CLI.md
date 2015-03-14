## Working with the Gauntlt CLI
As you may have noticed, in the port_check example, gauntlt comes with pre-packaged steps for you to use and doesn't allow you to create new ones (though that may change in the future).  To work with gauntlt, you need to know what attack steps are available for you to use.

Run each of these commands
```
$ bundle exec gauntlt --help
$ bundle exec gauntlt --allsteps
$ bundle exec gauntlt --steps
$ bundle exec gauntlt --list
```

We will be doing a regex example next, so make sure you look through the output of `--allsteps` to be familiar with it.