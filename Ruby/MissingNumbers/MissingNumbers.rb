require 'json'
require 'stringio'


def missingNumbers(arrivedList, originalList)
  counterOriginal = Hash.new(0)
  originalList.each{|num| counterOriginal[num] += 1}

  counterArrived = Hash.new(0)
  arrivedList.each{|num| counterArrived[num] += 1}

  result = []
  counterOriginal.each{|key, value| result << key if counterArrived[key] != value }
  return result.sort

end


fptr = File.open(ENV['OUTPUT_PATH'], 'w')
n = gets.to_i
arr = gets.rstrip.split(' ').map(&:to_i)
m = gets.to_i
brr = gets.rstrip.split(' ').map(&:to_i)
result = missingNumbers arr, brr
fptr.write result.join " "
fptr.write "\n"
fptr.close()