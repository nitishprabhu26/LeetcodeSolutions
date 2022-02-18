# Approach 1: Linear time solution

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1



# without using counter

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         dict = {}
        
#         for i in s:
#             dict[i] = dict.get(i, 0) + 1

#         # find the index
#         for idx, ch in enumerate(s):
#             if dict[ch] == 1:
#                 return idx    
            
#         return -1



s = "leetcode"
obj = Solution()
print(obj.firstUniqChar(s))

# Complexity Analysis:

# Time complexity : O(N) since we go through the string of length N two times.
# Space complexity : O(1) because English alphabet contains 26 letters.