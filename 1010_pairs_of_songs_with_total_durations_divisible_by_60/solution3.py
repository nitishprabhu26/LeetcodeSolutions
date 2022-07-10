# https://youtu.be/wxqN1HX4Djk

# using array of size 60
# for the array, pairs will be created for the values (1, 59), (2, 58)..(29, 31)

# The case for values 0 and 30 are special cases
# values 60 and 0 will be stored in 0(can pair with each other); 
# and also items with value 30 can pair up with each other.
# eg: if at index 0, the values are [0, 0, 60, 0]
# value at index 0 can pair with next 3 values, similarly value at index 1 can pair with next 2 values
# and lastly value at index 2 can pair with next 1 value i.e. 3 + 2 + 1 = 6 possible pairs
# if len(values) = n+1, then pairs = n(n+1)/2 pairs


from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        def sumOfN(n):
            return (n * (n+1)) // 2
        
        count = [0] * 60
        
        for i in time:
            count[i % 60] += 1
            
        pair = 0
        # for all values between 1 amd 29
        for i in range(1, 30):
            pair += count[i] * count[60-i]
            
        # to find pairs at 0 and 30 indices
        pair += sumOfN(count[0] - 1) + sumOfN(count[30] - 1)
        
        return pair


time = [30, 20, 150, 100, 40]
obj = Solution()
print(obj.numPairsDivisibleBy60(time))


# Complexity Analysis:
# Time complexity: O(n), when n is the length of the input array.
# Space complexity: O(1), because the size of the array remainders is fixed with 60.
