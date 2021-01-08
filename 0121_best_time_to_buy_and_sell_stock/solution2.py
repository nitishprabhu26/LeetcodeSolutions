class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0
        max_profit = 0

# almost same
        # min_price = prices[0]
        # for price in prices[1:]:
        #     max_profit = max(max_profit, price - min_price)
        #     min_price = min(min_price, price)
        # return max_profit


# fastest
        min_price = float('+inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                if prices[i] - min_price > max_profit:
                    max_profit = prices[i] - min_price
        return max_profit


nums = [7,1,5,3,6,4]

obj = Solution()
print(obj.maxProfit(nums))