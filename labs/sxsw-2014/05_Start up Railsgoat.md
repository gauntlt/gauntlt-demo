## Start up our Target


### Start Railsgoat
```
$ cd ./vendor/railsgoat
$ bundle install --binstubs
$ rake db:setup
$ rake server:start
```
You should be able to point your browser at http://localhost:3000 and see railsgoat running.

At the end of the workshop, you can go back to `vendor/railsgoat` and run `$ rake server:stop` to stop railsgoat.
