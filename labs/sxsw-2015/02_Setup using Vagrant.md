## Gauntlt 
The workshop uses a Vagrant box for the hands-on portion. Vagrant uses VirtualBox to run a fully contained virtual machine that will let you setup a test lab and get you started using gauntlt. These instructions should work with any host, however OS X and Ubuntu are preferred.

### Download gauntlt-sxsw-2015.box (~700MB) 

This box was made using the gauntlt starter kit. We just made it as a box to save time building all the dependencies.  The gauntlt is available at https://github.com/gauntlt/gauntlt-starter-kit.

```
$ mkdir -p ~/sxsw-2015/box
$ cd ~/sxsw-2015/box
$ wget https://s3.amazonaws.com/gauntlt-sxsw/gauntlt-sxsw-2015.box
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
$ cd ~/sxsw-2015
$ vagrant box add sxsw-2015 ~/sxsw-2015/box/gauntlt-sxsw-2015.box
$ vagrant init sxsw-2015
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
You should be greeted with `vagrant@vagrant-ubuntu-trusty-64:~$` if it worked ok.

### Initialize
Make sure the repo is up-to-date
```
vagrant@vagrant-ubuntu-trusty-64:~$ cd ./gauntlt-demo
vagrant@vagrant-ubuntu-trusty-64:~/gauntlt-demo$ git pull origin master
vagrant@vagrant-ubuntu-trusty-64:~/gauntlt-demo$ bundle install
```
