# Approach: O(N^2) approach

from typing import List

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        # recursive function to find gcd
        def calc_gcd(a, b):
            if b == 0:
                return a
            return calc_gcd(b, a % b)
            
        def calc_lcm(a, b):
            return (a // calc_gcd(a,b)) * b

        count = 0
        for i in range(len(nums)):
            if nums[i] == k:
                count += 1
            lcm = nums[i]
            for j in range(i + 1, len(nums)):
                lcm = calc_lcm(lcm, nums[j])
                if lcm == k:
                    count += 1
                # break out if lcm becomes greater than k; start with new 'i'
                if lcm > k:
                    break
                
        return count


nums = [3,6,2,7,1]
k = 6
obj = Solution()
print(obj.subarrayLCM(nums, k))


# Complexity Analysis:
# Time complexity : O(N * N).
# Space complexity : O(1).