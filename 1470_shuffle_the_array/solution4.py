# Approach: NeetcodeIO
# https://youtu.be/IvIKD_EU8BY


from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i + n] #store x, y 

        j = 2 * n - 1
        for i in range(n - 1, -1, -1):
            y = nums[i] & (2**10 - 1)
            x = nums[i] >> 10

            nums[j] = y
            nums[j - 1] = x

            j-= 2

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