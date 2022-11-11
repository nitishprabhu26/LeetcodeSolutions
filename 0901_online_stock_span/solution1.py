# Approach : Brute force

# The brute force approach would be to keep an array of all the stock prices, and then iterate backwards on each 
# call to next until you find a price that is greater than the current price.
# The problem with this approach is that we are potentially looping over the same elements many times. 
# https://leetcode.com/problems/online-stock-span/


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 0
        self.stack.append(price)
        
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] <= price:
                span += 1
            else:
                break
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# Complexity Analysis:
# Given N as the number of calls to next,
# Time Complexity: O(N) OR [O(N^2) if we need to find span for entire input array elements], where N is the length 
# of nums in stack at that point. Since, for each price, we need to loop thorugh all the previous elements.
# Space Complexity: O(N) to store stock array.
