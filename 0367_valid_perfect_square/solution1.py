import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # efficient
        if int(num ** 0.5) ** 2 == num:
            return True
        return False

        # OR

        # this works
        for i in range(int(num ** 0.5) + 1):
            if i ** 2 == num:
                return True
        return False

        # OR

        # this also works, and doesn't use any square root finding math
        O(sqrt(n))
        for i in range(1, num + 1):
            if i * i == num:
                return True
            if i * i > num:
                return False



num = 16
obj = Solution()
print(obj.isPerfectSquare(num))


