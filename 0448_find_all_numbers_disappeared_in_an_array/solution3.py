# Approach 2: O(1) Space InPlace Modification Solution

# Intuition:
# All the elements are in the range [1, N]
# Since we are given this information, we can make use of the input array itself to somehow mark visited numbers 
# and then find our missing numbers. Now, we don't want to change the actual data in the array but who's stopping 
# us from changing the magnitude of numbers in the array? That is the basic idea behind this algorithm.
# We will be negating the numbers seen in the array and use the sign of each of the numbers for finding our 
# missing numbers. We will be treating numbers in the array as indices and mark corresponding locations in the 
# array as negative.

# Algorithm:
# 1. Iterate over the input array one element at a time.
# 2. For each element nums[i], mark the element at the corresponding location negative if it's not already marked 
#    so i.e. nums[\; nums[i] \;- 1\;] \times -1nums[nums[i]−1]×−1 .
# 3. Now, loop over numbers from 1 \cdots N1⋯N and for each number check if nums[j] is negative. If it is negative, 
#    that means we've seen this number somewhere in the array.
# 4. Add all the numbers to the resultant array which don't have their corresponding locations marked as negative 
# in the original array.


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Iterate over each of the elements in the original array
        for i in range(len(nums)):
            
            # Treat the value as the new index
            new_index = abs(nums[i]) - 1
            
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative 
            # thus indicating that the number nums[i] has 
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
                
        return result
        

nums = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDisappearedNumbers(nums))


# Complexity Analysis:
# Time Complexity: O(N).
# Space Complexity: O(1) since we are reusing the input array itself as a hash table and the space occupied by the 
# output array doesn't count toward the space complexity of the algorithm.