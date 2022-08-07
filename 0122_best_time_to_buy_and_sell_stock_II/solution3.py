# Approach 3: Simple One Pass
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
# OR
# Neetcode: https://youtu.be/3SJ3pUkPQMc

# Algorithm:
# This solution follows the logic used in Approach 2 itself, but with only a slight variation. 
# In this case, instead of looking for every peak following a valley, we can simply go on crawling over the slope 
# and keep on adding the profit obtained from every consecutive transaction. In the end, we will be using the peaks 
# and valleys effectively, but we need not track the costs corresponding to the peaks and valleys along with the 
# maximum profit, but we can directly keep on adding the difference between the consecutive numbers of the array if 
# the second number is larger than the first one; and total sum we obtain will be the maximum profit. 
# This approach will simplify the solution. 


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
            
        return maxprofit

            
prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))


# Complexity Analysis:
# Time complexity: O(n). Single pass.
# Space complexity : O(1). Constant space required.