#!/usr/bin/ruby
require 'parallel'

def nextr(state)
  a = 1103515245
  c = 12345
  m = 0x7fffffff

  new_state = (state*a+c)&m
  return new_state,(new_state>>16)
end

rands = Array.new 5
(0..4).each do |i|
  rands[i] = gets.chomp.to_i
end

$state = 0
Parallel.each(0x0..0x7, :in_processes => 8) do |upper_bit|
  upper_bit <<= 7*4;
  (0x0000000..0xfffffff).each do |lower_bits|
    state_candidate = upper_bit | lower_bits
    (0..5).each do |i|
      if i == 5
        $state = state_candidate
        puts "0x#{$state.to_s(16)}"
        Parallel::Kill
        exit
      end
      state_candidate,rand_candidate = nextr(state_candidate)
      if rand_candidate != rands[i]
        break;
      end
    end
  end
end

10.times do
  $state, rand = nextr($state)
  puts rand
end
