# Approach #2: Linear Scan [Accepted]
# OR
# https://youtu.be/MGPHPadxhtQ


# Intuition and Algorithm:
# We can amend our Approach #1 to calculate the answer on the fly. Instead of storing groups, we will remember 
# only prev = groups[-2] and cur = groups[-1]. Then, the answer is the sum of min(prev, cur) over each different 
# final (prev, cur) we see.


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)


s = "00110011"
obj = Solution()
print(obj.countBinarySubstrings(s))


# Complexity Analysis:
# Time complexity : O(N), where N is the length of s. Every loop is through O(N) items with O(1) work inside the 
# for-block.
# Space complexity : O(1), the space used by prev, cur, and ans.
