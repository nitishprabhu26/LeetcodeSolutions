# Approach 3: Keep Track of 3 Maximums Using a Set


from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximums = set()
        for num in nums:
            maximums.add(num)
            if len(maximums) > 3:
                maximums.remove(min(maximums))
        if len(maximums) == 3:
            return min(maximums)
        return max(maximums)


nums = [3,2,1]
nums = [1,2]
obj = Solution()
print(obj.thirdMax(nums))


# Complexity Analysis:

# Time Complexity : O(n).
# For each of the n values in the input Array, we insert it into a Set for a cost of O(1). We then sometimes find 
# and remove the minimum of the Set. Because there are never more than 3 items in the Set, the time complexity of 
# doing this is O(1). In total, we're left with O(n).
# Space Complexity : O(n).
# Because maximums never holds more than 3 items at a time, it is considered to be constant O(1).