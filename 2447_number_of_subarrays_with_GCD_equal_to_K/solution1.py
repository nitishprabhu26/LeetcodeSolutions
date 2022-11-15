# Approach: O(N^2) approach
# https://youtu.be/Fp92Zvs0uKw

# We need to remember the following, (for the break out condition)
# eg: GCD of (9, 3) = 3
# If we add any new element (3rd element) to array, the new GCD (of all 3 elements) can't be greater than the 
# already calculated GCD of the previous 2 numbers.
# i.e. if we want to find GCD of (9, 3, 1) or (9, 3, 6)
# GCD of (9, 3, 1) = 1 (it is either lesser than or equal to GCD of 2 numbers)
# GCD of (9, 3, 6) = 3 (it is either lesser than or equal to GCD of 2 numbers)


from typing import List

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        # recursive function to find gcd
        def calc_gcd(a, b):
            if b == 0:
                return a
            return calc_gcd(b, a % b)

        count = 0
        for i in range(len(nums)):
            if nums[i] == k:
                count += 1
            gcd = nums[i]
            for j in range(i + 1, len(nums)):
                gcd = calc_gcd(gcd, nums[j])
                if gcd == k:
                    count += 1
                # break out if GCD becomes lesser than k; start with new 'i'
                if gcd < k:
                    break
                
        return count


nums = [9,3,1,2,6,3]
k = 3
obj = Solution()
print(obj.subarrayGCD(nums, k))


# Complexity Analysis:
# Time complexity : O(N * N).
# Space complexity : O(1).