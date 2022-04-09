from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(numbers)):
                dict[numbers[i]] = i
        for i in range(len(numbers)):
            y = target - numbers[i]
            if y in dict and dict[y] !=i:
                return [i+1, dict[y]+1]


nums = [2, 7, 11, 15]
target = 9
obj = Solution()
print(obj.twoSum(nums, target))


# Complexity analysis:
# Time complexity : O(n). 
# Space complexity : O(n). Extra space used.
