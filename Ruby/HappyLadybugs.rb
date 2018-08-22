
def happyLadybugs(boardList)
  unless boardList.include? "_"
    return isInitialPositionHappy(boardList)
    
  else
    charCounter = Hash.new(0)
    boardList.each_char{|item| charCounter[item] += 1 if item != "_"}
    charCounter.each{|key, value| return false if value == 1 } 
  end
  return true   
end


def isInitialPositionHappy(boardList)
  for item in boardList.each_char.slice_when(&:!=).map(&:join)
      if item.length < 2
          return false
      end 
  end
  return true 
end   

b = "RBY_YBR"
x = happyLadybugs("AABBCCCCCDD")
puts x
        
=begin
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
=end