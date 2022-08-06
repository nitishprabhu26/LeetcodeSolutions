# Neetcode: Sliding window using 2 pointer concept
# https://youtu.be/1pkOgXD63yU


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # left=buy, right=sell
        l, r = 0, 1
        max_profit = 0

        while(r < len(prices)):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit


# nums = [7, 6, 4, 3, 1]
nums = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(nums))


# Complexity Analysis:
# Time complexity: O(n). Only a single pass is needed.
# Space complexity: O(1). Only few exta variables are used.