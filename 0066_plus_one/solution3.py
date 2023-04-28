# Approach : Neetcode
# https://youtu.be/jIaA8boiG1s


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        
        # var one is carry
        one, i = 1, 0
        
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
            
        return digits[::-1]
            

digits = [1,2,3]
obj = Solution()
print(obj.plusOne(digits))


# Complexity Analysis:
# Let N be the number of elements in the input list.
# Time complexity: O(N) since it's not more than one pass along the input list.
# Space complexity: O(N)
# Although we perform the operation in-place (i.e. on the input list itself), in the worst scenario, we would need 
# to allocate an intermediate space to hold the result, which contains the N+1 elements (appending a 1). 
# Hence the overall space complexity of the algorithm is O(N).