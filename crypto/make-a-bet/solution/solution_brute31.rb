#!/usr/bin/ruby

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

state = catch(:found_it) do
  (0x00000000..0x7fffffff).each do |state_candidate|
    (0..5).each do |i|
      if i == 5
        throw :found_it, state_candidate
      end
      state_candidate,rand_candidate = nextr(state_candidate)
      if rand_candidate != rands[i]
        break;
      end
    end
  end
end

10.times do
  state, rand = nextr(state)
  puts rand
end
