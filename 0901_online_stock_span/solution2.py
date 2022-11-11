# Approach : Neetcode
# https://youtu.be/slYh0ZNEqSw
# OR
# Approach: Monotonic Stack
# https://leetcode.com/problems/online-stock-span/solution/ (explaination)

# A monotonic stack is a stack in which the elements are always sorted. A stack can be monotonically increasing 
# (sorted ascending) or monotonically decreasing (sorted descending). Let's say we have a monotonic decreasing 
# stack. If we want to push x, then all elements that are less than x are popped off first to maintain the sorted 
# property. 
# For example, if we have stack = [623, 532, 125] and we want to push 615, then the 532 and 135 must be popped 
# before the 615 is pushed, otherwise the stack will no longer be sorted.
# https://leetcode.com/problems/online-stock-span/solution/

# To summarize the algorithm: for a given price, say the previous element was y, where y <= price. However many 
# days are included in the span for y must also be included in the span for price. This must be true because if 
# there was an x > price earlier, that x would have also terminated the y since y <= price.

# Algorithm:
# 1.Initialize a stack. The stack will store elements in the format [price, answer] in a monotonic decreasing 
#   manner.
# 2.On each call to next:
# - First set ans = 1 representing the answer.
# - The top of the stack has a format [priceTop, answerTop]. While priceTop <= price, add answerTop to ans and pop 
#   from the stack.
# - Push the current [price, ans] onto the stack.
# - Return ans.


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        
        self.stack.append([price, ans])
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
        

# Complexity Analysis:
# Given n as the number of calls to next,
# Time Complexity of each call to next: O(1). or [O(N) if we need to find span for entire input array elements] 
# Even though there is a while loop in next, that while loop can only run n times total across the entire 
# algorithm. Each element can only be popped off the stack once, and there are up to n elements.
# This is called amortized analysis - if you average out the time it takes for next to run across n calls, it 
# works out to be O(1). If one call to next takes a long time because the while loop runs many times, then the 
# other calls to next won't take as long because their while loops can't run as long.
# Space Complexity: O(n).
# In the worst case scenario for space (when all the stock prices are decreasing), the while loop will never run, 
# which means the stack grows to a size of n.