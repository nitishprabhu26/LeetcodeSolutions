# Approach 2: Categorize by Count
# OR
# Neetcode : https://youtu.be/vzdNOK2oB2E

# Intuition:
# Two strings are anagrams if and only if their character counts (respective number of occurrences of each 
# character) are the same.

# Algorithm:
# We can transform each string s into a character count, count, consisting of 26 non-negative integers 
# representing the number of a's, b's, c's, etc. We use these counts as the basis for our hash map.

# In python, the representation will be a tuple of the counts. For example, abbccc will be (1, 2, 3, 0, 0, ..., 0),
# where again there are 26 entries total.


import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # list cannot be key of dict, so we use tuple which is non mutable
            ans[tuple(count)].append(s)
        return ans.values()


strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
print(obj.groupAnagrams(strs))


# Complexity Analysis:
# Time complexity : O(N.K) i.e. O(26.N.K), where N is the length of strs, and K is the maximum length of a 
# string in strs. Counting each string is linear in the size of the string, and we count every string.
# Space complexity : O(N.K), the total information content stored in ans. 
