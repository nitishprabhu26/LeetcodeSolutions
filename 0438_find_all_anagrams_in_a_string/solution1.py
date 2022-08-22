# One could allocate array or hashmap with 26 elements and use it as a letter counter in the sliding window.

# Approach 1: Sliding Window with HashMap
# Let's start from the simplest approach: sliding window + two counter hashmaps letter -> its count. The first 
# hashmap is a reference counter pCount for string p, and the second one is a counter sCount for string in the 
# sliding window.
# The idea is to move sliding window along the string s, recompute the second hashmap sCount in a constant time 
# and compare it with the first hashmap pCount. If sCount == pCount, then the string in the sliding window is a 
# permutation of string p, and one could add its start position in the output list.

# Algorithm:
# - Build reference counter pCount for string p.
# - Move sliding window along the string s:
#   -   Recompute sliding window counter sCount at each step by adding one letter on the right and removing one 
#       letter on the left.
#   -   If sCount == pCount, update the output list.
# - Return output list.


from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        
        p_count = Counter(p)
        s_count = Counter()
        
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter, on the right side of the window
            s_count[s[i]] += 1
            
            # remove one letter, from the left side of the window
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output
            

s = "cbaebabacd"
p = "abc"
obj = Solution()
print(obj.findAnagrams(s, p))


# Complexity Analysis:
# Let N_s and N_p be the length of s and p respectively. Let K be the maximum possible number of distinct 
# characters. In this problem, K equals 26 because s and p consist of lowercase English letters.
# Time complexity: O(N_s). We perform one pass along each string when N_s ≥ N_p which costs O(N_s + N_p) time. 
# Since we only perform this step when N_s ≥ N_p the time complexity simplifies to O(N_s).
# Space complexity: O(K). pCount and sCount will contain at most K elements each. Since K is fixed at 26 for this 
# problem, this can be considered as O(1) space.