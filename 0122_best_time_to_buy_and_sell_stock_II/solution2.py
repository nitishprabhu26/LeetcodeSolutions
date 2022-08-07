# Approach 2: Peak Valley Approach
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/

# If we analyze the graph(refer link), we notice that the points of interest are the consecutive valleys and peaks.
# Mathematically speaking: TotalProfit = ∑{i} [ (height(peak{i})) − (height(valley{i})) ]

# The key point is we need to consider every peak immediately following a valley to maximize the profit. In case 
# we skip one of the peaks (trying to obtain more profit), we will end up losing the profit over one of the 
# transactions leading to an overall lesser profit.


import sys
from typing import List

# Using for loop: 
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/ [video]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # running total to which we add the differences
        total = 0
        # the closest valley we are coming from
        valley = sys.maxsize
        # highest peak from that valley
        peak = valley
        
        for i in range(len(prices)):
            # if current value is smaller than our peak, find previous difference
            # when we come down from our peak
            if prices[i] < peak:
                total += peak - valley
                # update valley and peak
                valley = prices[i]
                peak = valley
            else:
                peak = prices[i]
        # when loop finishes, it may not add the last positive difference
        # so we add it manually
        # this occurs when last vallue in the prices array is a peak
        # handles itself when last value in the prices array is a valley
        total += peak - valley
        
        return total
            

# OR
# using while loop

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        
        while i < len(prices) - 1:
            
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            
            maxprofit += peak - valley
            
        return maxprofit
            

prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))


# Complexity Analysis:
# Time complexity: O(n). Single pass.
# Space complexity : O(1). Constant space required.