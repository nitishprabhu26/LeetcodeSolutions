# Approach 1: Linear search (video)
# https://leetcode.com/problems/missing-number-in-arithmetic-progression/solution/

# Intuition:
# Let's try to find the missing number by linearly scanning the array from start to end. Since we are given that 
# the first and the last numbers cannot be removed, we can use them to get the required difference between each 
# pair of consecutive elements.
# difference = [last value − first value] / number of values
# Once we have the difference we can use it to know what the value at each index is supposed to be. Using the 
# difference as calculated above, and defining initial to be the value at index 0, we have the following:
# index 0 = initial
# index 1 = initial + difference
# index 2 = initial + 2 ⋅ difference
# index 3 = initial + 3 ⋅ difference
# …
# index n = initial + n ⋅ difference

# Algorithm:
# 1.Get the value of difference using first and the last element, 
#   difference = last_value - first_value / number_of_values.
# 2.Start with the first element as expected value; expected = first_element
# 3.Run a loop from the first value to the last while checking if the current value is equal to expected. If it 
#   is, then increase expected by difference for the next iteration.
# 4.Return the first expected value that doesn't match value in the array`.


from typing import List

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Get the difference `difference`.
        difference = (arr[-1] - arr[0]) // n
        
        # The expected element equals the starting element.
        expected = arr[0]
        
        for val in arr:
            # Return the expected value that doesn't match val.
            if val != expected:
                return expected
            
            # Next element will be expected element + `difference`.
            expected += difference
            
        return expected


# OR

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return int((arr[0] + arr[-1])/2 * (len(arr) + 1) - sum(arr))

        
arr = [5,7,11,13]
obj = Solution()
print(obj.missingNumber(arr))


# Complexity Analysis:
# Time complexity : O(n). Where n is the length of array, since in the worst case we iterate over the entire array.
# Space complexity : O(1). Algorithm requires constant space to execute.