Before('@slow') do
  @aruba_timeout_seconds = 60
end

Before('@reallyslow') do
  @aruba_timeout_seconds = 300
end
