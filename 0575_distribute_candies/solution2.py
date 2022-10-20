# Approach 2a: Sorting using inbuilt sort method

# Intuition and Algorithm:
# One way is to sort candyType first, so that we can then count the number of unique candies by comparing adjacent 
# elements in the sorted array. This removes the need to do repeated traversals.

# In-place algorithms overwrite the input to save space, but sometimes this can cause problems. Here are a couple 
# of situations where an in-place algorithm might not be suitable.
# 1.The algorithm needs to run in a multi-threaded environment, without exclusive access to the array. Other 
#   threads might need to read the array too, and might not expect it to be modified.
# 2.Even if there is only a single thread, or the algorithm has exclusive access to the array while running, the 
#   array might need to be reused later or by another thread once the lock has been released.


from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # We start by sorting candyType.
        candyType.sort()
        # The first candy is always unique.
        unique_candies = 1
        # For each candy, starting from the *second* candy...
        for i in range(1, len(candyType)):
            # This candy is unique if it is different to the one
            # immediately before it.
            if candyType[i] != candyType[i - 1]:
                unique_candies += 1
            # Optimization: We should terminate the loop if unique_candies
            # is now at the maxium she can eat.
            if unique_candies == len(candyType) // 2:
                break
        # Like before, the answer is the minimum out of the number of unique candies, and 
        # half the length of the candyType array.
        return min(unique_candies, len(candyType) // 2)


candyType = [1,1,2,2,3,3]
obj = Solution()
print(obj.distributeCandies(candyType))


# Complexity Analysis:
# Let N be the the length of candyType.
# Time Complexity: O(N.log N). We start by sorting the N elements in candyType.
# We then perform a single pass through candyType, performing an O(1) operation at each step: this has a total 
# cost of O(N).
# Space Complexity: Dependent on the sorting algorithm implementation, which is generally between O(1) and O(N).
# Python and Java now use Timsort, which requires O(N) space.
# The heapify variant for Python is O(1), as it uses Heapsort.