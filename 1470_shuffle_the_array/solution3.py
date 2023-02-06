# Approach 2: In-place Filling
# https://leetcode.com/problems/shuffle-the-array/solution/

# One possible solution is storing two numbers together (the first number in the first ten bits and the second in 
# the next ten bits) without using additional space.
# We will store the last n numbers with the first n numbers of the nums array. Thus, x_i and y_i are stored at 
# i_th index.
# And then we can store the numbers at their respective positions after starting iteration on the stored pairs 
# from index (n−1) to index 0.

# Algorithm:
# 1. Iterate on the nums array from index i = n to 2 * n - 1:
#    -  Store the element y_i+1, that is, nums[i] with x_i+1 at index (i - n), using bit manipulation.
# 2. Iterate from index n - 1 to 0, and at each index i:
#    -  Extract both firstNumber and secondNumber using bit manipulation and store them at their respective 
#       indices 2 * i and 2 * i + 1 in the nums array.
# 3. Return the nums array.


from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Store each y(i) with respective x(i).
        for i in range(n, 2 * n):
            secondNum = nums[i] << 10
            nums[i - n] |= secondNum

        # '0000000000 1111111111' in decimal.
        allOnes = int(pow(2, 10)) - 1

        # We will start putting all numbers from the end, 
        # as they are empty places.
        for i in range(n - 1, -1, -1):
            # Fetch both the numbers from the current index.
            secondNum = nums[i] >> 10
            firstNum = nums[i] & allOnes
            nums[2 * i + 1] = secondNum
            nums[2 * i] = firstNum
        return nums


nums = [2,5,1,3,4,7]
n = 3
obj = Solution()
print(obj.shuffle(nums, n))


# Complexity Analysis:
# Here, 2∗n is the number of elements in the nums array.
# Time complexity: O(n). 
#   -   We only iterate on the n elements of the nums array twice, which takes us O(n) time.
# Space complexity: O(1).
#   -   We are not using any additional space other than the output array.