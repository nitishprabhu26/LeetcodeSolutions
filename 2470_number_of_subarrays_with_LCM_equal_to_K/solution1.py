# Approach: O(N^2) approach
# https://youtu.be/3eVYlm2p2_o

# We need to remember the following, (for the break out condition)
# eg: LCM of (9, 18) = 18
# If we add any new element (3rd element) to array, the new LCM (of all 3 elements) can't be less than the already 
# calculated LCM of the previous 2 numbers.
# i.e. if we want to find LCM of (9, 18, 3) or (9, 18, 5)
# LCM of (9, 18, 3) = 18 (greater than or equal to LCM of 2 numbers)
# LCM of (9, 18, 5) = 90 (greater than or equal to LCM of 2 numbers)


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