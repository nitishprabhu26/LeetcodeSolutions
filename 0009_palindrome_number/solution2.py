# Reverse the number and compare using while loop


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers are never a palindrome
        if x >= 0:
            temp = x
            n = 0
            while x > 0:
                n = n * 10 + x % 10
                x = x // 10
            return True if n == temp else False
        else:
            return False


# OR

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        n = 0
        while x > 0:
            n = n * 10 + x % 10
            x = x // 10
        return True if n == temp else False


x = 121
obj = Solution()
print(obj.isPalindrome(x))


# Complexity Analysis:
# Time complexity: O(n).
# Space complexity: O(n).
