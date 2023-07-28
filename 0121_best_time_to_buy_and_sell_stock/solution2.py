# Approach 2: One Pass
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

# The points of interest are the peaks and valleys in the given graph. We need to find the largest peak 
# following the smallest valley. We can maintain two variables - minprice and maxprofit corresponding to the 
# smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far 
# respectively.


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit

# OR

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit


# nums = [7, 6, 4, 3, 1]
nums = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(nums))


# Complexity Analysis:
# Time complexity: O(n). Only a single pass is needed.
# Space complexity: O(1). Only two variables are used.