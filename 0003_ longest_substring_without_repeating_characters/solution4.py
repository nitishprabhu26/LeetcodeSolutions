# Approach 3: Sliding Window Optimized
# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/

# Intuition:
# The previous solution requires at most 2n steps. In fact, it could be optimized to require only n steps. 
# Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to 
# its index. 
# Then we can skip the characters immediately when we found a repeated character.

# Algorithm:
# The reason is that if s[j] have a duplicate in the range [i, j) with index j', we don't need to increase i 
# little by little. We can skip all the elements in the range [i, j'] and let i to be j' + 1 directly.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans


inp_str = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(inp_str))


# Complexity Analysis:
# Time complexity : O(n). Index j will iterate n times.
# Space complexity : O(min(m, n)). Same as the previous approach. We need O(k) space for the sliding window, where 
# k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the 
# charset/alphabet m.
