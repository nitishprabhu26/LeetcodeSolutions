# Approach: Bruteforce O(N^2) [Time Limit Exceeded]

class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            newStr = s[:i] + s[i + 1:]

            # we can also use two pointer with while loop 
            if newStr == newStr[::-1]:
                return True
            
        return False


s = "aba"
obj = Solution()
print(obj.validPalindrome(s))


# Complexity Analysis:
# Time complexity : O(N^2). Given N as the length of s.
# newStr == newStr[::-1]: uses O(N) time.
# Space complexity : O(N). Extra space is used for temporary string/substring created.
