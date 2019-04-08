
def happyLadybugs(boardList)
  unless boardList.include? "_"
    return isInitialPositionHappy(boardList)
  end  
  return canBeMadeHappy(boardList) 
end

def canBeMadeHappy(boardList)
  charCounter = Hash.new(0)
  boardList.each_char{|item| charCounter[item] += 1 if item != "_"}
  return charCounter.all? {|key, value| value >= 2 }
end    


def isInitialPositionHappy(boardList)
  return boardList.each_char.slice_when(&:!=).to_a.all? {|item| item.length >= 2}
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
