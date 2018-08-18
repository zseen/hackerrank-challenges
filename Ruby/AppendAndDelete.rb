

def appendAndDelete(str1, str2, steps)
    chop_steps = (str1.length - str2.length).abs
    #puts chop_steps
    
    remaining_steps = steps - chop_steps
    #puts remaining_steps
    same_length_strings_list = chopSameLength(str1, str2)  
    
    modified_str1 = same_length_strings_list[0]
    modified_str2 = same_length_strings_list[1]
    
    check = twoStringsSamePossible(modified_str1, modified_str2)
    
  
    if check == true and remaining_steps % 2 == 0
      return true
      end
    if check == true and modified_str1.length * 2 <= remaining_steps
  
   
      return true
      end
    if check == true and  remaining_steps % 2 != 0
  
      return false
      end
  
    if check == false
  
      first_different_index = compareStringsFindFirstDifference(modified_str1, modified_str2)
  
  
        if (remaining_steps - (first_different_index *2)) % 2 == 0
        return true
        else
          return false
        end 
      end
    end
  
   
     
  
  
  
  
  def compareStringsFindFirstDifference(s1, s2)
      for index in (0...s1.length)
        if s1[index] != s2[index]
          return s1.length - index 
        end
      end  
    end
   
  
  
  
  
  def twoStringsSamePossible(str1, str2)
    
    if str1 == str2
      return true
    else  
      return false
    end
    end  
  
  def chopSameLength(str1, str2)
    if str1.length >= str2.length
      shortened_str1 = str1.byteslice(0, str2.length)
      return shortened_str1, str2
    else
      shortened_str2 = str2.byteslice(0, str1.length)
      return str1, shortened_str2 
      end
  end
  =begin
  def makeStringArraysSameLength(initial_string, string_to_get, initial_delete_steps)
      arrays = stringsToArrays(initial_string, string_to_get)
    
      if arrays[0].length > arrays[1].length
          initial_delete_steps.times{arrays[0].pop()}
  
      else
          initial_delete_steps.times{arrays[1].pop()}  
      end    
      return arrays
      end
     
  
  def compareArraysFromBeginningUntilDifferent(array1, array2)
      for index in (0...array1.length)
        if array1[index] != array2[index]
          return array1.length - index 
        end
      end  
    end  
  
  =end
  
  =begin
  i = "uoiauwrebgiwrhgiuawheirhwebvjforidkslweufgrhvjqasw"
  s = "vgftrheydkoslwezxcvdsqjkfhrydjwvogfheksockelsnbkeq"
  steps = 100
  puts i.length
  puts s.length
  =end
  
  i = "zzzzz" 
  s = "zzzzzzz"
  steps = 4
  
  p = appendAndDelete(i, s, steps)
  
  if p == true
    puts "Yes"
  else
    puts "No"
  end
     
  