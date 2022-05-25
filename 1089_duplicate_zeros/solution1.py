# The problem demands the array to be modified in-place. If in-place was not a constraint we might have just 
# copied the elements from a source array to a destination array.

# Solution 1: straightforward solution with O(n) time and O(n) space
# https://leetcode.com/problems/duplicate-zeros/discuss/313225/Different-Python-Solutions


from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        """
        Do not return anything, modify arr in-place instead.
        """
        res = []
        for x in arr:
            res.append(x)
            if x == 0:
                res.append(x)
        for i in range(len(arr)):
            arr[i] = res[i]

        return res[:len(arr)]


arr = [1,0,2,3,0,4,5,0]
arr = [1,2,3]
obj = Solution()
print(obj.duplicateZeros(arr))


# Complexity Analysis:
# Time complexity : O(n)
# Space complexity : O(n)