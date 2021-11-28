# Neetcode (Memoization)
# https://www.youtube.com/watch?v=6aEyTjOwlJU

class Solution:
    def numDecodings(self, s: str) -> int:
        # if length of string is 0, empty string; then return 1
        dp = { len(s) : 1 }
        
        def dfs(i):
            # if i is already been cached or if i is the last position in the string (initially dp ={ len(s) : 1 } )
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)
            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            
            dp[i] = res
            
            return res
            
            
        return dfs(0)

s = "12"
s = "226"
# s = "11106"
# s = "0"
# s = "06"
s = "11111110111311121111"
obj = Solution()
print(obj.numDecodings(s))


# Complexity Analysis:
# Time Complexity: O(N), where N is length of the string. Memoization helps in pruning the recursion tree and hence decoding for an 
# index only once. Thus this solution is linear time complexity.
# Space Complexity: O(N). The dictionary used for memoization would take the space equal to the length of the string. There would be 
# an entry for each index value. The recursion stack would also be equal to the length of the string.