## Start up the Railsgoat target
The gauntlt-demo repo adds on [Railsgoat](https://github.com/OWASP/railsgoat) as a target for you test against.  Railsgoat is a vulnerable web application provided by [OWASP](http://owasp.org) and @cktricky.  Please use caution as running a vulnerable web application like Railsgoat and turn on your firewall and make sure you dont have port 3000 open in your firewall.

### Start Railsgoat
```
$ cd vendor/railsgoat
$ bundle install --binstubs
$ rake db:setup
$ rake server:start
```
You should be able to point your browser at http://localhost:3000 and see railsgoat running.

At the end of the workshop, you can go back to `vendor/railsgoat` and run `$ rake server:stop` to stop railsgoat.