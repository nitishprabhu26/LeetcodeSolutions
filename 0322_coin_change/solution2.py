# Approach #2 (Dynamic programming - Top down) [Accepted]
# https://leetcode.com/problems/coin-change/solution/ (video)

# Algorithm: (Memoization)
# To improve time complexity we should store the solutions of the already calculated subproblems in a table.


import sys
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if (amount < 1): 
            return 0
        # there could be amount+1 different nodes(different remain values in tree) 
        memo = [None] * (amount + 1)

        def helper(remain):
            # cant make a negative amount
            if remain < 0 : return -1
            # dont need to chose a coin again
            if remain == 0: return 0
            
            if memo[remain]:
                return memo[remain]
            
            minCount = sys.maxsize
            for coin in coins:
                count = helper(remain - coin)
                if count == -1: continue
                minCount = min(minCount, count + 1)
            
            memo[remain] = -1 if minCount == sys.maxsize else minCount
            return memo[remain]
            
            
        return helper(amount)


coins = [1,2,5]
amount = 11
obj = Solution()
print(obj.coinChange(coins, amount))


# Complexity Analysis:
# Time Complexity: O(S*n). S is the amount and n is the number of denominations.
# In the worst case the recursive tree of the algorithm has height of S. The algorithm solves only S subproblems 
# because it caches precalculated solutions in a table. Each subproblem is computed with n iterations, one by 
# coin denomination.
# Space Complexity : O(S), where S is the amount of change. We use extra space for the memoization table.

