# We have to determine the maximum profit that can be obtained by making the transactions (no limit on the number 
# of transactions done). For this we need to find out those sets of buying and selling prices which together lead 
# to the maximization of profit.

# Approach 1: Brute Force [Time Limit Exceeded]
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/

# In this case, we simply calculate the profit corresponding to all the possible sets of transactions and find out 
# the maximum profit out of them.


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def calculate(prices, s):
            if s >= len(prices):
                return 0
            
            max_p = 0
            for start in range(s, len(prices)):
                max_profit = 0
                for i in range(start, len(prices)):
                    if prices[start] < prices[i]:
                        profit = calculate(prices, i + 1) + prices[i] - prices[start]
                        if profit > max_profit:
                            max_profit = profit
                    
                if max_profit > max_p:
                    max_p = max_profit
            
            return max_p
        
        return calculate(prices, 0)


prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))


# Complexity Analysis:
# Time complexity: O(n^n). Recursive function is called n^n times.
# Space complexity : O(n). Depth of recursion is n.