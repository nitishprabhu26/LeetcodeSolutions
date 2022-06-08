# Clarifying what is meant by a subsequence?
# A subsequence is obtained by deleting some characters of the string. The subsequence is what's left, and doesn't 
# have to be letters that were consecutive in the original string. For example, some of the subsequences of the 
# word computer are:
# computer → cop
# computer → put
# computer → cope
# computer → cut
# computer → e
# computer → computer
# Some of these are also what we call a substring. A substring is where the characters are consecutive in the 
# original string. The subsequences above that are also substrings of computer are 'put', 'e' and 'computer'.

# A substring is a type of subsequence, but a subsequence is not a type of substring.

# Since there are only 2 unique letters that can appear in the string, we know we can always solve the problem 
# with at most 2 steps. i.e.
# Remove all the a's as a single palindromic subsequence.
# Remove all the b's as a single palindromic subsequence.

# This leaves us with only 3 possible answers for any given string: 
# - 0(input string is empty), 
# - 1(input string itself is a palindrome), or 
# - 2(input string is non-empty, and it is not a palindrome, then we would have to firstly remove the a's and then 
#   secondly remove the b's. So if neither of the first 2 cases apply, we can simply return 2). 


# Approach 1: Palindrome Check by Reversing String

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2


# OR One liner
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 - (s == s[::-1]) - (s == "")
        
        
s = "baabb"
obj = Solution()
print(obj.removePalindromeSub(s))


# Complexity Analysis:
# Let n be the length of the input string.
# Time complexity : O(n).
# Reversing a string using the library methods above has a cost of O(n). Checking if 2 strings are equal is also 
# O(n). Therefore, the overall function is O(n).
# Space complexity : O(n).
# Reversing a string creates a second string the same length as the first. Therefore, this algorithm requires 
# O(n) space.