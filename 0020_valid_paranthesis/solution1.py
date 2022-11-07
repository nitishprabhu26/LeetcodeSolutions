# Approach 1: Stacks
# https://leetcode.com/problems/valid-parentheses/solution/
# OR
# https://youtu.be/WTzjTskDFMg (Similar)


# Algorithm:
# - Initialize a stack S.
# - Process each bracket of the expression one at a time.
# - If we encounter an opening bracket, we simply push it onto the stack. This means we will process it later, 
#   let us simply move onto the sub-expression ahead.
# - If we encounter a closing bracket, then we check the element on top of the stack. If the element at the top 
#   of the stack is an opening bracket of the same type, then we pop it off the stack and continue processing. 
#   Else, this implies an invalid expression.
# - In the end, if we are left with a stack still having elements, then this implies an invalid expression.


class Solution:
    def isValid(self, s: str) -> bool:
        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings.
        mapping = {")": "(", "}": "{", "]": "["}
        
        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


s = "()"
s = "()[]{}"
obj = Solution()
print(obj.isValid(s))


# Complexity Analysis:
# Time complexity : O(n) because we simply traverse the given string one character at a time and push and pop 
# operations on a stack take O(1) time.
# Space complexity : O(n) as we push all opening brackets onto the stack and in the worst case, we will end up 
# pushing all the brackets onto the stack. e.g. ((((((((((.