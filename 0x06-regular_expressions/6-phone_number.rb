#!usr/bin/env ruby
# Matches for 10 diguts phone number

puts ARGV[0].scan(/^[0-9]{10}$/).join
