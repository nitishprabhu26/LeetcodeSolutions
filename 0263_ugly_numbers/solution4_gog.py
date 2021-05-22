# https://www.geeksforgeeks.org/ugly-numbers/
# https://practice.geeksforgeeks.org/problems/ugly-numbers2254/1#

class Solution:
    def getNthUglyNo(self, n):
        ugly = [0] * n  # To store ugly numbers

        # 1 is the first ugly number
        ugly[0] = 1

        # i2, i3, i5 will indicate indices for
        # 2,3,5 respectively
        i2 = i3 = i5 = 0

        # Set initial multiple value
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        # Start loop to find value from ugly[1] to ugly[n]
        for i in range(1, n):
            # Choose the min value of all available multiples
            ugly[i] = min(next_multiple_of_2,
                        next_multiple_of_3, next_multiple_of_5)

            # Increment the value of index accordingly
            if ugly[i] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2]*2

            if ugly[i] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3]*3

            if ugly[i] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5]*5
        return ugly[-1]


num = 42
obj = Solution()
print(obj.getNthUglyNo(num))
