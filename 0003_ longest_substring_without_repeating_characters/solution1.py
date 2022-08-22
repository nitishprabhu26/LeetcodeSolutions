# Approach 1: Brute Force [Time limit exceeded]
# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/

# Intuition:
# Check all the substring one by one to see if it has no duplicate character.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        max = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if len(s[i:j+1]) == len(set(s[i:j+1])):
                    if len(s[i:j+1]) > max:
                        max = len(s[i:j+1])
        return max

# OR

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def checkAllUnique(start, end):
            chars = [0]*128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        maximum = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if checkAllUnique(i, j):
                    maximum = max(maximum, j-i+1)
        return maximum


inp_str = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(inp_str))


# Complexity Analysis:
# Time complexity : O(n^3)
# Space complexity : O(min(n, m)). We need O(k) space for checking a substring has no duplicate characters, 
# where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the 
# size of the charset/alphabet m.