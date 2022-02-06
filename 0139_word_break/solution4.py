# Approach 4: Using Dynamic Programming
# https://leetcode.com/problems/word-break/solution/

# Algorithm:

# The intuition behind this approach is that the given problem (s) can be divided into subproblems s1 and s2. 
# If these subproblems individually satisfy the required conditions, the complete problem, 's' also satisfies 
# the same. 
# e.g. "catsanddog" can be split into two substrings "catsand", "dog". The subproblem "catsand" can be 
# further divided into "cats","and", which individually are a part of the dictionary making "catsand" satisfy 
# the condition. Going further backwards, "catsand", "dog" also satisfy the required criteria individually 
# leading to the complete string "catsanddog" also to satisfy the criteria.

# Now, we'll move onto the process of dp array formation. We make use of dp array of size (n+1), where n is the 
# length of the given string. We also use two index pointers i and j, where i refers to the length of the 
# substring (s) considered currently starting from the beginning, and j refers to the index partitioning the 
# current substring (s) into smaller substrings s1(0,j) and s2(j+1,i). To fill in the dp array, we initialize 
# the element dp[0] as true, since the null string is always present in the dictionary, and the rest of the 
# elements of dp as false. We consider substrings of all possible lengths starting from the beginning by 
# making use of index i. For every such substring, we partition the string into two further substrings 
# s11 and s22 in all possible ways using the index j (Note that the i now refers to the ending index of s22). 
# Now, to fill in the entry dp[i], we check if the dp[j] contains true, i.e. if the substring s11 fulfills the 
# required criteria. If so, we further check if s22 is present in the dictionary. If both the strings fulfill 
# the criteria, we make dp[i] as true, otherwise as false.

from typing import List, Set

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]
            
s = "leetcode"
wordDict = ["leet","code"]
obj = Solution()
print(obj.wordBreak(s, wordDict))

# Complexity Analysis:
# n is the length of the input string.
# Time Complexity: O(n^3). There are two nested loops, and substring computation at each iteration. Overall 
# that results in O(n^3) time complexity.
# Space Complexity: O(n). Length of p array is n+1.