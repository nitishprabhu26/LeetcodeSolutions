# Neetcode: https://youtu.be/0sWShKIJoo4
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # iterate throght all charecters of strs[0]
        for i in range(len(strs[0])):
            # loop through all the strings of the array
            for s in strs:
                # 1st condition, if strs[0] is not the shortest word amongst all the words
                # else s[i] could be out of bounds
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res



strs = ["flower","flow","flight"]
obj = Solution()
print(obj.longestCommonPrefix(strs))


# Complexity Analysis:
# Time complexity : O(N^2).
# In actual, its O(n.m), where n is length of input array and m is the length of the smallest word
# Space complexity : O(1) since it's a constant space solution.