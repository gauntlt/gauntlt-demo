require 'aruba/cucumber'

Before do
  @aruba_timeout_seconds = 20  # Add more time for sloooooowww networks
end
