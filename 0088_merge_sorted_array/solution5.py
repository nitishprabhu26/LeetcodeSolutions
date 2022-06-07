# Approach 3: Three Pointers (Start From the End)

# Intuition:
# Approach 2 already demonstrates the best possible time complexity, O(n+m), but still uses additional space. This 
# is because the elements of array nums1 have to be stored somwhere so that they aren't overwritten.
# So, what if instead we start to overwrite nums1 from the end, where there is no information yet?

# The algorithm is similar to before, except this time we set p1 to point at index m - 1 of nums1, p2 to point at 
# index n - 1 of nums2, and p to point at index m + n - 1 of nums1. This way, it is guaranteed that once we start 
# overwriting the first m values in nums1, we will have already written each into its new position. In this way, 
# we can eliminate the additional space.


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


# OR
# Neetcode: https://youtu.be/P1Ic85RarKY

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # last index nums1
        last = m + n - 1
        
        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
            
        # fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1


# OR similar to Neetcode

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1

        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1

        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]
        print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj = Solution()
obj.merge(nums1, m, nums2, n)