# Approach 2: Counting Sort

# Intuition:
# In this approach, we will be sorting the list nums using counting sort. We will store the frequency count for 
# each element in the array elementToCount. After sorting, we will iterate over all of the elements in sorted 
# order, and add even indexed elements to maxSum. After that, we will iterate over the frequency array and use a 
# boolean variable that flips at each element and is only true when we are on an even indexed element.

# Since we are using an array where the element values will be used as indices, we need to ensure that we don't 
# have any negative elements. The elements in the list nums can be negative with a value down to -10^4. Hence, we 
# will add 10^4 to each element so that all the elements convert to a non-negative value. Therefore, our 
# elementToCount array will need to be of size (2 * 10^4) + 1 to account for the full range of possible values in 
# nums.

# Algorithm:
# 1. Iterate over each element in the list nums and for each element we will:
#    a. Add the value K = 10^4
#    b. Increment the frequency corresponding to the above element in the array elementToCount.
# 2. Initialize the answer variable maxSum as 0. Initialize the variable isEvenIndex as true. This variable will 
# be true when we are at an even position and will be false for odd positions. Since we start with index 0 we have 
# initialized it as true.
# 3. Iterate through elementToCount, and for each element:
#    a. Iterate over the instances of element and for each instance:
#       - If the current element is at an even index, then we will add the value of that element to the maxSum. 
#         Since we shifted each element by K when creating the frequency array, the element's value is element - K.
#       - Decrement the frequency of element in elementToCount by 1.
#       - Flip the value of isEvenIndex. This is because if the current position is even the next will be odd and 
#         the variable isEvenIndex should be false in that case and vice versa.
# 4. Return maxSum.


from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        K = 10000
        # Store the frequency of each element
        element_to_count = [0] * (2 * K + 1)
        for element in nums:
            # Add K to element to offset negative values
            element_to_count[element + K] += 1
            
        # Initialize sum to zero
        max_sum = 0
        is_even_index = True
        for element in range(2 * K + 1):
            while element_to_count[element] > 0 :
                # Add element if it is at even index
                if is_even_index:
                    max_sum += element - K
                # Flip the value (one to zero or zero to one)
                is_even_index = not is_even_index
                # Decrement the frequency count
                element_to_count[element] -= 1
        return max_sum
            

nums = [6,2,6,5,1,2]
obj = Solution()
print(obj.arrayPairSum(nums))


# Complexity Analysis:
# Here, N is the number of pairs that will be produced (i.e., the size of list nums is 2⋅N), and K is the range of 
# possible values in nums, which in this problem equals 2·10^4.
# Time complexity: O(N + K)
# First, we iterate over each of the 2N elements in nums in O(2N) time. Then we iterate through the 2K elements in 
# elementToCount during which we'll have another 2N frequency count operations for a total of O(2K + 2N) time. 
# Hence the total time complexity reduces to O(N + K).
# Space complexity: O(K)
# The size of elementToCount needs to be able to accommodate the full range of values in nums, which can be up to 
# 2K. Hence the total space complexity reduces to O(K).