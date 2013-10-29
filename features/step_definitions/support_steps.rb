require 'pathname'
Given /^I copy the attack files from the "(.*?)" directory$/ do |folder|
  Dir.glob("./#{folder}/**/*.attack").each do |path|
  name     = Pathname.new(path).basename.to_s
  contents = File.read(path)
  write_file(name, contents)
  end
end

