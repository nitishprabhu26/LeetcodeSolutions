# Approach 2: Counting Sort (Greedy)

# Intuition:
# We can further optimize the previous approach by using counting sort.
# A comparison-based sorting method (like heapsort, mergesort, etc.) takes (n.logn) time. However, using counting 
# sort, we can access the elements in sorted order in linear time.

# Counting sort is a sorting technique that is based on the keys between specific ranges. We store each element's 
# frequency in an array and thus using this new array we can access all elements in sorted order.
# The idea behind counting sort is that in an additional array arrayFreq we store the frequency of each element of 
# the input array where arrayFreq's index denotes the element of the input array. Thus, in an indirect way when 
# the indices of arrayFreq are accessed in increasing order, we also access the element of the input array in 
# sorted order.

# Algorithm:
# 1. Initialize variables:
#    -  n, length of the input array.
#    -  m, maximum cost in the costs array.
#    -  icecreams, number of ice creams we picked.
#    -  costsFrequency, to store the frequency of each cost from the costs array.
# 2. Iterate over the costs array and store each element's frequency costsFrequency.
# 3. Iterate over each cost from 1 to m.
#    -  For each cost, if there are ice creams and we have enough coins, then count the maximum number of ice 
#       creams we can pick.
#    -  Reduce the cost of those picked ice creams from our coins.
#    -  Add the count of those picked ice creams in the icecreams variable.
# 4. Return the number of ice creams we picked, i.e. the icecreams variable.


from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n, icecreams = len(costs), 0
        m = max(costs)

        costsFrequency = [0] * (m + 1)
        for cost in costs:
            costsFrequency[cost] += 1

        for cost in range(1, m + 1):
            # No ice cream is present costing 'cost'.
            if not costsFrequency[cost]:
                continue
            # We don't have enough 'coins' to even pick one ice cream.
            if coins < cost:
                break
            
            # Count how many icecreams of 'cost' we can pick with our 'coins'.
            # Either we can pick all ice creams of 'cost' or we will be limited by remaining 'coins'.
            count = min(costsFrequency[cost], coins // cost)
            # We reduce price of picked ice creams from our coins.
            coins -= cost * count
            icecreams += count
            
        return icecreams


costs = [1,3,2,4,1]
coins = 7
obj = Solution()
print(obj.maxIceCream(costs, coins))


# Complexity Analysis:
# Let n be the length of the input array, and m be the maximum element in it.
# Time complexity : O(n+m). 
# - We once iterate on the input array to find the maximum element and then iterate once again to store the 
#   frequencies of its elements in costsFrequency array, thus it takes O(2n) time.
# - We then iterate over the whole costsFrequency array which in the worst case can take O(m) time.
# - Thus, overall we take O(2n + m) = O(n + m) time.
# Space complexity : O(m).
# We use an additional array costsFrequency of size m.