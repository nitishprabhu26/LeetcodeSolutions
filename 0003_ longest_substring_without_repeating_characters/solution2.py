# Approach 2: Sliding Window
# In the naive approaches, we repeatedly check a substring to see if it has duplicate character. But it is unnecessary.
# If a substring s_{ij}, from index i to j−1 is already checked to have no duplicate characters. We only need to check
# if s[j] is already in the substring s_{ij}

# solution: We use HashSet to store the characters in current window [i, j) (j = i initially). Then we slide the index j
# to the right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already in the HashSet.
# At this point, we found the maximum size of substrings without duplicate characters start with index i.
# If we do this for all i, we get our answer.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0]*128
        left = right = 0
        res = 0

        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right-left+1)
            right += 1

        return res


inp_str = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(inp_str))

# Complexity Analysis:
# Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by i and j.
# Space complexity : O(min(m, n)). Same as the previous approach. 