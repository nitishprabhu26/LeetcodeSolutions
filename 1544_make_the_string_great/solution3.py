# Approach 3: Stack
# https://leetcode.com/problems/make-the-string-great/solution/ (go through overview as well)

# Intuition
# In the previous approaches, we have to make multiple iterations in some cases. Can we solve the problem using 
# just one iteration? The answer is Yes!
# Let's suppose that we find a pair in step i in the iteration, it means that the characters s[i] and s[i - 1] 
# make a pair. We should ignore the s[i] and remove s[i - 1] from the end of the good string. Otherwise, we should 
# add s[i] to the end of the good string.
# Looks familiar? If we store all the previously visited characters in a stack, then the operations on the stack 
# equal the operations on the end of the previous good string! Hence, let's try using a stack to store all the 
# characters we encounter but haven't been removed.

# Algorithm
# 1.Initialize an empty stack 'stack'.
# 2.For each character currChar in s:
# - If currChar pairs with the last character in stack, remove the character at the top of stack.
# - Otherwise, add currChar to stack.
# 3.Once we have finished iterating, return the string concatenated by all the remaining characters in stack.


class Solution:
    def makeGood(self, s: str) -> str:
        # Use stack to store the visited characters.
        stack = []
        
        # Iterate over 's'.
        for curr_char in list(s):
            # If the current character make a pair with the last character in the stack,
            # remove both of them. Otherwise, we add the current character to stack.
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr_char)
        
        # Returns the string concatenated by all characters left in the stack.
        return "".join(stack)
        

s = "leEeetcode"
obj = Solution()
print(obj.makeGood(s))


# Complexity Analysis:
# Let n be the length of the input string s.
# Time complexity: O(n).
# - We only need one iteration over s.
# - At each step, we either remove the last character from stack, or add a character to stack, both of which take 
#   constant time.
# - Therefore, the overall time complexity is O(n).
# Space complexity: O(n). 
# - We use a stack to store all the characters we encounter. Since we only pop characters when finding a pair, in 
#   worst-case scenario, we may have O(n) characters stored in stack. Thus the space complexity is O(n).