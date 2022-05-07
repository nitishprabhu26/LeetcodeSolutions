# Approach 3: Hardcoding the Only Cycle (Advanced)
# Note: not something you'd write in an interview, vs the previous 2 approaches.
# https://leetcode.com/problems/happy-number/solution/


# Algorithm:
# What's the biggest number that could have a next value bigger than itself? Well we know it has to be less than 
# 243, from the analysis we did previously. Therefore, we know that any cycles must contain numbers smaller than 
# 243, as anything bigger could not be cycled back to. With such small numbers, it's not difficult to write a 
# brute force program that finds all the cycles.
# If you do this, you'll find there's only one cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4. All 
# other numbers are on chains that lead into this cycle, or on chains that lead into 1.
# Therefore, we can just hardcode a HashSet containing these numbers, and if we ever reach one of them, then we 
# know we're in the cycle. There's no need to keep track of where we've been previously.


class Solution:
    def isHappy(self, n: int) -> bool:

        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        while n != 1 and n not in cycle_members:
            n = get_next(n)

        return n == 1


n = 19
n = 2
obj = Solution()
print(obj.isHappy(n))


# Complexity Analysis:
# Time complexity : O(logn). Same as above.
# Space complexity : O(1). We are not maintaining any history of numbers we've seen. The hardcoded HashSet is of a 
# constant size.
