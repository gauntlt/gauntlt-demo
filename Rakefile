Dir['rake_tasks/**/*.rake'].each { |rake| load rake }

task :default => [:gauntlt]

task :kill_targets do
  sh "cd vendor/gruyere/ && ./manual_kill.sh && cd ../../"
end

