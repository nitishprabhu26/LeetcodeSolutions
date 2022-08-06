# Approach 1: Brute Force [Time Limit Exceeded]


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit


# nums = [7, 6, 4, 3, 1]
nums = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(nums))


# Complexity Analysis:
# Time complexity: O(n^2). Loop runs {n.(n-1)}/{2} times.
# Space complexity: O(1). Only two variables - maxprofit and profit are used.