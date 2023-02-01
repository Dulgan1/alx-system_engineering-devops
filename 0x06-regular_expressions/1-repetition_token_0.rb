#!/usr/bin/env ruby
# Matches repetitive tokens

puts ARGV[0].scan(/hbt{2,5}n/).join
