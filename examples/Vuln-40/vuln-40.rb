#!/usr/bin/env ruby

require 'rubygems'
require 'watir-webdriver'
require 'headless'

headless = Headless.new
headless.start

browser = Watir::Browser.new
browser.goto 'http://127.0.0.1:8080/WebGoat/login.mvc'

browser.text_field(:name => 'username').set 'guest'
browser.text_field(:name => 'password').set 'guest'

browser.button(:value, "Sign in").click

browser.link(:index => 23).click
browser.link(:index => 25).click

browser.text_field(:name => 'person').set '<img src="images/logos/owasp.jpg"/>'

vulnString = 'Hello, <img src="images/logos/owasp.jpg" />!'

vulnerable = browser.html.include? vulnString

browser.close

headless.destroy

if vulnerable
  puts "Vulnerable"

  exit 1
else
  puts "Safe"

  exit 0
end