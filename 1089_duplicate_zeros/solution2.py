# Solution 2: 
# create a map: i <--> i + # zeros in arr[:i]
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
        n = len(arr)
        zeros = 0
        i = 0
        mp = dict()
        while i + zeros < n:
            mp[i+zeros] = i
            if arr[i] == 0:
                zeros += 1
                mp[i+zeros] = i
            i += 1
        for i in range(n - 1, -1, -1):
            arr[i] = arr[mp[i]]
        return arr


arr = [1,0,2,3,0,4,5,0]
arr = [1,2,3]
obj = Solution()
print(obj.duplicateZeros(arr))


# Complexity Analysis:
# Time complexity : O(n)
# Space complexity : O(n)