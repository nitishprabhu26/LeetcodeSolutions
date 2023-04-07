# Approach 1: Brute Force (Time Limit Exceeded)
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/solution/

# Intuition:
# An intuitive approach would be to start with checking ship capacity equal to the largest weight in weights, 
# say w. The ship's capacity cannot be smaller than w. We check if it is possible to ship all the packages within 
# 'days' days, using w as the capacity of the ship. If we are able to ship all the packages within the required 
# days, we have w as our required answer.
# Otherwise, we increment the capacity and try with w + 1. If we are able to ship the packages within the required 
# days now, w + 1 is the answer. Otherwise, we try with ship's capacity as w + 2.
# How long can we go? In the worst case, we might need to choose the capacity of the ship equal to the sum of all 
# the weights in weights and send them all in one day. So, our range starts from the largest weight and goes until 
# the sum of the weights in weights.

# This approach will provide the right answer to all the test cases but will indicate that the time limit has been 
# exceeded. Because, in the worst case, we might need to check the ship's capacity from the largest weight to the 
# sum of all elements in weights. The sum of all elements can reach n * 500, since 500 is the maximum weight we 
# can have as per the problem constraints. So, we might need to check O(n ⋅ 500) different values of ship capacity. 
# For each capacity, we need to iterate over all the elements of weights to check whether we can ship the packages 
# in the required number of days or not, this would require O(n) time. As a result, the total time required would 
# be O(n ⋅ n ⋅ 500) = O(n^2 ⋅ 500) which would lead to TLE.


from typing import List

class Solution:
    def feasible(self, weights, c, days):
        daysNeeded = 1
        currentLoad = 0
        for weight in weights:
            currentLoad += weight
            if currentLoad > c:
                daysNeeded += 1
                currentLoad = weight
                
        return daysNeeded <= days
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        totalLoad, maxLoad = sum(weights), max(weights)
        
        for cap in range(maxLoad, totalLoad + 1):
            if self.feasible(weights, cap, days):
                return cap


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
obj = Solution()
print(obj.shipWithinDays(weights, days))


# Complexity Analysis:
# Time complexity: O(n^2 ⋅ 500), when n is the length of the input array.
# Space complexity: O(1).