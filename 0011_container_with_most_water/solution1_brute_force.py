# Approach 1: Brute Force (Time Limit exceeded)
# Algorithm:
# In this case, we will simply consider the area for every possible pair of the lines and find out the maximum area out of those.


class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                prod = (j-i) * min(height[i], height[j])
                if prod > max_area:
                    max_area = prod
        return max_area


height = [4, 3, 2, 1, 4]
obj = Solution()
print(obj.maxArea(height))


# Complexity Analysis:
# Time complexity : O(n^2). Calculating area for all n.(n−1)/2 height pairs.
# Space complexity : O(1). Constant extra space is used.
