# Approach 2: Sliding Window with Array
# Let's implement approach 1 using 26-elements array instead of hashmap:

# Algorithm:
# - Build reference array pCount for string p.
# - Move sliding window along the string s:
#   -   Recompute sliding window array sCount at each step by adding one letter on the right and removing one 
#       letter on the left.
#   -   If sCount == pCount, update the output list.
# - Return output list.


from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        
        p_count, s_count = [0] * 26, [0] * 26
        # build reference array using string p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
            
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter, on the right side of the window
            s_count[ord(s[i]) - ord('a')] += 1
            
            # remove one letter, from the left side of the window
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')] -= 1
            
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