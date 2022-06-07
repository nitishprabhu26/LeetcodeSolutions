# Approach 2: Three Pointers (Start From the Beginning)

# Intuition:
# Because each array is already sorted, we can achieve an O(n + m) time complexity with the help of the 
# two-pointer technique.

# Algorithm:
# The simplest implementation would be to make a copy of the values in nums1, called nums1Copy, and then use two 
# read pointers to read values from nums1Copy and nums2; and one write pointer to write them into nums1.
# - Initialize nums1Copy to be a new array containing the first m values of nums1.
# - Initialize read pointer p1 to the beginning of nums1Copy.
# - Initialize read pointer p2 to the beginning of nums2.
# - Initialize write pointer p to the beginning of nums1.
# - While p is still within nums1:
#   -   If nums1Copy[p1] exists and is less than or equal to nums2[p2]:
#       -   Write nums1Copy[p1] into nums1[p], and increment p1 by 1.
#   -   Else
#       -   Write nums2[p2] into nums1[p], and increment p2 by 1.
#   -   Increment p by 1.


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m] 
        
        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0
        
        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1] 
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

        print(nums1)


# OR


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Make a copy of nums1.
        nums1_copy = nums1[:m]
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

        print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj = Solution()
obj.merge(nums1, m, nums2, n)


# Complexity Analysis:
# Time complexity: O(n + m).
# We are performing (n+2⋅m) reads and (n+2⋅m) writes. Because constants are ignored in Big O notation, this gives 
# us a time complexity of O(n + m).
# Space complexity: O(m).
# We are allocating an additional array of length m.