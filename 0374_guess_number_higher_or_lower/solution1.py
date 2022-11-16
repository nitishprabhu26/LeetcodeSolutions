# Approach 1: Brute Force
# We check every number from 1 to n and pass it to the guess function. The number for which a 0 is returned 
# is the required answer.


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        for i in range(1, n+1):
            if guess(i) == 0:
                return i


n = 10
pick = 6
obj = Solution()
print(obj.guessNumber(n))


# Complexity Analysis:
# Time complexity : O(n). We scan all the numbers from 1 to n.
# Space complexity : O(1). No extra space is used.