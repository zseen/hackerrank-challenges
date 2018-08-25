
require "test/unit"
require 'json'
require 'stringio'

IS_UNIT_TEST = true

def appendAndDelete(s1, s2, moves)
  if moves > s1.length + s2.length
    return true
  end
        
  first_different_index = compareStringsFindFirstDifferentIndex(s1, s2)
  remaining_free_steps = moves - (s1.length - first_different_index) - (s2.length - first_different_index)
  if remaining_free_steps >= 0 and remaining_free_steps % 2 == 0
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

if IS_UNIT_TEST == false
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


else
  class TestAppendAndDelete < Test::Unit::TestCase

    def test_appendAndDelete_differentLengthStrings_exactNumSteps_notPrefix_true
        assert_true(appendAndDelete('hackerhappy', 'hackerrank', 9))   
    end
    def test_appendAndDelete_sameStrings_emptyDeleteNeeded_true
        assert_true(appendAndDelete("aba", "aba", 7))
    end
    def test_appendAndDelete_differentLengthStringss_Prefix_false
        assert_false(appendAndDelete("abcd", "abcdert", 10))
    end
    def test_appendAndDelete_differentLengthStrings_Prefix_evenSteps_true
        assert_true(appendAndDelete("zzzzz", "zzzzzzz", 4))
    end
    def test_appendAndDelete_differentLengthStrings_firstStringLonger_emptyDeleteNeeded_true
        assert_true(appendAndDelete("aaa", "a", 5))
    end
    def test_appendAndDelete_sameLengthStrings_allCharsDifferent_moreStepsThanSumStringsLength_true
        assert_true(appendAndDelete("abcdef", "fedcba", 15))
    end                    
  end
end        
