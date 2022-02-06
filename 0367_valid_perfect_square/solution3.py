# Approach : Neetcode [Binary Search]
# [ignoring the if condition for num = 1 as seen in approach 1, and using a while loop instead to handle it ]

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left, right = 1, num
        
        while left <= right:
            x = (left + right) // 2
            guess_squared = x * x
            if guess_squared > num:
                right = x - 1
            elif guess_squared < num:
                left = x + 1
            else:
                return True
        
        return False


num = 16
obj = Solution()
print(obj.isPerfectSquare(num))


# Complexity Analysis:
# Time complexity : O(logN).
# Space complexity : O(1).
