# Approach : Neetcode
# https://youtu.be/FzTYfsmtOso


from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()
        for l in range(len(s) - 9):
            cur = s[l : l + 10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
obj = Solution()
print(obj.findRepeatedDnaSequences(s))


# Complexity Analysis:
# Time Complexity: O(N).
# Space Complexity: O(N).