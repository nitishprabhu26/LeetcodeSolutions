# Approach 2: Recursion with memoization [Accepted]
# https://leetcode.com/problems/word-break/solution/
# https://youtu.be/3ao_ms-bT9M (JS Solution)

# Algorithm:
# In the previous approach we can see that many subproblems were redundant, i.e we were calling the recursive 
# function multiple times for a particular string. To avoid this we can use memoization method, where an array 
# memo is used to store the result of the subproblems. Now, when the function is called again for a particular 
# string, value will be fetched and returned using the memo array, if its value has been already evaluated.

# With memoization many redundant subproblems are avoided and recursion tree is pruned and thus it reduces the 
# time complexity by a large factor.

from typing import List, Set

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def wordBreakRecur(s: str, word_dict: Set[str], start: int):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        return wordBreakRecur(s, set(wordDict), 0)
            
s = "leetcode"
wordDict = ["leet","code"]
obj = Solution()
print(obj.wordBreak(s, wordDict))


# ============================== EXTRA ==============================

# Advantage of memoization: branches get pruned
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         memo = {}
#         def wordBreakRecur(s: str, word_dict: Set[str], start: int, guess):
#             # printing and shown in output - extra
#             print(guess, start)
#             if start == len(s):
#                 return True
#             if start in memo:
#                 return memo[start]
#             for end in range(start + 1, len(s) + 1):
#                 if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end, s[start:end]):
#                     memo[start] = True
#                     return True
#             memo[start] = False
#             return False
#         return wordBreakRecur(s, set(wordDict), 0, "")

# # input to test:
# s = "aaab"
# wordDict = ["a","aa","aaa"]
# obj = Solution()
# print(obj.wordBreak(s, wordDict))

# without using memo and so no pruning
# output:
# a 1
# a 2
# a 3
# aa 3
# aa 2
# a 3
# aaa 3

# using memo and after pruning
# output:
# a 1
# a 2
# a 3
# aa 3
# aa 2
# aaa 3

# Note: a 3 gets repeated, so its pruned

# =============================== END ===============================


# Complexity Analysis:
# n is the length of the input string.
# Time Complexity: O(n^3). Size of recursion tree can go up to n^2.
# Space Complexity: O(n). The depth of the recursion tree can go upto n.