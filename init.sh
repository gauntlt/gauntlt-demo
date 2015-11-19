#!/usr/bin/env bash
export SSLYZE_PATH="/home/vagrant/gauntlt-demo/vendor/sslyze/sslyze.py"
export SQLMAP_PATH="/home/vagrant/gauntlt-demo/vendor/sqlmap/sqlmap.py"
export DIRB_WORDLISTS="/home/vagrant/gauntlt-demo/vendor/dirb/wordlists"
cd /home/vagrant/gauntlt-demo
cd vendor/Garmr && sudo python setup.py install && cd ../..
cd vendor && \
  wget http://downloads.sourceforge.net/project/dirb/dirb/2.03/dirb203.tar.gz && \
  tar xvfz dirb203.tar.gz && \
  cd dirb && \
  ./configure && \
  make && \
  sudo cp dirb /usr/local/bin/ && \
  cd ../../

