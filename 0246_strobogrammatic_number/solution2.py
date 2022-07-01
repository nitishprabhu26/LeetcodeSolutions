# https://leetcode.com/problems/strobogrammatic-number/solution/


# Approach 2: Two Pointers
# Intuition:
# We have observed a pattern in how digits move in the rotation: the first and last swap, the second and the 
# second-to-last swap, etc.
# For the number to be strobogrammatic, we have to write the same number back into each index. As we deduced 
# earlier, there are only five valid pairs of numbers for this to work.
# 0 and 0.
# 1 and 1.
# 6 and 9.
# 8 and 8.
# 9 and 6.
# Therefore, we can check each pair that would swap in the reversal for whether or not it is one of the five pairs 
# listed above. If all pairs are on the list, then the number is strobogrammatic. For odd-lengthed numbers, the 
# middle digit has to be 0, 1, or 8.

# Algorithm:
# We initialize two pointers; left and right. We then iterate both pointers towards the middle at each step, 
# ensuring that the digits at left and right correspond to one of the five valid pairs. An elegant way of doing 
# this is to define a hash map of valid left -> right mappings.
# If no invalid pairs are found, then the number must be strobogrammatic. Note that the 
# middle-digit-of-an-odd-number case is handled correctly; the final iteration will have left = right. 
# If they are both pointing to the same 0, 1, or 8, then the condition will be false, and true returned at the end. 
# If they are both pointing at a 6, then the condition will be true, and false will be returned, as 
# expected_rotation will be 9, and num[right] will be 6.


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        
        left = 0 
        right = len(num) - 1
        
        while left <= right:
            if num[left] not in rotated_digits \
                    or rotated_digits[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True


num = "69"
obj = Solution()
print(obj.isStrobogrammatic(num))


# Complexity analysis:
# Let N be the length of the input string.
# Time complexity : O(N)
# For each of the N digits in the string, we're doing a single lookup and comparison.
# Space complexity : O(1). 
# We are only using constant extra space. This is an in-place algorithm.