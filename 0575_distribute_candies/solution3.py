# Approach 2b: Sorting using heapify functions

# If you're using a language that has a built-in heapify function, then you can use this to further optimize the 
# space complexity to O(1). Here is an example of using heapify in Python.


import heapq
from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # We start by heapifying candyType.
        heapq.heapify(candyType)
        # We need to save this now, as we're going to be modifying candyType.
        maximum_candies_allowed = len(candyType) // 2
        unique_candies = 0
        # And now, remove elements off the heap until 
        while candyType and unique_candies < maximum_candies_allowed:
            # Take a candy off, we'll be checking if it is unique.
            candy = heapq.heappop(candyType)
            # If the next candy is not the same as this one, or there isn't a next
            # candy, then this candy must be unique.
            if not candyType or candyType[0] != candy:
                unique_candies += 1
        # Like before, the answer is the minimum out of the number of unique candies, and 
        # half the length of the candyType array.
        return min(unique_candies, maximum_candies_allowed)


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