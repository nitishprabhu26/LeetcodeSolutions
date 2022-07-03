# Approach 2: Quickselect
# This textbook algorthm has O(N) average time complexity. Like quicksort, it was developed by Tony Hoare, and is 
# also known as Hoare's selection algorithm.
# The approach is basically the same as for quicksort. For simplicity let's notice that kth largest element is the 
# same as N - kth smallest element, hence one could implement kth smallest algorithm for this problem.

# First one chooses a pivot, and defines its position in a sorted array in a linear time. This could be done with 
# the help of partition algorithm.
# To implement partition one moves along an array, compares each element with a pivot, and moves all elements 
# smaller than pivot to the left of the pivot.
# As an output we have an array where pivot is on its perfect position in the ascending sorted array, all elements 
# on the left of the pivot are smaller than pivot, and all elements on the right of the pivot are larger or equal 
# to pivot.
# Hence the array is now split into two parts. If that would be a quicksort algorithm, one would proceed 
# recursively to use quicksort for the both parts that would result in O(NlogN) time complexity. Here there is 
# no need to deal with both parts since now one knows in which part to search for N - kth smallest element, and 
# that reduces average time complexity to O(N).

# Finally the overall algorithm is quite straightforward :
# - Choose a random pivot.
# - Use a partition algorithm to place the pivot into its perfect position pos in the sorted array, move smaller 
#   elements to the left of pivot, and larger or equal ones - to the right.
# - Compare pos and N - k to choose the side of array to proceed recursively.


import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # imp: 
        # kth largest is (n - k + 1)th smallest, which is in (n - k)th position
        # if 6 elements in array, 1st largest is 6th smallest, which is in 5th position
        # last parameter is the index, for which we need to find the element
        return select(0, len(nums) - 1, len(nums) - k)


nums = [3,2,3,1,2,4,5,5,6]
k = 4
obj = Solution()
print(obj.findKthLargest(nums, k))


# Complexity analysis:
# Time complexity : O(N) in the average case, O(N^2) in the worst case.
# Space complexity : O(1).