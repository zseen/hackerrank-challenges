#!/bin/ruby

require 'json'
require 'stringio'


def happyLadybugs(field)
  unless field.include? "_"
    initiallyHappy = checkInitialPositionHappy(field)
    return initiallyHappy
  else
    charCounter = Hash.new(0)
    lettersAlphabet = ('A'..'Z').to_a
    lettersAlphabet.each{|item| charCounter[item] += field.count(item) if field.include? item}
    charCounter.each{|key, value| return false if value == 1 } 
  end
  return true   
end


def checkInitialPositionHappy(board)
  for item in board.each_char.slice_when(&:!=).map(&:join)
      if item.length < 2
          return false
      end 
  end
  return true 
end            
        

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

g = gets.to_i

g.times do |g_itr|
n = gets.to_i

b = gets.to_s.rstrip

result = happyLadybugs b
if result == true
  result = "YES"
else
  result = "NO"
end    
fptr.write result
fptr.write "\n"
end

fptr.close()