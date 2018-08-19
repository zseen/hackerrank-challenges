#!/bin/ruby

require 'json'
require 'stringio'

# Complete the findDigits function below.
def findDigits(number_to_divide)
    divisor_count = 0
    
    char_array = number_to_divide.to_s.each_char.map {|ch| ch.to_i}
    char_array.delete_if{|ch| ch == 0}
    
    char_array.each{|digit| divisor_count += 1 if number_to_divide % digit == 0}
    return divisor_count   



end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

t = gets.to_i

t.times do |t_itr|
    number_to_divide = gets.to_i

    result = findDigits number_to_divide

    fptr.write result
    fptr.write "\n"
end

fptr.close()