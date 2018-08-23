

require 'json'
require 'stringio'


def appendAndDelete(s1, s2, moves)
  if s1.length + s2.length - moves < 0
    return true
  end
        
  first_different_index = compareStringsFindFirstDifferentIndex(s1, s2)
  remaining_free_steps = moves - (s1.length - first_different_index) - (s2.length - first_different_index)
  if remaining_free_steps % 2 == 0 and remaining_free_steps >= 0
    return true
  end 
  return false  
end  

  
def compareStringsFindFirstDifferentIndex(s1, s2)
  for index in (0...[s1.length, s2.length].min)
    if s1[index] != s2[index]
      return index
    end
  end
  return [s1.length, s2.length].min + 1
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
