# From the looks of it, this seems like a simple enough problem to solve in linear time and space. We can simply 
# take the product of all the elements in the given array and then, for each of the elements x of the array, we 
# can simply find product of array except self value by dividing the product by x. (But in case where if x is 0, 
# we will get a division by 0 error)
# Doing this for each of the elements would solve the problem. However, there's a note in the problem which says 
# that we are not allowed to use division operation. That makes solving this problem a bit harder.

# Approach 1: Left and Right product lists
# https://leetcode.com/problems/product-of-array-except-self/solution/ (video)

# Algorithm:
# 1. Initialize two empty arrays, L and R where for a given index i, L[i] would contain the product of all the 
#    numbers to the left of i and R[i] would contain the product of all the numbers to the right of i.
# 2. We would need two different loops to fill in values for the two arrays. For the array L, L[0] would be 1 
#    since there are no elements to the left of the first element. For the rest of the elements, we simply use 
#    L[i] = L[i - 1] * nums[i - 1]. Remember that L[i] represents product of all the elements to the left of 
#    element at index i.
# 3. For the other array, we do the same thing but in reverse i.e. we start with the initial value of 1 in 
#    R[length - 1] where length is the number of elements in the array, and keep updating R[i] in reverse. 
#    Essentially, R[i] = R[i + 1] * nums[i + 1]. Remember that R[i] represents product of all the elements to the 
#    right of element at index i.
# 4. Once we have the two arrays set up properly, we simply iterate over the input array one element at a time, 
#    and for each element at index i, we find the product except self as L[i] * R[i].


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The left and right arrays as described in the algorithm
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]
        
        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all 
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]
        
        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]
        
        return answer
        

# OR


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_product = []
        right_product = []
        answer = []
        
        Lprod = 1
        Rprod = 1
        
        left_product.append(1)
        right_product.append(1)
        
        for i in range(1, len(nums)):
            left_product.append(Lprod * nums[i-1])
            Lprod *= nums[i-1]
            right_product.append(Rprod * nums[len(nums)-i])
            Rprod *= nums[len(nums)-i]
            
        right_product.reverse()
        
        for i in range(len(nums)):
            answer.append(left_product[i] * right_product[i])
        return answer


nums = [1,2,3,4]
obj = Solution()
print(obj.productExceptSelf(nums))


# Complexity analysis:
# Time complexity : O(N) where N represents the number of elements in the input array. We use one iteration to 
# construct the array L, one to construct the array R and one last to construct the answer array using L and R.
# Space complexity : O(N) used up by the two intermediate arrays that we constructed to keep track of product 
# of elements to the left and right.
