# Approach #1: Using 'while', without slice or reversed
# https://youtu.be/hyaKe7Bgst8


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            start, end = i, min(i + k - 1, len(a) - 1)
            while start < end:
                a[start], a[end] = a[end], a[start]
                start += 1
                end -= 1
        return "".join(a)


s = "abcdefg"
k = 2
obj = Solution()
print(obj.reverseStr(s, k))


# Complexity analysis:
# Time complexity : O(N), where N is the size of s.
# Space complexity : O(N), the size of a.

