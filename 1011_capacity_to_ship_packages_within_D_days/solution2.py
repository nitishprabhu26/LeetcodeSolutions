# Approach: Binary Search
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/solution/

# Let's think of a faster way by making some observations.
# If we cannot ship the packages in the required days with capacity A, we can never ship the packages with capacity
# less than A. Also, if we can ship the packages in the required days with capacity B, we can always ship it with 
# capacity greater than B. So, in such a case, the optimal capacity lies between [A + 1, B] (both inclusive).
# A scenario like this where our task is to search for an element X from a given range (L, R) where all values 
# smaller than X do not satisfy a certain condition and all values greater than or equal to X satisfy it 
# (or vice-versa), can be solved optimally with a binary search algorithm. In binary search, we repeatedly divide 
# the solution space where the answer could be in half until the range contains just one element.

# Following the above discussion, we set the starting of the range to the largest weight in weights, say maxWeight 
# and set the ending of the range to the sum of the elements of weights, say totalWeight. We define two variables, 
# l = maxWeight and r = totalWeight to indicate the start and end of the range, respectively. Notice that the end 
# of the range r is always a way to ship the elements within the required days.

# If we are able to ship the packages with mid capacity within the required days, we know the answer is at most 
# mid, so we can look for a better answer by moving to the lower half i.e. change r = mid.
# Otherwise, if we are not able to ship the packages with mid capacity, we cannot ship the packages with any 
# capacity less than or equal to mid. So, we move to the upper half of the range by moving l = mid + 1.

# To check whether we can ship all the packages with a given capacity, c, we create a method and define two 
# variables in it, daysNeeded = 1 and currentLoad = 0 which store the total number of days needed to ship all the 
# weights with c ship capacity and to keep track of how much weight has been placed in the ship on a day, 
# respectively. We iterate over all the weights, and for each weight, we place the weight in the ship and increase 
# its load to currentLoad = currentLoad + weight. We keep on placing the weights until currentLoad > c. If 
# currentLoad exceeds capacity, we cannot keep adding weight and need an additional day. So, we increase the days 
# needed to ship the packages by one, i.e., daysNeeded = daysNeeded + 1 we also set currentLoad = weight as this is 
# the current load for the next day. 
# Finally, if daysNeeded <= days, we return true. Otherwise, we return false.

# Algorithm:
# 1. Initialize two integer variables, totalLoad and maxLoad. totalLoad stores the sum of all the elements of 
#    weights and maxLoad stores the largest element of weights.
# 2. Create a method feasible which takes weights, c, days as the parameters and returns true if we can ship all 
#    the packages with c capacity.
# 3. Perform binary search over the range maxLoad to totalLoad.
#    -  Create two variables, l and r, to represent the beginning and end of the range. Set l = maxLoad and 
#       r = totalLoad. We can always ship all the weights within days days with r capacity.
# 4. Then, while l < r:
#    -  Find the midpoint of the range (l, r) in the variable mid = (l + r) / 2.
#    -  Call feasible(weights, mid, days) to see if we can ship all the weights in days days while using mid as 
#       the ship's capacity.
#    -  If we can ship the packages with mid as ship's capacity in less than or equal to days days, we move to 
#       lower half of the range by setting r = mid.
#    -  Otherwise, if we cannot ship the packages with m capacity in required days, we move to upper half of the 
#       range by setting l = mid + 1.
# 5. Return l (or r) when l = r.


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
        l = maxLoad
        r = totalLoad
        
        while l < r:
            mid = (l + r) // 2
            if self.feasible(weights, mid, days):
                r = mid
            else:
                l = mid + 1
        
        return l


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
obj = Solution()
print(obj.shipWithinDays(weights, days))


# Complexity Analysis:
# Time complexity: O(n ⋅ log(500 ⋅ n)) = O(n ⋅ log(n)). 
# - It takes O(n) time to iterate through weights to compute maxLoad and totalLoad.
# - In the binary search algorithm, we divide our range by half every time. So for a range of length R, it performs 
#   O(log(R)) operations. In our case, the range is from maxLoad to totalLoad. As mentioned in the problem 
#   constraints, maxLoad can be 500, so the totalLoad can be n * 500. So, in the worst case, the size of the range 
#   would be (n - 1) * 500 which would require O(log(500n − 500)) = O(log(n)) operations using a binary search 
#   algorithm.
# - To see if we can deliver the packages in the required number of days with a specific capacity, we iterate 
#   through the weights array to see if the current capacity allows us to carry the all the packages in 'days' 
#   days, which needs O(n) time.
# - So it would take O(n⋅log(n)) time in total.
# Space complexity: O(1). We are only defining a few integer variables.