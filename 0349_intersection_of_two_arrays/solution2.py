# Approach 2: Built-in Set Intersection

# Intuition:
# There are built-in intersection facilities, which provide O(n+m) time complexity in the average case and O(n×m) 
# time complexity in the worst case.


from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
        

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj = Solution()
print(obj.intersection(nums1, nums2))


# Complexity Analysis:
# Time complexity : O(n+m) in the average case and O(n×m) in the worst case when load factor is high enough.
# Space complexity : O(m+n) in the worst case when all elements in the arrays are different.