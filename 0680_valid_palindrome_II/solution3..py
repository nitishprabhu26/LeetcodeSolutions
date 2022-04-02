# Approach: Neetcode
# https://youtu.be/JrxRYBwG6EI


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1:r + 1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            
            l += 1
            r -= 1
            
        return True


s = "aba"
obj = Solution()
print(obj.validPalindrome(s))


# Complexity Analysis:
# Time complexity : O(N). Given N as the length of s.
# i.e. O(2.N) = O(N).
# Space complexity : O(N). Extra space is used while creating skipL and skipR.
