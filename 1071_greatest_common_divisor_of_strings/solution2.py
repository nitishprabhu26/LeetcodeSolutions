# Approach 2: Greatest Common Divisor
# https://leetcode.com/problems/greatest-common-divisor-of-strings/solution/
# OR
# https://youtu.be/-nDN4idlP10

# Intuition:
# Here is a more mathmatical approach to the problem.
# https://leetcode.com/problems/greatest-common-divisor-of-strings/solution/

# Algorithm
# 1. Check if the concatenations of str1 and str2 in different orders are the same.
#   -   If not, return "".
# 2. Get the GCD gcdLength of the two lengths of str1 and str2.
# 3. Return the prefix string with a length of gcdLength of either str1 or str2 as the answer.


from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
        

str1 = "ABABABAB"
str2 = "ABAB"
obj = Solution()
print(obj.gcdOfStrings(str1, str2))


# Complexity Analysis:
# Let m, n be the lengths of the two input strings str1 and str2.
# Time complexity : O(m + n).
# We need to compare the two concatenations of length O(m + n), it takes O(m + n) time. We calculate the GCD using 
# binary Euclidean algorithm, it takes log(m ⋅ n) time.
# To sum up, the overall time complexity is O(m + n).
# Space complexity : O(m + n) We need to compare the two concatenations of length O(m + n).