# Using Deque
# https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100


import collections

class Solution:
    def sortedSquares(self, nums: int) -> int:
        answer = collections.deque()
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)


nums = [-4, -1, 0, 3, 10]
obj = Solution()
print(obj.sortedSquares(nums))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(N) if you take output into account and O(1) otherwise.
