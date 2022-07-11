# Neetcode
# https://youtu.be/q6IEA26hvXc
# In question, The overall run time complexity should be O(log (m+n)) worst case.
# So it is supposed to be binary search
# Remember that the given input arrays are in sorted order

class Solution:
    def findMedianSortedArrays(self, nums1: int, nums2: int) -> float:

        A, B = nums1, nums2
        total = len(nums1)+len(nums2)
        half = total//2

        # making A the array with less number of elements
        if len(B) < len(A):
            A, B = B, A

        # Run binary search on A, i.e. for the small array
        # Array has 0 indexing
        l, r = 0, len(A)-1

        # Theres a guarantee that there is a minimum
        while True:
            # i,j (pointer for A and B respectively) are index values
            i = (l+r) // 2  # Middle value for A
            j = half - i - 1 - 1  # B

            # if condition - since indices could be out of bounds
            # if array A has 0 values or if i<0
            Aleft = A[i] if i >= 0 else float('-infinity')
            # we want all the values in array A to be in the left partition
            Aright = A[i+1] if (i+1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if (j+1) < len(B) else float('infinity')

            # partition is done correctly, otherwise go to elif and else
            if Aleft <= Bright and Bleft <= Aright:
                # odd case (odd number of elements)
                if total % 2:
                    return min(Aright, Bright)
                # even case (odd number of elements)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1


nums1 = [1, 2, 6, 6]
nums2 = [3, 4]
obj = Solution()
print(obj.findMedianSortedArrays(nums1, nums2))


# Complexity Analysis:
# Time complexity : O(log min(m,n)). Assume that m and n represents the length of nums1 and nums2 respectively.
