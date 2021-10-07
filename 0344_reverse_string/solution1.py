# Using inbuilt reverse function
# Life is short, use Python.

class Solution:
    def reverseString(self, s):
        s.reverse()
        return s


s = ["h","e","l","l","o"]
obj = Solution()
print(obj.reverseString(s))

# Complexity analysis:
# Time complexity : O(n) for a list with n elements.
# Space complexity : O(1).

