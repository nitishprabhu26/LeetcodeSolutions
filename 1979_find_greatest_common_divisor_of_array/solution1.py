# Simple approach with recursive GCD


from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def calc_gcd(a, b):
            if b == 0:
                return a
            return calc_gcd(b, a % b)
        
        smallest = min(nums)
        largest = max(nums)
            
        return calc_gcd(smallest, largest)


nums = [2,5,6,9,10]
obj = Solution()
print(obj.findGCD(nums))


# Time Complexity : O(log(min(a,b)).
# Auxiliary Space : O(log(min(a,b)).