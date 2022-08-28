# To put as many apples in the basket as possible, we would want to choose the apple with the smallest weight each 
# time in a greedy manner, until we reach 5000 units of weights or we've taken all apples.

# Approach 1: Sort
# Intuition:
# The most straightforward approach would be sorting the input array arr first. Then we can iterate through it, 
# and count how many apples we can put in the basket until it reaches the weight limit.

# Algorithm:
# - Sort arr, and initialize two integer variables: apples to count the number of apples we have put in the basket 
#   and units to record the current weight of the basket.
# - Iterate through arr until units reaches 5000:
#   -   increment apple by 1;
#   -   increment units by the weight of the current apple.


from typing import List

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        apples = units = 0

        for weight in weight:
            units += weight
            if units > 5000:
                break

            apples += 1
        return apples
        

weight = [900,950,800,1000,700,800]
obj = Solution()
print(obj.maxNumberOfApples(weight))


# Complexity Analysis:
# Time complexity : O(N.logN), where N is the length of the input array. This is determined by the sorting.
# Space complexity : O(1). This is because we do not use additional data structures.