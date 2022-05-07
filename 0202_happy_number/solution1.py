# Approach 1: Detect Cycles with a HashSet
# https://leetcode.com/problems/happy-number/solution/
# OR
# Neetcode: https://youtu.be/ljz85bxOYJ0


# Algorithm:
# There are 2 parts to the algorithm we'll need to design and code.
# 1. Given a number n, what is its next number?
# 2. Follow a chain of numbers and detect if we've entered a cycle.
# - Part 1 can be done by using the division and modulus operators to repeatedly take digits off the number until 
#   none remain, and then squaring each removed digit and adding them together.
# - Part 2 can be done using a HashSet. Each time we generate the next number in the chain, we check if it's 
#   already in our HashSet.
#   -   If it is not in the HashSet, we should add it.
#   -   If it is in the HashSet, that means we're in a cycle and so should return false.


class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


# OR


class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSqares(n)
            
            if n == 1:
                return True
            
        return False
    
    def sumOfSqares(self, n):
        output = 0
        while n:
            digit = n %10
            digit = digit ** 2
            output += digit
            n = n// 10
        return output


n = 19
n = 2
obj = Solution()
print(obj.isHappy(n))


# Complexity analysis:
# https://leetcode.com/problems/happy-number/solution/
# Time complexity : O(logn).
# Finding the next value for a given number has a cost of O(logn) because we are processing each digit in the 
# number, and the number of digits in a number is given by logn.
# Space complexity : O(logn).
