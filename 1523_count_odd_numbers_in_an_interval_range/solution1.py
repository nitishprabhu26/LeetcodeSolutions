# Approach : Brute force [Time Limit Exceeded]

# The brute force way of solving this problem would be to iterate over each number from low to high and check if 
# the number is odd and increment a counter variable accordingly.


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            if num % 2 != 0:
                count += 1
        return count


low = 3
high = 7
obj = Solution()
print(obj.countOdds(low, high))


# Complexity Analysis:
# Time complexity : O(high - low) and high - low could be up to 10 ^9, and hence this is not feasible.
# Space complexity : O(1)