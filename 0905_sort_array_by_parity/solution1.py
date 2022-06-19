# Approach 1: Sort

# Intuition and Algorithm:
# Use a custom comparator when sorting, to sort by parity.

# Sort a List using Lambda Expression- Python
# https://youtu.be/zk15irJMms0


from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # sorts all the numbers in the list, with its updated value
        # i.e. on the modified list, after it goes through the lambda function.
        nums.sort(key = lambda x: x % 2)
        return nums
        

nums = [3,1,2,4]
obj = Solution()
print(obj.sortArrayByParity(nums))


# Complexity Analysis:
# Time Complexity: O(N.logN), where N is the length of nums.
# Space Complexity: O(N) for the sort, depending on the built-in implementation of sort.
