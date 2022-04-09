# Better approach compared to solution2.py

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers)-1
        while(low < high):
            sum = numbers[low] + numbers[high]
            if target == sum:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            else:
                high -= 1


nums = [2, 7, 11, 15]
target = 9
obj = Solution()
print(obj.twoSum(nums, target))


# Complexity analysis:
# Time complexity : O(n). Each of the n elements is visited at most once, thus the time complexity is O(n).
# Space complexity : O(1). We only use two indexes, the space complexity is O(1).
