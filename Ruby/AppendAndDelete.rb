
#!/bin/ruby

require 'json'
require 'stringio'


def appendAndDelete(string1, string2, steps)
    chars_to_chop = (string1.length - string2.length).abs
    
    remaining_steps = steps - chars_to_chop
  
    same_length_strings_list = chopSameLength(string1, string2)  
    shortened_str1 = same_length_strings_list[0]
    shortened_str2 = same_length_strings_list[1]
 
    if remaining_steps >= 2 * shortened_str1.length      
      return true
    end
    
    check = checkTwoStringsSame(shortened_str1, shortened_str2)
  
    if check == true 
      if remaining_steps % 2 == 0
        return true
      else
        return false
      end     
        
    else
      first_different_index = compareStringsFindFirstDifference(shortened_str1, shortened_str2)
      num_chars_to_change = shortened_str1.length - first_different_index

        if (remaining_steps - num_chars_to_change *2) % 2 == 0 and remaining_steps - num_chars_to_change * 2 >= 0
        return true
        end 
      end
    return false  
    end
  
  def compareStringsFindFirstDifference(s1, s2)
      for index in (0...s1.length)
        if s1[index] != s2[index]
          return index 
        end
      end  
    end
   
  def checkTwoStringsSame(string1, string2)
    if string1 == string2
      return true
    else  
      return false
    end
    end  
  
  def chopSameLength(string1, string2)
    if string1.length >= string2.length
      shortened_str1 = string1.byteslice(0, string2.length)
      return shortened_str1, string2
    else
      shortened_str2 = string2.byteslice(0, string1.length)
      return string1, shortened_str2 
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
     