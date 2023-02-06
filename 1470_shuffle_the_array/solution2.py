# Approach : Simple Iteration O(2*n)
# https://youtu.be/hpg65ugGG3E


from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * (2 * n)
        
        for i in range(2 * n):
            if i % 2 == 0:
                result[i] = nums[i // 2]
            else:
                result[i] = nums[n + i // 2]
            # OR
            # result[i] = nums[i // 2] if (i % 2 == 0) else nums[n + i // 2]

        return result


nums = [2,5,1,3,4,7]
n = 3
obj = Solution()
print(obj.shuffle(nums, n))


# Complexity Analysis:
# Here, 2∗n is the number of elements in the nums array.
# Time complexity: O(n). 
#   -   We iterate on n elements of the nums array, which takes us O(n) time.
#   -   Initializing the result array will take O(2n) time.
#   -   Thus, overall we take O(n + 2n) = O(n) time.
# Space complexity: O(1).
#   -   We are not using any additional space other than the output array.