require 'gauntlt'

task :gauntlt do
  sh "cd ./vendor/gruyere && ./manual_launch.sh && cd ../.."
  sh "cd ./examples && bundle exec gauntlt --tags @final && cd .."
  sh "cd ./vendor/gruyere && ./manual_kill.sh && cd ../.."
end
