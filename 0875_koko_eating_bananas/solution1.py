# Approach 1: Brute Force [Time Limit Exceeded]

# Algorithm:
# 1. Start at speed = 1.
# 2. Given the current speed, calculate how many hours Koko needs to eat all of the piles.
#    -  If Koko cannot finish all piles within h hours, increment speed by 1, that is speed = speed + 1 and 
#       start over step 2.
#    -  If Koko can finish all piles within h hours, go to step 3.
# 3. Return the speed as the answer.


import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Start at an eating speed of 1.
        speed = 1

        while True:
            # hour_spent stands for the total hour Koko spends with 
            # the given eating speed.
            hour_spent = 0

            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / speed)
            for pile in piles:
                hour_spent += math.ceil(pile / speed)    

            # Check if Koko can finish all the piles within h hours,
            # If so, return speed. Otherwise, let speed increment by
            # 1 and repeat the previous iteration.                
            if hour_spent <= h:
                return speed
            else:
                speed += 1


piles = [3,6,7,11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(piles, h))


# Complexity Analysis:
# Let n be the length of input array piles and m be the upper bound of elements in piles.
# Time complexity: O(n.m).
# - For each eating speed speed, we iterate over piles and calculate the overall time, which takes O(n) time.
# - Before finding the first workable eating speed, we must try every smaller eating speed. Suppose in the 
#   worst-case scenario (when the answer is m), we have to try every eating speed from 1 to m, that is a total 
#   of m iterations over the array.
# - To sum up, the overall time complexity is O(n.m).
# Space complexity: O(1).
# - For each eating speed speed, we iterate over the array and calculate the total hours Koko spends, which 
#   costs constant space.
# - Therefore, the overall space complexity is O(1).