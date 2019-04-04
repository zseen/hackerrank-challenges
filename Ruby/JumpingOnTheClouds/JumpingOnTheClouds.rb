#!/bin/ruby

require 'json'
require 'stringio'

# Complete the jumpingOnClouds function below.
INITIAL_ENERGY = 100

def jumpingOnClouds(cloudsTypes, jumpLength)
    actuallyJumpedClouds = []
    (0...cloudsTypes.length).step(jumpLength) { |i| actuallyJumpedClouds.push(cloudsTypes[i]) }
    highJump = actuallyJumpedClouds.count(1)

    lost_energy= highJump*2 + actuallyJumpedClouds.length
    
    return INITIAL_ENERGY - lost_energy

end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

nk = gets.rstrip.split

cloudsNum = nk[0].to_i

jumpLength = nk[1].to_i

cloudsTypes = gets.rstrip.split(' ').map(&:to_i)

result = jumpingOnClouds cloudsTypes, jumpLength

fptr.write result
fptr.write "\ "

fptr.close()