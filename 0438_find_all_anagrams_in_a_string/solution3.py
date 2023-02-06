# Approach Neetcode : https://youtu.be/G8xtZy0fDKg
# (Similar to approach 1)


from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            
        res = [0] if pCount == sCount else []
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            
            l += 1
            if sCount == pCount:
                res.append(l)
        
        return res
            

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