#!/bin/ruby

require 'json'
require 'stringio'


def appendAndDelete(s1, s2, moves)
  if moves >= 2 * [s1.length, s2.length].min + (s1.length - s2.length).abs     
    return true

  elsif s1 == s2 
    return moves % 2 == 0  
        
  else
    first_different_index = compareStringsFindFirstDifference(s1, s2)

    necessary_steps = moves - (s1.length - first_different_index) - (s2.length - first_different_index)

    if necessary_steps % 2 == 0 and necessary_steps >= 0
      return true
    end 
  end
  return false  
end  

  
def compareStringsFindFirstDifference(s1, s2)
  for index in (0...[s1.length, s2.length].max)
    if s1[index] != s2[index]
      return index 
    end
  end
end



  fptr = File.open(ENV['OUTPUT_PATH'], 'w')

  s = gets.to_s.rstrip
  
  t = gets.to_s.rstrip
  
  k = gets.to_i
  
  result = appendAndDelete s, t, k
  if result == true
      result = "Yes"
  else
      result = "No"
  end    
  
  fptr.write result
  fptr.write "\n"
  
  fptr.close()
     