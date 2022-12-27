# Approach #1: Direct [Accepted]

# Intuition and Algorithm:
# - We will reverse each block of 2k characters directly.
# - Each block starts at a multiple of 2k: for example, 0, 2k, 4k, 6k, .... One thing to be careful about is we 
#   may not reverse each block if there aren't enough characters.
# - To reverse a block of characters from i to j, we can swap characters in positions i++ and j--.


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)

# OR


# use slicing, instead of reversed

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = a[i:i+k][::-1]
        return "".join(a)


s = "abcdefg"
k = 2
obj = Solution()
print(obj.reverseStr(s, k))


# Complexity analysis:
# Time complexity : O(N), where N is the size of s. We build a helper array, plus reverse about half the 
# characters in s.
# Space complexity : O(N), the size of a.

