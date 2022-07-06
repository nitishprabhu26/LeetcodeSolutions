# Approach 1: Two Sets

# Intuition:
# The naive approach would be to iterate along the first array nums1 and to check for each value if this value is 
# in nums2 or not. If yes - add the value to output. Such an approach would result in a pretty bad O(n×m) time 
# complexity, where n and m are arrays' lengths.
# To solve the problem in linear time, let's use the structure set, which provides in/contains operation in O(1) 
# time in average case.
# The idea is to convert both arrays into sets, and then iterate over the smallest set checking the presence of 
# each element in the larger set. Time complexity of this approach is O(n+m) in the average case.


from typing import List

class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
        

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj = Solution()
print(obj.intersection(nums1, nums2))


# Complexity Analysis:
# Time complexity : O(n+m), where n and m are arrays' lengths. O(n) time is used to convert nums1 into set, 
# O(m) time is used to convert nums2, and contains/in operations are O(1) in the average case.
# Space complexity : O(m+n) in the worst case when all elements in the arrays are different.