# Neetcode: O(m + n) solution using Stack
# https://youtu.be/68a1Dc_qVq4


from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # mapping every single value in nums1 to its index
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)        
            
        return res
        
        
nums1 = [4,1,2]
nums2 = [2,1,3,4]

obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))


# Complexity Analysis:
# Let n and m represent the length of the nums2 and nums1 array respectively.
# Time complexity: O(n). The entire nums2 array (of size n) is scanned only once. Each of the stack's m elements 
# are pushed and popped exactly once. All together this requires O(n + m) time. Since nums1 must be a subset of 
# nums2, we know m must be less than or equal to n. Therefore, the time complexity can be simplified to O(n).
# Space complexity: O(m). map will store m key-value pairs while stack will contain at most m elements at any 
# given time because we are adding only elements of nums1 to the stack.
