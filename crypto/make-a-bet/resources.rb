
class String
	# colorization
	def colorize(color_code)
	  "\e[#{color_code}m#{self}\e[0m"
	end
  
	def red
	  colorize(31)
	end
  
	def green
	  colorize(32)
	end
  
	def yellow
	  colorize(33)
	end
  
	def blue
	  colorize(34)
	end
  
	def pink
	  colorize(35)
	end
  
	def light_blue
	  colorize(36)
	end

	def lolcol
		$lolcol_color = 0 if $lolcol_color == nil
		tmp = [31, 32, 33, 34, 35 ,36].shuffle
		tmp.delete($lolcol_color)
		$lolcol_color = tmp[0]
		colorize($lolcol_color)
    end
    
    def validate arr
        return arr.include? self
    end
end

$strings = {
    :welcome => '
    Welcome in a MAKE-A-BET challenge!
    Here, you will face with your lack of luck
    and hopefully prove that, professionals
    dont need such a thing.
    Are You ready? [y/n]
> ',
    :notaccepted => "Sorry to hear that :(\nBye!",
    :notunderstood => "Congratulations, you've lost even, before begining.",
    :challengeaccepted => "Glad to hear that!\nGet ready!"
}