# Approach 1: Check All Substrings
# There's another optimization that we can do. Because the problem wants the longest palindrome, we can start 
# by checking the longest-length substrings and iterate toward the shorter-length substrings. This way, the 
# first time we find a substring that is a palindrome, we can immediately return it as the answer.

# Algorithm:
# 1.Create a helper method check(i, j) to determine if a substring is a palindrome.
#   - To save space, we will not pass the substring itself. Instead, we will pass two indices that represent 
#     the substring in question. The first character will be s[i] and the last character will be s[j - 1].
#   - In this function, declare two pointers left = i and right = j - 1.
#   - While left < right, do the following steps:
#   - If s[left] != s[right], return false.
#   - Otherwise, increment left and decrement right.
#   - If we get through the while loop, return true.
# 2.Use a for loop to iterate a variable 'length' starting from s.length until 1. This variable represents the 
#   length of the substrings we are currently considering.
# 3.Use a for loop to iterate a variable 'start' starting from 0 until and including s.length - length. This 
#   variable represents the starting point of the substring we are currently considering.
# 4.In each inner loop iteration, we are considering the substring starting at start until start + length. Pass 
#   these values into check to see if this substring is a palindrome. If it is, return the substring.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1
            
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start : start + length]

        return ""


# OR
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j
            
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length - 1):
                    return s[start:start + length]

        return ""


s = "babad"
obj = Solution()
print(obj.longestPalindrome(s))
    

# Complexity Analysis:
# Given n as the length of s.
# Time complexity : O(n^3). 
# The two nested for loops iterate O(n^2) times. We check one substring of length n, two substrings of length 
# n - 1, three substrings of length n - 2, and so on.
# There are n substrings of length 1, but we don't check them all since any substring of length 1 is a 
# palindrome, and we will return immediately.
# In each iteration of the while loop, we perform a palindrome check. The cost of this check is linear with n 
# as well, giving us a time complexity of O(n^3).
# - Due to the optimizations of checking the longer length substrings first and exiting the palindrome check 
#   early if we determine that a substring cannot be a palindrome, the practical runtime of this algorithm is 
#   not too bad and better than earlier approach.