# Approach : Stacks


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                return False
        return stack == []


# OR

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "({[":
                stack.append(i)
            elif stack:
                    if i==")" and stack[-1]=="(":
                        stack.pop()
                    elif i=="}" and stack[-1]=="{":
                        stack.pop()
                    elif i=="]" and stack[-1]=="[":
                        stack.pop()
                    else:
                        return False
            else:
                return False
        return stack==[]


s = "()"
s = "()[]{}"
obj = Solution()
print(obj.isValid(s))


# Complexity Analysis:
# Time complexity : O(n) because we simply traverse the given string one character at a time and push and pop 
# operations on a stack take O(1) time.
# Space complexity : O(n) as we push all opening brackets onto the stack and in the worst case, we will end up 
# pushing all the brackets onto the stack. e.g. ((((((((((.