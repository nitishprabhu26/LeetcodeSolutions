# Approach : Neetcode (solution 2)
# https://youtu.be/jJXJ16kPFWg
# Linear time, constant space algorithm.(without using built in isalnum() function)
# ASCII values:
# [0 - 9] -> [48 - 57]
# [A - Z] -> [65 - 90]
# [a - z] -> [97 - 122]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            
            while l < r and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))


inp = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(inp))


# Complexity Analysis:

# Time complexity : O(n), in length n of the string. We traverse over each character at-most once.
# Space complexity : O(1). No extra space required.
