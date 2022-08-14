# Approach 2: Backtracking
# OR
# Neetcode:https://youtu.be/s9fokUqJ76A

# Intuition and Algorithm:
# Instead of adding '(' or ')' every time as in Approach 1, let's only add them when we know it will remain a 
# valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so 
# far.
# We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if 
# it would not exceed the number of opening brackets.


from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans


# OR
# Neetcode

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid iff open == closed == n
        
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


n = 3
obj = Solution()
print(obj.generateParenthesis(n))


# Complexity Analysis:
# https://leetcode.com/problems/generate-parentheses/solution/