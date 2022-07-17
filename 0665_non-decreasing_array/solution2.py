# Approach: Neetcode
# https://youtu.be/RegQckCegDk


from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False

        for i in range(len(nums) - 1):
            
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False
            
            # for the case: 1, 4, 3; the correct modification is to change the number 4 to 3
            # resulting in 1, 3, 3
            if i ==0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            # for the case: 4, 5, 3; the correct modification is to change the number 3 to 5
            # resulting in 4, 5, 5
            else:
                nums[i + 1] = nums[i]
            changed = True

        return True
        

nums = [4,2,3]
obj = Solution()
print(obj.checkPossibility(nums))


# Complexity Analysis:
# Time Complexity: O(n) considering there are n elements in the array and we process each element at most once.
# Space Complexity: O(1) since we don't use any additional space apart from a couple of variables for executing 
# this algorithm.
