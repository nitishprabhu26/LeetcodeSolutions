# Approach : Neetcode
# https://youtu.be/yubRKwixN-U


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        # come up with the divider value
        div = 1
        # keep increasing the divider
        while x >= 10 * div:
            div *= 10
            
        while x:
            right = x % 10
            left = x // div
            
            if left != right:
                return False
            
            # chop off both left and right digits
            x = (x % div) // 10
            div = div // 100
            
        return True


x = 121
obj = Solution()
print(obj.isPalindrome(x))


# Complexity Analysis:
# Time complexity: O(log_10(n)). We divided the input by 10 for every iteration, so the time complexity is 
# O(log_10(n)).
# Space complexity: O(1).