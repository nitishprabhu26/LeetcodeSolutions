# Approach 1: Brute Force [Time Limit Exceeded]
# https://leetcode.com/problems/word-break/solution/

# Algorithm:
# The naive approach to solve this problem is to use recursion and backtracking. For finding the solution, we 
# check every possible prefix of that string in the dictionary of words, if it is found in the dictionary, then 
# the recursive function is called for the remaining portion of that string. And, if in some function call it 
# is found that the complete string is in dictionary, then it will return true.

from typing import List, Set

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBreakRecur(s: str, word_dict: Set[str], start: int):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True
            return False

        return wordBreakRecur(s, set(wordDict), 0)
            
s = "leetcode"
wordDict = ["leet","code"]
obj = Solution()
print(obj.wordBreak(s, wordDict))

# Complexity Analysis:
# n is the length of the input string.
# Time Complexity: O(2^n). Given a string of length n, there are n+1 ways to split it into two parts. At each 
# step, we have a choice: to split or not to split. In the worse case, when all choices are to be checked, that 
# results in O(2^n)
# https://leetcode.com/problems/word-break/discuss/169383/The-Time-Complexity-of-The-Brute-Force-Method-Should-Be-O(2n)-and-Prove-It-Below
# Space Complexity: O(n). The depth of the recursion tree can go upto n.