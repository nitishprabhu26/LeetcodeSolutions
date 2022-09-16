# Convert to string, reverse and compare


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return int(str(abs(x))[::-1]) == x

        
x = 121
obj = Solution()
print(obj.isPalindrome(x))


# Complexity Analysis:
# Time complexity: O(n).
# Space complexity: O(n).