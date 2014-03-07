## Using the Repo Only
This is not the recommended method for completing the labs, however you may want to work with gauntlt natively on your machine rather than use virtual box. If you have RVM and homebrew installed, you should be ok.

### Initialize your box
```
$ git clone https://github.com/gauntlt/gauntlt-demo
$ cd ./gauntlt-demo
$ git submodule update --init --recursive
$ bundle
```

### Other tools
Gauntlt is not a package manager and does not install security or testing tools. You will need to install the different tools that you use in the gauntlt attacks you write.  One way to figure out what you need to install is to have a peak at our Travis CI build steps in `.travis.yml`. 
