# Approach 1: One Pass

# Intuition:
# If we walk along the mountain from left to right, we have to move strictly up, then strictly down.

# Algorithm:
# Let's walk up from left to right until we can't: that has to be the peak. We should ensure the peak is not the 
# first or last element. Then, we walk down. If we reach the end, the array is valid, otherwise its not.


from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0
        
        # walk up
        while i < N - 1 and arr[i] < arr[i + 1]:
            i += 1
            
        # peak can't be first or last
        if i == 0 or i == N - 1:
            return False
        
        # walk down
        while i < N - 1 and arr[i] > arr[i+1]:
            i += 1

        return i == N - 1


arr = [0,3,2,1]
obj = Solution()
print(obj.validMountainArray(arr))


# Complexity Analysis:
# Time complexity: O(N). where N is the length of A.
# Space complexity: O(1).