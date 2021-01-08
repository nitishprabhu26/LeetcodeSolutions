class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
obj = Solution()
obj.merge(nums1, m, nums2, n)