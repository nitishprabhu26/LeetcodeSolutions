# Approach 3: Bitwise Operators : NOT, AND and XOR (Non Intuitive)
# https://leetcode.com/problems/single-number-ii/solution/
# OR
# https://youtu.be/cOFAmaMBVps?t=476 (explaination)
# seen_once: Keeps the elements which will repeat only once.
# seen_twice: Keeps the elements which will repeat only twice.


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        
        for num in nums:
            # first appearance: 
            # add num to seen_once 
            # don't add to seen_twice because of presence in seen_once
            
            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice
            
            # third appearance: 
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once
            
            
nums = [2,2,3,2]
obj = Solution()
print(obj.singleNumber(nums))


# Complexity Analysis:
# Time complexity : O(N) to iterate over the input array.
# Space complexity : O(1)  since no additional data structures are allocated.