# Time Limit eceeded eror

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit=0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > max_profit:
                    max_profit = prices[j]-prices[i]
        return max_profit

# nums = [7, 6, 4, 3, 1]
nums = [7,1,5,3,6,4]

obj = Solution()
print(obj.maxProfit(nums))