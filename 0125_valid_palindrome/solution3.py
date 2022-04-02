# Approach : Neetcode (solution 1)
# https://youtu.be/jJXJ16kPFWg


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


inp = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(inp))


# Complexity Analysis:

# Time complexity : O(n), in length n of the string. We traverse over each character at-most once.
# Space complexity : O(n) extra space required.
