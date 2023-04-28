# Approach 1: Schoolbook Addition with Carry
# https://leetcode.com/problems/plus-one/solution/

# Algorithm:
# 1. Move along the input array starting from the end of array.
# 2. Set all the nines at the end of array to zero.
# 3. If we meet a not-nine digit, we would increase it by one. The job is done - return digits.
# 4. If not, then We're here because all the digits were equal to nine. Now they have all been set to zero. We 
#    then append the digit 1 in front of the other digits and return the result.


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits
            

digits = [1,2,3]
obj = Solution()
print(obj.plusOne(digits))


# Complexity Analysis:
# Let N be the number of elements in the input list.
# Time complexity: O(N) since it's not more than one pass along the input list.
# Space complexity: O(N)
# Although we perform the operation in-place (i.e. on the input list itself), in the worst scenario, we would need 
# to allocate an intermediate space to hold the result, which contains the N+1 elements. Hence the overall space 
# complexity of the algorithm is O(N).