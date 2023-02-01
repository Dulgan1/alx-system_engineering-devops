#!/usr/bin/env ruby
# parses a logfile and prints [sender],[receiver],[flags]

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
