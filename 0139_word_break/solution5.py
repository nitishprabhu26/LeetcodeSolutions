# Approach: Neetcode [Dynamic Programing]
# https://youtu.be/Sx9NNgInc3A


from typing import List, Set

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
            
s = "leetcode"
wordDict = ["leet","code"]
obj = Solution()
print(obj.wordBreak(s, wordDict))
