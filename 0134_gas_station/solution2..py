# Approach : Neetcode.
# https://youtu.be/lJwbPZGo05A
# Remember: If there exists a solution, it is guaranteed to be unique.(given)


# O(n^2) approach (own code, derieved from neetcode):[Time Limit Exceeded]
# The first idea is to check every single station :
# - Choose the station as starting point.
# - Perform the road trip and check how much gas we have in tank at each station.

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n= len(gas)
        diff = [0] * n
        for i in range(n):
            diff[i] = gas[i] - cost[i]
        
        # Choose each station as starting point.
        for start_station_index in range(n):
            total_tank = 0
            # travel full circle of diff array, from start_station_index
            for diff_val in diff[start_station_index:] + diff[:start_station_index]:
                total_tank +=  diff_val
                # at any point when total_tank becomes negative, 
                # cost is too high and we dont have enough fuel to travel further
                if total_tank < 0:
                    break
            # if we travel full circle, with total_tank >= 0
            if total_tank >= 0:
                return start_station_index
        return -1
            

# O(n) approach:(Neetcode)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # we need enough gas to complete a loop
        # check if atleast a solution exists, (also given that only one solution exixts)
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        # starting position
        res = 0
        
        # https://youtu.be/lJwbPZGo05A?t=604 (dont need to redo the loop once we reach end of loop)
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            
            # if dips below 0, this position doesnt work. so try next position
            if total < 0:
                total = 0
                res = i + 1
        return res


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
obj = Solution()
print(obj.canCompleteCircuit(gas, cost))


# Complexity Analysis:
# Time Complexity: O(N) since there is only one loop over all stations here(O(n) for sum function).
# Space Complexity: O(1) since it's a constant space solution.