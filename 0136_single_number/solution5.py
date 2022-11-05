# Approach 4: Bit Manipulation : (Actual solution): 
# Could you implement a solution with a linear runtime complexity and without using extra memory?
# or
# Neetcode: https://youtu.be/qMPX1AOa83k

# Concept: Approach 4: Bit Manipulation
# - If we take XOR of zero and some bit, it will return that bit
#   a ⊕ 0 = a
# - If we take XOR of two same bits, it will return 0
#   a ⊕ a = 0
# - a ⊕ b ⊕ a = ( a ⊕ a ) ⊕ b = 0 ⊕ b = b
# So we can XOR all bits together to find the unique number.


class Solution:
    def singleNumber(self, nums):
        res=0
        for el in nums:
            res ^= el
        return res
            

nums = [4,1,2,1,2]
obj = Solution()
print(obj.singleNumber(nums))


# Complexity Analysis:
# Time complexity : O(n). We only iterate through nums, so the time complexity is the number of elements in nums.
# Space complexity : O(1).