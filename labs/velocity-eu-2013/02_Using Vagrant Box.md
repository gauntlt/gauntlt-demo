## Using the Vagrant Box

### Download [gauntlt-velocity.box](http://bit.ly/velocity-gauntlt) (~700MB) 
```
wget http://bit.ly/velocity-gauntlt
```

### Install Vagrant
```
http://downloads.vagrantup.com/
```

### Set up a working directory
```
mkdir ~/velocity
cd ~/velocity
vagrant box add velocity /path/where/you/downloaded/gauntlt-velocity.box
vagrant init velocity
```

### Edit VagrantFile and add this line
```
config.vm.network :forwarded_port, guest: 3000, host: 3000
```

### Start up the box
```
vagrant up
vagrant ssh
```
You should be greeted with `vagrant@precise32:~$` if it all worked ok.

### Initialize
Make sure the repo is up-to-date
```
vagrant@precise32:~$ cd gauntlt-demo
vagrant@precise32:~/gauntlt-demo$ git pull
vagrant@precise32:~/gauntlt-demo$ rvm use 1.9.3
vagrant@precise32:~/gauntlt-demo$ bundle install
```
