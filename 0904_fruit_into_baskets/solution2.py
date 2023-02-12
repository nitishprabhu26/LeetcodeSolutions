# Approach 2: Optimized Brute Force [Time Limit Exceeded]
# https://leetcode.com/problems/fruit-into-baskets/solution/

# Intuition:
# There are 3 nested loops in approach 1, so as tons of duplicated calculations. Let's try a better method to 
# reduce the workload!

# https://leetcode.com/problems/fruit-into-baskets/solution/
# No inner loop:
# Let's look at the subarrays generated in every iteration.
# For every consecutive subarray, the only difference is that the second subarray has one added fruit, while the 
# rest fruits are the same! Therefore, to get the types of fruits in the second subarray, we just need to add the 
# new fruit to the basket of the first subarray, rather than initializing an empty set and recounting all the 
# fruits again!
# Early stop:
# Take a look at the picture below, suppose the iteration of right stops by here, do we need to continue the 
# iteration of right until it reaches the end of the array?
# No! Since the current window already has more than 2 types of fruits, adding more fruits from the right side 
# does not decrease the number of types, which means that the rest of the windows also have more than 2 types of 
# fruits. Hence, it is time to stop iterating over right, and start over from the next left.
# Therefore, we only need two nested loops, the outer loop for the left index left and the inner loop for the 
# right index right.

# Algorithm:
# 1. Initialize max_picked as 0.
# 2. Iterate over left, the left index of the subarray.
# 3. For every subarray start at index left, we iterate over every index right to fix the end of subarray, and 
#    calculate the types of fruits in this subarray.
#    -  If there are no more than 2 types, this subarray is valid, we update max_picked with the length of this 
#       subarray.
#    -  Otherwise, the current subarray, as well as all the longer subarrays (with the same left index left) are 
#       invalid. Move on to the next left index left + 1.
# 4. Once we finish the iteration, return max_picked as the maximum number of fruits we can collect.


from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Maximum number of fruits we can pick
        max_picked = 0
        
        # Iterate over the left index left of subarrays.
        for left in range(len(fruits)):
            # Empty set to count the type of fruits.
            basket = set()
            right = left
            
            # Iterate over the right index right of subarrays.
            while right < len(fruits):
                # Early stop. If adding this fruit makes 3 types of fruit,
                # we should stop the inner loop.
                if fruits[right] not in basket and len(basket) == 2:
                    break
                
                # Otherwise, update the number of this fruit.
                basket.add(fruits[right])
                right += 1
            
            # Update max_picked
            max_picked = max(max_picked, right - left)
        
        # Return maxPicked as the maximum length of valid subarray.
        # (maximum number of fruits we can pick).
        return max_picked


fruits = [1,2,3,2,2]
obj = Solution()
print(obj.totalFruit(fruits))


# Complexity Analysis:
# Let n be the length of the input array fruits.
# Time Complexity: O(n^2).
# - Compared with approach 1, we only have two nested loops now.
# - In each iteration step, we need to add the current fruit to the hash set basket, which takes constant time.
# Space Complexity: O(1).
# - During the iteration, we need to count the number of types in every possible subarray and update the maximum 
#   length. Since we used the early stop method, thus the types will never exceed 3. Therefore, the space 
#   complexity is O(1).