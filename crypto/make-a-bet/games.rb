require 'socket'
require './resources.rb'

class LibcRand
    def initialize seed
        @m = 0x7fffffff
        @a = 1103515245
        @c = 12345
        @state = seed & @m
    end

    def rand
        @state = (@a * @state + @c) & @m
        return @state>>16
    end
end

def error s
    s.puts 'I didnt understood that.'.red
    sleep 1
    s.puts '> Protocol mismatched <'.red
    raise ArgumentError.new
end

def give_flag s
    s.puts "Nice!"
    sleep 1
    s.puts "Here goes the flag"
    sleep 1
    s.puts "You deserve it"
    sleep 1
    s.puts File.read('flag.txt').green
end

def play_coin s
    s.puts "Now, you'll be betting on the result of the " + "coin tossing".yellow
    s.print "\nheads? or tails? [h/t] > "
    bet = s.gets.chomp
    error s unless bet.validate ['h','t']
    
    s.puts "\nOkay"
    sleep 1
    s.puts 'Tossing coin...'.yellow
    toss = ['h','t'][LibcRand.new(Random.new_seed).rand&1]
    
    s.puts "\nToss: #{toss}\n"

    sleep 1

    if toss == bet
        s.puts "Congratulations! You won!".green
        return true
    else
        s.puts "Sorry, not this time.".red
        return false
    end
    raise Error.new
end

def play_dice s
    s.puts "Now, you'll be betting on the result of the "+'dice throwing'.yellow
    s.print "\nyour number? [1-6] > "
    bet = s.gets.chomp
    error s unless bet.validate ['1','2','3','4','5','6']
    
    s.puts "\nOkay"
    sleep 1
    s.puts 'Throwing dice against the wall...'.yellow
    toss = ['1','2','3','4','5','6'][LibcRand.new(Random.new_seed).rand%6]
    
    s.puts "\nResult: #{toss}\n"

    sleep 1

    if toss == bet
        s.puts "Congratulations! You won!".green
        return true
    else
        s.puts "Sorry, not this time.".red
        return false
    end
    raise Error.new
end

def play_rand s
    s.puts "Now, you'll be betting on the result of the "+'properly seeded old C rand() on old libc'.yellow
    sleep 1
    s.puts "Many lost this game before you"
    sleep 1
    s.puts "Last 5 for example:"
    sleep 1

    prng = LibcRand.new(Random.new_seed)
    prng.rand
    r = Random.new
    s.puts '
    +-----+--------+--------+
    |  i  |   bet  | result |
    +-----+--------+--------+'
    x = 100 + (prng.rand % 895)
    (x+1..x+5).each do |i|
        s.puts "    | #{i.to_s} | #{r.rand(0x7fff).to_s.rjust(6)} | #{prng.rand.to_s.rjust(6)} |"
        sleep 0.2
    end
    s.puts "    +-----+--------+--------+"
    
    s.puts "\nas you can see - many failed before"
    sleep 1

    s.print "\nyour number? [0-32767] > "
    bet = 0
    begin
        bet = s.gets.chomp.to_i
    rescue
        error s
        return false # Unreachable
    end
    
    s.puts "\nOkay"
    sleep 1
    s.puts 'generating true randomness '.yellow
    toss = prng.rand
    
    s.puts "\nResult: #{toss}\n"

    sleep 1

    if toss == bet
        s.puts "Congratulations! You won even this!".green
        return true
    else
        s.puts "Sorry, not this time.".red
        return false
    end
    raise Error.new
end
