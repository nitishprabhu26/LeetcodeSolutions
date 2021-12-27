# Neetcode (DP)
# https://youtu.be/RyBM56RIWrM

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0]*(n+1)
        offset = 1

        # offset is most significant bit that we have reached so far
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i

            dp[i] = 1 + dp[i-offset]

        return dp


n = 51
obj = Solution()
print(obj.countBits(n))

# Complexity Analysis:
# Time Complexity: O(N).
# Space Complexity: O(1). if result array is not considered.
