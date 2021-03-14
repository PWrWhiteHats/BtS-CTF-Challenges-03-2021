#!/usr/bin/ruby

a = 1103515245
c = 12345
m = 0x7fffffff

upper_16_bits = gets.chomp.to_i # First value
rand2 = gets.chomp.to_i # second value
rand3 = gets.chomp.to_i # second value

state = 0 # State of the LCG PRNG

# brute force lower 16 bits of PRNG state
(0x0000..0xffff).each do |lower_candidate|
    state_candidate = (upper_16_bits<<16) | lower_candidate
    rand2_candidate = ((state_candidate*a + c)&m)>>16
    if rand2_candidate == rand2
        # found it!
        state = state_candidate
        # verify rand 3
        state = (a * state + c) & m
        if (state>>16) == rand3
            # really found it
            break
        end
    end
end

state = (a * state + c) & m # skip rand3 duplicate
# generate next numbers
5.times do
    state = (a * state + c) & m
    puts (state>>16).to_s
end