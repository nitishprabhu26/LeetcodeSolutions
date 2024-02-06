# Approach 2: Sliding Window
# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
# OR
# Neetcode: https://youtu.be/wiGpQwVHdE0

# Intuition:
# Given a substring with a fixed end index in the string, maintain a HashMap to record the frequency of each 
# character in the current substring. If any character occurs more than once, drop the leftmost characters until 
# there are no duplicate characters.

# Algorithm:
# In the naive approaches, we repeatedly check a substring to see if it has duplicate character. But it is
# unnecessary.
# If a substring s_{ij}, from index i to j−1 is already checked to have no duplicate characters. We only need
# to check if s[j] is already in the substring s_{ij}
# Solution: 
# We use HashSet to store the characters in current window [i, j) (j = i initially). Then we slide
# the index j to the right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already
# in the HashSet.
# At this point, we found the maximum size of substrings without duplicate characters start with index i.
# If we do this for all i, we get our answer.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        left = right = 0
        res = 0

        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res


# OR
# using counter

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res

# OR
# Neetcode: https://youtu.be/wiGpQwVHdE0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r - l + 1)
            
        return res


inp_str = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(inp_str))


# Complexity Analysis:
# Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by i and j.
# Space complexity : O(min(m, n)). Same as the previous approach. We need O(k) space for the sliding window, where 
# k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the 
# charset/alphabet m.
