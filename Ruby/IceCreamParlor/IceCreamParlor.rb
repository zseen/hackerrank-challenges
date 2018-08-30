require "test/unit"

TESTMODE = "OF"


if TESTMODE == "OFF"
  def getPurchaseOption(money, flavorsArr)
    for first_child in (0...((flavorsArr.length) - 1))
      for second_child in (1...((flavorsArr.length)))
        if flavorsArr[first_child] + flavorsArr[second_child] == money and first_child != second_child 
          return first_child + 1, second_child + 1
        end
      end
    end    
  end


  fptr = File.open(ENV['OUTPUT_PATH'], 'w')

  t = gets.to_i

  t.times do |t_itr|
      m = gets.to_i

      n = gets.to_i

      arr = gets.rstrip.split(' ').map(&:to_i)

      result = getPurchaseOption m, arr

      fptr.write result.join " "
      fptr.write "\n"
  end

  fptr.close()




elsif TESTMODE == "ON"

  class TestGetPurchaseOptions < Test::Unit::TestCase
    def getPurchaseOption(money, flavorsArr)
      for first_child in (0...((flavorsArr.length) - 1))
        for second_child in (1...((flavorsArr.length)))
          if flavorsArr[first_child] + flavorsArr[second_child] == money and first_child != second_child 
            return first_child + 1, second_child + 1
          end
        end
      end    
    end

    def test_getPurchaseOptions_noSamePrices_firstChildIsIndex0
      assert_equal([1,4],(getPurchaseOption(4, [1, 4, 5, 3, 2])))
    end

    def test_getPurchaseOptions_twoSamePrices_firstChildIsIndex0
      assert_equal([1,2],(getPurchaseOption(4, [2, 2, 4, 3])))
    end  

    def test_getPurchaseOptions_twoSamePricesMiddle_firstChildIsIndex2
      assert_equal([3,4],(getPurchaseOption(8, [1, 3, 4, 4, 6, 8])))
    end  

    def test_getPurchaseOptions_pricesArrayLengthIs2
      assert_equal([1,2],(getPurchaseOption(3, [1,2])))
    end 
  end  

else 
  puts "I do not know what to run. Please set TESTMODE to 'ON' or 'OFF'."
end  