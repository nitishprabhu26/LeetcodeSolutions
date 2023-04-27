# Approach 1: Stack
# OR
# Neetcode: https://youtu.be/pRyFZIaKegA


class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in range(0, len(s)):
            if s[i] == '*':
                st.pop()
            else:
                st.append(s[i])

        return ''.join(st)
        

# Neetcode: https://youtu.be/pRyFZIaKegA

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack and stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)


s = "leet**cod*e"
obj = Solution()
print(obj.removeStars(s))


# Complexity Analysis:
# Time complexity : O(n). 
# - We iterate over s and for every character we either push it in the stack or pop the top character from the 
#   stack which takes O(1) time per character. It takes O(n) time for n characters.
# Space complexity : O(n). 
# - The stack used in the solution can grow to a maximum size of n. We would need O(n) space in that case.