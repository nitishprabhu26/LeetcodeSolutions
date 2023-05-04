# Approach 1: Categorize by Sorted String

# Intuition:
# Two strings are anagrams if and only if their sorted strings are equal.

# Algorithm:
# Maintain a map ans : {String -> List} 
# where each key K is a sorted string, and each value is the list of strings from the initial input that when 
# sorted, are equal to K.

# In Java, we will store the key as a string, eg. code. 
# In Python, we will store the key as a hashable tuple, eg. ('c', 'o', 'd', 'e').


import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


# OR
# storing key as string in Python

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[''.join(sorted(s))].append(s)
        return ans.values()


# OR Using regular dictionary

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            k =''.join(sorted(i))

            if k in dict:
                dict[k] += [i]
            else:
                dict[k] = [i]

        return dict.values()


strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
print(obj.groupAnagrams(strs))


# Complexity Analysis:
# Time complexity : O(N.K.logK), where N is the length of strs, and K is the maximum length of a string in strs. 
# The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in 
# O(KlogK) time.
# Space complexity : O(N.K), the total information content stored in ans. 
