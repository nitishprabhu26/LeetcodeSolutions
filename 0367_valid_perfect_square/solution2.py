# Approach 1: Binary Search

# For num>2 the square root a is always less than num/2 and greater than 1: 1 < x < num/2. 
# Since x is an integer, the problem goes down to the search in the sorted set of integer numbers. Binary 
# search is a standard way to proceed in such a situation.


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        
        return False



num = 16
obj = Solution()
print(obj.isPerfectSquare(num))


# Complexity Analysis:
# Time complexity : O(logN).
# Space complexity : O(1).
