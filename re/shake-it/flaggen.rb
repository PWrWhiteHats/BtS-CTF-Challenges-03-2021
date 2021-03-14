#!/usr/bin/ruby
require 'pry'

def uber_hash_function x
    x = x.unpack("H*")[0].to_i(16)
    x = x ^ (x >> 3);
    return x.to_s(16)
end

flag = 'BtS-CTF{L1ke_m3rs3nne_Tw15ter_19937}'
hash = uber_hash_function(flag)

puts "Flag: #{flag}"
puts "Hash: #{hash}"