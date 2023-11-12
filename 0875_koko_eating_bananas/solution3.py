# Approach : Binary Search
# Neetcode: https://youtu.be/U2SozAs9RzA?si=6n7oc68Q-z5JL0t3


import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)
        res = right
        
        while left <= right:
            k = (left + right) // 2            
            hours = 0
            
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        
        return res


piles = [3,6,7,11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(piles, h))


# Complexity Analysis:
# Let n be the length of input array piles and m be the upper bound of elements in piles.
# Time complexity: O(n.log m).
# - The initial search space is from 1 to m, it takes log m comparisons to reduce the search space to 1.
# - For each eating speed middle, we traverse the array and calculate the overall time Koko spends, which takes 
#   O(n) for each traversal.
# - To sum up, the overall time complexity is O(n.log m).
# Space complexity: O(1).
# - For each eating speed middle, we iterate over the array and calculate the total hours Koko spends, which 
#   costs constant space.
# - Therefore, the overall space complexity is O(1).