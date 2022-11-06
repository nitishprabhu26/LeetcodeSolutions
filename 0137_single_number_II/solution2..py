# Approach 1: HashSet

# The idea is to convert an input array into hashset and then to compare the tripled sum of the set with the array 
# sum
# 3 * (a + b + c) - (a + a + a + b + b + b + c) = 2c


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2
            
            
nums = [2,2,3,2]
obj = Solution()
print(obj.singleNumber(nums))


# Complexity Analysis:
# Time complexity : O(N) to iterate over the input array.
# Space complexity : O(N) to keep the set of N/3 elements.