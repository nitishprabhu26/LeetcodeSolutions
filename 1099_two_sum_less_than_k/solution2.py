# Approach 2: Two Pointers

# Algorithm:
# 1. Sort the array.
# 2. Set the left pointer to zero, and right - to the last index.
# 3. While left is smaller than right:
#       If nums[left] + nums[right] is less than k:
#           Track maximum nums[left] + nums[right] in the result answer.
#           Increment left.
#       Else:
#           Decrement right.
# 4. Return the result answer.


from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = -1
        left = 0
        right = len(nums) -1
        while left < right:
            sum = nums[left] + nums[right]
            if (sum < k):
                answer = max(answer, sum)
                left += 1
            else:
                right -= 1
        return answer
        

# Optimizations:
# We can break from the loop as soon as nums[left] > k / 2. In the sorted array, nums[left] is the smallest of 
# the remaining elements, so nums[right] > k / 2 for any right. Therefore, nums[left] + nums[right] will be equal 
# or greater than k for the remaining elements.

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = -1
        left = 0
        right = len(nums) -1
        while left < right:
            # optimization
            if nums[left] > k / 2:
                break
            sum = nums[left] + nums[right]
            if (sum < k):
                answer = max(answer, sum)
                left += 1
            else:
                right -= 1
        return answer


nums = [34,23,1,24,75,33,54,8]
k = 60
obj = Solution()
print(obj.twoSumLessThanK(nums, k))


# Complexity analysis:
# Time Complexity: O(nlogn) to sort the array. The two pointers approach itself is O(n), so the time complexity 
# would be linear if the input is sorted.
# Space Complexity: from O(1).
