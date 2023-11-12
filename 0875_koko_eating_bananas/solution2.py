# Approach 2: Binary Search
# https://leetcode.com/problems/koko-eating-bananas/editorial/

# Intuition:
# We can use binary search to locate the boundary that separates workable speeds and unworkable speeds, to get 
# the minimum workable speed.
# First, let's set a reasonable upper and lower bound for binary search (to ensure that we do not miss any 
# workable speed). 
# Let the lower bound be 1, the minimum possible eating speed since there is no speed slower than 1. The upper 
# bound will be the maximum eating speed, that is the maximum number of bananas in a pile. For instance, if the 
# piles are [3,5,7,9], then 9 is the maximum number of bananas in a single pile, we can set the upper boundary 
# as 9. 
# Because Koko can eat every pile within 1 hour with a speed of 9, or any other faster speed; 9 is thus 
# guaranteed to be a workable value.


# Algorithm:
# 1. Initialize the two boundaries of the binary search as left = 1, right = max(piles).
# 2. Get the middle value from left and right, that is, middle = (left + right) / 2, this is Koko's eating 
#    speed during this iteration.
# 3. Iterate over the piles and check if Koko can eat all the piles within h hours given this eating speed of 
#    middle.
# 4. If Koko can finish all the piles within h hours, set right equal to middle signifying that all speeds 
#    greater than middle are workable but less desirable by Koko. Otherwise, set left equal to middle + 1 
#    signifying that all speeds less than or equal to middle are not workable.
# 5. Repeat the steps 2, 3, and 4 until the two boundaries overlap, i.e., left = right, which means that we 
#    have found the minimum speed by which Koko could finish eating all the piles within h hours. We can return 
#    either left or right as the answer.


import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right


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