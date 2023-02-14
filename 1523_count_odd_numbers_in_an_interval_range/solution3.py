# Approach 1: Maths

# The count of odd integers between x and a greater integer y, where x is odd would be [(y - x)/ 2] + 1.

# We need to find the count of odd integers between an odd integer x and an integer y. In total, there are y − x 
# integers between them excluding y, and every other number is odd. Thus, the number of odd numbers can be written 
# as (y − x) / 2. The important point to note here is that the above formula always leaves out the last odd 
# integer in the range (let's say x = 1, y = 3, then the formula gives us 1 as it leaves out the 3) and hence we 
# need to add 1. Therefore we have [(y - x)/ 2] + 1 odd integers between x and y, when x is odd.

# Algorithm:
# 1. Check if low is odd. This could be easily checked using % operator, but we used bit wise operator & as they 
#    are more efficient.
# 2. If low is even, increment it.
# 3. Return (high - low) / 2 + 1. The important point here is to check that if low after incrementing became 
#    greater than high this will happen when low = high, and in that case, we should return 0.


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # if low is even, make it odd
        if low & 1 == 0:
            low += 1
            
        # low could become greater than high due to incrementation
        # if it is, the answer is 0; otherwise, use the formula.
        return 0 if low > high else (high - low) // 2 + 1 


low = 3
high = 7
obj = Solution()
print(obj.countOdds(low, high))


# Complexity Analysis:
# Time complexity : O(1). We are using bit-wise and other arithmetic or relational operator that all cost us O(1) 
# time. Hence the time complexity would be constant.
# Space complexity : O(1). No extra variable or space is needed, and hence the space complexity would be constant.