# Approach 2: Recursion
# https://leetcode.com/problems/make-the-string-great/solution/ (go through overview as well)

# Intuition
# We will implement the same algorithm in approach 1 using recursive method.
# The trick is that each time a recursive function calls itself, it reduces the given problem into subproblems. 
# The recursion call continues until it reaches a point where the subproblem can be solved without further 
# recursion.
# In this problem, once we find a pair that should be deleted, we are actually reducing s into a new string s' 
# which is 2 characters smaller. Then the function calls itself for this smaller subproblem. When we can't find a 
# pair for s, we have reached the base case where the problem can be solved by just returning s without further 
# recursion!

# Algorithm
# Iterate over the input string s and check if a pair exists. - If we find one pair, remove it from s, and 
# start over this step with the remaining string. - Otherwise, return s.


class Solution:
    def makeGood(self, s: str) -> str:
        # If we find a pair in 's', remove this pair from 's'
        # and solve the remaining string recursively.
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                return self.makeGood(s[:i] + s[i + 2:])
        
        # Base case, if we can't find a pair, just return 's'.
        return s
        

s = "leEeetcode"
obj = Solution()
print(obj.makeGood(s))


# Complexity Analysis:
# Let n be the length of the input string s.
# Time complexity: O(n^2).
# - Similarly, it takes O(n) time to iterate through s to find a pair to be removed.
# - In the worst-case scenario, there might be O(n) pairs.
# - In summary, the time complexity is O(n^2).
# Space complexity: O(n^2). 
# - Recall the picture at the begining of this approach, the space complexity is proportional to the maximum depth 
#   of the recursion tree. We have up to n/2 pairs, which equals a recursion tree of depth O(n).
# - Each function call takes O(n) space.
# - Therefore, the space complexity is O(n^2).