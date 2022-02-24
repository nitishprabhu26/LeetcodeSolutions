# Approach #1 (Brute force) [Time Limit Exceeded]
# https://leetcode.com/problems/coin-change/solution/ (video)

# Algorithm:
# The algorithm uses backtracking technique to generate all combinations of coin frequencies. It makes a sum of 
# the combinations and returns their minimum or −1 in case there is no acceptable combination.


import sys
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if (amount < 1): 
            return 0

        def helper(coins, remain):
            # cant make a negative amount
            if remain < 0 : return -1
            # dont need to chose a coin again
            if remain == 0: return 0
            
            minCount = sys.maxsize
            for coin in coins:
                count = helper(coins, remain - coin)
                if count == -1: continue
                minCount = min(minCount, count + 1)
            
            return -1 if minCount == sys.maxsize else minCount
            
        return helper(coins, amount)

# OR
# remove coins as a parameter

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if (amount < 1): 
#             return 0
        
#         def helper(remain):
#             # cant make a negative amount
#             if remain < 0 : return -1
#             # dont need to chose a coin again
#             if remain == 0: return 0
            
#             minCount = sys.maxsize
#             for coin in coins:
#                 count = helper(remain - coin)
#                 if count == -1: continue
#                 minCount = min(minCount, count + 1)
            
#             return -1 if minCount == sys.maxsize else minCount
            
            
#         return helper(amount)


coins = [1,2,5]
amount = 11
obj = Solution()
print(obj.coinChange(coins, amount))


# Complexity Analysis:
# Time Complexity: O(S^n). S is the amount and n is the number of denominations.
# In the worst case, complexity is exponential in the number of the coins n. The reason is that every coin 
# denomination c_i could have at most S/(c_i) values. Therefore the number of possible combinations is :
# S^n / ( (c_1) * (c_2) ... (c_n))
# Space Complexity : O(S). In the worst case the maximum depth of recursion (maximum height of the tree) can be
# S, since the solution can take 'amount' coins of denomination 1 (or the lowest denomination amount in the list).

