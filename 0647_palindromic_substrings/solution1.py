# Approach #1: Check All Substrings [Time Limit Exceeded]
# We look at all substrings of the input string and check if they are palindromes.

# Algorithm:
# Each substring is denoted by a pair of variables pointing to the start and end indices of the sub-string.
# A single character substring is denoted by start and end indices being equal in value.

# Checking for a palindrome is simple; we check if the ends of the substring are the same character, going 
# outside-in:
# - If they aren't, this substring is not a palindrome.
# - Else, we continue checking inwards until we get to the middle.

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        def isPalindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
            
            
        for start in range(len(s)):
            for end in range(start, len(s)):
                ans += isPalindrome(s, start, end)
        return ans


s = "abc"
s = "aaa"
obj = Solution()
print(obj.countSubstrings(s))


# Complexity Analysis:
# Time complexity: O(N^3) for input string of length N.
# Space complexity : O(1). We don't need to allocate any extra space since we are repeatedly iterating on the 
# input string itself.
