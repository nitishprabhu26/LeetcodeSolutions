# Approach 1: One pass.

# Intuition:
# The first idea is to check every single station :
# - Choose the station as starting point.
# - Perform the road trip and check how much gas we have in tank at each station.
# That means O(N^2) time complexity, and for sure one could do better.

# Let's notice two things.
# - It's impossible to perform the road trip if sum(gas) < sum(cost). In this situation the answer is -1.
# One could compute total amount of gas in the tank total_tank = sum(gas) - sum(cost) during the round trip, and 
# then return -1 if total_tank < 0.
# - It's impossible to start at a station i if gas[i] - cost[i] < 0, because then there is not enough gas in the 
# tank to travel to i + 1 station.
# The second fact could be generalized. Let's introduce curr_tank variable to track the current amount of gas in 
# the tank. If at some station curr_tank is less than 0, that means that one couldn't reach this station.
# Next step is to mark this station as a new starting point, and reset curr_tank to zero since one starts with no 
# gas in the tank.

# Algorithm:
# 1.Initiate total_tank and curr_tank as zero, and choose station 0 as a starting station.
# 2.Iterate over all stations :
# - Update total_tank and curr_tank at each step, by adding gas[i] and subtracting cost[i].
# - If curr_tank < 0 at i + 1 station, make i + 1 station a new starting point and reset curr_tank = 0 to start 
#   with an empty tank.
# 3.Return -1 if total_tank < 0 and starting station otherwise.


from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1
            

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
obj = Solution()
print(obj.canCompleteCircuit(gas, cost))


# Complexity Analysis:
# Time Complexity: O(N) since there is only one loop over all stations here.
# Space Complexity: O(1) since it's a constant space solution.