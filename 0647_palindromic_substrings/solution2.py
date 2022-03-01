# Approach #3: Expand Around Possible Centers
# Multiple palindromes have the same centers. If we choose a center, we can continue to expand around it as long 
# as we can make larger and larger palindromes.

# Algorithm:
# 1. We choose all possible centers for potential palindromes:
#   - Every single character in the string is a center for possible odd-length palindromes
#   - Every pair of consecutive characters in the string is a center for possible even-length palindromes.
# 2. For every center, we can expand around it as long as we get palindromes (i.e. the first and last characters 
#   should match).


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        def countPalindromesAroundCenter(s, lo, hi):
            count = 0
            while lo >= 0 and hi < len(s):
                if s[lo] != s[hi]:
                    break
                hi += 1
                lo -= 1
                count += 1
            return count
        
        
        for i in range(len(s)):
            # odd-length palindromes, single character center
            ans += countPalindromesAroundCenter(s, i, i)
            # even-length palindromes, consecutive characters center
            ans += countPalindromesAroundCenter(s, i, i+1)
        return ans


s = "abc"
s = "aaa"
obj = Solution()
print(obj.countSubstrings(s))


# Complexity Analysis:
# Time complexity: O(N^2) for input string of length N. 
# The total time taken in this approach is dictated by two variables:
# - The number of possible palindromic centers we process.
# - How much time we spend processing each center.
# The number of possible palindromic centers is 2N−1: there are N single character centers and N−1 consecutive 
# character pairs as centers.
# Each center can potentially expand to the length of the string, so time spent on each center is linear on 
# average. Thus total time spent is N⋅(2N−1) ≃ N^2.
# Space complexity : O(1). We don't need to allocate any extra space since we are repeatedly iterating on the 
# input string itself.
