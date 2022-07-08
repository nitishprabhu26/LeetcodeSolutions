# Approach 1: Hash Map:

# For the previous problem: 349, we used a hash set to achieve a linear time complexity. Here, we need to use a 
# hash map to track the count for each number.
# We collect numbers and their counts from one of the arrays into a hash map. Then, we iterate along the second 
# array, and check if the number exists in the hash map and its count is positive. If so - add the number to the 
# result and decrease its count in the hash map.
# It's a good idea to check array sizes and use a hash map for the smaller array. It will reduce memory usage 
# when one of the arrays is very large.

# Algorithm:
# 1.If nums1 is larger than nums2, swap the arrays. (keep nums1 as the smaller array).
# 2.For each element in nums1:
#   - Add it to the hash map m.
#       - Increment the count if the element is already there.
# 3.Initialize the insertion pointer (k) with zero.
# 4.Iterate along nums2:
#   - If the current number is in the hash map and count is positive:
#       - Copy the number into nums1[k], and increment k.
#       - Decrement the count in the hash map.
# 5.Return first k elements of nums1.


from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
            
        dict = {}
        # create a hashmap of elements in nums1 array
        for i in nums1:
            dict[i] = dict.get(i, 0) + 1
            
        k = 0
        for i in nums2:
            # If the current number is in the hash map and count is positive
            if i in dict and dict[i] > 0:
                # Copy the number into nums1[k], and increment k
                nums1[k] = i
                k += 1
                # Decrement the count in the hash map
                dict[i] -= 1
                
        # Return first k elements of nums1  
        return nums1[:k]


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj = Solution()
print(obj.intersect(nums1, nums2))


# Complexity Analysis:
# Time Complexity: O(n + m), where n and m are the lengths of the arrays. We iterate through the first, and then 
# through the second array; insert and lookup operations in the hash map take a constant time.
# Space Complexity: O(min(n, m)). We use hash map to store numbers (and their counts) from the smaller array.