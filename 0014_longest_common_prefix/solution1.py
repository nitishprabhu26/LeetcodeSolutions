# My approach: Brute force
import sys
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        flag = True
        smallestLength = sys.maxsize
        # finding the smallest length word in the given string array
        for word in strs:
            if len(word) < smallestLength:
                smallestLength = len(word)
        
        index = 0
        # or could use a for loop
        while smallestLength > 0 and flag:
            substr = ""
            for i in range(len(strs)-1):
                if strs[i][index] != strs[i+1][index]:
                    flag = False
                    break
            if not flag:
                break
                
            smallestLength -= 1
            index += 1
            
        return strs[0][0:index]


strs = ["flower","flow","flight"]
obj = Solution()
print(obj.longestCommonPrefix(strs))


# Complexity Analysis:
# Time complexity : O(N^2).
# In actual, its O(n.m), where n is length of input array and m is the length of the smallest word
# Space complexity : O(1) since it's a constant space solution.