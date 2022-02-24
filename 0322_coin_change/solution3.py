# Approach 3:(Dynamic programming - Bottom up) [Accepted]
# OR
# Neetcode : https://youtu.be/H9bfqozjoqs


from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1 

# OR
# Neetcode:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # eg: if a = 7, coin = 4
                    #     dp[7] = 1 + dp[3]
                    dp[a] = min(dp[a], dp[a - c] + 1)
                    
        return dp[amount] if dp[amount] != (amount + 1) else -1 

# Time: O(amount * len(coins)).
# Space: O(amount).


coins = [1,2,5]
amount = 11
obj = Solution()
print(obj.coinChange(coins, amount))


# Complexity Analysis:
# Time Complexity: O(S*n). On each step the algorithm finds the next F(i) in n iterations, where 1 <= i <= S. 
# Therefore in total the iterations are S ∗ n. (two for loop)
# Space Complexity : O(S). We use extra space for the memoization table.
