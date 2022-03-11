# Approach: Simple Naive

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         count = 0
#         i = 1
#         while n >= 0:
#             n -= i
#             i += 1
#             count += 1
#         return count - 1
    
# OR

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n - i >= 0:
            n -= i
            i += 1
        return i - 1


n = 5
obj = Solution()
print(obj.arrangeCoins(n))


# Complexity Analysis:
# Time Complexity: O(N)
# Space Complexity: O(1)