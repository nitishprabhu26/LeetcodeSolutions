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
# break the inner loop when a substring is not unique [Accepted]
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        result = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if len(s[i:j+1]) == len(set(s[i:j+1])):
                    result = max(result, len(s[i:j+1]))
                else:
                    break
        return result

# OR
# getting rid of the empty string check [Accepted]
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(s[i:j+1]) == len(set(s[i:j+1])):
                    result = max(result, len(s[i:j+1]))
                else:
                    break
        return result


inp_str = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(inp_str))


# Complexity Analysis:
# Time complexity : O(n^3).
# Space complexity : O(n).