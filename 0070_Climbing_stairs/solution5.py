# Approach 5: Neetcode
# https://www.youtube.com/watch?v=Y0lT9Fck7qI


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            one, two = one + two, one

        return one


n = 38
obj = Solution()
print(obj.climbStairs(n))


# Complexity Analysis
# Time complexity : O(n). Single loop upto n is required.
# Space complexity : O(1). Constant space is used.
