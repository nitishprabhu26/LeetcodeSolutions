# Approach 1: Checking Loop
# https://youtu.be/fV0eOYlYfrM

# eg1:
# if K = 3,
# Remainders can be 0, 1, 2.
# Number          1       11      111     1111    11111
# Number % K      1       2       0       1       2

# eg2:
# if K = 6,
# Remainders can be 0, 1, 2, 3, 4, 5.
# Number          1       11      111     1111    11111     111111      1111111
# Number % K      1       5       3       1       5         3           1

# We can see that remainder only exists for 0 to K-1 values, for Kth value it will be 0 (in case of eg1)
# and also a pattern for the remainder (0 to K) and repeats further
# So, if there wont exists any remainder '0' between these K numbers, then there wont be any number which
# gives remainder '0' (in case of eg2)

# WKT, value of n may overflow the 64 bit integer. so we cant do 'N % K == 0' always.
# so we use a technique to find remainder from prev_remainder

# We can follow:
# N = prev_remainder * 10 + 1
# remainder = N % K
# i.e. remainder = (prev_remainder * 10 + 1) % K

# sinca all nums are 1, we can eliminate all nums which end with 2 and 5
# Also, note that 111...111 can never be divided by 2 or 5 because its last digit is never an even number or 5.
# You can just return -1 if you find that 2 or 5 is a factor of K.

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        for n in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return n

        return -1


k = 2
k = 3
obj = Solution()
print(obj.smallestRepunitDivByK(k))

# Complexity Analysis
# Time Complexity : O(k) since we at most run the loop k times.
# Space Complexity : O(1)