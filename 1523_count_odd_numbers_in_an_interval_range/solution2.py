# Approach : Better Brute force [Time Limit Exceeded]

# Another way would be to find the following odd number after low and then keep taking a jump of 2 (because there 
# is exactly one even number between every two consecutive odd numbers) and count the number of odd integers. 


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # if low is even, make it odd
        if low % 2 == 0:
            low += 1
            
        count = 0
        for num in range(low, high + 1, 2):
                count += 1
        return count


low = 3
high = 7
obj = Solution()
print(obj.countOdds(low, high))


# Complexity Analysis:
# Time complexity : O(high - low). This approach is still inefficient as the number of operations here would be 
# (high - low) / 2, and hence the time complexity would still be O(high − low).
# Space complexity : O(1)