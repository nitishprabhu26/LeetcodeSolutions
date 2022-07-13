# Approach: One pass

# Intuition:
# We keep a count of the number of 1's encountered. And reset the count whenever we encounter anything other than 
# 1 (which is 0 for this problem).


from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num == 1:
                # Increment the count of 1's by one.
                count += 1
            else:
                # Find the maximum till now.
                max_count = max(max_count, count)
                # Reset count of 1.
                count = 0
        return max(max_count, count)


# OR
# one liner


# https://www.geeksforgeeks.org/python-map-function/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, ''.join(map(str, nums)).split('0')))


nums = [1,1,0,1,1,1]
obj = Solution()
print(obj.findMaxConsecutiveOnes(nums))


# Complexity Analysis
# Time complexity: O(N), where N is the number of elements in the array.
# Space complexity:  O(1). We do not use any extra space.
