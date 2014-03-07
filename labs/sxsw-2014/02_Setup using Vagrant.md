## Gauntlt 
The workshop uses a Vagrant box for the hands-on portion. Vagrant uses VirtualBox to run a fully contained virtual machine that will let you setup a test lab and get you started using gauntlt. These instructions should work with any host, however OS X and Ubuntu are preferred.

### Download gauntlt-sxsw.box (~700MB) 
```
$ wget http://bit.ly/rugged-sxsw-box

# you might need to rename the box you downloaded
$ mv rugged-sxsw-box gauntlt-sxsw.box
```

### Install VirtualBox
```
https://www.virtualbox.org/
```

### Install Vagrant
```
http://downloads.vagrantup.com/
```

### Set up a working directory
```
$ mkdir ~/sxsw
$ cd ~/sxsw
$ vagrant box add sxsw /path/where/you/downloaded/gauntlt-sxsw.box
$ vagrant init sxsw
```

### Edit the newly created VagrantFile and add these two lines
```
config.vm.network :forwarded_port, guest: 3000, host: 3000
config.vm.network :forwarded_port, guest: 8008, host: 8008
```

### Start up the box
```
$ vagrant up
$ vagrant ssh
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
