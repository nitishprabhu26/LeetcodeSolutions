# Approach 1: Brute Force [Time Limit Exceeded]

# The task is to find out the maximum number of fruits we can collect under this premise.
# To start with, we focus on the mathematical part of the problem, this question equals: 
# Given an array of integers, find the longest subarray that contains at most 2 unique integers. (We will call 
# such subarray a valid subarray for convenience)

# Intuition:
# The steps are simple:
# - Iterate over all subarrays.
# - For each subarray, we count the types of fruits it contains. If the subarray has no more than 2 types of 
#   fruits, meaning it is valid, we take its length to update the maximum length.

# Algorithm:
# 1. Initialize max_picked = 0 to track the maximum number of fruits we can collect.
# 2. Iterate over the left index left of subarrays.
# 3. For every subarray start at index left, iterate over every index right to fix the end of subarray.
# 4. For each subarray (left, right), count the types of fruits it contains.
#    -  If there are no more than 2 types, this subarray is valid, we take its length to update max_picked.
#    -  Otherwise, if the current subarray is invalid, we move on to the next subarray.
# 5. Once we finish the iteration, return max_picked as the maximum number of fruits we can collect.


from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Maximum number of fruits we can pick
        max_picked = 0
        
        # Iterate over all subarrays: left index left, right index right.
        for left in range(len(fruits)):
            for right in range(left, len(fruits)):
                # Use a set to count the type of fruits.
                basket = set()
                
                # Iterate over the current subarray (left, right).
                for current_index in range(left, right + 1):
                    basket.add(fruits[current_index])
                    # little improvement wih this below break statement
                    # if len(basket) > 2:
                    #     break
                    
                # If the number of types of fruits in this subarray (types of fruits) 
                # is no larger than 2, this is a valid subarray, update 'max_picked'.
                if len(basket) <= 2:
                    max_picked = max(max_picked, right - left + 1)
        
        # Return 'max_picked' as the maximum length (maximum number of fruits we can pick).
        return max_picked


fruits = [1,2,3,2,2]
obj = Solution()
print(obj.totalFruit(fruits))


# Complexity Analysis:
# Let n be the length of the input array fruits.
# Time Complexity: O(n^3).
# - We have three nested loops, the first loop for the left index left, the second loop for the right index right, 
#   and the third loop for the index currentIndex between left and right.
# - In each step, we need to add the current fruit to the set basket, which takes constant time.
# - For each subarray, we need to calculate the size of the basket after the iteration, which also takes constant 
#   time.
# Space Complexity: O(n).
# - During the iteration, we need to count the types of fruits in every subarray and store them in a hash set. In 
#   the worst-case scenario, there could be O(n) different types in some subarrays, thus it requires O(n) space 
#   complexity.