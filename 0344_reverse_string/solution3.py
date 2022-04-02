# Approach 2: Two Pointers, Iteration, O(1) Space
# OR
# https://youtu.be/_d0T_2Lk2qA

class Solution:
    def reverseString(self, s):
        start = 0
        end = len(s)-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s


s = ["h", "e", "l", "l", "o"]
obj = Solution()
print(obj.reverseString(s))

# Complexity analysis:
# Time complexity : O(N) to swap N/2 element.
# Space complexity : O(1), it's a constant space solution.
