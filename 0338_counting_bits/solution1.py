# Approach 1: Pop Count
# Intuition:
# Solve the problem for one number at a time.

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        def pop_count(x: int) -> int:
            count = 0
            while x != 0:
                x &= x - 1  # zeroing out the least significant nonzero bit
                count += 1
            return count

        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)

        return ans


n = 51
obj = Solution()
print(obj.countBits(n))

# Complexity Analysis:
# Time Complexity: O(n.logn),For each integer x, in the worst case, we need to perform O(logn) operations,
# since the number of bits in x equals to logx + 1 and all the bits can be equal to 1. However, on average,
# each bit will be set n/2 times, so for each integer x, we will perform log(x)/2 operations, therefore,
# in total, it will cost O(n⋅log(n)/2) operations.
# Space Complexity: O(1). Since the output array does not count towards the space complexity.
