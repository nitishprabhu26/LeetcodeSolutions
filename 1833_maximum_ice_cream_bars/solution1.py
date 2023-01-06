# Approach 1: Sorting (Greedy)
# We are asked to maximize the number of ice creams we buy. Each time we buy any ice cream we will decrease our 
# remaining coins.
# So, the most greedy way to maximize the number of ice creams is to buy the least expensive ice cream. If we buy 
# the least expensive ice cream first, we will be left with more coins to buy more ice cream afterward.

# Algorithm:
# 1. Sort the costs array in ascending order.
# 2. Initialize variables:
#    -  n, length of the input array.
#    =  icecream, integer to denote the index of current ice cream.
# 3. While there is an ice cream left and we have enough coins to buy it:
#    -  Reduce the cost of current ice cream from our coins.
#    -  Increment icecream by 1 to move on to the next ice cream.
# 4. Return icecream, which denotes the number of ice creams we bought.


from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        res = 0
        for cost in costs:
            if coins - cost >= 0:
                coins -= cost
                res += 1
        
        return res


# OR

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Store ice cream costs in increasing order.
        costs.sort()
        n, icecream = len(costs), 0
        
        # Pick ice creams till we can.
        while icecream < n and costs[icecream] <= coins:
            # We can buy this icecream, reduce the cost from the coins. 
            coins -= costs[icecream]
            icecream += 1
        
        return icecream


costs = [1,3,2,4,1]
coins = 7
obj = Solution()
print(obj.maxIceCream(costs, coins))


# Complexity Analysis:
# Here, n is the number of ice cream bars given.
# Time complexity : O(n.logn). We sort the costs array, which will take O(n.logn) time, and then iterate over it, 
# in worst-case which may take O(n) time.
# Thus, overall we take O(n.logn + n) = O(n.logn) time.
# Space complexity : O(logn) or O(n).
# Some extra space is used when we sort the costs array in place. The space complexity of the sorting algorithm 
# depends on the programming language.
# - In Python, the sort() method sorts a list using the Timsort algorithm which has O(n) additional space where n 
#   is the number of the elements.
# - In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity 
#   of O(logn).
# - In JavaScript, the space complexity of sort() is O(logn).