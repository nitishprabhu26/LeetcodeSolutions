# In this problem, we are looking for the Greatest Common Divisor of two strings, which for convenience we will 
# consider as the GCD string. To remove ambiguity, here we regard:
# - all strings that divides both str1 and str2 as divisible strings.
# - the longest string among all divisible strings as the GCD string.

# Approach 1: Brute Force
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# OR
# Neetcode: https://youtu.be/i5I_wrbUdzM

# Intuition:
# We start by introducing a brute force method that checks every possible string until we find the GCD string. 
# Before we do that, let's clarify a few things:
# 1.What are the possible candidate strings?
# - Here we make use of prefix strings. If a string base is the GCD string, it must be a prefix of both str1 and 
#   str2. So instead of trying every combination of characters, we instead just take each prefix string of str1 
#   (or str2) and check if it is the GCD string.
# 2.What is the order we should check in? (check img)
# - As the problem indicates that we should look for the greatest common divisor string (longest length), we 
#   should start with the longest possible prefix string, which is the shorter string between str1 and str2 (any 
#   longer string is guaranteed not to be a divisible string since it will be longer than at least one string). If 
#   the current base is not valid, we can check the next shorter prefix by removing the last character from base.
# 3.How to verify if base is the GCD string? (check img)
# - If base is the GCD string, then both str1 and str2 are made up of multiples of base, so we just need to check 
#   if str1 and str2 can be made up of multiple base concatenations. We first check if the length of str is 
#   divisible by the length of base. If so, we multiply base by the number of times the lengths divide and check 
#   if the made-up string equals str.

# Algorithm
# 1. Find the shorter string among str1 and str2, without loss of generality, let it be str1.
# 2. Start with base = str1, and check if both str1 and str2 are made of multiples of base.
#   -   If so, return base.
#   -   Otherwise, we shall try a shorter string by removing the last character from base.
# 3. If we have checked all prefix strings without finding the GCD string, return "".


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def valid(k):
            if len1 % k or len2 % k: 
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base 
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""
        

str1 = "ABABABAB"
str2 = "ABAB"
obj = Solution()
print(obj.gcdOfStrings(str1, str2))


# Complexity Analysis:
# Let m, n be the lengths of the two input strings str1 and str2.
# Time complexity : O(min(m, n)⋅(m + n)) We checked every prefix string base of the shorter string among str1 
# and str2, and verify if both strings are made by multiples of base. There are up to min(m, n) prefix strings to 
# verify and each check involves iterating over the two input strings to check if the current base is the GCD 
# string, which costs O(m + n). Therefore, the overall time complexity is O(min(m, n)⋅(m + n)).
# Space complexity : O(min(m, n)) We need to keep a copy of base in each iteration, which takes O(min(m, n)) space.