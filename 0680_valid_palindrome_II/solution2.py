# Approach: Two Pointers
# https://leetcode.com/problems/valid-palindrome-ii/solution/

# Algorithm:
# 1. Create a helper function checkPalindrome that takes a string s, and two pointers i and j. This function 
#    returns a boolean indicating if s.substring(i, j) is a palindrome.
# 2. Initialize two pointers, i = 0 and j = s.length() - 1.
# 3. While i < j, check if the characters at indices i and j match. If they don't, that means we must spend our 
#    deletion on one of these characters. Try both options using checkPalindrome. In other words, return true if 
#    either checkPalindrome(s, i, j -1) or checkPalindrome(s, i + 1, j) is true.
# 4. If we exit the while loop, that means the original string is a palindrome. Since we didn't need to use the 
#    deletion, we should return true.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True


s = "aba"
obj = Solution()
print(obj.validPalindrome(s))


# Complexity Analysis:
# Time complexity : O(N). Given N as the length of s.
# The main while loop we use can iterate up to N / 2 times, since each iteration represents a pair of characters. 
# On any given iteration, we may find a mismatch and call checkPalindrome twice. checkPalindrome can also iterate 
# up to N / 2 times, in the worst case where the first and last character of s do not match.
# Because we are only allowed up to one deletion, the algorithm only considers one mismatch. This means that 
# checkPalindrome will never be called more than twice. As such, we have a time complexity of O(N).
# Space complexity : O(1). The only extra space used is by the two pointers i and j, which can be considered 
# constant relative to the input size.
