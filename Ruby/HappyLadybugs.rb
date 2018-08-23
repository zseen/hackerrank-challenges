
def happyLadybugs(boardList)
  unless boardList.include? "_"
    return isInitialPositionHappy(boardList)
  end  
  return isHappy(boardList) 
end

def isHappy(boardList)
  charCounter = Hash.new(0)
  boardList.each_char{|item| charCounter[item] += 1 if item != "_"}
  if charCounter.any? {|key, value| value == 1 } == true
    return false
  end
  return true
end    


def isInitialPositionHappy(boardList)
  for item in boardList.each_char.slice_when(&:!=).to_a
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
