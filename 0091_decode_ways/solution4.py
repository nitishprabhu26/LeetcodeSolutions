# Approach 2: Iterative Approach
# https://leetcode.com/problems/decode-ways/solution/

# We use an array for DP to store the results for subproblems. A cell with index i of the dp array is used to store the number of 
# decode ways for substring of s from index 0 to index i-1.
# We initialize the starting two indices of the dp array. The first two indices of the dp array hold a baton. As we iterate the dp 
# array from left to right this baton which signifies the number of ways of decoding is passed to the next index or not depending 
# on whether the decode is possible.
# dp[i] can get the baton from two other previous indices, either i-1 or i-2. Two previous indices are involved since both single 
# and two digit decodes are possible.

# dp[i] = Number of ways of decoding substring s[:i]. So we might say dp[i] = dp[i-1] + dp[i-2], Only when the decode is possible we 
# add the results of the previous indices. The baton is passed to the next index or not depending on possibility of the decode.


# Algorithm:
# Initialize dp array. dp[0] = 1 to provide the baton to be passed.
# If the first character of the string is zero then no decode is possible hence initialize dp[1] to 0, otherwise the first character 
# is valid to pass on the baton, dp[1] = 1.
# Iterate the dp array starting at index 2. The index i of dp is the i-1 th character of the string s, that is character at index i-1 of s.
# We check if valid single digit decode is possible. This just means the character at index s[i-1] is non-zero. Since we do not have a 
# decoding for zero. If the valid single digit decoding is possible then we add dp[i-1] to dp[i]. Since all the ways up to (i-1)-th 
# character now lead up to i-th character too.
# We check if valid two digit decode is possible. This means the substring s[i-2]s[i-1] is between 10 to 26. If the valid two digit 
# decoding is possible then we add dp[i-2] to dp[i].
# Once we reach the end of the dp array we would have the number of ways of decoding string s.

class Solution:
    def numDecodings(self, s: str) -> int:
        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]
        
        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1
        
        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]
                
        return dp[len(s)]


s = "12"
s = "226"
# s = "11106"
# s = "0"
# s = "06"
s = "11111110111311121111"
obj = Solution()
print(obj.numDecodings(s))


# Complexity Analysis:
# Time Complexity: O(N), where N is length of the string. We iterate the length of dp array which is N+1.
# Space Complexity: O(N). The length of the DP array.