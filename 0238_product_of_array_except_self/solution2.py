# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as 
# extra space for space complexity analysis.)

# Approach 2: O(1) space approach
# https://leetcode.com/problems/product-of-array-except-self/solution/ (video)

# OR

# Approach : Neetcode (Similar)
# https://youtu.be/bNvIQI2wAjk

# Algorithm:
# 1. Initialize the empty answer array where for a given index i, answer[i] would contain the product of all the 
#    numbers to the left of i.
# 2. We construct the answer array the same way we constructed the L array in the previous approach. These two 
#    algorithms are exactly the same except that we are trying to save up on space.
# 3. The only change in this approach is that we don't explicitly build the R array from before. Instead, we 
#    simply use a variable to keep track of the running product of elements to the right and we keep updating 
#    the answer array by doing answer[i] = answer[i] * R. For a given index i, answer[i] contains the product of 
#    all the elements to the left and R would contain product of all the elements to the right. We then update R 
#    as R = R * nums[i].


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer


nums = [1,2,3,4]
obj = Solution()
print(obj.productExceptSelf(nums))


# Complexity analysis:
# Time complexity : O(N) where N represents the number of elements in the input array. We use one iteration to 
# construct the array L, one to update the array answer.
# Space complexity : O(1) since don't use any additional array for our computations. The problem statement 
# mentions that using the answer array doesn't add to the space complexity.
