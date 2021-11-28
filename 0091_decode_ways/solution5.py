# Approach 3: Iterative, Constant Space
# https://leetcode.com/problems/decode-ways/solution/

# In Approach 2 we are using an array dp to save the results for future. As we move ahead character by character of the given string, 
# we look back only two steps. For calculating dp[i] we need to know dp[i-1] and dp[i-2] only. Thus, we can easily cut down our O(N)
# space requirement to O(1) by using only two variables to store the last two results.

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
    
        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1: i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current
        
        return one_back


s = "12"
s = "226"
# s = "11106"
# s = "0"
# s = "06"
s = "11111110111311121111"
obj = Solution()
print(obj.numDecodings(s))


# Complexity Analysis:
# Time Complexity: O(N), where N is length of the string. We're essentially doing the same work as what we were in Approach 2, 
# except this time we're throwing away calculation results when we no longer need them.
# Space Complexity: O(1). Instead of a dp array, we're simply using two variables.