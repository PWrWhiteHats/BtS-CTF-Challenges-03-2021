#!/usr/bin/ruby

def int2str x
    return [x.to_s(16)].pack("H*")
end

hash = '4a3ad948eb3eceb425b74609f480951c3d5503a3a9f4bef9d713dae9dc14d71e1e155192'.to_i(16)

plain_bits_mask = 7 << (hash.bit_length-3)
while plain_bits_mask > 0
    hash ^= (hash & plain_bits_mask) >> 3
    # print "#{int2str hash}\r" ; sleep 0.03 # Hollywood style
    plain_bits_mask >>= 3
end

puts int2str hash